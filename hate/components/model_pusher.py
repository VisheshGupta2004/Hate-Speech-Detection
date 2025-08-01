import sys
from hate.logger import logging
from hate.exception import CustomException
from hate.configuration.local_data_manager import LocalDataManager
from hate.entity.config_entity import ModelPusherConfig
from hate.entity.artifact_entity import ModelPusherArtifacts

class ModelPusher:
    def __init__(self, model_pusher_config: ModelPusherConfig):
        """
        :param model_pusher_config: Configuration for model pusher
        """
        self.model_pusher_config = model_pusher_config
        self.local_data_manager = LocalDataManager()

    
    
    def initiate_model_pusher(self) -> ModelPusherArtifacts:
        """
            Method Name :   initiate_model_pusher
            Description :   This method initiates model pusher.

            Output      :    Model pusher artifact
        """
        logging.info("Entered initiate_model_pusher method of ModelTrainer class")
        try:
            # Uploading the model to local storage

            self.local_data_manager.sync_folder_to_local(self.model_pusher_config.TRAINED_MODEL_PATH,
                                              self.model_pusher_config.MODEL_NAME)

            logging.info("Uploaded best model to local storage")

            # Saving the model pusher artifacts
            model_pusher_artifact = ModelPusherArtifacts(
                bucket_name=self.model_pusher_config.LOCAL_DATA_DIR
            )
            logging.info("Exited the initiate_model_pusher method of ModelTrainer class")
            return model_pusher_artifact

        except Exception as e:
            raise CustomException(e, sys) from e
