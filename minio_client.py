import os

from minio import Minio


class MinioClient:
    def __init__(
        self, access_key: str, secret_key: str, bucket_name: str, endpoint: str
    ):
        self.bucket_name = bucket_name
        self.client = Minio(
            endpoint=endpoint,
            access_key=access_key,
            secret_key=secret_key,
        )

    def upload_file(self, source: str, destination: str):
        self.client.fput_object(self.bucket_name, destination, source)

    def download_file(self, source: str, destination: str):
        self.client.fget_object(self.bucket_name, source, destination)

    def remove_file(self, file: str):
        self.client.remove_object(self.bucket_name, file)

    def upload_folder(self, source: str, destination: str):
        for file in os.listdir(source):
            source_file = os.path.join(source, file)
            destination_file = f"{destination}/{file}"
            self.client.fput_object(self.bucket_name, destination_file, source_file)

    def download_folder(self, source: str, destination: str):
        blob_list = self.client.list_objects(self.bucket_name, prefix=f"{source}/")
        os.makedirs(destination, exist_ok=True)
        for blob in blob_list:
            file = os.path.join(destination, blob.object_name.split("/")[-1])
            self.client.fget_object(self.bucket_name, blob.object_name, file)

    def remove_folder(self, folder: str):
        blob_list = self.client.list_objects(self.bucket_name, prefix=f"{folder}/")
        for blob in blob_list:
            self.client.remove_object(self.bucket_name, blob.object_name)
