from networksecurity.componets.data_ingestion import DataIngestion
from networksecurity.componets.data_validation import DataValidation
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig, DataValidationConfig
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

        
    except Exception as e:
           raise NetworkSecurityException(e,sys)