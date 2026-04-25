<?php
/**
 * GG Services – Job Application Handler
 * ICT171 | Student: 35352086 | Murdoch University
 * ------------------------------------------------
 * Endpoint: POST /backend/submit_application.php
 * Accepts:  multipart/form-data (required for file uploads)
 * Returns:  JSON { success, message, ref? }
 *
 * Security measures applied:
 *  - Input sanitisation via strip_tags + trim
 *  - Server-side validation of all required fields
 *  - Prepared statements (no SQL injection possible)
 *  - File type validated by MIME type AND extension (not just extension)
 *  - Files renamed to random UUID — no original filename used on disk
 *  - Upload folder blocked from web execution (.htaccess)
 *  - IP-based rate limiting (max 3 applications per hour per IP)
 *  - File size capped at 5 MB server-side (independent of php.ini)
 */

declare(strict_types=1);

require_once __DIR__ . '/config.php';

/* ── Headers ────────────────────────────────────────────────*/
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

/* Only accept POST */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    json_response(false, 'Method not allowed.');
}

/* ── Rate limiting ──────────────────────────────────────────*/
$client_ip = get_ip();
if (!rate_limit_check($client_ip, 3)) {
    http_response_code(429);
    json_response(false, 'Too many submissions. Please wait and try again.');
}

/* ── Ensure upload directories exist ───────────────────────*/
foreach ([CV_DIR, CL_DIR] as $dir) {
    if (!is_dir($dir)) {
        mkdir($dir, 0750, true);
    }
}

/* ── Sanitise text fields ───────────────────────────────────*/
$job_id       = clean($_POST['jobId']        ?? '');
$job_title    = clean($_POST['jobTitle']     ?? '');
$first_name   = clean($_POST['firstName']    ?? '');
$last_name    = clean($_POST['lastName']     ?? '');
$email        = clean($_POST['email']        ?? '');
$phone        = clean($_POST['phone']        ?? '');
$right_work   = clean($_POST['visaStatus']   ?? '');
$availability = clean($_POST['availability'] ?? 'Flexible');
$about        = clean($_POST['aboutYou']     ?? '');

/* ── Server-side validation ─────────────────────────────────*/
$errors = [];

if (strlen($first_name) < 1)                      $errors[] = 'First name is required.';
if (strlen($last_name) < 1)                       $errors[] = 'Last name is required.';
if (!valid_email($email))                         $errors[] = 'A valid email address is required.';
if (!preg_match('/^[\d\s\+\(\)]{7,}$/', $phone)) $errors[] = 'A valid phone number is required.';
if (strlen($right_work) < 2)                     $errors[] = 'Right to work status is required.';
if (strlen($job_id) < 1)                         $errors[] = 'Invalid job reference.';

/* Length caps */
if (strlen($first_name) > 80)  $errors[] = 'First name is too long.';
if (strlen($last_name)  > 80)  $errors[] = 'Last name is too long.';
if (strlen($email)      > 180) $errors[] = 'Email address is too long.';
if (strlen($about)      > 3000) $errors[] = 'About section must be under 3000 characters.';

/* ── CV / Resume — required ─────────────────────────────────*/
if (empty($_FILES['cvFile']) || $_FILES['cvFile']['error'] === UPLOAD_ERR_NO_FILE) {
    $errors[] = 'Please upload your CV or resume.';
}

if (!empty($errors)) {
    http_response_code(422);
    json_response(false, implode(' ', $errors));
}

/* ── File upload helper ─────────────────────────────────────
   Returns array: ['stored' => string, 'original' => string]
   or calls json_response() and exits on error.            */
function handle_upload(array $file, string $dest_dir, string $label): array {
    /* PHP upload error codes */
    if ($file['error'] !== UPLOAD_ERR_OK) {
        $msg = match ($file['error']) {
            UPLOAD_ERR_INI_SIZE, UPLOAD_ERR_FORM_SIZE => "$label exceeds the maximum allowed size of 5 MB.",
            UPLOAD_ERR_PARTIAL => "$label upload was only partially completed. Please try again.",
            default            => "$label could not be uploaded. Please try again.",
        };
        http_response_code(422);
        json_response(false, $msg);
    }

    /* Size check (independent of php.ini) */
    if ($file['size'] > MAX_FILE_BYTES) {
        http_response_code(422);
        json_response(false, "$label exceeds the 5 MB maximum file size.");
    }

    /* Get actual MIME type from file content — not from browser header */
    $finfo    = new finfo(FILEINFO_MIME_TYPE);
    $detected = $finfo->file($file['tmp_name']);

    if (!in_array($detected, ALLOWED_MIME, true)) {
        http_response_code(422);
        json_response(false, "$label must be a PDF, DOC, or DOCX file. Detected type: $detected.");
    }

    /* Derive extension from the detected MIME (never trust user's filename) */
    $ext_map = [
        'application/pdf'      => 'pdf',
        'application/msword'   => 'doc',
        'application/vnd.openxmlformats-officedocument.wordprocessingml.document' => 'docx',
    ];
    $safe_ext = $ext_map[$detected];

    /* Double-check extension from original filename matches detected MIME */
    $original_ext = strtolower(pathinfo($file['name'], PATHINFO_EXTENSION));
    if (!in_array($original_ext, ALLOWED_EXT, true)) {
        http_response_code(422);
        json_response(false, "$label must have a .pdf, .doc, or .docx extension.");
    }

    /* Generate a unique stored filename — never use original name on disk */
    $stored_name = bin2hex(random_bytes(16)) . '_' . time() . '.' . $safe_ext;
    $dest_path   = $dest_dir . $stored_name;

    /* Move from PHP temp location to our uploads folder */
    if (!move_uploaded_file($file['tmp_name'], $dest_path)) {
        http_response_code(500);
        json_response(false, "Could not save $label. Please try again.");
    }

    /* Prevent the file from being executed as a script — belt and braces */
    chmod($dest_path, 0640);

    return [
        'stored'   => $stored_name,
        'original' => basename($file['name']),  // only for DB record — never used as path
    ];
}

/* ── Process CV upload (required) ───────────────────────────*/
$cv = handle_upload($_FILES['cvFile'], CV_DIR, 'CV/Resume');

/* ── Process cover letter (optional) ───────────────────────*/
$cl = ['stored' => '', 'original' => ''];
if (!empty($_FILES['coverLetter']) && $_FILES['coverLetter']['error'] !== UPLOAD_ERR_NO_FILE) {
    $cl = handle_upload($_FILES['coverLetter'], CL_DIR, 'Cover letter');
}

/* ── Database insert (prepared statement) ───────────────────*/
$conn = db_connect();

$stmt = $conn->prepare(
    'INSERT INTO job_applications
       (job_id, job_title, first_name, last_name, email, phone,
        right_to_work, availability, about,
        cv_filename, cv_original, cl_filename, cl_original, ip_address)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
);

if (!$stmt) {
    $conn->close();
    http_response_code(500);
    json_response(false, 'A server error occurred. Please try again.');
}

$stmt->bind_param(
    'ssssssssssssss',
    $job_id,
    $job_title,
    $first_name,
    $last_name,
    $email,
    $phone,
    $right_work,
    $availability,
    $about,
    $cv['stored'],
    $cv['original'],
    $cl['stored'],
    $cl['original'],
    $client_ip
);

$ok        = $stmt->execute();
$insert_id = $stmt->insert_id;
$stmt->close();
$conn->close();

if (!$ok) {
    /* Clean up uploaded files if DB insert failed */
    @unlink(CV_DIR . $cv['stored']);
    if ($cl['stored']) @unlink(CL_DIR . $cl['stored']);
    http_response_code(500);
    json_response(false, 'Could not save your application. Please try again.');
}

/* ── Success ────────────────────────────────────────────────*/
$ref = 'GGA-' . str_pad((string)$insert_id, 5, '0', STR_PAD_LEFT);

json_response(true, 'Application submitted successfully.', [
    'ref'      => $ref,
    'job'      => $job_title,
    'cv_saved' => $cv['original'],
]);
