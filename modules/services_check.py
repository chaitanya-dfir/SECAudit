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
        services = output.decode().strip().split("\n")[1:]
        running_services = [line.split()[0] for line in services if line.strip()]

        result["details"] = f"Total running services: {len(running_services)}"
    except Exception as e:
        result["status"] = "Error"
        result["details"] = str(e)

    return result
