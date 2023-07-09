from collections import namedtuple
TrainingPipelineConfig = namedtuple('TrainingPipelineConfig',['artifact_dir'])

DataIngestionConfig= namedtuple('DataIngestionArtifact',[
    'download_url','raw_dir','tgz_dir','ingested_dir','train_dir','test_dir'])

DataValidationArtifact= namedtuple('DataIngestionArtifact',[])

DataTransforamtionArtifact= namedtuple('DataIngestionArtifact',[])

ModelTrainerArtifact = namedtuple('ModelTrainerArtifact',[])

ModelEvaluationArtifact = namedtuple('ModelTrainerArtifact',[])

ModelPusherArtifact = namedtuple('ModelTrainerArtifact',[])
