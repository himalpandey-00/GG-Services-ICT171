<?php
/**
 * GG Services – Admin Dashboard
 * ICT171 | Student: 35352086 | Murdoch University
 * Simple password-protected page showing live MySQL data
 * Demonstrates: Apache → PHP → MySQL integration
 */

/* ── Basic password protection ── */
$PASSWORD = 'GGAdmin2026';
$authed   = false;

if (isset($_POST['pwd']) && $_POST['pwd'] === $PASSWORD) {
    setcookie('gg_admin', hash('sha256', $PASSWORD), time() + 3600);
    $authed = true;
} elseif (isset($_COOKIE['gg_admin']) && $_COOKIE['gg_admin'] === hash('sha256', $PASSWORD)) {
    $authed = true;
}

/* ── Login form ── */
if (!$authed) { ?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Admin Login | GG Services</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:system-ui,sans-serif;background:#0d3b2a;display:flex;align-items:center;justify-content:center;min-height:100vh}
    .card{background:#fff;border-radius:12px;padding:40px;width:100%;max-width:360px;box-shadow:0 8px 32px rgba(0,0,0,0.2)}
    .logo{text-align:center;margin-bottom:24px}
    .logo img{height:52px}
    h2{font-size:1.2rem;color:#111;margin-bottom:6px;text-align:center}
    p{font-size:13px;color:#888;text-align:center;margin-bottom:24px}
    input{width:100%;padding:12px 14px;border:1.5px solid #ddd;border-radius:8px;font-size:14px;outline:none;margin-bottom:14px}
    input:focus{border-color:#1a4b3a}
    button{width:100%;background:#1a4b3a;color:#fff;border:none;padding:13px;border-radius:8px;font-size:15px;cursor:pointer}
    button:hover{background:#0d3b2a}
    .err{color:#e24b4a;font-size:13px;text-align:center;margin-top:10px}
  </style>
</head>
<body>
  <div class="card">
    <div class="logo"><img src="img/gglogo.png" alt="GG Services" /></div>
    <h2>Admin Dashboard</h2>
    <p>ICT171 | Student: 35352086</p>
    <form method="POST">
      <input type="password" name="pwd" placeholder="Enter admin password" required autofocus />
      <button type="submit">Login</button>
      <?php if (isset($_POST['pwd'])): ?>
        <p class="err">Incorrect password.</p>
      <?php endif; ?>
    </form>
  </div>
</body>
</html>
<?php
    exit;
}

/* ── Database connection ── */
require_once __DIR__ . '/backend/config.php';
$conn = db_connect();

/* ── Fetch stats ── */
$quote_count = $conn->query("SELECT COUNT(*) FROM quote_requests")->fetch_row()[0];
$job_count   = $conn->query("SELECT COUNT(*) FROM job_applications")->fetch_row()[0];

/* ── Fetch recent quotes ── */
$quotes = $conn->query(
    "SELECT id, full_name, email, phone, service_type, suburb, submitted_at
     FROM quote_requests ORDER BY submitted_at DESC LIMIT 20"
);

/* ── Fetch recent applications ── */
$jobs = $conn->query(
    "SELECT id, first_name, last_name, email, job_title, cv_original, right_to_work, submitted_at
     FROM job_applications ORDER BY submitted_at DESC LIMIT 20"
);

/* ── Server info ── */
$php_ver    = PHP_VERSION;
$mysql_ver  = $conn->query("SELECT VERSION()")->fetch_row()[0];
$server_ip  = $_SERVER['SERVER_ADDR'] ?? '20.92.251.195';
?>
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Admin Dashboard | GG Services</title>
  <style>
    *{box-sizing:border-box;margin:0;padding:0}
    body{font-family:system-ui,sans-serif;background:#f4f6f4;color:#222;font-size:14px}

    /* Header */
    .header{background:#0d3b2a;padding:16px 32px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px}
    .header img{height:40px}
    .header-right{color:rgba(255,255,255,0.7);font-size:13px;text-align:right}
    .header-right strong{color:#fff;display:block;font-size:15px}

    /* Layout */
    .container{max-width:1200px;margin:0 auto;padding:32px 24px}

    /* Stack cards */
    .stat-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-bottom:32px}
    .stat-card{background:#fff;border-radius:10px;padding:24px;border:1px solid #e0e0e0;text-align:center}
    .stat-number{font-size:2.4rem;font-weight:700;color:#1a4b3a;line-height:1}
    .stat-label{font-size:12px;color:#888;margin-top:6px;text-transform:uppercase;letter-spacing:0.5px}

    /* Server info */
    .server-banner{background:#1a4b3a;color:#fff;border-radius:10px;padding:20px 24px;margin-bottom:32px;display:flex;flex-wrap:wrap;gap:24px;align-items:center}
    .server-banner h3{font-size:13px;text-transform:uppercase;letter-spacing:1px;color:rgba(255,255,255,0.5);margin-bottom:4px}
    .server-item strong{font-size:15px;color:#fff}
    .badge{display:inline-block;background:rgba(255,255,255,0.15);border-radius:4px;padding:2px 8px;font-size:12px;margin-left:6px}

    /* Tables */
    .section{background:#fff;border-radius:10px;border:1px solid #e0e0e0;margin-bottom:28px;overflow:hidden}
    .section-header{padding:18px 24px;border-bottom:1px solid #f0f0f0;display:flex;justify-content:space-between;align-items:center}
    .section-header h2{font-size:1rem;font-weight:600;color:#111}
    .section-header span{font-size:12px;color:#888}
    table{width:100%;border-collapse:collapse}
    th{padding:10px 16px;text-align:left;font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:0.5px;color:#888;border-bottom:1px solid #f0f0f0;background:#fafafa}
    td{padding:12px 16px;border-bottom:1px solid #f5f5f5;color:#333;vertical-align:top}
    tr:last-child td{border-bottom:none}
    tr:hover td{background:#f9fdfb}
    .id-badge{background:#e8f4f0;color:#1a4b3a;border-radius:4px;padding:2px 7px;font-size:11px;font-weight:600}
    .empty{padding:40px;text-align:center;color:#aaa}

    /* Back link */
    .back{display:inline-flex;align-items:center;gap:6px;color:#1a4b3a;font-size:13px;font-weight:500;margin-bottom:20px;text-decoration:none}
    .back:hover{text-decoration:underline}

    /* Logout */
    .logout{color:rgba(255,255,255,0.6);font-size:12px;text-decoration:none}
    .logout:hover{color:#fff}

    @media(max-width:600px){
      th,td{padding:8px 10px;font-size:12px}
      .container{padding:16px}
    }
  </style>
</head>
<body>

<!-- Header -->
<div class="header">
  <img src="img/gglogo.png" alt="GG Services" />
  <div class="header-right">
    <strong>GG Services Admin Dashboard</strong>
    ICT171 | Student: 35352086 | Murdoch University
  </div>
  <a href="?logout=1" class="logout">Logout</a>
</div>

<?php
/* Handle logout */
if (isset($_GET['logout'])) {
    setcookie('gg_admin', '', time() - 3600);
    header('Location: admin.php');
    exit;
}
?>

<div class="container">

  <a href="index.html" class="back">← Back to Website</a>

  <!-- Server info banner -->
  <div class="server-banner">
    <div class="server-item">
      <h3>Web Server</h3>
      <strong>Apache 2.4 <span class="badge">Running</span></strong>
    </div>
    <div class="server-item">
      <h3>PHP Version</h3>
      <strong><?= htmlspecialchars($php_ver) ?> <span class="badge">Active</span></strong>
    </div>
    <div class="server-item">
      <h3>MySQL Version</h3>
      <strong><?= htmlspecialchars($mysql_ver) ?> <span class="badge">Connected</span></strong>
    </div>
    <div class="server-item">
      <h3>Server IP</h3>
      <strong><?= htmlspecialchars($server_ip) ?></strong>
    </div>
    <div class="server-item">
      <h3>Domain</h3>
      <strong>pandey-himal.com.np</strong>
    </div>
  </div>

  <!-- Stats -->
  <div class="stat-grid">
    <div class="stat-card">
      <div class="stat-number"><?= $quote_count ?></div>
      <div class="stat-label">Quote Requests</div>
    </div>
    <div class="stat-card">
      <div class="stat-number"><?= $job_count ?></div>
      <div class="stat-label">Job Applications</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">19</div>
      <div class="stat-label">Website Pages</div>
    </div>
    <div class="stat-card">
      <div class="stat-number">10</div>
      <div class="stat-label">Services Listed</div>
    </div>
  </div>

  <!-- Quote requests table -->
  <div class="section">
    <div class="section-header">
      <h2>Quote Requests</h2>
      <span><?= $quote_count ?> total submissions</span>
    </div>
    <?php if ($quote_count == 0): ?>
      <p class="empty">No quote requests yet.</p>
    <?php else: ?>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Phone</th>
          <th>Service</th>
          <th>Suburb</th>
          <th>Submitted</th>
        </tr>
      </thead>
      <tbody>
        <?php while ($row = $quotes->fetch_assoc()): ?>
        <tr>
          <td><span class="id-badge">GGQ-<?= str_pad($row['id'], 5, '0', STR_PAD_LEFT) ?></span></td>
          <td><?= htmlspecialchars($row['full_name']) ?></td>
          <td><?= htmlspecialchars($row['email']) ?></td>
          <td><?= htmlspecialchars($row['phone']) ?></td>
          <td><?= htmlspecialchars($row['service_type']) ?></td>
          <td><?= htmlspecialchars($row['suburb']) ?></td>
          <td><?= htmlspecialchars($row['submitted_at']) ?></td>
        </tr>
        <?php endwhile; ?>
      </tbody>
    </table>
    <?php endif; ?>
  </div>

  <!-- Job applications table -->
  <div class="section">
    <div class="section-header">
      <h2>Job Applications</h2>
      <span><?= $job_count ?> total submissions</span>
    </div>
    <?php if ($job_count == 0): ?>
      <p class="empty">No job applications yet.</p>
    <?php else: ?>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Name</th>
          <th>Email</th>
          <th>Role</th>
          <th>CV File</th>
          <th>Right to Work</th>
          <th>Submitted</th>
        </tr>
      </thead>
      <tbody>
        <?php while ($row = $jobs->fetch_assoc()): ?>
        <tr>
          <td><span class="id-badge">GGA-<?= str_pad($row['id'], 5, '0', STR_PAD_LEFT) ?></span></td>
          <td><?= htmlspecialchars($row['first_name'] . ' ' . $row['last_name']) ?></td>
          <td><?= htmlspecialchars($row['email']) ?></td>
          <td><?= htmlspecialchars($row['job_title']) ?></td>
          <td><?= htmlspecialchars($row['cv_original']) ?></td>
          <td><?= htmlspecialchars($row['right_to_work']) ?></td>
          <td><?= htmlspecialchars($row['submitted_at']) ?></td>
        </tr>
        <?php endwhile; ?>
      </tbody>
    </table>
    <?php endif; ?>
  </div>

</div><!-- /container -->
</body>
</html>
<?php $conn->close(); ?>
