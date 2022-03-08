from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient
from dotenv import load_dotenv
import os
load_dotenv()

STORAGEACCOUNTURL = os.getenv('STORAGE_ACCOUNT_URL')
STORAGEACCOUNTKEY = os.getenv('STORAGE_ACCOUNT_KEY')
CONTAINERNAME = os.getenv('CONTAINER_NAME')

def download(url,blobname):
        blob_service_client_instance = BlobServiceClient(
            account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
        blob_client_instance = blob_service_client_instance.get_blob_client(
            CONTAINERNAME, blobname, snapshot=None)
        with open(url, "wb") as my_blob:
            blob_data = blob_client_instance.download_blob()
            blob_data.readinto(my_blob)

download("../data/output/train_model.csv","output/train_model.csv")
download("../train_models/model_risk.joblib","train_models/model_risk.joblib")

