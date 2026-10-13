import os
import sys
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()
mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)
import pymongo
from networksecurity.pipeline.training_pipeline import TrainingPipeline
from networksecurity.pipeline.batch_prediction import BatchPrediction

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, File, UploadFile, Request
from uvicorn import run as app_run
from fastapi.responses import Response
from starlette.responses import RedirectResponse
from networksecurity.constants.training_pipeline import DATA_INGESTION_COLLECTION_NAME
from networksecurity.constants.training_pipeline import DATA_IGESTION_DATABASE_NAME

client = pymongo.MongoClient(mongo_db_url, tlsCAFile=ca)
database = client[DATA_IGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_headers=["*"],
    allow_methods=["*"]
)

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")
    except Exception as e:
        raise NetworkSecurityException(e,sys)

@app.post("/predict")
async def predict_route(request:Request,file:UploadFile = File(...)):
    try:
        batch_prediction_obj = BatchPrediction()
        op_table_html = batch_prediction_obj.batch_prediction(file=file)
        return templates.TemplateResponse(name="table.html",request=request, context={"table": op_table_html})
    except Exception as e:
        raise NetworkSecurityException(e,sys)
 
if __name__  == "__main__":
    logging.info("Starting App server")
    app_run(app,host="0.0.0.0",port=8000)