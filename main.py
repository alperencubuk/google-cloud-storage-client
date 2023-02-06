from google_client import GoogleClient
from service_account import get_service_account

if __name__ == "__main__":
    service_account = get_service_account()
    bucket_name = "alperen-bucket"

    client = GoogleClient(service_account=service_account, bucket_name=bucket_name)

    client.download_folder("test", "test1")
    client.upload_folder("test1", "test2")
