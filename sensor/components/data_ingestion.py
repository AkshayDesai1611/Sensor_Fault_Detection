from sensor.exception import SensorException
from sensor.logger import logging
from sensor.entity.config_entity import DataIngestionConfig
from sensor.entity.artifact_entity import DataIngestionArtifact
import os, sys
from pandas import DataFrame
from sensor.data_access.sensordata import SensorData

class DataIngestion:

    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise SensorException(e,sys)

    def export_data_into_feature_store(self)-> DataFrame:
        """

        :return: Export data from MongoDB collection as Dataframe

        """
        try:
            logging.info("Exporting Data from mongodb to feature store")
            sensor_data = SensorData()
            dataframe = sensor_data.export_collection_as_dataframe(collection_name=self.data_ingestion_config.collection_name)

            feature_store_file_path=self.data_ingestion_config.feature_store_file_path
            #creating feature_store folder from feature store file path

            dir_path = os.path.dirname(feature_store_file_path)
            os.makedirs(dir_path,exist_ok=True)

            dataframe.to_csv(feature_store_file_path,index=False,header=True)
            return dataframe
        pass

    def split_data_into_train_test(self,dataframe:DataFrame):
        pass

    def initiate_data_ingestion(self)->DataIngestionArtifact:
        try:
            pass
        except Exception as e:
            raise SensorException(e,sys)
