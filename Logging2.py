import logging

LOG_FORMAT= "%(levelname)s %(asctime)s -%(message)s"
logging.basicConfig(filename="MYFile.log", level=logging.DEBUG, format=LOG_FORMAT)
logger=logging.getLogger()

logger.info("Our first message :) yay!")
print(logger.level)

#THis is different from the previous one in the sense, there's time added"
