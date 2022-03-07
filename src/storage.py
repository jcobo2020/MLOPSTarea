from azure.storage.blob import BlobServiceClient, BlobClient
from azure.storage.blob import ContentSettings, ContainerClient
from dotenv import load_dotenv
import os
load_dotenv()


STORAGEACCOUNTURL = os.getenv('STORAGE_ACCOUNT_URL')
STORAGEACCOUNTKEY = os.getenv('STORAGE_ACCOUNT_KEY')
CONTAINERNAME = os.getenv('CONTAINER_NAME')
BLOBNAME = os.getenv('BLOB_NAME')

class Storage:
    def __init__(self):
        self.blob_service_client_instance = BlobServiceClient(
            account_url=STORAGEACCOUNTURL, credential=STORAGEACCOUNTKEY)
        

    def download(self,url,blobname):
        blob_client_instance = self.blob_service_client_instance.get_blob_client(
            CONTAINERNAME, blobname, snapshot=None)
        with open(url, "wb") as my_blob:
            blob_data = blob_client_instance.download_blob()
            blob_data.readinto(my_blob)


    def upload(self,url,blobname):
        blob_client_instance = self.blob_service_client_instance.get_blob_client(
            CONTAINERNAME, blobname, snapshot=None)
        with open(url, "rb") as data:
            blob_client_instance.upload_blob(data,overwrite=True)
            pass
        
