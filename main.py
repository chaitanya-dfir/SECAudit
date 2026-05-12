import argparse
from modules import load_all_checks
from utils.logger import setup_logger
from utils.report import generate_markdown_report

logger = setup_logger()

def run_audit():
    logger.info("Starting security audit...")
    results = []

    for check in load_all_checks():
        result = check["fn"]()
        result["id"] = check["id"]
        result["severity"] = check["severity"]
        result["remediation"] = check["remediation"]
        results.append(result)

    for res in results:
        icon = "✅" if res["status"] == "Pass" else "❌" if res["status"] == "Fail" else "⚠️"
        msg = f"[{res['id']}] {icon} {res['check']}: {res['status']} — {res['details']}"
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

    if args.harden:
        logger.info("[*] Hardening feature coming soon...")

    if not any(vars(args).values()):
        parser.print_help()

if __name__ == "__main__":
    main()
