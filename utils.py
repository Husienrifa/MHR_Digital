import re
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def validate_email(email):
    """
    Validate the email address format.
    """
    pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    if re.match(pattern, email):
        logging.info(f'Email validated: {email}')
        return True
    logging.error(f'Invalid email address: {email}')
    return False


def handle_error(e):
    """
    Handle exceptions and log the error.
    """
    logging.error(f'An error occurred: {str(e)}')


def log_info(message):
    """
    Log informational messages.
    """
    logging.info(message)