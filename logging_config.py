import logging
from config import LOGGING_ENABLED

def logger():
    if LOGGING_ENABLED:
        logging.basicConfig(
            level=logging.INFO, 
            filename = "log.log", 
            format = "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
            datefmt='%H:%M:%S',
        )
        logging.info('Hello')
        
