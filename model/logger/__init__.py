import logging
import os
from datetime import datetime
from model.constant import *

CURRENT_TIME_STAMP = datetime.now().strftime(format = '%Y-%m-%d_%H-%M-%S')

LOG_PATH = os.path.join(ROOT_DIR,LOG_DIR)
os.makedirs(LOG_PATH,exist_ok=True)

LOG_FILE_NAME = f"log_{CURRENT_TIME_STAMP}.log"
FILE_PATH = os.path.join(ROOT_DIR,LOG_DIR,LOG_FILE_NAME)

logging.basicConfig(filename=FILE_PATH,filemode='w',
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s',level=1)







