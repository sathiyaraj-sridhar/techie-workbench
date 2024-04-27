"""
This module manages logging.
"""

# Import standard modules.
import logging

# Log format.
log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Initialized logger
logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)

# Create console handler.
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(log_format)

# Add console handler.
logger.addHandler(console_handler)
