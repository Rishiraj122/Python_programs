import logging
#This is to record progress and problems. 
#The levels: Debug, Info, Warning, Error, Critical

logging.basicConfig(filename="MYFile.log", level=logging.DEBUG)
logger=logging.getLogger()

logger.info("Our first message :) yay!")
print(logger.level)

#LEVEL          NUMERIC VALUE
#NOTSET         0
#DEBUG          10
#INFO           20
#WARNING        30
#ERROR          40
#CRITICAL       50