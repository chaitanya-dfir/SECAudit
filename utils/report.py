import os
from datetime import datetime

def generate_markdown_report(results):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = "reports"
    os.makedirs(report_dir, exist_ok=True)
    report_path = os.path.join(report_dir, f"secaudit_report_{timestamp}.md")

    with open(report_path, "w") as f:
        f.write(f"# 🔐 SecAudit Report\n")
        f.write(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

        for res in results:
            status_icon = "✅" if res["status"] == "Pass" else "❌" if res["status"] == "Fail" else "⚠️"
            f.write(f"## {status_icon} {res['check']}\n")
            f.write(f"**Status:** {res['status']}\n\n")
            f.write(f"**Details:** {res['details']}\n\n")
            f.write("---\n\n")

    return report_path
