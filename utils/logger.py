import logging
import os
import utils.logtimeformat as logtimeformat

def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_filename = os.path.join(log_dir, f"secaudit_{logtimeformat.utcTime()}.log")

    logger = logging.getLogger("SecAudit")
    logger.setLevel(logging.DEBUG)
    logger.propagate = False  # prevents double logging via root logger

    # Prevent duplicate handlers if setup_logger() is called more than once
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_filename, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger