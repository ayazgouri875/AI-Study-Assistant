import logging

# Create logger
logger = logging.getLogger("AI_Study_Assistant")

# Prevent duplicate handlers
if not logger.handlers:

    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler("application.log")

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s"
    )

    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)