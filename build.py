from model.pipeline import Pipeline
from model.exception import ModelException
from model.logger import    logging
import sys



def main_run():
    try :
       pipeline  = Pipeline()
       Pipeline.run()

    except Exception as e:
        ModelException(e,sys)
