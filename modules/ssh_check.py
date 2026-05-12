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

        permit_value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("permitrootlogin"):
                permit_value = stripped.split()[1].lower()
                break

        if permit_value == "no":
            result["status"] = "Pass"
            result["details"] = "PermitRootLogin is set to 'no'"
        elif permit_value is not None:
            result["status"] = "Fail"
            result["details"] = f"PermitRootLogin is set to '{permit_value}' in sshd_config"
        else:
            result["status"] = "Warn"
            result["details"] = "PermitRootLogin setting not found. Default behavior may allow root login."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result

def check_password_authentication():
    result = {
        "check": "SSH Password Authentication",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        permit_value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("passwordauthentication"):
                permit_value = stripped.split()[1].lower()
                break

        if permit_value == "no":
            result["status"] = "Pass"
            result["details"] = "PasswordAuthentication is set to 'no'"
        elif permit_value is not None:
            result["status"] = "Fail"
            result["details"] = f"PasswordAuthentication is set to '{permit_value}' in sshd_config"
        else:
            result["status"] = "Warn"
            result["details"] = "PasswordAuthentication setting not found. Default behavior may allow password authentication."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result

def check_permit_empty_passwords():
    result = {
        "check": "SSH Permit Empty Passwords",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        permit_value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("permitemptypasswords"):
                permit_value = stripped.split()[1].lower()
                break

        if permit_value == "no":
            result["status"] = "Pass"
            result["details"] = "PermitEmptyPasswords is set to 'no'"
        elif permit_value is not None:
            result["status"] = "Fail"
            result["details"] = f"PermitEmptyPasswords is set to '{permit_value}' in sshd_config"
        else:
            result["status"] = "Warn"
            result["details"] = "PermitEmptyPasswords setting not found. Default behavior may allow empty passwords."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result

CHECKS = [
    {
        "id": "5.2.8",
        "severity": "High",
        "remediation": "Set 'PermitRootLogin no' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_ssh_root_login,
    },
    {
        "id":"5.2.11",
        "severity":"High",
        "remediation": "Set 'PasswordAuthentication no' in /etc/ssh/sshd_config and restart sshd. Use SSH keys instead.",
        "fn": check_password_authentication
    },
    {
        "id":"5.2.12",
        "severity":"High",
        "remediation": "Set 'PermitEmptyPasswords no' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_permit_empty_passwords
    }
]
