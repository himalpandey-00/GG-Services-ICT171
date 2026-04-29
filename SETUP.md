# GG Services — PHP/MySQL Backend Setup Guide
# ICT171 | Student: 35352086 | Murdoch University
# ==============================================

## Files Delivered

```
gg-site/
├── backend/
│   ├── config.php              ← DB credentials + shared functions
│   ├── submit_quote.php        ← Handles quote form POST
│   ├── submit_application.php  ← Handles job application POST + file uploads
│   ├── database.sql            ← Run once to create DB and tables
│   └── .htaccess               ← Blocks direct browser access to config.php
│
├── uploads/
│   ├── .htaccess               ← Blocks ALL web access to uploaded files
│   ├── cv/                     ← CV/resume files stored here (renamed)
│   └── coverletter/            ← Cover letter files stored here (renamed)
│
├── quote.html                  ← Updated — posts to backend/submit_quote.php
├── job-senior-cleaner.html     ← Updated — posts to backend/submit_application.php
├── job-casual-cleaner.html     ← Updated
└── job-driver-logistics.html   ← Updated
```

---

## LOCAL SETUP (XAMPP on Windows or MAMP on Mac)

### Step 1 — Install XAMPP
Download from https://www.apachefriends.org and install.
Start Apache and MySQL from the XAMPP Control Panel.

### Step 2 — Copy project files
Copy the entire gg-site folder to:
  Windows: C:\xampp\htdocs\gg-site\
  Mac:     /Applications/MAMP/htdocs/gg-site/

### Step 3 — Create the database
Open your browser and go to: http://localhost/phpmyadmin
Click "Import" → Choose file → select backend/database.sql → Click "Go"

This creates the gg_services database with two tables:
  - quote_requests
  - job_applications

### Step 4 — Check config.php credentials
Open backend/config.php and confirm these match your XAMPP setup:
  DB_HOST = 'localhost'
  DB_USER = 'root'
  DB_PASS = ''          (XAMPP default is blank)
  DB_NAME = 'gg_services'

### Step 5 — Set uploads folder permissions (Mac/Linux only)
  chmod 750 uploads/
  chmod 750 uploads/cv/
  chmod 750 uploads/coverletter/

  (Windows XAMPP handles permissions automatically)

### Step 6 — Open the site
  http://localhost/gg-site/quote.html
  http://localhost/gg-site/job-senior-cleaner.html

Fill out a form and submit. Check phpMyAdmin — a new row should appear
in the quote_requests or job_applications table.

---

## AZURE / cPanel DEPLOYMENT

### On cPanel hosting:
1. Upload all files via File Manager or FTP.
2. Open phpMyAdmin → Create database → Import database.sql.
3. Update backend/config.php with your hosting DB credentials:
     DB_HOST = 'localhost'
     DB_USER = 'your_cpanel_db_user'
     DB_PASS = 'your_cpanel_db_password'
     DB_NAME = 'your_db_name'
4. Set permissions:
     chmod 750 uploads/
     chmod 750 uploads/cv/
     chmod 750 uploads/coverletter/
5. Test: https://www.pandey-himal.com.np/quote.html

### On Azure VM (Apache + PHP + MySQL):
  sudo apt install php php-mysqli mysql-server
  mysql -u root -p < /var/www/gg-services/backend/database.sql
  sudo chown -R www-data:www-data /var/www/gg-services/uploads/
  sudo chmod -R 750 /var/www/gg-services/uploads/

---

## WHERE DATA IS STORED

### Quote requests:
  Database: gg_services
  Table:    quote_requests
  Columns:  id, full_name, phone, email, address, suburb, postcode,
            service_type, hours_required, preferred_time, notes,
            ip_address, submitted_at

### Job applications:
  Database: gg_services
  Table:    job_applications
  Columns:  id, job_id, job_title, first_name, last_name, email, phone,
            right_to_work, availability, about,
            cv_filename (stored name), cv_original (user's original name),
            cl_filename, cl_original, ip_address, submitted_at

### Uploaded files (CVs + cover letters):
  Stored:   gg-site/uploads/cv/            (CV files)
            gg-site/uploads/coverletter/   (cover letter files)
  Format:   Random hex name + timestamp + extension
            Example: a3f9c12d8e4b7a01_1714800000.pdf
  Web access: BLOCKED — files cannot be accessed via URL
  DB record:  Only the stored filename and original name are saved in DB

---

## VIEWING SUBMITTED DATA

### In phpMyAdmin (local or cPanel):
  1. Open phpMyAdmin
  2. Select gg_services database
  3. Click quote_requests or job_applications
  4. Click "Browse" to see all rows

## To download a CV:
  CVs are stored in uploads/cv/ on the server.
  Use FTP / File Manager or SSH to access them.
  They cannot be accessed via the browser (intentionally blocked).

---

## SECURITY MEASURES IMPLEMENTED

  1. Prepared statements       — No SQL injection possible
  2. Input sanitisation        — All inputs stripped of HTML tags
  3. Server-side validation    — All required fields checked in PHP
  4. File MIME validation      — File type checked by content, not just extension
  5. Safe file renaming        — Uploaded files get random hex names on disk
  6. PHP disabled in uploads   — .htaccess blocks script execution in uploads/
  7. Web access blocked        — .htaccess denies all direct URL access to uploads/
  8. config.php protected      — .htaccess prevents browser from reading config
  9. IP rate limiting          — Max 5 quote / 3 application submissions per IP/hour
 10. No credentials in JS      — DB details only exist in PHP on the server

---

## REQUIRED PHP SETTINGS (php.ini)

For file uploads to work, verify these are set in php.ini:
  file_uploads = On
  upload_max_filesize = 5M
  post_max_size = 10M
  max_file_uploads = 2

XAMPP: Edit C:\xampp\php\php.ini and restart Apache.
cPanel: PHP Settings → PHP Options in the control panel.
