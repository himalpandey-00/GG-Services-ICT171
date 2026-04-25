<?php
/**
 * GG Services – Quote Request Handler
 * ICT171 | Student: 35352086 | Murdoch University
 * ------------------------------------------------
 * Endpoint: POST /backend/submit_quote.php
 * Accepts:  JSON body or application/x-www-form-urlencoded
 * Returns:  JSON { success, message, ref? }
 *
 * Security measures applied:
 *  - Input sanitisation via strip_tags + trim
 *  - Server-side validation of all required fields
 *  - Prepared statements (no SQL injection possible)
 *  - IP-based rate limiting (max 5 requests per hour per IP)
 *  - CORS restricted to same origin in production
 *  - No sensitive data echoed back
 */

declare(strict_types=1);

require_once __DIR__ . '/config.php';

/* ── CORS & Headers ─────────────────────────────────────────
   Allows the HTML pages (same server) to call this endpoint.
   In production this should be locked to your exact domain.  */
header('Content-Type: application/json; charset=utf-8');
header('X-Content-Type-Options: nosniff');

/* Only accept POST */
if ($_SERVER['REQUEST_METHOD'] !== 'POST') {
    http_response_code(405);
    json_response(false, 'Method not allowed.');
}

/* ── Rate limiting ──────────────────────────────────────────*/
$client_ip = get_ip();
if (!rate_limit_check($client_ip, 5)) {
    http_response_code(429);
    json_response(false, 'Too many submissions. Please wait and try again.');
}

/* ── Parse incoming body ────────────────────────────────────
   Supports both JSON (fetch) and form-encoded (traditional). */
$content_type = $_SERVER['CONTENT_TYPE'] ?? '';

if (str_contains($content_type, 'application/json')) {
    $raw  = file_get_contents('php://input');
    $data = json_decode($raw, true) ?? [];
} else {
    $data = $_POST;
}

/* ── Sanitise all inputs ────────────────────────────────────*/
$full_name      = clean($data['name']         ?? '');
$phone          = clean($data['phone']        ?? '');
$email          = clean($data['email']        ?? '');
$address        = clean($data['address']      ?? '');
$suburb         = clean($data['suburb']       ?? '');
$postcode       = clean($data['postcode']     ?? '');
$service_type   = clean($data['service']      ?? '');
$hours_required = clean($data['hours']        ?? 'Not sure');
$preferred_time = clean($data['preferred']    ?? '');
$notes          = clean($data['notes']        ?? '');

/* ── Server-side validation ─────────────────────────────────*/
$errors = [];

if (strlen($full_name) < 2)               $errors[] = 'Full name is required.';
if (!preg_match('/^[\d\s\+\(\)]{7,}$/', $phone))
                                           $errors[] = 'A valid phone number is required.';
if (!valid_email($email))                 $errors[] = 'A valid email address is required.';
if (strlen($address) < 4)                $errors[] = 'Property address is required.';
if (strlen($suburb) < 2)                 $errors[] = 'Suburb is required.';
if (strlen($service_type) < 2)           $errors[] = 'Please select a service type.';

/* Postcode: optional, but if provided must be 4 digits */
if ($postcode !== '' && !preg_match('/^\d{4}$/', $postcode)) {
    $errors[] = 'Postcode must be 4 digits.';
}

/* Length caps — prevent oversized inputs */
if (strlen($full_name)    > 120) $errors[] = 'Full name is too long.';
if (strlen($email)        > 180) $errors[] = 'Email address is too long.';
if (strlen($address)      > 255) $errors[] = 'Address is too long.';
if (strlen($suburb)       > 100) $errors[] = 'Suburb is too long.';
if (strlen($service_type) > 100) $errors[] = 'Invalid service type.';
if (strlen($notes)        > 2000) $errors[] = 'Notes must be under 2000 characters.';

if (!empty($errors)) {
    http_response_code(422);
    json_response(false, implode(' ', $errors));
}

/* ── Database insert (prepared statement) ───────────────────*/
$conn = db_connect();

$stmt = $conn->prepare(
    'INSERT INTO quote_requests
       (full_name, phone, email, address, suburb, postcode,
        service_type, hours_required, preferred_time, notes, ip_address)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'
);

if (!$stmt) {
    $conn->close();
    http_response_code(500);
    json_response(false, 'A server error occurred. Please try again.');
}

$stmt->bind_param(
    'sssssssssss',
    $full_name,
    $phone,
    $email,
    $address,
    $suburb,
    $postcode,
    $service_type,
    $hours_required,
    $preferred_time,
    $notes,
    $client_ip
);

$ok = $stmt->execute();
$insert_id = $stmt->insert_id;
$stmt->close();
$conn->close();

if (!$ok) {
    http_response_code(500);
    json_response(false, 'Could not save your request. Please try again.');
}

/* ── Success ────────────────────────────────────────────────*/
$ref = 'GGQ-' . str_pad((string)$insert_id, 5, '0', STR_PAD_LEFT);

json_response(true, 'Quote request received.', [
    'ref'     => $ref,
    'service' => $service_type,
]);
