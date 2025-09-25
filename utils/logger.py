import logging
import os
from datetime import datetime

def setup_logger():
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)

    log_filename = os.path.join(log_dir, f"secaudit_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    logger = logging.getLogger("SecAudit")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(log_filename)
    file_handler.setLevel(logging.DEBUG)

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
