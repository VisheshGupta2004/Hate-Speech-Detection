import os
import shutil
from pathlib import Path


class LocalDataManager:
    """
    Local data manager for local deployment
    """
    
    def __init__(self, local_data_dir="local_data"):
        self.local_data_dir = local_data_dir
        self.models_dir = os.path.join(local_data_dir, "models")
        self.data_dir = os.path.join(local_data_dir, "data")
        
        # Create directories if they don't exist
        os.makedirs(self.local_data_dir, exist_ok=True)
        os.makedirs(self.models_dir, exist_ok=True)
        os.makedirs(self.data_dir, exist_ok=True)
    
    def sync_folder_to_local(self, source_path, filename):
        """
        Copy file to local storage 
        """
        try:
            source_file = os.path.join(source_path, filename)
            destination_file = os.path.join(self.models_dir, filename)
            
            if os.path.exists(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"Copied {filename} to local storage")
            else:
                print(f"Source file {source_file} not found")
                
        except Exception as e:
            print(f"Error copying file: {e}")
    
    def sync_folder_from_local(self, filename, destination):
        """
        Copy file from local storage 
        """
        try:
            source_file = os.path.join(self.models_dir, filename)
            destination_file = os.path.join(destination, filename)
            
            if os.path.exists(source_file):
                shutil.copy2(source_file, destination_file)
                print(f"Copied {filename} from local storage")
            else:
                print(f"Local file {source_file} not found")
                
        except Exception as e:
            print(f"Error copying file: {e}")
    
    def get_dataset_path(self):
        """
        Get the path to the dataset in the data directory
        """
        dataset_path = os.path.join(self.data_dir, "dataset.zip")
        if os.path.exists(dataset_path):
            return dataset_path
        else:
            # If dataset doesn't exist in local_data, look in the original data directory
            original_dataset = os.path.join("data", "dataset.zip")
            if os.path.exists(original_dataset):
                return original_dataset
            else:
                raise FileNotFoundError("Dataset not found. Please ensure dataset.zip is in the data/ directory") 