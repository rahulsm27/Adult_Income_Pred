import os

ROOT_DIR = os.getcwd()
CONFIG_DIR = 'config'
CONFIG_FILE = 'config.yaml'

LOG_DIR = 'model_logs'

CONFIG_FILE_PATH = os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE)

# Data Ingestion pipleline variable
DATA_INGESTION_CONFIG_KEY = 'data_ingestion_config'
DATA_INGESTION_DOWNLOAD_URL_KEY= 'download_url'
DATA_INGESTION_RAW_DIR_KEY = 'raw_dir'
DATA_INGESTION_TGZ_DIR_KEY = 'tgz_dir'
DATA_INGESTION_INGESTED_DIR_KEY = 'ingested_dir'
DATA_INGESTION_TRAIN_DIR_KEY = 'train_dir'
DATA_INGESTION_TEST_DIR_KEY = 'test_dir'

DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"

#Training pipeline related variable
TRAINING_PIPELINE_CONFIG_KEY = 'training_pipeline_config'
TRAINING_PIPELINE_NAME_KEY = 'pipeline_name'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = 'artifact_dir'

