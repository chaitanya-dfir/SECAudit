import subprocess
import shutil

def check_firewall_status():
    result = {
        "check": "Firewall Status (UFW/Iptables)",
        "status": "Fail",
        "details": "No firewall active"
    }

    try:
        if shutil.which("ufw"):
            output = subprocess.check_output(["ufw", "status"], stderr=subprocess.DEVNULL).decode()
            if "Status: active" in output:
                result["status"] = "Pass"
                result["details"] = "UFW is active"
            else:
                result["details"] = "UFW is installed but inactive"

        elif shutil.which("iptables"):
            output = subprocess.check_output(["iptables", "-L"], stderr=subprocess.DEVNULL).decode()
            if "Chain" in output:
                result["status"] = "Warn"
                result["details"] = "Iptables rules exist but UFW is not installed"

    except Exception as e:
        result["status"] = "Error"
        result["details"] = str(e)

    return result

CHECKS = [
    {
        "id": "3.5.1.1",
        "severity": "Critical",
        "remediation": "Enable UFW with: ufw enable. Ensure rules are configured before enabling.",
        "fn": check_firewall_status,
    }
]
