import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging
from networksecurity.utils.main_utils.utils import load_object
from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from fastapi import File,UploadFile
import pandas as pd

class BatchPrediction:
    def __init__(self):
        try:
            preprocessor = load_object("final_model/preprocessor.pkl")
            model = load_object("final_model/model.pkl")
            self.final_model = NetworkModel(preprocessor=preprocessor,model=model)
        except Exception as e:
            raise NetworkSecurityException(e,sys)

    def batch_prediction(self,file:UploadFile = File(...)) -> str:
        df = pd.read_csv(file.file)
        y_pred = self.final_model.predict(df)
        df['predicted_column'] = y_pred
        df.to_csv('prediction_output/output.csv')
        return df.to_html(classes='table table-striped')