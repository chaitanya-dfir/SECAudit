import subprocess

def check_running_services():
    result = {
        "check": "Running System Services",
        "status": "Pass",
        "details": ""
    }

    try:
        output = subprocess.check_output(["systemctl", "list-units", "--type=service", "--state=running"],
                                         stderr=subprocess.DEVNULL)
        services = output.decode().strip().split("\n")
        running_services = [
            line.split()[0] for line in services
            if line.strip() and line.split()[0].endswith(".service")
        ]

        result["details"] = f"Total running services: {len(running_services)}"
    except Exception as e:
        result["status"] = "Error"
        result["details"] = str(e)

    return result

CHECKS = [
    {
        "id": "2.1",
        "severity": "Info",
        "remediation": "Disable unnecessary services with: systemctl disable --now <service>",
        "fn": check_running_services,
    }
]
