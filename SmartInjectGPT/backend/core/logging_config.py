# logging_config.py — Logger for SmartInjectGPT

import logging
from pathlib import Path

log_file = Path(__file__).resolve().parent.parent.parent / "logs/server.log"
log_file.parent.mkdir(parents=True, exist_ok=True)

logger = logging.getLogger("SmartInjectGPT")
logger.setLevel(logging.INFO)

if not logger.handlers:
    formatter = logging.Formatter('%(asctime)s — %(levelname)s — %(message)s')

    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
