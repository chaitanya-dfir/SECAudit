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



def check_max_auth_tries():
    result = {
        "check": "SSH MaxAuthTries",
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
            if stripped.lower().startswith("maxauthtries"):
                permit_value = int(stripped.split()[1])
                break

        if permit_value is not None and permit_value <= 4:
            result["status"] = "Pass"
            result["details"] = f"MaxAuthTries is set to '{permit_value}'"
        elif permit_value is not None:
            result["status"] = "Fail"
            result["details"] = f"MaxAuthTries is set to '{permit_value}' in sshd_config, which is too high"
        else:
            result["status"] = "Warn"
            result["details"] = "MaxAuthTries setting not found. Default behavior may allow too many authentication attempts."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result
    



def check_login_grace_time():
    result = {
        "check": "SSH LoginGraceTime",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        grace_value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("logingracetime"):
                grace_value = int(stripped.split()[1])
                break

        if grace_value is not None and grace_value <= 60:
            result["status"] = "Pass"
            result["details"] = f"LoginGraceTime is set to '{grace_value}' seconds"
        elif grace_value is not None:
            result["status"] = "Fail"
            result["details"] = f"LoginGraceTime is set to '{grace_value}' seconds, which is too high"
        else:
            result["status"] = "Warn"
            result["details"] = "LoginGraceTime not found. SSH default (120s) allows connections to linger unauthenticated."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result

def check_x11_forwarding():
    result = {
        "check": "SSH X11 Forwarding",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("x11forwarding"):
                value = stripped.split()[1].lower()
                break

        if value == "no":
            result["status"] = "Pass"
            result["details"] = "X11Forwarding is set to 'no'"
        elif value is not None:
            result["status"] = "Fail"
            result["details"] = f"X11Forwarding is set to '{value}' — disable it on servers"
        else:
            result["status"] = "Warn"
            result["details"] = "X11Forwarding not found. SSH defaults to allowing it."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result

def check_tcp_forwarding():
    result = {
        "check": "SSH TCP Forwarding",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("allowtcpforwarding"):
                value = stripped.split()[1].lower()
                break

        if value == "no":
            result["status"] = "Pass"
            result["details"] = "AllowTcpForwarding is set to 'no'"
        elif value is not None:
            result["status"] = "Fail"
            result["details"] = f"AllowTcpForwarding is set to '{value}' — disable it on servers"
        else:
            result["status"] = "Warn"
            result["details"] = "AllowTcpForwarding not found. SSH defaults to allowing it."

    except FileNotFoundError:
        result["status"] = "Error"
        result["details"] = "sshd_config file not found"

    return result

def check_client_alive_interval():
    result = {
        "check": "SSH ClientAliveInterval",
        "status": "Unknown",
        "details": ""
    }

    try:
        with open("/etc/ssh/sshd_config", "r") as f:
            content = f.read()

        value = None
        for line in content.splitlines():
            stripped = line.strip()
            if stripped.startswith("#") or not stripped:
                continue
            if stripped.lower().startswith("clientaliveinterval"):
                value = int(stripped.split()[1])
                break

        if value is not None and 0 < value <= 300:
            result["status"] = "Pass"
            result["details"] = f"ClientAliveInterval is set to '{value}' seconds"
        elif value is not None:
            result["status"] = "Fail"
            result["details"] = f"ClientAliveInterval is set to '{value}' — must be between 1 and 300"
        else:
            result["status"] = "Warn"
            result["details"] = "ClientAliveInterval not found. Idle sessions may never be terminated."

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
    },
    {
        "id":"5.2.13",
        "severity":"Medium",
        "remediation": "Set 'MaxAuthTries 4' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_max_auth_tries
    },
    {
        "id":"5.2.14",
        "severity":"Medium",
        "remediation": "Set 'LoginGraceTime 60' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_login_grace_time
    },
    {
        "id":"5.2.4",
        "severity":"Medium",
        "remediation": "Set 'X11Forwarding no' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_x11_forwarding
    },
    {
        "id":"5.2.15",
        "severity":"Medium",
        "remediation": "Set 'AllowTcpForwarding no' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_tcp_forwarding
    },
    {
        "id": "5.2.16",
        "severity": "Medium",
        "remediation": "Set 'ClientAliveInterval 300' in /etc/ssh/sshd_config and restart sshd.",
        "fn": check_client_alive_interval
    }
]
