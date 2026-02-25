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

        for res in results:
            status_icon = "✅" if res["status"] == "Pass" else "❌" if res["status"] == "Fail" else "⚠️"
            f.write(f"## {status_icon} {res['check']}\n")
            f.write(f"**Status:** {res['status']}\n\n")
            f.write(f"**Details:** {res['details']}\n\n")
            f.write("---\n\n")

    return report_path