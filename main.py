import argparse
from modules.ssh_check import check_ssh_root_login
from modules.users_check import check_privileged_users
from modules.services_check import check_running_services
from modules.firewall_check import check_firewall_status
from utils.logger import setup_logger
from utils.report import generate_markdown_report

logger = setup_logger()

def run_audit():
    logger.info("Starting security audit...")
    results = []

    results.append(check_ssh_root_login())
    results.append(check_privileged_users())
    results.append(check_running_services())
    results.append(check_firewall_status())

    for res in results:
        icon = "✅" if res["status"] == "Pass" else "❌" if res["status"] == "Fail" else "⚠️"
        msg = f"{icon} {res['check']}: {res['status']} → {res['details']}"
        logger.info(msg)

    return results

def main():
    parser = argparse.ArgumentParser(
        description="SecAudit - Linux Security Audit and Hardening Tool"
    )
    parser.add_argument("--scan", action="store_true", help="Run security audit scan")
    parser.add_argument("--report", action="store_true", help="Generate audit report (use after --scan)")
    parser.add_argument("--harden", action="store_true", help="Apply security hardening (with prompts)")

    args = parser.parse_args()
    results = None

    if args.scan:
        results = run_audit()

    if args.report:
        if not results:
            logger.error("Run a scan first before generating report.")
        else:
            report_file = generate_markdown_report(results)
            logger.info(f"📄 Report saved to {report_file}")

    elif args.harden:
        logger.info("[*] Hardening feature coming soon...")

    elif not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
