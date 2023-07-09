from model.pipeline.pipeline import Pipeline
from model.exception import ModelException
from model.logger import    logging
import sys



def main_run():
    try :
       pipeline  = Pipeline()
       pipeline.run()

    except Exception as e:
           
        logging.error(f"e")
        print
        raise ModelException(e,sys)


if __name__ =="__main__":
    main_run()