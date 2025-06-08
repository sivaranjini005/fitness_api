"""
Logging configuration for the Fitness Studio Booking API.
Logs are written to both console and a file (app.log).
"""

import logging

# Configure the base logger
logging.basicConfig(
    level=logging.INFO,  # Log level: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format="%(asctime)s | %(levelname)s | %(message)s",  # Log format
    handlers=[
        logging.FileHandler("app.log"),  # Log to file
        logging.StreamHandler(),  # Log to stdout
    ],
)

# Create a module-specific logger
logger = logging.getLogger(__name__)
