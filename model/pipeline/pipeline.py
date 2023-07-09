
from model.exception import ModelException
from model.logger import logging
from model.config.configuration import Configuration
from model.entity.artifiact import *
from model.entity.config import *
from model.component.data_ingestion import DataIngestion

import sys





class Pipeline:
    
    def __init__(self, config:Configuration = Configuration()) -> None:
        try:
            self.config = config

        except Exception as e:
            raise ModelException(e,sys) from e
    
    def start_data_ingestion(self)->DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            
            return(data_ingestion.initiate_data_ingestion())
        
        except Exception as e:
            raise ModelException(e,sys) from e
        
    def run(self):
        try:
            # data ingestion

            data_ingestion_artifact = self.start_data_ingestion()

        except Exception as e:
            raise ModelException(e,sys) from e