/**
 * GG Services – Main JavaScript
 * ICT171 | Student: 35352086 | Murdoch University
 * -------------------------------------------------
 * Shared functionality used across all pages:
 *  - Mobile navigation toggle
 *  - Scroll-reveal animations
 *  - Active nav link highlighting
 *  - Form validation utilities
 */

/* ============================================================
   NAVIGATION
   ============================================================ */

/**
 * Toggle mobile navigation menu open/closed.
 * Called on hamburger button click.
 */
function initNav() {
  const hamburger = document.getElementById('hamburger');
  const mobileMenu = document.getElementById('mobileMenu');

  if (hamburger && mobileMenu) {
    hamburger.addEventListener('click', () => {
      mobileMenu.classList.toggle('open');

      /* Animate hamburger lines into × shape */
      hamburger.classList.toggle('is-open');
    });

    /* Close menu when any mobile link is clicked */
    mobileMenu.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => mobileMenu.classList.remove('open'));
    });

    /* Close menu when clicking outside */
    document.addEventListener('click', (e) => {
      if (!hamburger.contains(e.target) && !mobileMenu.contains(e.target)) {
        mobileMenu.classList.remove('open');
        hamburger.classList.remove('is-open');
      }
    });
  }

  /* Mark active nav link based on current page */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-links a, .mobile-menu a').forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPage || (currentPage === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });
}

/* ============================================================
   SCROLL REVEAL ANIMATIONS
   ============================================================ */

/**
 * Observe elements with class 'reveal' and add
 * 'visible' when they enter the viewport.
 */
function initReveal() {
  if (!('IntersectionObserver' in window)) {
    /* Fallback: just show everything for older browsers */
    document.querySelectorAll('.reveal').forEach(el => el.classList.add('visible'));
    return;
  }

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target); /* Only animate once */
      }
    });
  }, { threshold: 0.1 });

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
}

/* ============================================================
   FORM VALIDATION UTILITIES
   ============================================================ */

/**
 * Validate a single input field.
 * @param {HTMLElement} input - The input element
 * @param {Function} checkFn - Returns true if valid
 * @param {string} errorId - ID of the error message element
 * @returns {boolean}
 */
function validateField(input, checkFn, errorId) {
  const errorEl = document.getElementById(errorId);
  if (!checkFn(input.value)) {
    input.classList.add('field-error');
    if (errorEl) errorEl.style.display = 'block';
    return false;
  }
  input.classList.remove('field-error');
  if (errorEl) errorEl.style.display = 'none';
  return true;
}

/**
 * Clear field error styling on input.
 * Attach to 'input' event listener.
 * @param {HTMLElement} input
 * @param {string} errorId
 */
function clearFieldError(input, errorId) {
  input.classList.remove('field-error');
  const errorEl = document.getElementById(errorId);
  if (errorEl) errorEl.style.display = 'none';
}

/**
 * Show spinner and disable button during form submission.
 * @param {string} btnId - Button element ID
 * @param {string} spinnerId - Spinner element ID
 */
function showSubmitSpinner(btnId, spinnerId) {
  const btn = document.getElementById(btnId);
  const spinner = document.getElementById(spinnerId);
  if (btn) btn.disabled = true;
  if (spinner) spinner.style.display = 'block';
}

/**
 * Format a card number string as groups of 4 digits.
 * @param {HTMLInputElement} input
 */
function formatCardNumber(input) {
  let val = input.value.replace(/\D/g, '').slice(0, 16);
  input.value = val.replace(/(.{4})/g, '$1 ').trim();
}

/**
 * Format expiry date as MM/YY.
 * @param {HTMLInputElement} input
 */
function formatExpiry(input) {
  let val = input.value.replace(/\D/g, '');
  if (val.length >= 2) val = val.slice(0, 2) + '/' + val.slice(2, 4);
  input.value = val;
}

/* ============================================================
   SMOOTH SCROLL TO ANCHOR
   ============================================================ */

/**
 * Smoothly scroll to an anchor hash in the URL.
 * Useful for in-page navigation (e.g. services.html#house).
 */
function scrollToHash() {
  if (window.location.hash) {
    const target = document.querySelector(window.location.hash);
    if (target) {
      setTimeout(() => {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 100);
    }
  }
}

/* ============================================================
   INITIALISE ON DOM READY
   ============================================================ */
document.addEventListener('DOMContentLoaded', () => {
  initNav();
  initReveal();
  scrollToHash();
});
