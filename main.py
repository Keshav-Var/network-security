
import sys

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, TrainingPipelineConfig
from networksecurity.exception.exception import NetworkSecurityException


if __name__ == "__main__":
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataigestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataigestionconfig)
        dataingestionartifact = data_ingestion.initiate_data_ingestion()
        data_validation_config = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact=dataingestionartifact,data_validation_config=data_validation_config)
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
    except Exception as e:
        raise NetworkSecurityException(e,sys)