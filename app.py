from flask import Flask
from model.logger import logging
from model.exception import ModelException
import sys

app = Flask(__name__)


@app.route("/",methods = ['GET','POST'])
def index():
    try:
        pass
    except Exception as e:
        housing = ModelException(error_message=e,error_detail=sys)
        logging.info(housing.error_message)
    logging.info("we are testing logging module")



if __name__ == "__main__":
    app.run(debug=True) 