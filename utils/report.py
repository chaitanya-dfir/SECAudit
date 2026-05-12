import os
import utils.logtimeformat as logtimeformat

def generate_markdown_report(results):
    timestamp = logtimeformat.utcTime()  # generate ONCE
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"{timestamp}_secaudit_report.md")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("# 🔐 SecAudit Report\n")
        f.write(f"**Generated:** {timestamp}\n\n")  # reuse same timestamp

        passed = sum(1 for r in results if r["status"] == "Pass")
        failed = sum(1 for r in results if r["status"] == "Fail")
        warned = sum(1 for r in results if r["status"] == "Warn")
        f.write(f"**Score:** {passed}/{len(results)} checks passed")
        f.write(f" | ❌ {failed} failed | ⚠️ {warned} warnings\n\n---\n\n")

        for res in results:
            status_icon = "✅" if res["status"] == "Pass" else "❌" if res["status"] == "Fail" else "⚠️"
            f.write(f"## {status_icon} [{res.get('id', '—')}] {res['check']}\n")
            f.write(f"**Severity:** {res.get('severity', '—')} | **Status:** {res['status']}\n\n")
            f.write(f"**Details:** {res['details']}\n\n")
            if res["status"] != "Pass":
                f.write(f"**Remediation:** {res.get('remediation', '—')}\n\n")
            f.write("---\n\n")

    return report_path