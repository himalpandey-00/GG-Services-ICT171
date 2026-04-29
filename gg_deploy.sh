#!/bin/bash
# GG Services – Server Setup & Health Monitor Script
# ICT171 | Student: 35352086 | Murdoch University
# Usage: sudo bash gg_deploy.sh [setup|health|report]

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

DOMAIN="pandey-himal.com.np"
WEB_ROOT="/var/www/gg-services"
DB_NAME="gg_services"
DB_USER="gg_user"
DB_PASS="GGServices2026!"
UPLOAD_DIR="$WEB_ROOT/uploads"
LOG_DIR="/var/log/gg-services"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S AWST')

print_banner() {
  echo ""
  echo -e "${GREEN}${BOLD}╔══════════════════════════════════════════════════╗${NC}"
  echo -e "${GREEN}${BOLD}║         GG Services – Server Manager             ║${NC}"
  echo -e "${GREEN}${BOLD}║   Professional Cleaning Perth, WA | ICT171       ║${NC}"
  echo -e "${GREEN}${BOLD}╚══════════════════════════════════════════════════╝${NC}"
  echo -e "  ${CYAN}Domain:${NC}  $DOMAIN"
  echo -e "  ${CYAN}Date:${NC}    $TIMESTAMP"
  echo ""
}

check_root() {
  if [ "$EUID" -ne 0 ]; then
    echo -e "${RED}[ERROR]${NC} Run as root: sudo bash gg_deploy.sh"
    exit 1
  fi
}

health_check() {
  echo -e "${BOLD}=== GG Services Health Check ===${NC}"
  echo ""
  PASS=0; FAIL=0

  # Apache
  if systemctl is-active --quiet apache2; then
    echo -e "  ${GREEN}[PASS]${NC} Apache is running."
    ((PASS++))
  else
    echo -e "  ${RED}[FAIL]${NC} Apache is NOT running. Attempting restart..."
    systemctl restart apache2
    systemctl is-active --quiet apache2 && { echo -e "  ${YELLOW}[RECOVERED]${NC} Apache restarted."; ((PASS++)); } || { echo -e "  ${RED}[FAIL]${NC} Apache could not restart."; ((FAIL++)); }
  fi

  # MySQL
  if systemctl is-active --quiet mysql; then
    echo -e "  ${GREEN}[PASS]${NC} MySQL is running."
    ((PASS++))
  else
    echo -e "  ${RED}[FAIL]${NC} MySQL is NOT running."
    ((FAIL++))
  fi

  # PHP
  PHP_VER=$(php -r 'echo PHP_VERSION;' 2>/dev/null)
  [ -n "$PHP_VER" ] && { echo -e "  ${GREEN}[PASS]${NC} PHP version: $PHP_VER"; ((PASS++)); } || { echo -e "  ${RED}[FAIL]${NC} PHP not working."; ((FAIL++)); }

  # Web root
  if [ -f "$WEB_ROOT/index.html" ]; then
    FILE_COUNT=$(find "$WEB_ROOT" -type f | wc -l)
    echo -e "  ${GREEN}[PASS]${NC} index.html exists. Files deployed: ${FILE_COUNT}"
    ((PASS++))
  else
    echo -e "  ${RED}[FAIL]${NC} index.html NOT found."
    ((FAIL++))
  fi

  # Database
  DB_CHECK=$(mysql -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" -e "SELECT COUNT(*) FROM quote_requests;" 2>/dev/null | tail -1)
  if [ -n "$DB_CHECK" ]; then
    JOB_COUNT=$(mysql -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" -e "SELECT COUNT(*) FROM job_applications;" 2>/dev/null | tail -1)
    echo -e "  ${GREEN}[PASS]${NC} Database connected. Quotes: ${DB_CHECK} | Applications: ${JOB_COUNT}"
    ((PASS++))
  else
    echo -e "  ${RED}[FAIL]${NC} Cannot connect to database."
    ((FAIL++))
  fi

  # Uploads
  if [ -w "$UPLOAD_DIR/cv" ]; then
    CV_COUNT=$(find "$UPLOAD_DIR/cv" -type f | wc -l)
    echo -e "  ${GREEN}[PASS]${NC} Uploads writable. CVs stored: ${CV_COUNT}"
    ((PASS++))
  else
    echo -e "  ${RED}[FAIL]${NC} Uploads folder not writable."
    ((FAIL++))
  fi

  # SSL
  SSL_EXPIRY=$(echo | openssl s_client -servername "$DOMAIN" -connect "$DOMAIN":443 2>/dev/null | openssl x509 -noout -dates 2>/dev/null | grep 'notAfter' | cut -d= -f2)
  if [ -n "$SSL_EXPIRY" ]; then
    EXPIRY_EPOCH=$(date -d "$SSL_EXPIRY" +%s 2>/dev/null)
    DAYS_LEFT=$(( (EXPIRY_EPOCH - $(date +%s)) / 86400 ))
    [ "$DAYS_LEFT" -gt 14 ] && { echo -e "  ${GREEN}[PASS]${NC} SSL valid. Expires in ${DAYS_LEFT} days."; ((PASS++)); } || { echo -e "  ${YELLOW}[WARN]${NC} SSL expires in ${DAYS_LEFT} days!"; ((FAIL++)); }
  else
    echo -e "  ${YELLOW}[INFO]${NC} SSL check skipped."
  fi

  # Disk
  DISK=$(df / | awk 'NR==2{print $5}' | tr -d '%')
  [ "$DISK" -lt 80 ] && { echo -e "  ${GREEN}[PASS]${NC} Disk: ${DISK}%"; ((PASS++)); } || { echo -e "  ${YELLOW}[WARN]${NC} Disk high: ${DISK}%"; ((FAIL++)); }

  # Memory
  MEM_T=$(free -m | awk 'NR==2{print $2}')
  MEM_U=$(free -m | awk 'NR==2{print $3}')
  MEM_P=$(( MEM_U * 100 / MEM_T ))
  [ "$MEM_P" -lt 80 ] && { echo -e "  ${GREEN}[PASS]${NC} Memory: ${MEM_U}MB/${MEM_T}MB (${MEM_P}%)"; ((PASS++)); } || { echo -e "  ${YELLOW}[WARN]${NC} Memory high: ${MEM_P}%"; ((FAIL++)); }

  # HTTP
  HTTP=$(curl -s -o /dev/null -w "%{http_code}" http://localhost 2>/dev/null)
  [[ "$HTTP" == "200" || "$HTTP" == "301" || "$HTTP" == "302" ]] && { echo -e "  ${GREEN}[PASS]${NC} HTTP response: $HTTP"; ((PASS++)); } || { echo -e "  ${RED}[FAIL]${NC} HTTP response: $HTTP"; ((FAIL++)); }

  echo ""
  echo -e "${BOLD}--- Summary ---${NC}"
  echo -e "  ${GREEN}Passed:${NC} $PASS   ${RED}Failed/Warned:${NC} $FAIL"
  [ $FAIL -eq 0 ] && echo -e "  ${GREEN}${BOLD}All systems healthy!${NC}" || echo -e "  ${YELLOW}${BOLD}Some checks need attention.${NC}"
  echo ""
}

generate_report() {
  mkdir -p "$LOG_DIR"
  REPORT="$LOG_DIR/health_$(date +%Y-%m-%d).txt"
  {
    echo "========================================"
    echo " GG Services – Daily Health Report"
    echo " Generated: $TIMESTAMP"
    echo " Domain: $DOMAIN | Student: 35352086"
    echo "========================================"
    echo ""
    echo "--- System ---"
    echo "Hostname: $(hostname)"
    echo "OS: $(lsb_release -ds 2>/dev/null)"
    echo "Uptime: $(uptime -p)"
    echo ""
    echo "--- Services ---"
    systemctl is-active apache2
    systemctl is-active mysql
    php -r 'echo "PHP " . PHP_VERSION . "\n";' 2>/dev/null
    echo ""
    echo "--- Database Counts ---"
    mysql -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" -e "SELECT COUNT(*) AS quotes FROM quote_requests; SELECT COUNT(*) AS applications FROM job_applications;" 2>/dev/null
    echo ""
    echo "--- Files ---"
    find "$WEB_ROOT" -type f | wc -l
    echo ""
    echo "--- Disk ---"
    df -h /
    echo ""
    echo "--- Memory ---"
    free -h
    echo "========================================"
  } > "$REPORT"
  echo -e "${GREEN}[OK]${NC} Report saved: $REPORT"
}

print_banner
check_root

case "${1:-help}" in
  health) health_check ;;
  report) health_check; generate_report ;;
  *)
    echo -e "${BOLD}Usage:${NC} sudo bash gg_deploy.sh [command]"
    echo -e "  ${CYAN}health${NC}   Run health check"
    echo -e "  ${CYAN}report${NC}   Health check + save report to $LOG_DIR"
    echo ""
    ;;
esac
