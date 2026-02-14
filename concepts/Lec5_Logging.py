from loguru import logger
import sys 
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - [%(filename)s - %(lineno)d] - %(levelname)s - %(message)s'
)
logging.debug("Dishant Debug message")
logging.info("Dishant info message")
# Output: DEBUG:root:Debug message
#         INFO:root:Info message

### Easy level switching
# levels = {"debug": logging.DEBUG, "info": logging.INFO, "warning": logging.WARNING}
# logging.basicConfig(level=levels.get("info", logging.WARNING))

## Loguru Library
logger.add(
    sys.stderr, 
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {file}:{line} | {message}"
)
logger.info("Dishant is learning logging and print statements")