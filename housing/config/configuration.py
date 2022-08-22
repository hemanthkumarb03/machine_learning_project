from housing.entity.config_entity import *
from housing.utils.util import read_yaml_file
import os
from housing.constant import * 
from housing.exception import HousingException
from housing.logger  import logging


class Configuration:
    def __init__(self,config_file_path = CONFIG_FILE_PATH,
                      current_time_stamp = CURRENT_TIME_STAMP,
                      ) -> None:
        self.config_info =  read_yaml_file(config_file_path)
        self.training_pipeline_config = self.get_training_pipeline_config()
        self.time_stamp = current_time_stamp 

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass 

    def get_data_validation_config(self) -> DataValidationConfig:
        pass 

    def get_data_transformation_config(self) -> DataTransformationConfig:
        pass 

    def model_trainer_config(self) -> modelTrainConfig:
        pass 

    def model_evaluation_config(self) -> modelEvaluationConfig:
        pass  

    def get_model_pusher_config(self) -> modelPusherConfig:
        pass 

    def get_training_pipeline_config(self) -> trainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])

            training_pipeline_config = trainingPipelineConfig(artifact_dir)
            logging.info(f"Training pipeline config: {training_pipeline_config}")
            return training_pipeline_config

        except Exception as e:
            raise HousingException(e,sys) from e

