import logging
import os
from datetime import datetime
from constant import *

CURRENT_TIME_STAMP = datetime.now().strftime(format = '%Y-%m-%d_%H-%M-%S')

DIR_PATH = os.makedirs(LOG_DIR,exist_ok=True)

FILE_PATH = os.path.join(DIR_PATH,CURRENT_TIME_STAMP)

logging.basicConfig(filename=FILE_PATH, mode='w', 
                    format='[%(asctime)s] %(name)s - %(levelname)s - %(message)s' , 
                    level=logging.info)







