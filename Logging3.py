import logging

LOG_FORMAT= "%(levelname)s %(asctime)s -%(message)s"
logging.basicConfig(filename="MYFile.log", level=logging.DEBUG, format=LOG_FORMAT, filemode='w')
logger=logging.getLogger()

logger.info("Our first message :) yay!")
print(logger.level)

#TO OVERWRITE, it's done here. 