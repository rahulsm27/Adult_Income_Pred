import yaml
from model.exception import ModelException
import sys



def read_yaml (file_path:str) -> dict:

    try :
       with open(file_path,'rb') as file_obj:
            return yaml.safe_load(file_obj)

    except Exception as e:
        ModelException(e,sys)

