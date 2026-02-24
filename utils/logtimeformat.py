from datetime import datetime, timezone

def utcTime():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d_%H:%M:%S_UTC")