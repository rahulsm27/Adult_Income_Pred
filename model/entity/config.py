from collections import namedtuple

DataIngestionArtifact= namedtuple('DataIngestionArtifact',['download_url','raw_dir','train_dir','test_dir'])

DataValidationArtifact= namedtuple('DataIngestionArtifact',[])

DataTransforamtionArtifact= namedtuple('DataIngestionArtifact',[])

ModelTrainerArtifact = namedtuple('ModelTrainerArtifact',[])

ModelEvaluationArtifact = namedtuple('ModelTrainerArtifact',[])

ModelPusherArtifact = namedtuple('ModelTrainerArtifact',[])
