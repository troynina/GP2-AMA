import logging 

LOGGING_ENABLED = True

LOG_CONFIG = {
    'level': 'INFO',
    'filename': 'log.log'
    'format': "%(asctime)s - %(module)s - %(levelname)s - %(funcName)s: %(lineno)d - %(message)s", 
    'datefmt'='%H:%M:%S',
}
