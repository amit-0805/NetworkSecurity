from networksecurity.componets.data_ingestion import DataIngestion
from networksecurity.componets.data_validation import DataValidation
from networksecurity.componets.data_transformation import DataTransformation
from networksecurity.componets.model_trainer import ModelTrainer
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig

import sys

if __name__=='__main__':
    try:
        trainingpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainingpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Initiate the data Ingesiton")
        dataingestionartifact = data_ingestion.initialte_data_ingestion()
        logging.info("Data Inititation Completed")
        print(dataingestionartifact)
        datavalidationconfig = DataValidationConfig(trainingpipelineconfig)
        data_validation = DataValidation(dataingestionartifact, datavalidationconfig)
        logging.info("Data Validation Initiated")
        datavalidationartifact = data_validation.initiate_data_validation()
        logging.info("Data Validation Completed")
        print(datavalidationartifact)
        datatransformationconfig = DataTransformationConfig(trainingpipelineconfig)
        data_transformation = DataTransformation(datavalidationartifact, datatransformationconfig)
        logging.info("Data Transformation Initiated")
        datatransformationartifact = data_transformation.initiate_data_transformation()
        logging.info("Data Transformation Completed")
        print(datatransformationartifact)

        logging.info("Model Training sstared")
        model_trainer_config=ModelTrainerConfig(trainingpipelineconfig)
        model_trainer=ModelTrainer(model_trainer_config=model_trainer_config,data_transformation_artifact=datatransformationartifact)
        model_trainer_artifact=model_trainer.initiate_model_trainer()

        logging.info("Model Training artifact created")

        
    except Exception as e:
           raise NetworkSecurityException(e,sys)