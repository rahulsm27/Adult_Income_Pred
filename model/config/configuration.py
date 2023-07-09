from model.entity.config import *
from model.constant import *
from model.util.util import read_yaml
from model.logger import logging
from model.exception import ModelException
from datetime import datetime
import sys

from model.logger import logging
from model.exception import ModelException
import os,sys

class Configuration():

    def __init__(self, CONFIG_FILE_PATH:str = CONFIG_FILE_PATH):

        try:
            logging.info("Reading Configuration file")
            self.config_info = read_yaml(CONFIG_FILE_PATH)
            self.current_time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            self.training_pipeline_config = self.get_training_pipeline_config()

        except Exception as e:
            raise ModelException(e,sys)



        


    def get_data_ingestion_config(self)->DataIngestionConfig:
        try:
            logging.info("Reading data ingestion configuration file")
            artifact_dir = self.training_pipeline_config.artifact_dir
            data_ingestion_artifact_dir=os.path.join(
                artifact_dir,
                DATA_INGESTION_ARTIFACT_DIR,
                self.current_time_stamp
            )
            data_ingestion_info = self.config_info[DATA_INGESTION_CONFIG_KEY]
            
            dataset_download_url = data_ingestion_info[DATA_INGESTION_DOWNLOAD_URL_KEY]
            tgz_download_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_TGZ_DIR_KEY]
            )
            raw_data_dir = os.path.join(data_ingestion_artifact_dir,
            data_ingestion_info[DATA_INGESTION_RAW_DIR_KEY]
            )

            ingested_data_dir = os.path.join(
                data_ingestion_artifact_dir,
                data_ingestion_info[DATA_INGESTION_INGESTED_DIR_KEY]
            )
            ingested_train_dir = os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TRAIN_DIR_KEY]
            )
            ingested_test_dir =os.path.join(
                ingested_data_dir,
                data_ingestion_info[DATA_INGESTION_TEST_DIR_KEY]
            )


            data_ingestion_config=DataIngestionConfig(
                download_url=dataset_download_url, 
                tgz_dir=tgz_download_dir, 
                raw_dir=raw_data_dir, 
                ingested_dir=ingested_data_dir,
                train_dir=ingested_train_dir, 
                test_dir=ingested_test_dir)
            
            logging.info(f"Data Ingestion config: {data_ingestion_config}")
            return data_ingestion_config
        except Exception as e:
            raise ModelException(e,sys) from e        


    def get_training_pipeline_config(self) -> TrainingPipelineConfig:
        
        try:
            training_config_info= self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            
            artifact_dir = os.path.join (ROOT_DIR,training_config_info[TRAINING_PIPELINE_NAME_KEY],
                                        training_config_info[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipeline config  {training_pipeline_config}")

            return training_pipeline_config
            
        except Exception as e:
                raise ModelException(e,sys)



