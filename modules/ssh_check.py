import os

def check_ssh_root_login():
    result = {
        "check": "SSH Root Login",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        if "PermitRootLogin yes" in content:
            result["status"] = "Fail"
            result["details"] = "PermitRootLogin is set to 'yes' in sshd_config"
        elif "PermitRootLogin no" in content:
            result["status"] = "Pass"
            result["details"] = "PermitRootLogin is set to 'no'"
        else:
            result["status"] = "Warn"
            result["details"] = "PermitRootLogin setting not found. Default behavior may allow root login."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result
