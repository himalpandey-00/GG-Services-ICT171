-- ============================================================
-- GG Services Database Schema
-- ICT171 | Student: 35352086 | Murdoch University
-- ============================================================
-- Run this file once to set up the database.
-- In phpMyAdmin: Import → select this file → Go
-- In terminal:   mysql -u root -p < backend/database.sql
-- ============================================================

CREATE DATABASE IF NOT EXISTS gg_services
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE gg_services;

-- ── QUOTE REQUESTS ──────────────────────────────────────────
CREATE TABLE IF NOT EXISTS quote_requests (
  id            INT UNSIGNED     NOT NULL AUTO_INCREMENT,
  full_name     VARCHAR(120)     NOT NULL,
  phone         VARCHAR(30)      NOT NULL,
  email         VARCHAR(180)     NOT NULL,
  address       VARCHAR(255)     NOT NULL,
  suburb        VARCHAR(100)     NOT NULL,
  postcode      VARCHAR(10)      NOT NULL DEFAULT '',
  service_type  VARCHAR(100)     NOT NULL,
  hours_required VARCHAR(50)     NOT NULL DEFAULT 'Not sure',
  preferred_time VARCHAR(120)    NOT NULL DEFAULT '',
  notes         TEXT             NOT NULL DEFAULT '',
  ip_address    VARCHAR(45)      NOT NULL DEFAULT '',
  submitted_at  DATETIME         NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ── JOB APPLICATIONS ────────────────────────────────────────
CREATE TABLE IF NOT EXISTS job_applications (
  id              INT UNSIGNED   NOT NULL AUTO_INCREMENT,
  job_id          VARCHAR(60)    NOT NULL,          -- e.g. 'senior-cleaner'
  job_title       VARCHAR(120)   NOT NULL,
  first_name      VARCHAR(80)    NOT NULL,
  last_name       VARCHAR(80)    NOT NULL,
  email           VARCHAR(180)   NOT NULL,
  phone           VARCHAR(30)    NOT NULL,
  right_to_work   VARCHAR(60)    NOT NULL,
  availability    VARCHAR(60)    NOT NULL DEFAULT 'Flexible',
  about           TEXT           NOT NULL DEFAULT '',
  cv_filename     VARCHAR(260)   NOT NULL DEFAULT '',  -- stored filename (renamed)
  cv_original     VARCHAR(260)   NOT NULL DEFAULT '',  -- original filename user uploaded
  cl_filename     VARCHAR(260)   NOT NULL DEFAULT '',  -- cover letter stored name
  cl_original     VARCHAR(260)   NOT NULL DEFAULT '',  -- cover letter original name
  ip_address      VARCHAR(45)    NOT NULL DEFAULT '',
  submitted_at    DATETIME       NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
