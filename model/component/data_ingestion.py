from model.entity.config import DataIngestionConfig
from model.entity.artifiact import DataIngestionArtifact

from model.exception import ModelException
from model.logger import logging

import sys,os
import pandas as pd
import numpy as np
import zipfile

os.environ['KAGGLE_USERNAME'] = "rahulsmahajan"
os.environ['KAGGLE_KEY'] = "549ba3722f0dd76516e76cd068d475ab"

from kaggle.api.kaggle_api_extended import KaggleApi
api = KaggleApi()
api.authenticate()


import tarfile
from six.moves import urllib
from sklearn.model_selection import train_test_split


class DataIngestion:

    def __init__(self, data_ingestion_config:DataIngestionConfig):
        try:
            logging.info(f"{'='*20}Data Ingestion log started.{'='*20}")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise ModelException(e,sys) from e
        
    def download_model_data(self,) -> str:
        try:
            #extracting remote url to download
            download_url = self.data_ingestion_config.download_url

            #folder location to download file
            tgz_download_dir = self.data_ingestion_config.tgz_dir

            os.makedirs(tgz_download_dir,exist_ok=True)

            model_file_name = 'adult-income-dataset.zip'

            tgz_file_path = os.path.join(tgz_download_dir,model_file_name)

            logging.info(f"Downloading file from :[{download_url}] into :[{tgz_file_path}]")
                
            api.dataset_download_files(download_url, path=tgz_download_dir)
           # urllib.request.urlretrieve(download_url,tgz_file_path)
            logging.info(f"File : [{tgz_file_path}] has been downloaded successfully")

            return tgz_file_path

        except Exception as e:
            raise ModelException(e,sys) from e

    def extract_tgz_file(self,tgz_file_path):
        try:
            raw_data_dir = self.data_ingestion_config.raw_dir
            if os.path.exists(raw_data_dir):
                os.remove(raw_data_dir)

            os.makedirs(raw_data_dir,exist_ok=True)

            logging.info(f"Extracign zip file :[{tgz_file_path}] into dir ; [{raw_data_dir}]")
            
            with zipfile.ZipFile(tgz_file_path, 'r') as zip_ref:
                zip_ref.extractall(raw_data_dir)

            # with tarfile.open(tgz_file_path) as model_file_obj:
            #     model_file_obj.extractall(path=raw_data_dir)
            logging.info(f"Extracting completed")
        except Exception as e:
            raise ModelException(e,sys) from e

    def split_data_as_train_test(self):
        try:
            raw_data_dir = self.data_ingestion_config.raw_dir
            file_name = os.listdir(raw_data_dir)[0]

            model_file_path = os.path.join(raw_data_dir,file_name)

            model_data_frame = pd.read_csv(model_file_path)

            
            strat_train_set,strat_test_set = train_test_split(model_data_frame,test_size=0.2)
            

           
            train_file_path = os.path.join(self.data_ingestion_config.train_dir,file_name)
            test_file_path = os.path.join(self.data_ingestion_config.test_dir,file_name)

            if strat_train_set is not None:
                os.makedirs(self.data_ingestion_config.train_dir,exist_ok=True)
                logging.info(f"Exporting training dataset fo file :[{train_file_path}]")
                strat_test_set.to_csv(train_file_path)

            if strat_test_set is not None:
                os.makedirs(self.data_ingestion_config.test_dir,exist_ok=True)
                logging.info(f"Exporting test dataset fo file :[{test_file_path}]")
                strat_test_set.to_csv(test_file_path)


            data_ingestion_artifact = DataIngestionArtifact(train_file_path=train_file_path,test_file_path=test_file_path,
                                  is_ingested=True,
                                  message=f"Data ingestion completed successfully")

            logging.info(f"Data Ignestion artifact:[{data_ingestion_artifact}]")
            return data_ingestion_artifact
            
        except Exception as e:
            raise ModelException(e,sys) from e

    def initiate_data_ingestion(self)-> DataIngestionArtifact:
        try:
            tgz_file_path = self.download_model_data()

            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            return self.split_data_as_train_test()
            
            
        except Exception as e:
            raise ModelException(e,sys) from e
        

    def __del__(self):
        logging.info(f"{'='*20} Data Ingestion log completed.{'='*20} \n\n")

