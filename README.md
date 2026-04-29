# GG Services – ICT171 Assignment 3

**Student:** Himal Pandey Sharma  
**Student Number:** 35352086  
**Unit:** ICT171 Introduction to Server Environments and Architectures  
**University:** Murdoch University, Perth WA  
**Semester:** Semester 1, 2026  

---

## Live Site

| | |
|--|--|
| **URL** | https://www.pandey-himal.com.np |
| **IP Address** | 20.92.251.195 |
| **DNS** | register.com.np → Cloudflare → Azure VM |
| **SSL** | Let's Encrypt via Certbot (HTTPS enforced) |
| **Server** | Ubuntu 24.04 LTS on Microsoft Azure |

---

## Project Overview

GG Services Pty Ltd is a family-owned cleaning company based in Perth, Western Australia, inspired by Ghodaghodi Temple in Far West Nepal. This project is built for ICT171 Assignment 3 and demonstrates a full cloud-hosted web system.

---

## Development Timeline

| Week | Dates | Work Completed |
|------|-------|----------------|
| Week 1 | 7–8 Apr 2026 | Project setup, homepage, CSS, navigation |
| Week 2 | 12–14 Apr 2026 | About page, Services listing, 10 service detail pages |
| Week 3 | 17–21 Apr 2026 | Careers, job pages, Products shop, Quote form |
| Week 4 | 25–29 Apr 2026 | PHP/MySQL backend, file uploads, Azure deployment, SSL |

---

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Frontend | HTML5, CSS3, JavaScript |
| Backend | PHP 8.3 |
| Database | MySQL 8.0 |
| Web Server | Apache 2.4 |
| Cloud | Microsoft Azure (Ubuntu 24.04 LTS) |
| DNS | Cloudflare |
| SSL | Let's Encrypt (Certbot) |
| Version Control | Git / GitHub |

---

## Website Features

- 19 HTML pages with consistent navigation
- 10 service detail pages with image sliders
- 3 job application pages with CV and cover letter upload
- Products shop with cart, filters, sort, and 3-step checkout
- Quote form connected to PHP/MySQL — data saved to database
- Job applications saved to database with files stored securely
- Fully responsive — mobile, tablet, desktop
- Accessible — ARIA labels, roles, semantic HTML throughout

---

## File Structure
---

## Local Setup (XAMPP)

1. Copy this folder into `/Applications/XAMPP/htdocs/GG/`
2. Start Apache and MySQL in XAMPP
3. Open `http://localhost/phpmyadmin` → Import → select `backend/database.sql`
4. Copy `backend/config.example.php` to `backend/config.php`
5. Update config.php with your credentials (default XAMPP: user=root, pass=blank)
6. Run: `chmod -R 777 uploads/`
7. Open `http://localhost/GG/`

---

## Cloud Deployment (Azure VM)

### Step 1 — Connect
```bash
ssh -i Himal_key.pem himal@20.92.251.195
```

### Step 2 — Clone repository
```bash
git clone https://github.com/himalpandey-00/GG-Services-ICT171.git
cd GG-Services-ICT171
```

### Step 3 — Run deploy script
```bash
sudo bash gg_deploy.sh setup
```

The script installs Apache, PHP, MySQL, imports the database, copies files, configures Apache virtual host, and obtains SSL certificate automatically.

---

## Deploy Script (gg_deploy.sh)

| Command | Description |
|---------|-------------|
| `sudo bash gg_deploy.sh setup` | Full LAMP stack setup |
| `sudo bash gg_deploy.sh health` | Health check — Apache, MySQL, PHP, DB, SSL, disk |
| `sudo bash gg_deploy.sh report` | Health check + saves dated report to /var/log/gg-services/ |

### Live Health Check Output
---

## DNS Configuration

Cloudflare DNS records:

| Type | Name | Content |
|------|------|---------|
| A | @ | 20.92.251.195 |
| A | www | 20.92.251.195 |

Nameservers at register.com.np set to:
- damiete.ns.cloudflare.com
- maisie.ns.cloudflare.com

---

## SSL/TLS

```bash
sudo certbot --apache -d pandey-himal.com.np -d www.pandey-himal.com.np --redirect
```

Auto-renewal enabled via Certbot systemd timer. Certificate valid for 89 days, renews automatically.

---

## Security

| Feature | Implementation |
|---------|---------------|
| SQL injection | Prepared statements (MySQLi) on all queries |
| Input sanitisation | strip_tags() and trim() on all user inputs |
| File validation | MIME type checked from file content, not extension |
| File storage | Files renamed to random hex — original name never used on disk |
| Upload protection | .htaccess blocks all web access to uploads/ folder |
| Rate limiting | Max 5 quotes and 3 applications per IP per hour |
| Credentials | config.php excluded from Git via .gitignore |

---

*GG Services Pty Ltd — "Your Growth, Our Commitment."*  
*Perth, Western Australia | pandey-himal.com.np*  
*Student: 35352086 | ICT171 | Murdoch University*

---

## Admin Dashboard

A password-protected admin dashboard demonstrates live Apache → PHP → MySQL integration.

**URL:** https://pandey-himal.com.np/admin.php  
**Password:** GGAdmin2026

### What it shows
- Live server info — Apache version, PHP version, MySQL version, Server IP
- Total quote requests pulled from MySQL in real time
- Total job applications pulled from MySQL in real time
- Full submission tables with reference numbers, names, emails, services, timestamps
- Proves end-to-end integration: Apache serves PHP which queries MySQL and returns live data
