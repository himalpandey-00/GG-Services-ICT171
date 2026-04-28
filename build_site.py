"""
GG Services Website Generator
ICT171 | Student: 35352086
Generates all HTML files with proper structure:
- External CSS (css/styles.css)
- External JS (js/main.js)
- Meta descriptions
- Favicons
- Consistent nav/footer
- Clean, properly indented HTML
"""

import os

OUT = '/home/claude/gg-site'
os.makedirs(OUT, exist_ok=True)

# ─── Social SVG icons ───────────────────────────────────────
YT = '<svg class="footer-social-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M23.5 6.2a3 3 0 00-2.1-2.1C19.5 3.5 12 3.5 12 3.5s-7.5 0-9.4.5A3 3 0 00.5 6.2 31.4 31.4 0 000 12a31.4 31.4 0 00.5 5.8 3 3 0 002.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 002.1-2.1A31.4 31.4 0 0024 12a31.4 31.4 0 00-.5-5.8zM9.75 15.5V8.5l6.25 3.5-6.25 3.5z"/></svg>'
LI = '<svg class="footer-social-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M20.45 20.45h-3.55v-5.57c0-1.33-.03-3.04-1.85-3.04-1.85 0-2.14 1.45-2.14 2.94v5.67H9.36V9h3.41v1.56h.05c.47-.9 1.63-1.85 3.36-1.85 3.59 0 4.26 2.37 4.26 5.44v6.3zM5.34 7.43a2.06 2.06 0 110-4.12 2.06 2.06 0 010 4.12zM3.56 20.45h3.55V9H3.56v11.45zM22.22 0H1.77C.79 0 0 .77 0 1.73v20.54C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.73V1.73C24 .77 23.2 0 22.22 0z"/></svg>'
FB = '<svg class="footer-social-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M24 12.07C24 5.41 18.63 0 12 0S0 5.41 0 12.07C0 18.1 4.39 23.1 10.13 24v-8.44H7.08v-3.49h3.04V9.41c0-3.02 1.8-4.7 4.54-4.7 1.31 0 2.68.24 2.68.24v2.97h-1.51c-1.49 0-1.95.93-1.95 1.88v2.27h3.32l-.53 3.5h-2.79V24C19.61 23.1 24 18.1 24 12.07z"/></svg>'
IG = '<svg class="footer-social-icon" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 3.25.15 4.77 1.69 4.92 4.92.06 1.27.07 1.65.07 4.85 0 3.2-.01 3.58-.07 4.85-.15 3.23-1.66 4.77-4.92 4.92-1.27.06-1.64.07-4.85.07-3.2 0-3.58-.01-4.85-.07-3.26-.15-4.77-1.7-4.92-4.92C2.17 15.58 2.16 15.2 2.16 12c0-3.2.01-3.58.07-4.85C2.38 3.86 3.9 2.31 7.15 2.23 8.42 2.17 8.8 2.16 12 2.16zM12 0C8.74 0 8.33.01 7.05.07 2.7.27.27 2.7.07 7.05.01 8.33 0 8.74 0 12c0 3.26.01 3.67.07 4.95.2 4.36 2.62 6.78 6.98 6.98C8.33 23.99 8.74 24 12 24c3.26 0 3.67-.01 4.95-.07 4.35-.2 6.78-2.62 6.98-6.98.06-1.28.07-1.69.07-4.95 0-3.26-.01-3.67-.07-4.95-.2-4.35-2.62-6.78-6.98-6.98C15.67.01 15.26 0 12 0zm0 5.84a6.16 6.16 0 100 12.32A6.16 6.16 0 0012 5.84zM12 16a4 4 0 110-8 4 4 0 010 8zm6.4-11.85a1.44 1.44 0 100 2.88 1.44 1.44 0 000-2.88z"/></svg>'

# ─── Shared HTML components ──────────────────────────────────

def html_head(title, description, css_path='css/styles.css'):
    """Generate the <head> section with all required meta tags."""
    return f'''  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta name="description" content="{description}" />
  <meta name="author" content="GG Services Pty Ltd" />
  <title>{title} | GG Services – Professional Cleaning Perth, WA</title>

  <!-- Favicon -->
  <link rel="icon" type="image/png" href="img/gglogo.png" />

  <!-- Google Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet" />

  <!-- Stylesheet -->
  <link rel="stylesheet" href="{css_path}" />'''


def nav_html(active_page=''):
    """Generate the sticky navigation bar with Home + all links."""
    pages = [
        ('index.html',    'Home'),
        ('services.html', 'Services'),
        ('products.html', 'Buy Products'),
        ('careers.html',  'Careers'),
        ('about.html',    'About Us'),
    ]
    desktop_links = ''
    mobile_links  = ''
    for href, label in pages:
        active = ' class="active"' if href == active_page else ''
        desktop_links += f'      <li><a href="{href}"{active}>{label}</a></li>\n'
        mobile_links  += f'    <a href="{href}"{active}>{label}</a>\n'

    return f'''<header class="nav-wrapper" role="banner">
  <nav class="nav-inner" aria-label="Main navigation">
    <!-- Logo — always returns to homepage -->
    <a href="index.html" class="logo" title="GG Services — Home">
      <img src="img/gglogo.png" alt="GG Services logo" />
    </a>

    <!-- Desktop navigation links -->
    <ul class="nav-links" role="list">
{desktop_links}      <li><a href="quote.html" class="nav-cta">Book a Quote</a></li>
    </ul>

    <!-- Mobile hamburger button -->
    <button class="hamburger" id="hamburger" aria-label="Toggle navigation menu" aria-expanded="false">
      <span></span>
      <span></span>
      <span></span>
    </button>
  </nav>

  <!-- Mobile dropdown menu -->
  <div class="mobile-menu" id="mobileMenu" role="navigation" aria-label="Mobile navigation">
{mobile_links}    <a href="quote.html" class="nav-cta" style="margin:4px 12px;border-radius:8px;text-align:center">Book a Quote</a>
  </div>
</header>'''


FOOTER_HTML = f'''<footer class="footer" role="contentinfo">
  <div class="container footer-inner">

    <!-- Brand column -->
    <div class="footer-brand">
      <a href="index.html" class="footer-logo-wrap" title="GG Services — Home">
        <img src="img/gglogo.png" alt="GG Services logo" class="footer-logo" />
      </a>
      <p>Professional cleaning solutions for Perth, Western Australia.</p>
      <p style="font-size:12px;color:rgba(255,255,255,.25)">© 2026 GG Services Pty Ltd</p>
    </div>

    <!-- Company links -->
    <div class="footer-links">
      <h4>Company</h4>
      <a href="about.html">About Us</a>
      <a href="careers.html">Careers</a>
      <a href="quote.html">Book a Quote</a>
    </div>

    <!-- Services links -->
    <div class="footer-links">
      <h4>Services</h4>
      <a href="services.html#house">House Cleaning</a>
      <a href="services.html#commercial">Commercial</a>
      <a href="services.html#healthcare">Healthcare</a>
      <a href="services.html">All Services</a>
    </div>

    <!-- Social links -->
    <div class="footer-links">
      <h4>Connect</h4>
      <a href="https://www.youtube.com/watch?v=yNJJ0OiDOLA" target="_blank" rel="noopener noreferrer">{YT} YouTube</a>
      <a href="https://www.linkedin.com/in/h1mal-pandey/" target="_blank" rel="noopener noreferrer">{LI} LinkedIn</a>
      <a href="https://www.facebook.com/h1malpandey" target="_blank" rel="noopener noreferrer">{FB} Facebook</a>
      <a href="https://www.instagram.com/h1mal_pandey/" target="_blank" rel="noopener noreferrer">{IG} Instagram</a>
    </div>

  </div>

  <!-- Footer bottom bar -->
  <div class="footer-bottom">
    <p>© Copyright 2026, GG Services Pty Ltd. All rights reserved.</p>
    <div class="footer-legal">
      <a href="#">Privacy Policy</a>
      <a href="#">Terms of Service</a>
    </div>
  </div>
</footer>'''


def js_scripts(extra=''):
    """Generate script tags at end of body."""
    return f'''  <!-- Main JavaScript -->
  <script src="js/main.js"></script>
{extra}'''


def full_page(title, description, active_page, body_html, extra_js='', extra_head=''):
    """Assemble a complete HTML page."""
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
{html_head(title, description)}
{extra_head}</head>
<body>

{nav_html(active_page)}

{body_html}

{FOOTER_HTML}

<script src="js/main.js"></script>
{extra_js}
</body>
</html>
'''

print("Build module loaded OK")

# ═══════════════════════════════════════════════════════════
# INDEX.HTML — Homepage
# ═══════════════════════════════════════════════════════════

INDEX_BODY = '''
<!-- ── HERO ── -->
<section class="hero" aria-label="Hero section">
  <div class="hero-left">
    <p class="hero-eyebrow">Perth, Western Australia</p>
    <p class="hero-tagline">Your Growth, Our Commitment</p>
    <h1 class="hero-title">Welcome to<br>GG Services</h1>
    <p class="hero-desc">
      Professional cleaning services you can rely on. Based in Perth, GG Services delivers
      high-standard residential, commercial, and specialised cleaning solutions — with a strong
      focus on quality, safety, and customer satisfaction.
    </p>
    <p class="hero-sub">
      Our team is fully trained, reliable, and committed to delivering consistent results on every project.
    </p>
    <div class="hero-actions">
      <a href="quote.html" class="hero-btn-primary">Book a Quote</a>
      <a href="services.html" class="hero-btn-ghost">View Services</a>
    </div>
  </div>
  <div class="hero-right" aria-hidden="true">
    <img src="img/background.jpg" alt="GG Services professional cleaners at work in a Perth property" />
  </div>
</section>

<!-- ── TRUST BAR ── -->
<section class="trust-bar" aria-label="Trust indicators">
  <div class="trust-inner">
    <div class="trust-item">
      <svg width="15" height="15" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M10 2L12.4 7.2L18 8.1L14 12L15.2 18L10 15.4L4.8 18L6 12L2 8.1L7.6 7.2L10 2Z" fill="#1a4b3a"/></svg>
      Trusted by Perth Families
    </div>
    <div class="trust-sep" aria-hidden="true"></div>
    <div class="trust-item">
      <svg width="15" height="15" viewBox="0 0 20 20" fill="none" aria-hidden="true"><rect x="3" y="9" width="14" height="9" rx="2" stroke="#1a4b3a" stroke-width="1.5"/><path d="M7 9V6a3 3 0 016 0v3" stroke="#1a4b3a" stroke-width="1.5" stroke-linecap="round"/></svg>
      Fully Insured
    </div>
    <div class="trust-sep" aria-hidden="true"></div>
    <div class="trust-item">
      <svg width="15" height="15" viewBox="0 0 20 20" fill="none" aria-hidden="true"><circle cx="10" cy="10" r="7" stroke="#1a4b3a" stroke-width="1.5"/><path d="M7 10l2 2 4-4" stroke="#1a4b3a" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
      Satisfaction Guaranteed
    </div>
    <div class="trust-sep" aria-hidden="true"></div>
    <div class="trust-item">
      <svg width="15" height="15" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M10 3v5l3 3" stroke="#1a4b3a" stroke-width="1.5" stroke-linecap="round"/><circle cx="10" cy="10" r="7" stroke="#1a4b3a" stroke-width="1.5"/></svg>
      Flexible Scheduling
    </div>
    <div class="trust-sep" aria-hidden="true"></div>
    <div class="trust-item">
      <svg width="15" height="15" viewBox="0 0 20 20" fill="none" aria-hidden="true"><path d="M3 10h14M10 3v14" stroke="#1a4b3a" stroke-width="1.5" stroke-linecap="round"/></svg>
      10+ Services Offered
    </div>
  </div>
</section>

<!-- ── SERVICES OVERVIEW ── -->
<section class="services-section" aria-labelledby="services-heading">
  <div class="container">
    <div class="section-header">
      <p class="section-eyebrow">What We Do</p>
      <h2 class="section-title" id="services-heading">Our Range of Services</h2>
      <p class="section-desc">From residential to commercial and specialised environments, GG Services delivers excellence in every clean.</p>
    </div>

    <div class="services-grid">
      <a href="services.html#house" class="service-card reveal">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
        </div>
        <h3>House Cleaning</h3>
        <p>End of lease, regular and one-off residential cleaning tailored to your needs.</p>
        <span class="card-link">Learn more →</span>
      </a>

      <a href="services.html#commercial" class="service-card featured reveal">
        <span class="service-badge">Popular</span>
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/></svg>
        </div>
        <h3>Commercial Cleaning</h3>
        <p>Office buildings, carpet, window, hazard cleaning for Perth businesses.</p>
        <span class="card-link">Learn more →</span>
      </a>

      <a href="services.html#floor" class="service-card reveal">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>
        </div>
        <h3>Floor &amp; Tiles</h3>
        <p>Professional strip and sealing to restore and protect all hard floor surfaces.</p>
        <span class="card-link">Learn more →</span>
      </a>

      <a href="services.html#healthcare" class="service-card reveal">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
        </div>
        <h3>Healthcare Cleaning</h3>
        <p>Specialised sanitation for aged care, nursing homes, and hospital environments.</p>
        <span class="card-link">Learn more →</span>
      </a>

      <a href="services.html#kitchen" class="service-card reveal">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 002-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 00-5 5v6c0 1.1.9 2 2 2h3z"/></svg>
        </div>
        <h3>Kitchen Cleaning</h3>
        <p>Deep degreasing and sanitation for commercial and domestic kitchens.</p>
        <span class="card-link">Learn more →</span>
      </a>

      <a href="services.html" class="service-card reveal" style="display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;">
        <div class="service-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="8" y1="6" x2="21" y2="6"/><line x1="8" y1="12" x2="21" y2="12"/><line x1="8" y1="18" x2="21" y2="18"/><line x1="3" y1="6" x2="3.01" y2="6"/><line x1="3" y1="12" x2="3.01" y2="12"/><line x1="3" y1="18" x2="3.01" y2="18"/></svg>
        </div>
        <h3>All Services</h3>
        <p>See our complete list of professional cleaning services across Perth.</p>
        <span class="card-link">View all →</span>
      </a>
    </div>

    <div class="services-cta">
      <a href="services.html" class="btn-outline">View All Services</a>
    </div>
  </div>
</section>

<!-- ── ABOUT STRIP ── -->
<section class="about-strip" aria-labelledby="about-strip-heading">
  <div class="about-strip-inner">
    <div class="about-strip-text">
      <p class="section-eyebrow">Our Story</p>
      <h2 id="about-strip-heading">Rooted in Heritage,<br>Built on Trust</h2>
      <p>
        GG Services is named after <strong>Ghodaghodi Temple</strong> — one of the most renowned
        and culturally significant places in Far West Nepal. That heritage shapes everything we do:
        trust, care, and an unwavering commitment to our community.
      </p>
      <p>
        A proud Perth family-owned business bringing the same values we grew up with into every
        home and workplace we serve.
      </p>
      <a href="about.html" class="btn-primary" style="margin-top:8px">About Us</a>
    </div>

    <div class="values-list" aria-label="Core values">
      <div class="value-item reveal">
        <div class="value-dot" aria-hidden="true"></div>
        <div>
          <strong>Trust</strong>
          <p>We earn it with every clean, every visit — no shortcuts.</p>
        </div>
      </div>
      <div class="value-item reveal">
        <div class="value-dot" aria-hidden="true"></div>
        <div>
          <strong>Care</strong>
          <p>Your space is treated like our own, with genuine attention to detail.</p>
        </div>
      </div>
      <div class="value-item reveal">
        <div class="value-dot" aria-hidden="true"></div>
        <div>
          <strong>Commitment</strong>
          <p>We show up on time, every time, and see every job through.</p>
        </div>
      </div>
      <div class="value-item reveal">
        <div class="value-dot" aria-hidden="true"></div>
        <div>
          <strong>Community</strong>
          <p>Local business, local pride — we grow together with Perth.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- ── CTA BANNER ── -->
<section class="cta-banner" aria-label="Call to action">
  <div class="cta-inner">
    <h2>Ready for a Cleaner Space?</h2>
    <p>Get a free quote today — no obligation, just professional advice.</p>
    <a href="quote.html" class="btn-white">Book a Quote →</a>
  </div>
</section>
'''

with open(f'{OUT}/index.html', 'w') as f:
    f.write(full_page(
        title='Home',
        description='GG Services provides professional residential, commercial, and healthcare cleaning across Perth, WA. Family-owned, fully insured, satisfaction guaranteed. Book a free quote today.',
        active_page='index.html',
        body_html=INDEX_BODY
    ))
print("index.html ✓")

# ═══════════════════════════════════════════════════════════
# ABOUT.HTML
# ═══════════════════════════════════════════════════════════
ABOUT_BODY = '''
<!-- ── ABOUT HERO ── -->
<section class="about-hero" aria-label="About GG Services hero">
  <img class="hero-bg" src="img/partner.jpg" alt="GG Services founding team at a cultural event" />
  <div class="about-hero-overlay" aria-hidden="true"></div>
  <div class="about-hero-content">
    <p class="eyebrow">Who We Are</p>
    <h1>About GG Services</h1>
    <p>A Perth family business rooted in Nepali heritage — built on trust, care, and a genuine commitment to our community.</p>
  </div>
</section>

<!-- ── WHO WE ARE ── -->
<section class="who-section" aria-labelledby="who-heading">
  <div class="container">
    <div class="who-grid">

      <!-- Left: story text -->
      <div class="who-text">
        <p class="who-label">Our Heritage</p>
        <h2 id="who-heading">Named After a Sacred Place,<br>Built With Purpose</h2>

        <p>
          GG Services Pty Ltd is a family-owned cleaning company based in Perth, Western Australia,
          dedicated to delivering reliable, high-quality cleaning solutions for homes, businesses,
          and healthcare environments.
        </p>
        <p>
          Our name is inspired by <strong>Ghodaghodi Temple</strong> — one of the most renowned
          and culturally significant places in Far West Nepal. This heritage reflects our core values
          of trust, care, and commitment to serving our community with integrity.
        </p>
        <p>
          At GG Services, we take pride in providing professional, detail-oriented cleaning services
          tailored to each client's unique needs. We believe in building long-term relationships
          through consistent service, transparency, and a strong work ethic.
        </p>

        <a href="quote.html" class="btn-primary" style="margin-top:16px;display:inline-block">Book a Quote</a>

        <div class="stats-grid" style="margin-top:32px">
          <div class="stat-box reveal">
            <div class="stat-number">10+</div>
            <div class="stat-label">Services Offered</div>
          </div>
          <div class="stat-box reveal">
            <div class="stat-number">Perth</div>
            <div class="stat-label">Western Australia</div>
          </div>
          <div class="stat-box reveal">
            <div class="stat-number">100%</div>
            <div class="stat-label">Family Owned</div>
          </div>
          <div class="stat-box reveal">
            <div class="stat-number">6</div>
            <div class="stat-label">Team Members</div>
          </div>
        </div>
      </div>

      <!-- Right: key facts -->
      <div>
        <p class="who-label">Key Facts</p>
        <div class="facts-panel">
          <div class="fact-item">
            <div class="fact-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>
            </div>
            <div>
              <strong>Inspired by Ghodaghodi Temple</strong>
              <span>Far West Nepal — a sacred place that shaped our name and values.</span>
            </div>
          </div>
          <div class="fact-item">
            <div class="fact-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            </div>
            <div>
              <strong>Based in Perth, Western Australia</strong>
              <span>Proudly serving the Perth metro area and surrounding suburbs.</span>
            </div>
          </div>
          <div class="fact-item">
            <div class="fact-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
            </div>
            <div>
              <strong>Family-owned &amp; operated</strong>
              <span>Every team member is personally invested in the quality of every job.</span>
            </div>
          </div>
          <div class="fact-item">
            <div class="fact-icon" aria-hidden="true">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0110 0v4"/></svg>
            </div>
            <div>
              <strong>Fully insured — satisfaction guaranteed</strong>
              <span>Every job is backed by our quality guarantee. Not happy? We'll make it right.</span>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</section>

<!-- ── CORE VALUES ── -->
<section class="values-section" aria-labelledby="values-heading">
  <div class="container">
    <div class="section-header">
      <p class="section-eyebrow">What Drives Us</p>
      <h2 class="section-title" id="values-heading">Our Core Values</h2>
      <p class="section-desc">These principles guide every decision we make, every service we deliver, and every relationship we build.</p>
    </div>

    <div class="values-grid">
      <div class="value-card reveal">
        <div class="value-card-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>
        </div>
        <h3>Trust</h3>
        <p>We earn your trust through consistent, transparent service. When we commit, we deliver — every time.</p>
      </div>

      <div class="value-card reveal">
        <div class="value-card-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20.84 4.61a5.5 5.5 0 00-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 00-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 000-7.78z"/></svg>
        </div>
        <h3>Care</h3>
        <p>We treat every space as if it were our own — with genuine attention to detail, respect, and pride.</p>
      </div>

      <div class="value-card reveal">
        <div class="value-card-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12,6 12,12 16,14"/></svg>
        </div>
        <h3>Commitment</h3>
        <p>We go the extra mile on every job. We are not satisfied until you are — that is our promise.</p>
      </div>

      <div class="value-card reveal">
        <div class="value-card-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87"/><path d="M16 3.13a4 4 0 010 7.75"/></svg>
        </div>
        <h3>Community</h3>
        <p>We support local, hire local, and grow together with the people and businesses we serve.</p>
      </div>

      <div class="value-card reveal">
        <div class="value-card-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
        </div>
        <h3>Integrity</h3>
        <p>Transparent pricing, honest communication, no hidden surprises — what we say is what we do.</p>
      </div>

      <div class="value-card reveal">
        <div class="value-card-icon" aria-hidden="true">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><polyline points="22,12 18,12 15,21 9,3 6,12 2,12"/></svg>
        </div>
        <h3>Excellence</h3>
        <p>Continuous improvement, ongoing training, and rigorous quality control in everything we do.</p>
      </div>
    </div>
  </div>
</section>

<!-- ── MEET THE TEAM ── -->
<section class="team-section" aria-labelledby="team-heading">
  <div class="container">
    <div class="section-header">
      <p class="section-eyebrow">The People Behind GG Services</p>
      <h2 class="section-title" id="team-heading">Meet Our Team</h2>
      <p class="section-desc">A dedicated leadership team united by shared values and a genuine commitment to Perth\'s community.</p>
    </div>

    <div class="team-grid">

      <div class="team-card reveal">
        <div class="team-photo">
          <img src="img/team/Bishal.jpg" alt="Bishal Dhakal — Founder"
               onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />
          <div class="team-initials" style="display:none">BD</div>
        </div>
        <p class="team-name">Bishal Dhakal</p>
        <p class="team-role">Founder</p>
        <p class="team-bio">Visionary behind GG Services, driven by a passion for quality and community.</p>
      </div>

      <div class="team-card reveal">
        <div class="team-photo">
          <img src="img/team/Himal.jpg" alt="Himal Pandey Sharma — Executive Manager"
               onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />
          <div class="team-initials" style="display:none">HP</div>
        </div>
        <p class="team-name">Himal Pandey Sharma</p>
        <p class="team-role">Executive Manager</p>
        <p class="team-bio">Oversees all operations ensuring every client receives exceptional service.</p>
      </div>

      <div class="team-card reveal">
        <div class="team-photo">
          <img src="img/team/Kushal.jpg" alt="Kushal Dhakal — Financial Advisor"
               onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />
          <div class="team-initials" style="display:none">KD</div>
        </div>
        <p class="team-name">Kushal Dhakal</p>
        <p class="team-role">Financial Advisor</p>
        <p class="team-bio">Manages financial strategy and planning to ensure sustainable growth.</p>
      </div>

      <div class="team-card reveal">
        <div class="team-photo">
          <img src="img/team/Bibek.jpg" alt="Bibek Dhakal — Marketing Manager"
               onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />
          <div class="team-initials" style="display:none">BD</div>
        </div>
        <p class="team-name">Bibek Dhakal</p>
        <p class="team-role">Marketing &amp; Stakeholder Manager</p>
        <p class="team-bio">Drives brand growth and manages key client and partner relationships.</p>
      </div>

      <div class="team-card reveal">
        <div class="team-photo">
          <img src="img/team/Ananda.jpg" alt="Ananda Dhakal — Chief Information Officer"
               onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />
          <div class="team-initials" style="display:none">AD</div>
        </div>
        <p class="team-name">Ananda Dhakal</p>
        <p class="team-role">Chief Information Officer</p>
        <p class="team-bio">Leads our digital infrastructure and technology transformation.</p>
      </div>

      <div class="team-card reveal">
        <div class="team-photo">
          <img src="img/team/Krish.jpg" alt="Krish Neupane — Customer Engagement Manager"
               onerror="this.style.display=\'none\';this.nextElementSibling.style.display=\'flex\'" />
          <div class="team-initials" style="display:none">KN</div>
        </div>
        <p class="team-name">Krish Neupane</p>
        <p class="team-role">Customer Engagement Manager</p>
        <p class="team-bio">Ensures every client interaction is professional, warm, and responsive.</p>
      </div>

    </div>
  </div>
</section>

<!-- ── CTA ── -->
<section class="cta-banner" aria-label="Call to action">
  <div class="cta-inner">
    <h2>Ready to Work With Us?</h2>
    <p>Join Perth households and businesses who trust GG Services for all their cleaning needs.</p>
    <a href="quote.html" class="btn-white">Book a Free Quote →</a>
  </div>
</section>
'''

with open(f'{OUT}/about.html', 'w') as f:
    f.write(full_page(
        title='About Us',
        description='Learn about GG Services — a Perth family-owned cleaning company inspired by Ghodaghodi Temple in Far West Nepal. Meet our team and discover our values.',
        active_page='about.html',
        body_html=ABOUT_BODY
    ))
print("about.html ✓")

# ═══════════════════════════════════════════════════════════
# SERVICES.HTML
# ═══════════════════════════════════════════════════════════

# SVG icons for each category
ICON_HOUSE = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9,22 9,12 15,12 15,22"/></svg>'
ICON_COMMERCIAL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 7V5a2 2 0 00-2-2h-4a2 2 0 00-2 2v2"/></svg>'
ICON_FLOOR = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/></svg>'
ICON_HEALTH = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>'
ICON_KITCHEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M3 2v7c0 1.1.9 2 2 2h4a2 2 0 002-2V2"/><path d="M7 2v20"/><path d="M21 15V2a5 5 0 00-5 5v6c0 1.1.9 2 2 2h3z"/></svg>'

def service_category(anchor, icon_svg, title, desc, cards):
    """Render a service category block with sub-cards."""
    cards_html = ''
    for href, img, name, blurb in cards:
        cards_html += f'''        <a href="{href}" class="sub-card">
          <div class="sub-card-img">
            <img src="{img}" alt="{name}" loading="lazy" />
          </div>
          <div class="sub-card-body">
            <h3>{name}</h3>
            <p>{blurb}</p>
            <span class="sub-card-link">View details →</span>
          </div>
        </a>
'''
    return f'''    <!-- {title} -->
    <div class="category-block" id="{anchor}">
      <div class="category-header">
        <div class="category-icon" aria-hidden="true">{icon_svg}</div>
        <div>
          <h2>{title}</h2>
          <p>{desc}</p>
        </div>
      </div>
      <div class="sub-grid">
{cards_html}      </div>
    </div>
'''

SERVICES_BODY = '''
<section class="page-hero" aria-label="Services page hero">
  <p class="eyebrow">What We Offer</p>
  <h1>Our Range of Services</h1>
  <p>Professional, detail-oriented cleaning for every environment — tailored to your needs across Perth, WA.</p>
</section>

<section class="services-page" aria-label="All services">
  <div class="container">
''' + service_category(
    'house', ICON_HOUSE,
    'House Cleaning', 'Comprehensive residential cleaning services for every situation.',
    [
        ('service-endoflease.html', 'img/services/endoflease.jpg', 'End of Lease Cleaning', 'Bond-back guaranteed deep cleans meeting real estate agent standards across Perth.'),
        ('service-regular.html',    'img/services/regular.jpg',    'Regular Cleaning',       'Scheduled weekly or fortnightly maintenance cleaning to keep your home in top condition.'),
    ]
) + service_category(
    'commercial', ICON_COMMERCIAL,
    'Commercial Cleaning', 'Professional services for offices, businesses, and commercial premises.',
    [
        ('service-office.html',  'img/services/Office.jpg',  'Office Building Cleaning',   'Thorough cleaning of offices, reception areas, kitchenettes — after-hours available.'),
        ('service-carpet.html',  'img/services/Carpet.jpg',  'Carpet Cleaning',            'Hot-water extraction and dry methods to remove dirt, stains, and allergens.'),
        ('service-window.html',  'img/services/Window.jpg',  'Window and Glass Cleaning',  'Streak-free results inside and out using professional-grade tools.'),
        ('service-hazard.html',  'img/services/Hazard.jpg',  'Hazard Cleaning',            'Mould, biohazard, trauma, and post-event cleaning — handled discreetly.'),
    ]
) + service_category(
    'floor', ICON_FLOOR,
    'Floor and Tiles', 'Restore, protect, and maintain all hard floor surfaces.',
    [
        ('service-strip.html', 'img/services/Stripe.jpg', 'Strip and Sealing', 'Old sealant removal, deep scrub, and fresh protective sealer for a showroom finish.'),
    ]
) + service_category(
    'healthcare', ICON_HEALTH,
    'Health Care Cleaning', 'Infection-control cleaning for sensitive healthcare environments.',
    [
        ('service-agedcare.html', 'img/services/AgedCare.jpg', 'Aged Care and Nursing Home', 'Compassionate, thorough cleaning that respects resident dignity and safety.'),
        ('service-hospital.html', 'img/services/Hospital.jpg', 'Hospital Cleaning',          'Hospital-grade disinfection compliant with AS/NZS standards.'),
    ]
) + service_category(
    'kitchen', ICON_KITCHEN,
    'Kitchen Cleaning', 'Deep kitchen degreasing and sanitation for commercial and domestic environments.',
    [
        ('service-kitchen.html', 'img/services/kitchen.jpg', 'Kitchen Cleaning', 'Oven, rangehood, splashback, and full kitchen degreasing — commercial and residential.'),
    ]
) + '''  </div>
</section>

<section class="cta-banner" aria-label="Call to action">
  <div class="cta-inner">
    <h2>Not Sure What You Need?</h2>
    <p>Fill out our quote form and we\'ll recommend the right service for you.</p>
    <a href="quote.html" class="btn-white">Book a Free Quote →</a>
  </div>
</section>
'''

with open(f'{OUT}/services.html', 'w') as f:
    f.write(full_page(
        title='Our Services',
        description='Browse GG Services\' full range of professional cleaning services in Perth WA — house, commercial, healthcare, floor, and kitchen cleaning.',
        active_page='services.html',
        body_html=SERVICES_BODY
    ))
print("services.html ✓")

# ═══════════════════════════════════════════════════════════
# SERVICE DETAIL PAGES — one template, all 10 services
# ═══════════════════════════════════════════════════════════

SERVICE_DATA = [
    {
        'file': 'service-endoflease.html',
        'title': 'End of Lease Cleaning',
        'category': 'House Cleaning',
        'tagline': 'Bond-back guaranteed deep cleans that meet real estate agent standards across Perth, WA.',
        'img': 'img/services/endoflease.jpg',
        'about': 'Our end of lease cleaning is designed to get your bond back in full. We follow the real estate industry standard checklist and guarantee a thorough clean of every room, surface, and fixture. If the agent requests a re-clean for any covered area within 72 hours, we return at no additional cost.',
        'includes': [
            'Full kitchen deep clean — oven, stovetop, rangehood, cupboards',
            'Bathroom and toilet scrubbed to a high standard',
            'All floors vacuumed and mopped',
            'Windows, sills, and fly screens cleaned inside',
            'Light fittings, fans, and switches wiped down',
            'Marks removed from walls where possible',
            'Garage sweep if applicable',
        ],
        'highlights': ['Bond-back guarantee', 'Free re-clean within 72 hours', 'Full property checklist', 'Available 7 days a week', 'Flexible booking times'],
        'desc': 'Professional end of lease cleaning in Perth with a bond-back guarantee. GG Services follows real estate agent checklists to ensure full bond returns.',
    },
    {
        'file': 'service-regular.html',
        'title': 'Regular Cleaning',
        'category': 'House Cleaning',
        'tagline': 'Scheduled weekly or fortnightly maintenance cleaning to keep your home in perfect condition.',
        'img': 'img/services/regular.jpg',
        'about': 'Our regular cleaning service keeps your home consistently clean without the stress. We work to a customised schedule — weekly, fortnightly, or monthly — using professional products safe for your family and pets.',
        'includes': [
            'Kitchen surfaces, sink, stovetop, and appliance fronts',
            'Bathroom and toilet cleaned and disinfected',
            'All rooms vacuumed and mopped',
            'Dusting of all surfaces including shelves and furniture',
            'Bins emptied and relined',
            'Beds made on request',
            'Customisable checklist available',
        ],
        'highlights': ['Flexible scheduling', 'Same cleaner where possible', 'Insured and background-checked staff', 'Eco-friendly products available', 'Easy rescheduling'],
        'desc': 'Regular house cleaning in Perth by GG Services. Weekly or fortnightly home cleaning using professional products safe for families and pets.',
    },
    {
        'file': 'service-office.html',
        'title': 'Office Building Cleaning',
        'category': 'Commercial Cleaning',
        'tagline': 'Thorough professional cleaning for offices and commercial premises — after-hours service available.',
        'img': 'img/services/Office.jpg',
        'about': 'GG Services provides reliable and professional office cleaning tailored to Perth businesses. We understand a clean workplace boosts productivity and creates a strong first impression. All office cleaning is available outside business hours to minimise disruption.',
        'includes': [
            'Workstations, desks, and monitors wiped down',
            'Reception and waiting areas cleaned',
            'Kitchen and break room sanitation',
            'Bathroom and amenity restocking',
            'Bins emptied and waste removed',
            'Floors vacuumed or mopped',
            'Glass partitions and entry doors cleaned',
        ],
        'highlights': ['After-hours availability', 'Key-holder arrangements available', 'Recurring contract pricing', 'Police-checked staff', 'Certificate of Currency provided'],
        'desc': 'Professional office building cleaning in Perth by GG Services. After-hours commercial cleaning for businesses of all sizes.',
    },
    {
        'file': 'service-carpet.html',
        'title': 'Carpet Cleaning',
        'category': 'Commercial Cleaning',
        'tagline': 'Hot-water extraction and dry methods to remove embedded dirt, stains, and allergens.',
        'img': 'img/services/Carpet.jpg',
        'about': 'Our carpet cleaning service uses industry-standard hot-water extraction equipment to deep clean carpets, removing embedded soil, pet dander, bacteria, and allergens. We also offer dry-cleaning for delicate carpets. Carpets are typically dry within 2–4 hours.',
        'includes': [
            'Hot-water extraction (steam cleaning)',
            'Dry carpet cleaning for sensitive fibres',
            'Pre-treatment of stains and high-traffic areas',
            'Deodorising treatment available',
            'Scotchgard stain protection available',
            'Suitable for residential and commercial carpets',
            'Area rugs cleaned on-site or off-site',
        ],
        'highlights': ['Carpets dry in 2–4 hours', 'Stain pre-treatment included', 'Safe for children and pets', 'Commercial-grade equipment', 'All carpet types catered for'],
        'desc': 'Professional carpet cleaning in Perth using hot-water extraction. Safe for all carpet types, residential and commercial. GG Services Perth.',
    },
    {
        'file': 'service-window.html',
        'title': 'Window and Glass Cleaning',
        'category': 'Commercial Cleaning',
        'tagline': 'Streak-free results inside and out using professional-grade squeegees and purified water systems.',
        'img': 'img/services/Window.jpg',
        'about': 'Clear, streak-free windows make an immediate difference to any property. Our team uses purified water-fed pole systems for exterior windows and traditional squeegee methods for interior surfaces — delivering a spotless result every time.',
        'includes': [
            'Interior window glass and frames cleaned',
            'Exterior glass cleaned using purified water systems',
            'Window sills and tracks wiped down',
            'Fly screen cleaning available',
            'Shopfront and commercial glass',
            'Skylights and high-reach windows (pole access)',
            'Available as one-off or regular service',
        ],
        'highlights': ['Streak-free guarantee', 'Purified water system for exteriors', 'Fly screens cleaned on request', 'Safe and non-invasive methods', 'Available 7 days a week'],
        'desc': 'Professional window and glass cleaning in Perth. Streak-free results using purified water systems. GG Services — residential and commercial.',
    },
    {
        'file': 'service-hazard.html',
        'title': 'Hazard Cleaning',
        'category': 'Commercial Cleaning',
        'tagline': 'Specialised cleaning for mould, biohazard, trauma, and post-event situations — handled discreetly.',
        'img': 'img/services/Hazard.jpg',
        'about': 'GG Services provides discreet, professional hazard cleaning for sensitive situations including mould remediation, post-trauma cleaning, biohazard incidents, and post-event clean-ups. Our trained staff follow strict safety protocols using hospital-grade disinfectants.',
        'includes': [
            'Mould detection and full remediation',
            'Biohazard and trauma scene cleaning',
            'Post-event and party clean-up',
            'Chemical and substance spill clean-up',
            'Sewage and water damage clean-up',
            'Discreet and respectful service delivery',
            'Compliant disposal of contaminated materials',
        ],
        'highlights': ['Fully trained specialist team', 'Strict safety protocols followed', 'Hospital-grade disinfectants used', 'Discreet and professional', 'Police-checked staff'],
        'desc': 'Professional hazard cleaning services in Perth — mould remediation, biohazard, trauma, and post-event cleaning. Discreet and fully trained.',
    },
    {
        'file': 'service-strip.html',
        'title': 'Strip and Sealing',
        'category': 'Floor and Tiles',
        'tagline': 'Old sealant removal, deep scrub, and fresh protective sealer application for a showroom finish.',
        'img': 'img/services/Stripe.jpg',
        'about': 'Over time, floor sealant becomes worn, yellowed, and difficult to clean. Our strip and seal service completely removes the old finish, scrubs the floor to its original surface, and applies fresh layers of high-quality protective sealer. The result is a floor that looks brand new.',
        'includes': [
            'Complete removal of old sealant using professional strippers',
            'Machine scrubbing of floor surface',
            'Grout cleaning and restoration',
            'Application of 2–3 coats of fresh sealant',
            'Buffing to a high-gloss or satin finish',
            'Suitable for vinyl, timber, and tile floors',
            'After-hours work available to minimise downtime',
        ],
        'highlights': ['Floor looks brand new', 'Multiple finish options', 'Protects against future wear', 'All hard floor types', 'Commercial scheduling available'],
        'desc': 'Professional floor strip and sealing services in Perth by GG Services. Restore vinyl, tile, and timber floors to a showroom finish.',
    },
    {
        'file': 'service-agedcare.html',
        'title': 'Aged Care and Nursing Home Cleaning',
        'category': 'Health Care Cleaning',
        'tagline': 'Compassionate, infection-control cleaning for aged care facilities and nursing homes across Perth.',
        'img': 'img/services/AgedCare.jpg',
        'about': 'Cleaning in aged care environments requires sensitivity, reliability, and strict adherence to infection control standards. GG Services staff are trained in aged care-specific cleaning protocols, treating all residents with dignity and respect.',
        'includes': [
            'Resident room cleaning and disinfection',
            'Common area and dining room sanitation',
            'Bathroom and shower room hygiene maintenance',
            'High-touch surface disinfection (handrails, switches, handles)',
            'Waste management compliant with healthcare guidelines',
            'Odour management and floor care',
            'Coordination with facility staff and schedules',
        ],
        'highlights': ['Trained in infection control', 'Respectful of residents', 'Aged Care Quality Standards compliant', 'Police-checked and uniformed staff', 'Flexible scheduling'],
        'desc': 'Professional aged care and nursing home cleaning in Perth. Infection-control trained staff. GG Services — compassionate, reliable cleaning.',
    },
    {
        'file': 'service-hospital.html',
        'title': 'Hospital Cleaning',
        'category': 'Health Care Cleaning',
        'tagline': 'Hospital-grade disinfection compliant with AS/NZS standards for clinical environments.',
        'img': 'img/services/Hospital.jpg',
        'about': 'Hospital and clinical cleaning requires specialist knowledge, TGA-registered products, and strict compliance with AS/NZS 4187 standards. GG Services provides trained clinical cleaning teams for hospitals, day surgeries, medical centres, and allied health facilities.',
        'includes': [
            'Terminal cleaning of operating theatres and treatment rooms',
            'Ward, corridor, and common area disinfection',
            'Colour-coded equipment to prevent cross-contamination',
            'High-touch surface disinfection protocols',
            'Waste segregation and disposal compliance',
            'Spill kits and immediate response capability',
            'Documented cleaning records for audits',
        ],
        'highlights': ['TGA-registered products', 'AS/NZS 4187 compliant', 'Colour-coded cleaning systems', 'Trained clinical staff', 'Documentation and audit trail'],
        'desc': 'Hospital and clinical cleaning services in Perth — AS/NZS 4187 compliant, TGA-registered disinfectants. GG Services healthcare cleaning specialists.',
    },
    {
        'file': 'service-kitchen.html',
        'title': 'Kitchen Cleaning',
        'category': 'Kitchen Cleaning',
        'tagline': 'Deep degreasing and full sanitation of commercial and domestic kitchens to the highest standard.',
        'img': 'img/services/kitchen.jpg',
        'about': 'Commercial kitchens accumulate grease, carbon, and bacteria faster than any other surface. Our deep kitchen cleaning service uses hot degreasers, steam, and specialised scrubbing tools to restore every surface to a hygienic and compliant standard.',
        'includes': [
            'Oven, grill, and fryer degreasing',
            'Rangehood, filter, and duct cleaning',
            'Splashback and tile scrubbing',
            'Benchtop and prep surface sanitation',
            'Floor degreasing and disinfection',
            'Refrigerator and cool room cleaning available',
            'Suitable for commercial and domestic kitchens',
        ],
        'highlights': ['After-hours for commercial kitchens', 'Food Safety Standard compliant', 'Hot degreaser and steam equipment', 'Grease and odour elimination', 'Suitable for health inspections'],
        'desc': 'Professional kitchen cleaning in Perth for commercial and residential kitchens. Deep degreasing, rangehood cleaning, Food Safety Standard compliant.',
    },
]


def make_service_detail(svc):
    """Generate a complete service detail page."""
    includes_html = '\n'.join(f'        <li>{item}</li>' for item in svc['includes'])
    highlights_html = '\n'.join(
        f'''        <div class="highlight-item">
          <div class="hl-dot" aria-hidden="true"></div>
          {h}
        </div>''' for h in svc['highlights']
    )

    body = f'''
<div class="svc-hero" aria-label="{svc['title']} hero">
  <div class="svc-hero-inner">
    <a href="services.html" class="back-link" aria-label="Back to all services">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      Back to Services
    </a>
    <p class="category-label">{svc['category']}</p>
    <h1>{svc['title']}</h1>
    <p>{svc['tagline']}</p>
  </div>
</div>

<div class="svc-body">

  <!-- Main content -->
  <div>
    <!-- Image slider -->
    <div class="img-slider" role="region" aria-label="{svc['title']} photos">
      <div class="slider-track" id="sliderTrack">
        <div class="slide"><img src="{svc['img']}" alt="{svc['title']} — photo 1" loading="lazy" /></div>
        <div class="slide"><img src="{svc['img']}" alt="{svc['title']} — photo 2" loading="lazy" /></div>
        <div class="slide"><img src="{svc['img']}" alt="{svc['title']} — photo 3" loading="lazy" /></div>
      </div>
      <button class="slider-btn slider-prev" onclick="slide(-1)" aria-label="Previous image">&#8249;</button>
      <button class="slider-btn slider-next" onclick="slide(1)" aria-label="Next image">&#8250;</button>
    </div>
    <div class="slider-dots" id="sliderDots" aria-label="Slide indicators">
      <button class="dot active" onclick="goSlide(0)" aria-label="Slide 1"></button>
      <button class="dot" onclick="goSlide(1)" aria-label="Slide 2"></button>
      <button class="dot" onclick="goSlide(2)" aria-label="Slide 3"></button>
    </div>

    <!-- About this service -->
    <div class="info-block">
      <h2>About This Service</h2>
      <p>{svc['about']}</p>
    </div>

    <!-- What's included -->
    <div class="info-block">
      <h2>What\'s Included</h2>
      <ul class="check-list">
{includes_html}
      </ul>
    </div>
  </div>

  <!-- Sidebar -->
  <aside class="svc-sidebar" aria-label="Book this service">
    <div class="sidebar-card">
      <h3>Book This Service</h3>
      <p>We\'ll call you back within 2–4 business hours with a tailored quote.</p>
      <a href="quote.html?service={svc['file'].replace('.html','')}" class="sidebar-btn">Book a Quote →</a>
      <a href="services.html" class="sidebar-btn ghost">← All Services</a>
      <div class="highlights">
        <h4>Service Highlights</h4>
{highlights_html}
      </div>
    </div>
  </aside>

</div>

<section class="cta-banner" aria-label="Call to action">
  <div class="cta-inner">
    <h2>Ready to Book {svc['title']}?</h2>
    <p>Get a free tailored quote — no obligation, just professional advice.</p>
    <a href="quote.html" class="btn-white">Book a Free Quote →</a>
  </div>
</section>

<script>
  /* Simple image slider */
  let current = 0;
  const total = 3;
  const track = document.getElementById('sliderTrack');
  const dots = document.querySelectorAll('.dot');

  function goSlide(n) {{
    current = n;
    track.style.transform = 'translateX(-' + (current * 100) + '%)';
    dots.forEach((d, i) => d.classList.toggle('active', i === current));
  }}

  function slide(dir) {{
    goSlide((current + dir + total) % total);
  }}

  /* Auto-advance every 4.5 seconds */
  setInterval(() => slide(1), 4500);
</script>
'''
    return full_page(
        title=svc['title'],
        description=svc['desc'],
        active_page='services.html',
        body_html=body
    )


for svc in SERVICE_DATA:
    with open(f'{OUT}/{svc["file"]}', 'w') as f:
        f.write(make_service_detail(svc))
    print(f"{svc['file']} ✓")

# ═══════════════════════════════════════════════════════════
# CAREERS.HTML + 3 JOB DETAIL PAGES
# ═══════════════════════════════════════════════════════════

CAREERS_BODY = '''
<section class="page-hero" aria-label="Careers hero">
  <p class="eyebrow">Join Our Team</p>
  <h1>Current Opportunities</h1>
  <p>We\'re growing our team in Perth, WA. Find a role where you can make a real difference and be part of something we\'re genuinely proud of.</p>
</section>

<section class="jobs-section" aria-labelledby="jobs-heading">
  <div class="container">

    <div class="jobs-header">
      <div>
        <h2 id="jobs-heading">Open Positions</h2>
        <p>Perth, Western Australia · All roles are in-person</p>
      </div>
    </div>

    <!-- Search and filter bar -->
    <div class="filter-bar" role="search" aria-label="Filter job listings">
      <input
        type="text"
        id="jobSearch"
        placeholder="Search by title or keyword…"
        oninput="filterJobs()"
        aria-label="Search jobs"
      />
      <select id="typeFilter" onchange="filterJobs()" aria-label="Filter by employment type">
        <option value="">All employment types</option>
        <option value="Full-time">Full-time</option>
        <option value="Part-time">Part-time</option>
        <option value="Casual">Casual</option>
      </select>
    </div>

    <p class="job-count" aria-live="polite"><span id="jobCountNum">3</span> positions available</p>

    <!-- Job listings rendered by JS -->
    <div id="jobsList" role="list" aria-label="Job listings"></div>

    <!-- No results message -->
    <div id="noJobsMsg" class="no-jobs" style="display:none" aria-live="polite">
      <p style="font-size:16px;margin-bottom:6px">No matching positions found.</p>
      <p style="font-size:14px">Try adjusting your search or check back soon for new openings.</p>
    </div>

  </div>
</section>

<section class="cta-banner" aria-label="Call to action">
  <div class="cta-inner">
    <h2>Don\'t See the Right Role?</h2>
    <p>Send us a general application and we\'ll keep you in mind for future openings.</p>
    <a href="mailto:careers@ggservices.com.au?subject=General%20Application" class="btn-white">Send a General Application →</a>
  </div>
</section>
'''

CAREERS_JS = '''<script>
/* Job listing data */
const JOBS = [
  {
    id: 'senior-cleaner',
    title: 'Senior Cleaner',
    type: 'Full-time',
    salary: '$26–$30/hr + super',
    location: 'Perth, WA',
    closes: '30 May 2026',
    summary: 'Lead a small cleaning team and deliver high-quality results across residential and commercial sites throughout Perth metro.'
  },
  {
    id: 'casual-cleaner',
    title: 'Casual Cleaner',
    type: 'Casual',
    salary: '$25–$27/hr + loading',
    location: 'Perth, WA',
    closes: '30 May 2026',
    summary: 'Flexible casual shifts across residential and end-of-lease cleaning. Great for students or those seeking additional income.'
  },
  {
    id: 'driver-logistics',
    title: 'Driver / Logistics Support',
    type: 'Part-time',
    salary: '$24–$26/hr + super',
    location: 'Perth, WA',
    closes: '15 June 2026',
    summary: 'Transport cleaning staff and equipment to job sites across Perth metro. Company vehicle provided.'
  }
];

/** Render the list of jobs filtered by search and type. */
function filterJobs() {
  const query    = document.getElementById('jobSearch').value.toLowerCase();
  const typeFilter = document.getElementById('typeFilter').value;

  const filtered = JOBS.filter(j => {
    const matchesText = !query || j.title.toLowerCase().includes(query) || j.summary.toLowerCase().includes(query);
    const matchesType = !typeFilter || j.type === typeFilter;
    return matchesText && matchesType;
  });

  renderJobs(filtered);
}

/** Build and insert job card HTML into the DOM. */
function renderJobs(list) {
  const container = document.getElementById('jobsList');
  const noMsg     = document.getElementById('noJobsMsg');
  const countEl   = document.getElementById('jobCountNum');

  countEl.textContent = list.length;

  if (!list.length) {
    container.innerHTML = '';
    noMsg.style.display = 'block';
    return;
  }

  noMsg.style.display = 'none';

  container.innerHTML = list.map(j => `
    <div class="job-card" role="listitem" onclick="window.location.href='job-${j.id}.html'" style="cursor:pointer;" aria-label="View ${j.title} role">
      <div class="job-info">
        <h3>${j.title}</h3>
        <p class="job-summary">${j.summary}</p>
        <div class="job-tags">
          <span class="job-tag tag-type">${j.type}</span>
          <span class="job-tag tag-location">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0118 0z"/><circle cx="12" cy="10" r="3"/></svg>
            ${j.location}
          </span>
          <span class="job-tag tag-salary">${j.salary}</span>
        </div>
      </div>
      <div class="job-action">
        <p class="job-close-date">Closes ${j.closes}</p>
        <button
          class="btn-view-job"
          onclick="event.stopPropagation(); window.location.href='job-${j.id}.html';"
          aria-label="View and apply for ${j.title}"
        >
          View &amp; Apply
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </button>
      </div>
    </div>
  `).join('');
}

/* Render all jobs on page load */
renderJobs(JOBS);
</script>
'''

with open(f'{OUT}/careers.html', 'w') as f:
    f.write(full_page(
        title='Careers',
        description='Join the GG Services team in Perth, WA. View current job openings and apply online — cleaning, logistics, and management roles available.',
        active_page='careers.html',
        body_html=CAREERS_BODY,
        extra_js=CAREERS_JS
    ))
print("careers.html ✓")


# ─── Job detail pages ────────────────────────────────────────
JOB_DATA = [
    {
        'id': 'senior-cleaner',
        'title': 'Senior Cleaner',
        'type': 'Full-time',
        'salary': '$26–$30/hr + super',
        'location': 'Perth, WA',
        'closes': '30 May 2026',
        'tagline': 'Lead a small cleaning team and deliver high-quality results across residential and commercial sites throughout Perth metro.',
        'about': '''As a Senior Cleaner at GG Services, you will lead a team of 2–3 cleaners across residential and commercial sites in Perth. You will be responsible for quality control, ensuring all work meets our high standards, and acting as the primary on-site contact for clients.

This is an excellent opportunity for an experienced cleaner ready to take the next step in their career with a growing Perth family business.''',
        'responsibilities': [
            'Lead and supervise a small cleaning team across multiple sites',
            'Perform high-quality cleaning to GG Services standards',
            'Conduct quality inspections before leaving each site',
            'Liaise professionally with clients on-site',
            'Manage cleaning supplies and report replenishment needs',
            'Train new team members in GG Services procedures',
            'Report any incidents, damages, or concerns to management promptly',
        ],
        'requirements': [
            'Minimum 2 years of professional cleaning experience',
            'Previous team leadership or supervisory experience (preferred)',
            'Valid Australian driver\'s licence',
            'Strong communication and organisational skills',
            'Reliable, punctual, and highly detail-oriented',
            'National Police Clearance (or willingness to obtain)',
            'Valid right to work in Australia',
        ],
        'provided': ['All cleaning equipment and products', 'Uniform provided', 'Vehicle / travel reimbursement', 'Ongoing training and development', 'Performance bonuses'],
        'desc': 'Senior Cleaner — Full-time role with GG Services Perth. Lead a cleaning team, $26–$30/hr + super. Apply online.',
    },
    {
        'id': 'casual-cleaner',
        'title': 'Casual Cleaner',
        'type': 'Casual',
        'salary': '$25–$27/hr + loading',
        'location': 'Perth, WA',
        'closes': '30 May 2026',
        'tagline': 'Flexible casual shifts across residential and end-of-lease cleaning. Great for students or those seeking additional income.',
        'about': '''We are looking for reliable, hardworking casual cleaners to join our growing team in Perth. You will work flexible shifts completing residential and end-of-lease cleans to a high standard.

No prior experience is required — we provide full training. What matters most is a positive attitude and a strong work ethic.''',
        'responsibilities': [
            'Perform high-quality residential and end-of-lease cleaning',
            'Follow the GG Services cleaning checklist for each job',
            'Maintain a professional and friendly attitude with clients',
            'Communicate issues or delays promptly to your team leader',
            'Use all cleaning products safely and according to instructions',
            'Complete all assigned jobs on time and to a high standard',
            'Represent GG Services with professionalism and care',
        ],
        'requirements': [
            'No experience necessary — full paid training provided',
            'Reliable, punctual, and physically capable',
            'Good communication skills and a positive attitude',
            'Own transport preferred (not essential)',
            'Valid right to work in Australia',
            'National Police Clearance (or willingness to obtain)',
        ],
        'provided': ['Full paid training', 'All cleaning equipment and products', 'Uniform provided', 'Flexible scheduling', 'Supportive team environment'],
        'desc': 'Casual Cleaner — Flexible shifts with GG Services Perth. No experience needed, training provided. $25–$27/hr + casual loading. Apply online.',
    },
    {
        'id': 'driver-logistics',
        'title': 'Driver / Logistics Support',
        'type': 'Part-time',
        'salary': '$24–$26/hr + super',
        'location': 'Perth, WA',
        'closes': '15 June 2026',
        'tagline': 'Transport our cleaning crew and equipment to job sites across Perth metro. Company vehicle provided.',
        'about': '''GG Services is looking for a reliable and friendly Driver to join our logistics team. You will transport our cleaning crew and equipment to sites across Perth, coordinate schedules, and help keep our operations running smoothly.

A great part-time opportunity for someone who enjoys driving and working as part of a close-knit family business.''',
        'responsibilities': [
            'Transport cleaning team and equipment to job sites across Perth',
            'Maintain accurate trip records and mileage logs',
            'Assist with loading and unloading of equipment',
            'Coordinate pick-up and drop-off schedules with team leaders',
            'Ensure the company vehicle is clean and well-maintained',
            'Report any vehicle issues or maintenance needs promptly',
            'Represent GG Services professionally at all times',
        ],
        'requirements': [
            'Valid Australian driver\'s licence (minimum C class)',
            'Clean driving record — no recent serious offences',
            'Strong time management and punctuality',
            'Good communication and interpersonal skills',
            'Physically capable of assisting with loading equipment',
            'Valid right to work in Australia',
            'National Police Clearance (or willingness to obtain)',
        ],
        'provided': ['Company vehicle provided', 'Fuel and running costs covered', 'Uniform provided', 'Flexible part-time scheduling', 'Supportive team environment'],
        'desc': 'Driver / Logistics Support — Part-time with GG Services Perth. Company vehicle provided. $24–$26/hr + super. Apply online.',
    },
]


def make_job_page(job):
    """Generate a complete job detail + apply form page."""
    resp_html  = '\n'.join(f'        <li>{r}</li>' for r in job['responsibilities'])
    req_html   = '\n'.join(f'        <li>{r}</li>' for r in job['requirements'])
    prov_tags  = '\n'.join(f'        <span class="provided-tag">{p}</span>' for p in job['provided'])

    body = f'''
<div class="job-hero" aria-label="{job['title']} job listing">
  <div class="job-hero-inner">
    <a href="careers.html" class="back-link" aria-label="Back to all jobs">
      <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M19 12H5M12 19l-7-7 7-7"/></svg>
      Back to all jobs
    </a>
    <h1>{job['title']}</h1>
    <div class="job-meta-badges">
      <span class="job-badge jb-type">{job['type']}</span>
      <span class="job-badge jb-location">{job['location']}</span>
      <span class="job-badge jb-salary">{job['salary']}</span>
      <span class="job-badge jb-closes">Closes {job['closes']}</span>
    </div>
    <p>{job['tagline']}</p>
  </div>
</div>

<div class="job-detail-body">

  <!-- Role details -->
  <div>
    <div class="job-detail-block">
      <h2>About the Role</h2>
      <p>{job['about']}</p>
    </div>

    <div class="job-detail-block">
      <h2>Key Responsibilities</h2>
      <ul class="check-list">
{resp_html}
      </ul>
    </div>

    <div class="job-detail-block">
      <h2>What We\'re Looking For</h2>
      <ul class="check-list">
{req_html}
      </ul>
    </div>

    <div class="job-detail-block">
      <h2>What GG Services Provides</h2>
      <div class="provided-tags">
{prov_tags}
      </div>
    </div>
  </div>

  <!-- Apply form -->
  <aside class="apply-card" aria-label="Apply for this role">

    <div id="applyFormWrap">
      <h2>Apply for this Role</h2>
      <p class="form-sub">Complete the form below. We review all applications and respond within 2 business days.</p>

      <div class="form-row">
        <div class="form-group">
          <label for="af-first">First Name <span class="req" aria-hidden="true">*</span></label>
          <input type="text" id="af-first" name="firstName" placeholder="Himal" autocomplete="given-name" required aria-required="true" />
          <p class="error-message" id="err-first" role="alert">Please enter your first name.</p>
        </div>
        <div class="form-group">
          <label for="af-last">Last Name <span class="req" aria-hidden="true">*</span></label>
          <input type="text" id="af-last" name="lastName" placeholder="Pandey" autocomplete="family-name" required aria-required="true" />
          <p class="error-message" id="err-last" role="alert">Please enter your last name.</p>
        </div>
      </div>

      <div class="form-group">
        <label for="af-email">Email Address <span class="req" aria-hidden="true">*</span></label>
        <input type="email" id="af-email" name="email" placeholder="you@example.com" autocomplete="email" required aria-required="true" />
        <p class="error-message" id="err-email" role="alert">Please enter a valid email address.</p>
      </div>

      <div class="form-group">
        <label for="af-phone">Phone Number <span class="req" aria-hidden="true">*</span></label>
        <input type="tel" id="af-phone" name="phone" placeholder="04XX XXX XXX" autocomplete="tel" required aria-required="true" />
        <p class="error-message" id="err-phone" role="alert">Please enter a valid phone number.</p>
      </div>

      <div class="form-group">
        <label for="af-visa">Right to Work in Australia <span class="req" aria-hidden="true">*</span></label>
        <select id="af-visa" name="visaStatus" required aria-required="true">
          <option value="">— Select —</option>
          <option>Australian Citizen</option>
          <option>Permanent Resident</option>
          <option>Working Holiday Visa</option>
          <option>Student Visa (20 hrs/week)</option>
          <option>Other Work Visa</option>
        </select>
        <p class="error-message" id="err-visa" role="alert">Please select your right to work status.</p>
      </div>

      <div class="form-group">
        <label for="af-avail">Availability</label>
        <select id="af-avail" name="availability">
          <option value="Flexible">Flexible</option>
          <option value="Weekdays only">Weekdays only</option>
          <option value="Weekends only">Weekends only</option>
          <option value="Both weekdays and weekends">Both weekdays and weekends</option>
        </select>
      </div>

      <!-- CV / Resume upload -->
      <div class="form-group">
        <label>Upload CV / Resume <span class="req" aria-hidden="true">*</span></label>
        <div class="upload-area" id="cvDropZone">
          <input type="file" id="af-cv" name="cvFile" accept=".pdf,.doc,.docx" onchange="handleFileUpload(this, 'cv-chosen', 'err-cv')" aria-label="Upload CV or resume file" />
          <div class="upload-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15v4a2 2 0 01-2 2H5a2 2 0 01-2-2v-4"/><polyline points="17,8 12,3 7,8"/><line x1="12" y1="3" x2="12" y2="15"/></svg>
          </div>
          <p>Click to upload or drag &amp; drop</p>
          <p class="upload-hint">PDF, DOC, DOCX · Max 5MB</p>
          <p class="file-chosen" id="cv-chosen"></p>
        </div>
        <p class="error-message" id="err-cv" role="alert">Please upload your CV or resume.</p>
      </div>

      <!-- Cover letter upload (optional) -->
      <div class="form-group">
        <label>Cover Letter <span style="font-weight:400;color:var(--text-muted)">(optional)</span></label>
        <div class="upload-area" id="clDropZone">
          <input type="file" id="af-cl" name="coverLetter" accept=".pdf,.doc,.docx" onchange="handleFileUpload(this, 'cl-chosen', null)" aria-label="Upload cover letter file" />
          <div class="upload-icon" aria-hidden="true">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14,2 14,8 20,8"/></svg>
          </div>
          <p>Upload cover letter</p>
          <p class="upload-hint">PDF, DOC, DOCX · Max 5MB</p>
          <p class="file-chosen" id="cl-chosen"></p>
        </div>
      </div>

      <div class="form-group">
        <label for="af-about">Tell Us About Yourself</label>
        <textarea id="af-about" name="aboutYou" placeholder="Briefly describe your experience and why you\'d like to join GG Services…"></textarea>
      </div>

      <button class="apply-submit-btn" id="applySubmitBtn" onclick="submitApplication()" type="button">
        <span id="applyBtnText">Submit Application →</span>
        <div class="spinner" id="applySpinner" aria-hidden="true"></div>
      </button>
      <p style="font-size:12px;color:var(--text-muted);text-align:center;margin-top:10px">We respond to all applications within 2 business days.</p>
    </div>

    <!-- Success state (shown after submission) -->
    <div class="apply-success" id="applySuccess" role="status" aria-live="polite">
      <div class="apply-success-icon">✅</div>
      <h3>Application Submitted!</h3>
      <p>Thank you for applying for the <strong>{job['title']}</strong> position at GG Services.</p>
      <p style="margin-top:8px">Our team will review your application and be in touch within 2 business days.</p>
      <a href="careers.html">← View other positions</a>
    </div>

  </aside>

</div>

<script>
  /** Show file name after upload and clear error. */
  function handleFileUpload(input, chosenId, errorId) {{
    const file = input.files[0];
    const chosenEl = document.getElementById(chosenId);
    if (file) {{
      chosenEl.textContent = '✓ ' + file.name;
      chosenEl.style.display = 'block';
      if (errorId) document.getElementById(errorId).style.display = 'none';
    }}
  }}

  /** Enable drag-and-drop highlight on upload areas. */
  ['cvDropZone', 'clDropZone'].forEach(id => {{
    const el = document.getElementById(id);
    if (!el) return;
    el.addEventListener('dragover', e => {{ e.preventDefault(); el.classList.add('drag-over'); }});
    el.addEventListener('dragleave', () => el.classList.remove('drag-over'));
    el.addEventListener('drop', e => {{
      e.preventDefault();
      el.classList.remove('drag-over');
      const inp = el.querySelector('input[type="file"]');
      if (e.dataTransfer.files.length) {{
        inp.files = e.dataTransfer.files;
        inp.dispatchEvent(new Event('change'));
      }}
    }});
  }});

  /** Clear field error on input. */
  ['af-first','af-last','af-email','af-phone','af-visa'].forEach(id => {{
    const el = document.getElementById(id);
    if (el) el.addEventListener('input', () => {{
      el.classList.remove('field-error');
      const errId = 'err-' + id.replace('af-','');
      const errEl = document.getElementById(errId);
      if (errEl) errEl.style.display = 'none';
    }});
  }});

  /** Validate and submit the application form. */
  function submitApplication() {{
    const rules = [
      {{ id: 'af-first', errId: 'err-first',  check: v => v.trim().length > 0 }},
      {{ id: 'af-last',  errId: 'err-last',   check: v => v.trim().length > 0 }},
      {{ id: 'af-email', errId: 'err-email',  check: v => /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v.trim()) }},
      {{ id: 'af-phone', errId: 'err-phone',  check: v => /^[\\d\\s\\+\\(\\){{}}]{{8,}}$/.test(v.trim()) }},
      {{ id: 'af-visa',  errId: 'err-visa',   check: v => v !== '' }},
    ];

    let isValid = true;

    rules.forEach(rule => {{
      const input = document.getElementById(rule.id);
      const errEl = document.getElementById(rule.errId);
      if (!rule.check(input.value)) {{
        input.classList.add('field-error');
        if (errEl) errEl.style.display = 'block';
        isValid = false;
      }} else {{
        input.classList.remove('field-error');
        if (errEl) errEl.style.display = 'none';
      }}
    }});

    /* Check CV is uploaded */
    const cvFile = document.getElementById('af-cv').files[0];
    if (!cvFile) {{
      document.getElementById('err-cv').style.display = 'block';
      isValid = false;
    }}

    if (!isValid) {{
      /* Scroll to first error */
      document.querySelector('.field-error, .error-message[style*="block"]')?.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      return;
    }}

    /* Show spinner and disable button */
    document.getElementById('applyBtnText').style.display = 'none';
    document.getElementById('applySpinner').style.display = 'block';
    document.getElementById('applySubmitBtn').disabled = true;

    /* Simulate form submission — replace with real fetch() to backend */
    setTimeout(() => {{
      document.getElementById('applyFormWrap').style.display = 'none';
      document.getElementById('applySuccess').style.display = 'block';
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}, 1400);
  }}
</script>
'''
    return full_page(
        title=job['title'],
        description=job['desc'],
        active_page='careers.html',
        body_html=body
    )


for job in JOB_DATA:
    fname = f'job-{job["id"]}.html'
    with open(f'{OUT}/{fname}', 'w') as f:
        f.write(make_job_page(job))
    print(f"{fname} ✓")

# ═══════════════════════════════════════════════════════════
# QUOTE.HTML
# ═══════════════════════════════════════════════════════════

QUOTE_BODY = '''
<section class="page-hero" aria-label="Book a quote hero">
  <p class="eyebrow">Free Consultation</p>
  <h1>Book a Quote</h1>
  <p>Fill in your details and we\'ll reach out within 24 hours with a tailored quote — no obligation, no pressure.</p>
</section>

<div class="quote-layout">

  <!-- Left: explanation -->
  <div class="quote-intro">
    <h2>Get a Tailored Quote<br>for Your Cleaning Needs</h2>
    <p>Every property is different. Rather than offering a one-size-fits-all price, we take the time to understand your specific needs and provide a quote that is accurate, transparent, and competitive.</p>
    <p>We serve homes, offices, healthcare facilities, and commercial premises across Perth, WA.</p>

    <div class="process-steps">
      <div class="process-step">
        <div class="step-number" aria-hidden="true">1</div>
        <div>
          <strong>Submit your request</strong>
          <p>Tell us about your property, the service you need, and your preferred timing.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-number" aria-hidden="true">2</div>
        <div>
          <strong>We\'ll call you back</strong>
          <p>Our team contacts you within 2–4 business hours to confirm pricing and availability.</p>
        </div>
      </div>
      <div class="process-step">
        <div class="step-number" aria-hidden="true">3</div>
        <div>
          <strong>We get to work</strong>
          <p>Our trained cleaners arrive on time and deliver a spotless result — guaranteed.</p>
        </div>
      </div>
    </div>
  </div>

  <!-- Right: form card -->
  <div class="quote-form-card" role="form" aria-label="Quote request form">
    <h2>Request a Call Back</h2>
    <p class="quote-form-subtitle">
      Fields marked <span style="color:var(--green-mid)">*</span> are required.
      We respond within 2–4 hours Mon–Fri, 8am–5pm AWST.
    </p>

    <div id="quoteFormBody">

      <div class="form-row">
        <div class="form-group">
          <label for="q-name">Full Name <span class="req" aria-hidden="true">*</span></label>
          <input type="text" id="q-name" name="fullName" placeholder="Himal Pandey" autocomplete="name" required aria-required="true" />
          <p class="error-message" id="err-name" role="alert">Please enter your name.</p>
        </div>
        <div class="form-group">
          <label for="q-phone">Phone <span class="req" aria-hidden="true">*</span></label>
          <input type="tel" id="q-phone" name="phone" placeholder="04XX XXX XXX" autocomplete="tel" required aria-required="true" />
          <p class="error-message" id="err-phone" role="alert">Please enter a valid phone number.</p>
        </div>
      </div>

      <div class="form-group">
        <label for="q-email">Email Address <span class="req" aria-hidden="true">*</span></label>
        <input type="email" id="q-email" name="email" placeholder="you@example.com" autocomplete="email" required aria-required="true" />
        <p class="error-message" id="err-email" role="alert">Please enter a valid email address.</p>
      </div>

      <div class="form-group">
        <label for="q-address">Property Address <span class="req" aria-hidden="true">*</span></label>
        <input type="text" id="q-address" name="address" placeholder="123 Example St, Murdoch WA 6150" autocomplete="street-address" required aria-required="true" />
        <p class="error-message" id="err-address" role="alert">Please enter your property address.</p>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="q-suburb">Suburb <span class="req" aria-hidden="true">*</span></label>
          <input type="text" id="q-suburb" name="suburb" placeholder="Murdoch" required aria-required="true" />
          <p class="error-message" id="err-suburb" role="alert">Please enter your suburb.</p>
        </div>
        <div class="form-group">
          <label for="q-postcode">Postcode</label>
          <input type="text" id="q-postcode" name="postcode" placeholder="6150" maxlength="4" autocomplete="postal-code" />
        </div>
      </div>

      <div class="form-group">
        <label for="q-service">Type of Service <span class="req" aria-hidden="true">*</span></label>
        <select id="q-service" name="serviceType" required aria-required="true">
          <option value="">— Select a service —</option>
          <option>End of Lease Cleaning</option>
          <option>Regular House Cleaning</option>
          <option>Office Building Cleaning</option>
          <option>Carpet Cleaning</option>
          <option>Window and Glass Cleaning</option>
          <option>Hazard Cleaning</option>
          <option>Floor Strip and Sealing</option>
          <option>Aged Care Cleaning</option>
          <option>Hospital Cleaning</option>
          <option>Kitchen Cleaning</option>
          <option>Other / Not Sure</option>
        </select>
        <p class="error-message" id="err-service" role="alert">Please select a service type.</p>
      </div>

      <div class="form-row">
        <div class="form-group">
          <label for="q-hours">Hours Required</label>
          <select id="q-hours" name="hoursRequired">
            <option>Not sure</option>
            <option>2–3 hours</option>
            <option>3–5 hours</option>
            <option>5–8 hours</option>
            <option>Full day (8+ hours)</option>
          </select>
        </div>
        <div class="form-group">
          <label for="q-preferred">Preferred Date / Time</label>
          <input type="text" id="q-preferred" name="preferredTime" placeholder="e.g. Any morning, ASAP" />
        </div>
      </div>

      <div class="form-group">
        <label for="q-notes">Anything Else We Should Know?</label>
        <textarea id="q-notes" name="notes" placeholder="Pets at home, access instructions, property size, specific areas of concern…"></textarea>
      </div>

      <button class="form-submit" id="quoteSubmitBtn" onclick="submitQuote()" type="button">
        <span id="quoteBtnText">Book a Quote →</span>
        <div class="spinner" id="quoteSpinner" aria-hidden="true"></div>
      </button>

    </div>

    <!-- Success state -->
    <div class="quote-success" id="quoteSuccess" role="status" aria-live="polite">
      <div class="success-icon">✅</div>
      <h3>Quote Request Received!</h3>
      <p>Thank you for choosing GG Services, <strong id="successName"></strong>.</p>
      <p style="margin-top:8px">Our team will review your details and call you within 24 hours to discuss your tailored quote.</p>
      <a href="services.html" style="display:inline-block;margin-top:16px;font-size:14px;font-weight:500;color:var(--green-mid)">← Explore our services</a>
    </div>

  </div>
</div>
'''

QUOTE_JS = '''<script>
/*
 * Quote form validation and submission.
 *
 * Google Sheets integration:
 *  1. Open your Sheet → Extensions → Apps Script
 *  2. Paste the doPost() function from the comment below
 *  3. Deploy → New Deployment → Web App → Anyone → Deploy
 *  4. Paste the Web App URL into APPS_SCRIPT_URL below
 *
 * doPost() function for Apps Script:
 * -----------------------------------
 * function doPost(e) {
 *   try {
 *     var sheet = SpreadsheetApp
 *       .openById('1ExyIlQih4uZDXuCbYXtS0l2b6POVrEp9zp3bfEsQ3bo')
 *       .getSheetByName('Sheet1');
 *     var d = JSON.parse(e.postData.contents);
 *     if (sheet.getLastRow() === 0)
 *       sheet.appendRow(['Timestamp','Name','Phone','Email','Address','Suburb','Postcode','Service','Hours','Preferred','Notes']);
 *     sheet.appendRow([
 *       new Date().toLocaleString('en-AU', {timeZone:'Australia/Perth'}),
 *       d.name, d.phone, d.email, d.address, d.suburb, d.postcode,
 *       d.service, d.hours, d.preferred, d.notes
 *     ]);
 *     return ContentService
 *       .createTextOutput(JSON.stringify({status:'ok'}))
 *       .setMimeType(ContentService.MimeType.JSON);
 *   } catch(err) {
 *     return ContentService
 *       .createTextOutput(JSON.stringify({status:'error', message: err.toString()}))
 *       .setMimeType(ContentService.MimeType.JSON);
 *   }
 * }
 */

/* Paste your Apps Script Web App URL here to enable Google Sheets submission */
const APPS_SCRIPT_URL = 'YOUR_APPS_SCRIPT_WEB_APP_URL_HERE';

/* Validation rules */
const QUOTE_RULES = [
  { id: 'q-name',    errId: 'err-name',    check: v => v.trim().length > 1 },
  { id: 'q-phone',   errId: 'err-phone',   check: v => /^[\\d\\s\\+\\(\\)]{8,}$/.test(v.trim()) },
  { id: 'q-email',   errId: 'err-email',   check: v => /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v.trim()) },
  { id: 'q-address', errId: 'err-address', check: v => v.trim().length > 3 },
  { id: 'q-suburb',  errId: 'err-suburb',  check: v => v.trim().length > 1 },
  { id: 'q-service', errId: 'err-service', check: v => v !== '' },
];

/* Clear errors on input */
QUOTE_RULES.forEach(rule => {
  const el = document.getElementById(rule.id);
  if (el) el.addEventListener('input', () => {
    el.classList.remove('field-error');
    const errEl = document.getElementById(rule.errId);
    if (errEl) errEl.style.display = 'none';
  });
});

/* Pre-select service if passed via URL param */
window.addEventListener('DOMContentLoaded', () => {
  const params = new URLSearchParams(window.location.search);
  const svcParam = params.get('service');
  if (svcParam) {
    const sel = document.getElementById('q-service');
    const opt = [...sel.options].find(o => o.value.toLowerCase().replace(/\\s/g,'-').includes(svcParam.split('-')[0]));
    if (opt) sel.value = opt.value;
  }
});

async function submitQuote() {
  /* Validate all required fields */
  let isValid = true;

  QUOTE_RULES.forEach(rule => {
    const input = document.getElementById(rule.id);
    const errEl = document.getElementById(rule.errId);
    if (!rule.check(input.value)) {
      input.classList.add('field-error');
      if (errEl) errEl.style.display = 'block';
      isValid = false;
    } else {
      input.classList.remove('field-error');
      if (errEl) errEl.style.display = 'none';
    }
  });

  if (!isValid) {
    document.querySelector('.field-error')?.scrollIntoView({ behavior: 'smooth', block: 'center' });
    return;
  }

  /* Show spinner */
  document.getElementById('quoteBtnText').style.display = 'none';
  document.getElementById('quoteSpinner').style.display = 'block';
  document.getElementById('quoteSubmitBtn').disabled = true;

  const payload = {
    name:      document.getElementById('q-name').value.trim(),
    phone:     document.getElementById('q-phone').value.trim(),
    email:     document.getElementById('q-email').value.trim(),
    address:   document.getElementById('q-address').value.trim(),
    suburb:    document.getElementById('q-suburb').value.trim(),
    postcode:  document.getElementById('q-postcode').value.trim(),
    service:   document.getElementById('q-service').value,
    hours:     document.getElementById('q-hours').value,
    preferred: document.getElementById('q-preferred').value.trim(),
    notes:     document.getElementById('q-notes').value.trim(),
  };

  /* Submit to Google Sheets if URL is configured */
  try {
    if (APPS_SCRIPT_URL !== 'YOUR_APPS_SCRIPT_WEB_APP_URL_HERE') {
      await fetch(APPS_SCRIPT_URL, {
        method: 'POST',
        mode: 'no-cors',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(payload)
      });
    }
  } catch (e) {
    console.warn('Google Sheets submission note:', e);
  }

  /* Show success state after short delay */
  setTimeout(() => {
    document.getElementById('quoteFormBody').style.display = 'none';
    document.getElementById('successName').textContent = payload.name.split(' ')[0];
    document.getElementById('quoteSuccess').style.display = 'block';
    window.scrollTo({ top: 0, behavior: 'smooth' });
  }, 1000);
}
</script>
'''

with open(f'{OUT}/quote.html', 'w') as f:
    f.write(full_page(
        title='Book a Quote',
        description='Get a free cleaning quote from GG Services Perth. No obligation — we\'ll call you back within 24 hours with a tailored price for your home or business.',
        active_page='quote.html',
        body_html=QUOTE_BODY,
        extra_js=QUOTE_JS
    ))
print("quote.html ✓")

# ═══════════════════════════════════════════════════════════
# PRODUCTS.HTML — E-commerce shop
# ═══════════════════════════════════════════════════════════

PRODUCTS_BODY = '''
<section class="page-hero" aria-label="Products page hero">
  <p class="eyebrow">GG Services Shop</p>
  <h1>Buy Cleaning Products</h1>
  <p>Professional-grade cleaning products available for delivery and click-and-collect across Perth, WA.</p>
</section>

<div class="shop-layout">

  <!-- Sidebar Filters -->
  <aside class="shop-sidebar" aria-label="Product filters">

    <div class="sidebar-box">
      <p class="sidebar-box-title">Category</p>
      <label class="checkbox-item">
        <input type="checkbox" value="all" id="cat-all" onchange="toggleAll(this)" checked /> All Categories
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="mops" class="cat-check" onchange="applyFilters()" /> Mops &amp; Buckets
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="chemicals" class="cat-check" onchange="applyFilters()" /> Chemicals &amp; Cleaners
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="microfibre" class="cat-check" onchange="applyFilters()" /> Microfibre &amp; Cloths
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="equipment" class="cat-check" onchange="applyFilters()" /> Equipment &amp; Machines
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="ppe" class="cat-check" onchange="applyFilters()" /> PPE &amp; Safety
      </label>
    </div>

    <div class="sidebar-box">
      <p class="sidebar-box-title">Brand</p>
      <label class="checkbox-item">
        <input type="checkbox" value="oates" class="brand-check" onchange="applyFilters()" /> Oates
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="selleys" class="brand-check" onchange="applyFilters()" /> Selleys
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="proquip" class="brand-check" onchange="applyFilters()" /> ProQuip
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="rubbermaid" class="brand-check" onchange="applyFilters()" /> Rubbermaid
      </label>
      <label class="checkbox-item">
        <input type="checkbox" value="cleaneasy" class="brand-check" onchange="applyFilters()" /> CleanEasy
      </label>
    </div>

    <div class="sidebar-box">
      <p class="sidebar-box-title">Price Range</p>
      <div class="price-inputs">
        <input type="number" id="priceMin" value="0" min="0" placeholder="$0" oninput="applyFilters()" aria-label="Minimum price" />
        <span>–</span>
        <input type="number" id="priceMax" value="500" min="0" placeholder="$500" oninput="applyFilters()" aria-label="Maximum price" />
      </div>
    </div>

    <button class="btn-ghost" onclick="resetFilters()" style="width:100%">Reset Filters</button>

  </aside>

  <!-- Main shop area -->
  <main aria-label="Product listings">

    <div class="shop-toolbar">
      <div class="search-wrap" role="search" aria-label="Search products">
        <input type="text" id="productSearch" placeholder="Search products…" oninput="applyFilters()" aria-label="Search products" />
        <button aria-label="Search" type="button">&#128269;</button>
      </div>
      <select class="sort-select" id="sortSelect" onchange="applyFilters()" aria-label="Sort products">
        <option value="default">Sort: Featured</option>
        <option value="price-asc">Price: Low to High</option>
        <option value="price-desc">Price: High to Low</option>
        <option value="name-asc">Name: A–Z</option>
        <option value="name-desc">Name: Z–A</option>
      </select>
    </div>

    <div class="results-bar" aria-live="polite">
      <p><span id="productCount">20</span> products found</p>
    </div>

    <div class="product-grid" id="productGrid" role="list" aria-label="Products">
      <!-- Products rendered by JavaScript -->
    </div>

    <div id="noProductsMsg" style="display:none" class="no-jobs" aria-live="polite">
      <p style="font-size:16px;margin-bottom:6px">No products match your filters.</p>
      <p style="font-size:14px">Try adjusting your search or clearing the filters.</p>
    </div>

  </main>

</div>

<!-- ── FLOATING CART BUTTON ── -->
<button class="cart-float" id="cartFloat" onclick="openCart()" aria-label="View shopping cart">
  🛒 Cart
  <span class="cart-bubble" id="cartBubble">0</span>
</button>

<!-- ── PRODUCT DETAIL MODAL ── -->
<div class="modal-overlay" id="productModal" onclick="closeModal('productModal')" role="dialog" aria-modal="true" aria-label="Product details">
  <div class="modal-card" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal(\'productModal\')" aria-label="Close product details">&#215;</button>
    <div class="product-modal-inner" id="modalInner">
      <!-- Filled by JS -->
    </div>
  </div>
</div>

<!-- ── CART MODAL ── -->
<div class="modal-overlay" id="cartModal" onclick="closeModal(\'cartModal\')" role="dialog" aria-modal="true" aria-label="Shopping cart">
  <div class="modal-card cart-modal" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal(\'cartModal\')" aria-label="Close cart">&#215;</button>
    <h2>Your Cart</h2>
    <div class="cart-body" id="cartBody"><!-- Filled by JS --></div>
  </div>
</div>

<!-- ── CHECKOUT MODAL ── -->
<div class="modal-overlay" id="checkoutModal" onclick="closeModal(\'checkoutModal\')" role="dialog" aria-modal="true" aria-label="Checkout">
  <div class="modal-card checkout-modal" onclick="event.stopPropagation()">
    <button class="modal-close" onclick="closeModal(\'checkoutModal\')" aria-label="Close checkout">&#215;</button>

    <div id="checkoutFlow">
      <div class="checkout-steps">
        <div class="checkout-step active" id="step1tab">Delivery</div>
        <div class="checkout-step" id="step2tab">Payment</div>
        <div class="checkout-step" id="step3tab">Confirm</div>
      </div>

      <div class="checkout-body">

        <!-- Step 1: Delivery -->
        <div class="step-panel show" id="step1">
          <p class="checkout-heading">Delivery Details</p>
          <div class="form-row">
            <div class="form-group">
              <label for="ch-first">First Name <span class="req" aria-hidden="true">*</span></label>
              <input type="text" id="ch-first" name="firstName" placeholder="Himal" autocomplete="given-name" />
              <p class="error-message" id="err-ch-first" role="alert">Required</p>
            </div>
            <div class="form-group">
              <label for="ch-last">Last Name <span class="req" aria-hidden="true">*</span></label>
              <input type="text" id="ch-last" name="lastName" placeholder="Pandey" autocomplete="family-name" />
              <p class="error-message" id="err-ch-last" role="alert">Required</p>
            </div>
          </div>
          <div class="form-group">
            <label for="ch-address">Delivery Address <span class="req" aria-hidden="true">*</span></label>
            <input type="text" id="ch-address" name="address" placeholder="123 Example St, Murdoch WA 6150" autocomplete="street-address" />
            <p class="error-message" id="err-ch-address" role="alert">Required</p>
          </div>
          <div class="form-row">
            <div class="form-group">
              <label for="ch-suburb">Suburb <span class="req" aria-hidden="true">*</span></label>
              <input type="text" id="ch-suburb" name="suburb" placeholder="Murdoch" autocomplete="address-level2" />
              <p class="error-message" id="err-ch-suburb" role="alert">Required</p>
            </div>
            <div class="form-group">
              <label for="ch-post">Postcode <span class="req" aria-hidden="true">*</span></label>
              <input type="text" id="ch-post" name="postcode" placeholder="6150" maxlength="4" autocomplete="postal-code" />
              <p class="error-message" id="err-ch-post" role="alert">Required</p>
            </div>
          </div>
          <div class="form-group">
            <label for="ch-email">Email Address <span class="req" aria-hidden="true">*</span></label>
            <input type="email" id="ch-email" name="email" placeholder="you@example.com" autocomplete="email" />
            <p class="error-message" id="err-ch-email" role="alert">Enter a valid email</p>
          </div>
          <div class="form-group">
            <label for="ch-phone">Phone</label>
            <input type="tel" id="ch-phone" name="phone" placeholder="04XX XXX XXX" autocomplete="tel" />
          </div>
          <button class="pay-btn" onclick="goStep(2)" type="button">Continue to Payment →</button>
        </div>

        <!-- Step 2: Payment -->
        <div class="step-panel" id="step2">
          <p class="checkout-heading">Payment Details</p>
          <div class="card-icons">
            <span class="card-icon-badge">VISA</span>
            <span class="card-icon-badge">Mastercard</span>
            <span class="card-icon-badge">AMEX</span>
          </div>
          <div class="form-group">
            <label for="ch-cardnum">Card Number <span class="req" aria-hidden="true">*</span></label>
            <input type="text" id="ch-cardnum" name="cardNumber" placeholder="1234 5678 9012 3456" maxlength="19" inputmode="numeric" autocomplete="cc-number" oninput="fmtCard(this)" />
            <p class="error-message" id="err-ch-cardnum" role="alert">Enter a valid 16-digit card number</p>
          </div>
          <div class="form-group">
            <label for="ch-name">Name on Card <span class="req" aria-hidden="true">*</span></label>
            <input type="text" id="ch-name" name="nameOnCard" placeholder="HIMAL PANDEY" autocomplete="cc-name" />
            <p class="error-message" id="err-ch-name" role="alert">Required</p>
          </div>
          <div class="card-row">
            <div class="form-group">
              <label for="ch-expiry">Expiry Date <span class="req" aria-hidden="true">*</span></label>
              <input type="text" id="ch-expiry" name="expiry" placeholder="MM/YY" maxlength="5" inputmode="numeric" autocomplete="cc-exp" oninput="fmtExpiry(this)" />
              <p class="error-message" id="err-ch-expiry" role="alert">Enter MM/YY</p>
            </div>
            <div class="form-group">
              <label for="ch-cvv">CVV <span class="req" aria-hidden="true">*</span></label>
              <input type="text" id="ch-cvv" name="cvv" placeholder="123" maxlength="4" inputmode="numeric" autocomplete="cc-csc" />
              <p class="error-message" id="err-ch-cvv" role="alert">Required</p>
            </div>
          </div>
          <button class="pay-btn" onclick="goStep(3)" type="button">Review Order →</button>
          <button class="btn-ghost" onclick="goStep(1)" type="button" style="width:100%;margin-top:8px">← Back</button>
        </div>

        <!-- Step 3: Confirm -->
        <div class="step-panel" id="step3">
          <p class="checkout-heading">Review Your Order</p>
          <div class="order-lines" id="orderLines"><!-- filled by JS --></div>
          <div class="checkout-total" id="checkoutTotal"><!-- filled by JS --></div>
          <button class="pay-btn" id="payNowBtn" onclick="placeOrder()" type="button">Place Order →</button>
          <button class="btn-ghost" onclick="goStep(2)" type="button" style="width:100%;margin-top:8px">← Back</button>
        </div>

      </div><!-- .checkout-body -->
    </div><!-- #checkoutFlow -->

    <!-- Order success -->
    <div class="order-success" id="orderSuccess" role="status" aria-live="polite">
      <div class="order-success-icon">🎉</div>
      <h3>Order Placed!</h3>
      <p>Thank you for your order. We\'ll email you a confirmation shortly.</p>
      <p style="margin-top:10px">Estimated delivery: <strong>3–5 business days</strong> across Perth metro.</p>
      <a href="products.html" class="btn-primary" style="margin-top:18px;display:inline-block">Continue Shopping</a>
    </div>

  </div>
</div>
'''

PRODUCTS_JS = '''<script>
/* ================================================================
   PRODUCT DATA
   ================================================================ */
const PRODUCTS = [
  // Mops & Buckets
  { id:1, name:'Professional Wet Mop', brand:'Oates', category:'mops', price:34.95, rating:4.7, reviews:128, badge:'Bestseller', img:'img/products/mop.jpg', desc:'Heavy-duty cotton wet mop suitable for all hard floor surfaces. Compatible with standard 15L mop buckets.', specs:[['Material','Cotton blend'],['Handle Length','140 cm'],['Head Weight','400 g'],['Compatibility','Standard mop buckets']] },
  { id:2, name:'Commercial Mop Bucket 15L', brand:'Rubbermaid', category:'mops', price:49.95, rating:4.5, reviews:87, badge:null, img:'img/products/mop.jpg', desc:'Heavy-duty 15L commercial mop bucket with wringer. Splash guard and foot pedal for hands-free wringing.', specs:[['Capacity','15 Litres'],['Material','Polypropylene'],['Wringer','Built-in foot pedal'],['Colour','Yellow']] },
  { id:3, name:'Microfibre Flat Mop Kit', brand:'Oates', category:'mops', price:59.00, rating:4.8, reviews:215, badge:'New', img:'img/products/mop.jpg', desc:'Complete flat mop kit with telescopic handle and 4 washable microfibre heads. Machine washable up to 300 times.', specs:[['Handle','Telescopic 120–160 cm'],['Heads','4× washable microfibre'],['Floor Types','Tiles, timber, vinyl'],['Washable','Yes, 300+ times']] },

  // Chemicals
  { id:4, name:'Heavy-Duty Degreaser 5L', brand:'CleanEasy', category:'chemicals', price:29.95, rating:4.6, reviews:342, badge:'Bestseller', img:'img/products/mop.jpg', desc:'Powerful alkaline degreaser for commercial kitchens, floors, and machinery. Dilutable up to 1:50 for light-duty use.', specs:[['Volume','5 Litres'],['Type','Alkaline degreaser'],['Dilution','1:10 to 1:50'],['Suitable For','Kitchens, floors, machinery']] },
  { id:5, name:'Disinfectant Multi-Surface 5L', brand:'CleanEasy', category:'chemicals', price:24.95, rating:4.5, reviews:198, badge:null, img:'img/products/mop.jpg', desc:'Hospital-grade quaternary disinfectant. Kills 99.9% of bacteria and viruses including influenza and COVID-19.', specs:[['Volume','5 Litres'],['Type','Quaternary disinfectant'],['Kill Rate','99.9%'],['Dilution','1:20 standard']] },
  { id:6, name:'Grout & Tile Cleaner 1L', brand:'Selleys', category:'chemicals', price:12.95, rating:4.3, reviews:76, badge:null, img:'img/products/mop.jpg', desc:'Targeted tile and grout cleaner. Removes mould, soap scum, and calcium deposits without scrubbing.', specs:[['Volume','1 Litre'],['Action','Acid-based'],['Suitable For','Ceramic, porcelain tiles'],['Ready to Use','Yes']] },
  { id:7, name:'Glass & Window Cleaner 5L', brand:'CleanEasy', category:'chemicals', price:19.95, rating:4.7, reviews:154, badge:'New', img:'img/products/mop.jpg', desc:'Streak-free glass cleaner with anti-static formula. Leaves no residue on windows, mirrors, and glass partitions.', specs:[['Volume','5 Litres'],['Finish','Streak-free'],['Dilution','1:10 concentrate'],['Suitable For','All glass surfaces']] },

  // Microfibre
  { id:8, name:'Microfibre Cloths (10-pack)', brand:'Oates', category:'microfibre', price:22.00, rating:4.8, reviews:412, badge:'Bestseller', img:'img/products/mop.jpg', desc:'Professional-grade microfibre cloths. 40×40 cm. Machine washable 300+ times. Ideal for all surfaces.', specs:[['Size','40 × 40 cm'],['Pack','10 cloths'],['Washable','300+ machine washes'],['GSM','320 gsm']] },
  { id:9, name:'Microfibre Duster Set', brand:'Oates', category:'microfibre', price:18.50, rating:4.5, reviews:93, badge:null, img:'img/products/mop.jpg', desc:'Set of 4 microfibre dusters including a washable duster head and extendable pole for high-reach dusting.', specs:[['Pack','4 heads + pole'],['Handle','Extendable 80–120 cm'],['Washable','Yes'],['Coverage','Blinds, fans, shelves']] },
  { id:10, name:'Heavy-Duty Scrubbing Pads (20-pack)', brand:'Oates', category:'microfibre', price:14.95, rating:4.4, reviews:67, badge:null, img:'img/products/mop.jpg', desc:'Green heavy-duty scouring pads. Safe for oven racks, pots, and commercial appliances. Won\'t scratch non-stick.', specs:[['Pack','20 pads'],['Size','15 × 10 cm'],['Type','Heavy-duty scouring'],['Safe For','Ovens, pots, sinks']] },

  // Equipment
  { id:11, name:'Commercial Vacuum Cleaner', brand:'ProQuip', category:'equipment', price:299.00, rating:4.9, reviews:58, badge:'Pro Grade', img:'img/products/mop.jpg', desc:'1400W commercial upright vacuum. HEPA filtration. Suitable for carpets and hard floors. 2-year warranty.', specs:[['Power','1400 W'],['Filter','HEPA H13'],['Cord Length','12 m'],['Warranty','2 years']] },
  { id:12, name:'Pressure Washer 2200PSI', brand:'ProQuip', category:'equipment', price:449.00, oldPrice:549.00, rating:4.7, reviews:39, badge:'Sale', img:'img/products/mop.jpg', desc:'Electric pressure washer 2200 PSI with adjustable nozzle. Ideal for driveways, decks, and building exteriors.', specs:[['Pressure','2200 PSI'],['Motor','2000 W'],['Hose Length','8 m'],['Weight','15 kg']] },
  { id:13, name:'Floor Scrubber 17-inch', brand:'ProQuip', category:'equipment', price:899.00, rating:4.8, reviews:24, badge:'Pro Grade', img:'img/products/mop.jpg', desc:'17-inch single-disc floor scrubber with pad driver. 1500 RPM. Suitable for stripping, scrubbing, and polishing.', specs:[['Disc Size','17 inches'],['Speed','1500 RPM'],['Motor','1100 W'],['Weight','39 kg']] },

  // PPE
  { id:14, name:'Nitrile Gloves Medium (100-pack)', brand:'CleanEasy', category:'ppe', price:16.95, rating:4.6, reviews:234, badge:null, img:'img/products/mop.jpg', desc:'Powder-free nitrile gloves. Chemical resistant. Suitable for professional cleaning and food handling.', specs:[['Size','Medium'],['Pack','100 gloves'],['Material','Nitrile'],['Standard','AS/NZS 2161.3']] },
  { id:15, name:'Safety Glasses Clear', brand:'ProQuip', category:'ppe', price:6.95, rating:4.4, reviews:88, badge:null, img:'img/products/mop.jpg', desc:'Anti-fog safety glasses with UV protection. Meets AS/NZS 1337 standard. Comfortable wrap-around design.', specs:[['Lens','Clear anti-fog'],['Standard','AS/NZS 1337'],['Protection','UV400'],['Weight','28 g']] },
  { id:16, name:'High-Vis Safety Vest', brand:'ProQuip', category:'ppe', price:11.95, rating:4.3, reviews:52, badge:null, img:'img/products/mop.jpg', desc:'Class-D high visibility safety vest. Meets AS/NZS 4602 standard. Breathable mesh. Available S–3XL.', specs:[['Class','Day/Night D'],['Standard','AS/NZS 4602.1'],['Material','Polyester mesh'],['Sizes','S–3XL']] },
  { id:17, name:'Chemical Resistant Apron', brand:'CleanEasy', category:'ppe', price:8.95, rating:4.5, reviews:44, badge:null, img:'img/products/mop.jpg', desc:'PVC-coated chemical resistant apron for protection against splashes and spills. Adjustable neck and waist ties.', specs:[['Material','PVC coated'],['Length','90 cm'],['Adjustment','Neck + waist ties'],['Colour','Yellow']] },

  // More mops
  { id:18, name:'Twist Mop 400g', brand:'Oates', category:'mops', price:19.95, rating:4.3, reviews:107, badge:null, img:'img/products/mop.jpg', desc:'Easy-wring twist mop with self-wringing mechanism. Suitable for residential use on all sealed hard floors.', specs:[['Head Weight','400 g'],['Handle','Fixed 130 cm'],['Wringer','Self-wringing twist'],['Floor Types','Sealed hard floors']] },
  { id:19, name:'Spray Mop with Refill', brand:'Oates', category:'mops', price:39.95, rating:4.7, reviews:178, badge:'New', img:'img/products/mop.jpg', desc:'Spray mop with built-in 500mL tank and 2 washable pads. Perfect for quick clean-ups. Refillable with your choice of cleaner.', specs:[['Tank','500 mL'],['Pads','2× washable'],['Handle','Fixed 130 cm'],['Refillable','Yes']] },
  { id:20, name:'Mop Handle Replacement', brand:'Oates', category:'mops', price:9.95, rating:4.0, reviews:28, badge:null, img:'img/products/mop.jpg', desc:'Replacement mop handle 140 cm. Aluminium alloy construction. Compatible with Oates standard fittings.', specs:[['Length','140 cm'],['Material','Aluminium alloy'],['Fitting','Standard'],['Compatibility','Oates fittings']] },
];

/* ================================================================
   CART STATE
   ================================================================ */
let cart = []; /* Array of { product, qty } */

function cartTotal() {
  return cart.reduce((sum, item) => sum + item.product.price * item.qty, 0);
}

function cartQty() {
  return cart.reduce((sum, item) => sum + item.qty, 0);
}

function addToCart(product, qty = 1) {
  const existing = cart.find(i => i.product.id === product.id);
  if (existing) {
    existing.qty += qty;
  } else {
    cart.push({ product, qty });
  }
  updateCartUI();
  flashCartButton();
}

function removeFromCart(productId) {
  cart = cart.filter(i => i.product.id !== productId);
  updateCartUI();
  renderCartModal();
}

function changeCartQty(productId, delta) {
  const item = cart.find(i => i.product.id === productId);
  if (item) {
    item.qty += delta;
    if (item.qty < 1) removeFromCart(productId);
    else {
      updateCartUI();
      renderCartModal();
    }
  }
}

function updateCartUI() {
  const qty = cartQty();
  const bubble = document.getElementById('cartBubble');
  const floatBtn = document.getElementById('cartFloat');
  bubble.textContent = qty;
  floatBtn.style.display = qty > 0 ? 'flex' : 'none';
}

function flashCartButton() {
  const btn = document.getElementById('cartFloat');
  btn.style.transform = 'translateY(-2px) scale(1.05)';
  setTimeout(() => { btn.style.transform = ''; }, 250);
}

/* ================================================================
   MODAL HELPERS
   ================================================================ */
function openModal(id) {
  document.getElementById(id).classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal(id) {
  document.getElementById(id).classList.remove('open');
  document.body.style.overflow = '';
}

/* Escape key closes all modals */
document.addEventListener('keydown', e => {
  if (e.key === 'Escape') {
    ['productModal','cartModal','checkoutModal'].forEach(id => {
      document.getElementById(id).classList.remove('open');
    });
    document.body.style.overflow = '';
  }
});

/* ================================================================
   PRODUCT DETAIL MODAL
   ================================================================ */
let modalQty = 1;
let modalProduct = null;

function openProduct(id) {
  const p = PRODUCTS.find(x => x.id === id);
  if (!p) return;
  modalProduct = p;
  modalQty = 1;

  const specsHtml = p.specs
    ? p.specs.map(([k,v]) => `<tr><td>${k}</td><td>${v}</td></tr>`).join('')
    : '';

  document.getElementById('modalInner').innerHTML = `
    <div class="product-modal-img">
      <img src="${p.img}" alt="${p.name}" />
    </div>
    <div class="product-modal-info">
      <p class="product-brand">${p.brand}</p>
      <p class="product-modal-name">${p.name}</p>
      <div class="product-rating">
        <span class="stars">${'★'.repeat(Math.round(p.rating))}${'☆'.repeat(5-Math.round(p.rating))}</span>
        <span class="review-count">${p.rating} (${p.reviews} reviews)</span>
      </div>
      <p class="product-modal-price">$${p.price.toFixed(2)}</p>
      <p class="product-modal-desc">${p.desc}</p>
      ${specsHtml ? `<table class="spec-table">${specsHtml}</table>` : ''}
      <div class="qty-row">
        <label>Qty</label>
        <div class="qty-control">
          <button class="qty-btn" onclick="changeModalQty(-1)" aria-label="Decrease quantity">−</button>
          <span class="qty-value" id="modalQtyVal">1</span>
          <button class="qty-btn" onclick="changeModalQty(1)" aria-label="Increase quantity">+</button>
        </div>
      </div>
      <button class="modal-add-btn" onclick="addToCartFromModal()">Add to Cart</button>
      <button class="modal-wishlist-btn" onclick="closeModal('productModal')">Continue Shopping</button>
    </div>
  `;
  openModal('productModal');
}

function changeModalQty(delta) {
  modalQty = Math.max(1, modalQty + delta);
  document.getElementById('modalQtyVal').textContent = modalQty;
}

function addToCartFromModal() {
  if (modalProduct) {
    addToCart(modalProduct, modalQty);
    closeModal('productModal');
  }
}

/* ================================================================
   CART MODAL
   ================================================================ */
function openCart() {
  renderCartModal();
  openModal('cartModal');
}

function renderCartModal() {
  const body = document.getElementById('cartBody');
  if (cart.length === 0) {
    body.innerHTML = '<div class="cart-empty"><p style="font-size:36px">🛒</p><p style="margin-top:10px">Your cart is empty.</p></div>';
    return;
  }

  const linesHtml = cart.map(item => `
    <div class="cart-line">
      <div class="cart-line-img"><img src="${item.product.img}" alt="${item.product.name}" /></div>
      <div>
        <div class="cart-line-name">${item.product.name}</div>
        <div class="cart-line-brand">${item.product.brand}</div>
      </div>
      <div class="cart-qty">
        <button class="cart-qty-btn" onclick="changeCartQty(${item.product.id}, -1)" aria-label="Decrease quantity">−</button>
        <span class="cart-qty-num">${item.qty}</span>
        <button class="cart-qty-btn" onclick="changeCartQty(${item.product.id}, 1)" aria-label="Increase quantity">+</button>
      </div>
      <div class="cart-line-price">$${(item.product.price * item.qty).toFixed(2)}</div>
    </div>
  `).join('');

  const delivery = cartTotal() >= 100 ? 0 : 9.95;
  const tax = cartTotal() * 0.10;
  const grandTotal = cartTotal() + delivery + tax;

  body.innerHTML = `
    ${linesHtml}
    <div class="cart-summary">
      <div class="summary-row"><span>Subtotal</span><span>$${cartTotal().toFixed(2)}</span></div>
      <div class="summary-row"><span>Delivery${delivery === 0 ? ' (free over $100)' : ''}</span><span>${delivery === 0 ? 'FREE' : '$' + delivery.toFixed(2)}</span></div>
      <div class="summary-row"><span>GST (10%)</span><span>$${tax.toFixed(2)}</span></div>
      <div class="summary-total"><span>Total</span><span>$${grandTotal.toFixed(2)}</span></div>
    </div>
    <button class="checkout-proceed-btn" onclick="openCheckout()">Proceed to Checkout →</button>
  `;
}

/* ================================================================
   CHECKOUT MODAL
   ================================================================ */
let currentStep = 1;

function openCheckout() {
  closeModal('cartModal');
  currentStep = 1;
  renderOrderLines();
  showStep(1);
  document.getElementById('checkoutFlow').style.display = 'block';
  document.getElementById('orderSuccess').style.display = 'none';
  openModal('checkoutModal');
}

function showStep(n) {
  currentStep = n;
  [1,2,3].forEach(i => {
    document.getElementById('step' + i).classList.toggle('show', i === n);
    document.getElementById('step' + i + 'tab').classList.toggle('active', i === n);
  });
}

function renderOrderLines() {
  const delivery = cartTotal() >= 100 ? 0 : 9.95;
  const tax = cartTotal() * 0.10;
  const grand = cartTotal() + delivery + tax;

  document.getElementById('orderLines').innerHTML = cart.map(item =>
    `<div class="order-line"><span>${item.product.name} × ${item.qty}</span><span class="order-line-price">$${(item.product.price * item.qty).toFixed(2)}</span></div>`
  ).join('');

  document.getElementById('checkoutTotal').innerHTML = `<span>Total (inc. GST)</span><span>$${grand.toFixed(2)}</span>`;
}

function goStep(n) {
  /* Validate current step before advancing */
  if (n > currentStep) {
    if (currentStep === 1 && !validateDelivery()) return;
    if (currentStep === 2 && !validatePayment()) return;
  }
  showStep(n);
}

function validateDelivery() {
  const fields = [
    ['ch-first', 'err-ch-first', v => v.trim().length > 0],
    ['ch-last',  'err-ch-last',  v => v.trim().length > 0],
    ['ch-address','err-ch-address', v => v.trim().length > 3],
    ['ch-suburb','err-ch-suburb', v => v.trim().length > 1],
    ['ch-post',  'err-ch-post',  v => /^\\d{4}$/.test(v.trim())],
    ['ch-email', 'err-ch-email', v => /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/.test(v.trim())],
  ];
  return validateFields(fields);
}

function validatePayment() {
  const fields = [
    ['ch-cardnum','err-ch-cardnum', v => v.replace(/\\s/g,'').length === 16],
    ['ch-name',  'err-ch-name',   v => v.trim().length > 2],
    ['ch-expiry','err-ch-expiry', v => /^\\d{2}\\/\\d{2}$/.test(v.trim())],
    ['ch-cvv',   'err-ch-cvv',   v => /^\\d{3,4}$/.test(v.trim())],
  ];
  return validateFields(fields);
}

function validateFields(rules) {
  let valid = true;
  rules.forEach(([id, errId, check]) => {
    const inp = document.getElementById(id);
    const err = document.getElementById(errId);
    if (!check(inp.value)) {
      inp.classList.add('field-error');
      if (err) err.style.display = 'block';
      valid = false;
    } else {
      inp.classList.remove('field-error');
      if (err) err.style.display = 'none';
    }
  });
  return valid;
}

function fmtCard(input) {
  let val = input.value.replace(/\\D/g,'').slice(0,16);
  input.value = val.replace(/(.{4})/g,'$1 ').trim();
}

function fmtExpiry(input) {
  let val = input.value.replace(/\\D/g,'');
  if (val.length >= 2) val = val.slice(0,2) + '/' + val.slice(2,4);
  input.value = val;
}

function placeOrder() {
  const btn = document.getElementById('payNowBtn');
  btn.disabled = true;
  btn.textContent = 'Processing…';
  setTimeout(() => {
    cart = [];
    updateCartUI();
    document.getElementById('checkoutFlow').style.display = 'none';
    document.getElementById('orderSuccess').style.display = 'block';
  }, 1500);
}

/* ================================================================
   PRODUCT FILTERING & RENDERING
   ================================================================ */
let currentProducts = [...PRODUCTS];

function applyFilters() {
  const query    = document.getElementById('productSearch').value.toLowerCase();
  const priceMin = parseFloat(document.getElementById('priceMin').value) || 0;
  const priceMax = parseFloat(document.getElementById('priceMax').value) || 99999;
  const sortVal  = document.getElementById('sortSelect').value;

  /* Category filter */
  const catChecks  = [...document.querySelectorAll('.cat-check:checked')].map(el => el.value);
  const brandChecks = [...document.querySelectorAll('.brand-check:checked')].map(el => el.value);

  let filtered = PRODUCTS.filter(p => {
    const matchCat   = !catChecks.length || catChecks.includes(p.category);
    const matchBrand = !brandChecks.length || brandChecks.includes(p.brand.toLowerCase());
    const matchPrice = p.price >= priceMin && p.price <= priceMax;
    const matchQuery = !query || p.name.toLowerCase().includes(query) || p.brand.toLowerCase().includes(query);
    return matchCat && matchBrand && matchPrice && matchQuery;
  });

  /* Sorting */
  switch (sortVal) {
    case 'price-asc':  filtered.sort((a,b) => a.price - b.price); break;
    case 'price-desc': filtered.sort((a,b) => b.price - a.price); break;
    case 'name-asc':   filtered.sort((a,b) => a.name.localeCompare(b.name)); break;
    case 'name-desc':  filtered.sort((a,b) => b.name.localeCompare(a.name)); break;
  }

  renderProducts(filtered);
}

function toggleAll(allCheckbox) {
  document.querySelectorAll('.cat-check').forEach(cb => cb.checked = false);
  applyFilters();
}

function resetFilters() {
  document.getElementById('productSearch').value = '';
  document.getElementById('priceMin').value = 0;
  document.getElementById('priceMax').value = 500;
  document.getElementById('sortSelect').value = 'default';
  document.getElementById('cat-all').checked = true;
  document.querySelectorAll('.cat-check, .brand-check').forEach(cb => cb.checked = false);
  applyFilters();
}

function renderProducts(list) {
  const grid  = document.getElementById('productGrid');
  const noMsg = document.getElementById('noProductsMsg');
  document.getElementById('productCount').textContent = list.length;

  if (!list.length) {
    grid.innerHTML  = '';
    noMsg.style.display = 'block';
    return;
  }

  noMsg.style.display = 'none';

  grid.innerHTML = list.map(p => `
    <div class="product-card" role="listitem" onclick="openProduct(${p.id})" aria-label="${p.name}">
      <div class="product-img">
        <img src="${p.img}" alt="${p.name}" loading="lazy" />
        ${p.badge ? `<span class="product-badge">${p.badge}</span>` : ''}
        <button class="product-fav" onclick="event.stopPropagation()" aria-label="Add ${p.name} to wishlist">♡</button>
      </div>
      <div class="product-body">
        <p class="product-brand">${p.brand}</p>
        <p class="product-name">${p.name}</p>
        <div class="product-rating">
          <span class="stars">${'★'.repeat(Math.round(p.rating))}${'☆'.repeat(5-Math.round(p.rating))}</span>
          <span class="review-count">(${p.reviews})</span>
        </div>
        <div class="product-footer">
          <span>
            <span class="product-price">$${p.price.toFixed(2)}</span>
            ${p.oldPrice ? `<span class="product-old-price">$${p.oldPrice.toFixed(2)}</span>` : ''}
          </span>
          <button class="add-to-cart-btn" onclick="event.stopPropagation(); addToCart(PRODUCTS.find(x=>x.id===${p.id}))" aria-label="Add ${p.name} to cart">Add</button>
        </div>
      </div>
    </div>
  `).join('');
}

/* Initial render */
renderProducts(PRODUCTS);
</script>
'''

with open(f'{OUT}/products.html', 'w') as f:
    f.write(full_page(
        title='Buy Cleaning Products',
        description='Shop professional-grade cleaning products online. Mops, chemicals, microfibre, equipment, and PPE — delivered across Perth, WA. GG Services shop.',
        active_page='products.html',
        body_html=PRODUCTS_BODY,
        extra_js=PRODUCTS_JS
    ))
print("products.html ✓")

print("\n✅ ALL PAGES BUILT SUCCESSFULLY")
print(f"📁 Output folder: {OUT}")
import glob
files = sorted(glob.glob(f'{OUT}/*.html'))
print(f"📄 {len(files)} HTML files generated:")
for f in files:
    size = os.path.getsize(f)
    print(f"   {os.path.basename(f):40s} {size//1024}KB")
