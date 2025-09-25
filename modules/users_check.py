import pwd

def check_privileged_users():
    result = {
        "check": "Privileged Users (UID 0 or Sudo)",
        "status": "Pass",
        "details": ""
    }

    try:
        uid0_users = [user.pw_name for user in pwd.getpwall() if user.pw_uid == 0]
        sudo_users = []

        with open("/etc/group", "r") as f:
            for line in f:
                if line.startswith("sudo:") or line.startswith("wheel:"):
                    parts = line.strip().split(":")
                    if len(parts) >= 4:
                        sudo_users = parts[3].split(",") if parts[3] else []

        if len(uid0_users) > 1 or sudo_users:
            result["status"] = "Fail"
            result["details"] = f"UID 0 users: {uid0_users}. Sudo group users: {sudo_users}"
        else:
            result["details"] = "Only root user has UID 0. No extra sudo users found."

    except Exception as e:
        result["status"] = "Error"
        result["details"] = str(e)

    return result
