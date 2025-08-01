import os
import io
import sys
import keras
import pickle
from PIL import Image
from hate.logger import logging
from hate.constants import *
from hate.exception import CustomException
from keras.utils import pad_sequences
from hate.configuration.local_data_manager import LocalDataManager
from hate.components.data_transforamation import DataTransformation
from hate.entity.config_entity import DataTransformationConfig
from hate.entity.artifact_entity import DataIngestionArtifacts


class PredictionPipeline:
    def __init__(self):
        self.local_data_dir = LOCAL_DATA_DIR
        self.model_name = MODEL_NAME
        self.model_path = os.path.join("artifacts", "PredictModel")
        self.local_data_manager = LocalDataManager()
        self.data_transformation = DataTransformation(data_transformation_config= DataTransformationConfig,data_ingestion_artifacts=DataIngestionArtifacts)


    
    def get_model_from_local(self) -> str:
        """
        Method Name :   get_model_from_local
        Description :   This method to get best model from local storage
        Output      :   best_model_path
        """
        logging.info("Entered the get_model_from_local method of PredictionPipeline class")
        try:
            # Loading the best model from local storage
            os.makedirs(self.model_path, exist_ok=True)
            self.local_data_manager.sync_folder_from_local(self.model_name, self.model_path)
            best_model_path = os.path.join(self.model_path, self.model_name)
            logging.info("Exited the get_model_from_local method of PredictionPipeline class")
            return best_model_path

        except Exception as e:
            raise CustomException(e, sys) from e
        

    
    def predict(self,best_model_path,text):
        """load image, returns cuda tensor"""
        logging.info("Running the predict function")
        try:
            best_model_path:str = self.get_model_from_local()
            load_model=keras.models.load_model(best_model_path)
            with open('tokenizer.pickle', 'rb') as handle:
                load_tokenizer = pickle.load(handle)
            
            text=self.data_transformation.concat_data_cleaning(text)
            text = [text]            
            print(text)
            seq = load_tokenizer.texts_to_sequences(text)
            padded = pad_sequences(seq, maxlen=300)
            print(seq)
            pred = load_model.predict(padded)
            pred
            print("pred", pred)
            if pred>0.5:

                print("hate and abusive")
                return "hate and abusive"
            else:
                print("no hate")
                return "no hate"
        except Exception as e:
            raise CustomException(e, sys) from e

    
    def run_pipeline(self,text):
        logging.info("Entered the run_pipeline method of PredictionPipeline class")
        try:

            best_model_path: str = self.get_model_from_local() 
            predicted_text = self.predict(best_model_path,text)
            logging.info("Exited the run_pipeline method of PredictionPipeline class")
            return predicted_text
        except Exception as e:
            raise CustomException(e, sys) from e
