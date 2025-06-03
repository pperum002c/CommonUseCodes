import logging
from logging.handlers import TimedRotatingFileHandler

rotate = TimedRotatingFileHandler(
    'logs\\my_mail.log',
    when="D",
    interval=1,
    backupCount=10
)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(lineno)d:%(message)s')

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
rotate.setFormatter(formatter)
logger.addHandler(rotate)

logger.info("Sample Input Message")
logger.error("Sample Error Message")
