"""
This is a custom class created to map the target values i.e, to 0 and 1
respectively. A label encoding can also be used alternatively
"""
import os
from sensor.constants.training_pipeline import SAVED_MODEL_DIR, MODEL_FILE_NAME


class TargetValueMapping:
    def __init__(self):
        self.neg: int = 0
        self.pos: int = 1

    def to_dict(self):
        return self.__dict__


    def reverse_mapping(self):
        """
        Reverse Mapping function is created to reverse the effect of target mapping
        to its original values i.e, positive and negative
        """
        mapping_response = self.to_dict()
        return dict(zip(mapping_response.values(),mapping_response.keys()))

    #Write a code to train model and check the accuracy

class SensorModel:
    def __init__(self, preprocessor, model):
        self.preprocessor = preprocessor
        self.model = model

    def get_best_model(self):
        pass

    def predict(self, x):
        try:
            x_transform = self.preprocessor.transform(x)
            y_hat = self.model.predict(x_transform)
            return y_hat
        except Exception as e:
            raise e

class ModelResolver:

    def __init__(self,model_dir=SAVED_MODEL_DIR):
        try:
            self.model_dir = model_dir

        except Exception as e:
            raise e

    def get_best_model(self)->str:
        try:
            timestamps = list(map(int,os.listdir(self.model_dir)))
            latest_timestamp = max(timestamps)
            latest_model_path = os.path.join(self.model_dir,f"{latest_timestamp}",MODEL_FILE_NAME)
            return latest_model_path

        except Exception as e:
            raise e

    def is_model_exists(self)->bool:
        try:
            if not os.path.exists(self.model_dir):
                return False

            timestamps = os.listdir(self.model_dir)
            if len(timestamps)==0:
                return False

            latest_model_path = self.get_best_model()

            if not os.path.exists(latest_model_path):
                return False

            return True
        except Exception as e:
            raise e




