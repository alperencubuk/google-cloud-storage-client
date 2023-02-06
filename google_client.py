import os

from google.cloud import storage


class GoogleClient:
    def __init__(self, service_account: dict, bucket_name: str):
        self.bucket_name = bucket_name
        self.client = storage.Client.from_service_account_info(service_account)
        self.bucket = self.client.bucket(bucket_name)

    def upload_file(self, source: str, destination: str):
        blob = self.bucket.blob(destination)
        blob.upload_from_filename(source)

    def download_file(self, source: str, destination: str):
        blob = self.bucket.blob(source)
        blob.download_to_filename(destination)

    def remove_file(self, file: str):
        self.bucket.blob(file).delete()

    def upload_folder(self, source: str, destination: str):
        for file in os.listdir(source):
            source_file = f"{source}/{file}"
            destination_file = f"{destination}/{file}"
            blob = self.bucket.blob(destination_file)
            blob.upload_from_filename(source_file)

    def download_folder(self, source: str, destination: str):
        blob_list = self.client.list_blobs(self.bucket_name, prefix=source)
        os.makedirs(destination, exist_ok=True)
        for blob in blob_list:
            blob = self.bucket.blob(blob.name)
            file = os.path.join(destination, str(blob.name).split("/")[-1])
            blob.download_to_filename(file)

    def remove_folder(self, folder: str):
        blob_list = self.client.list_blobs(self.bucket_name, prefix=folder)
        for blob in blob_list:
            self.bucket.blob(blob.name).delete()
