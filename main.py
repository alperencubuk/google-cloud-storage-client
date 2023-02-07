from auth import get_bucket_name, get_hmac_keys, get_service_account
from google_client import GoogleClient
from minio_client import MinioClient

bucket_name = get_bucket_name()


def google_client():
    service_account = get_service_account()
    return GoogleClient(service_account=service_account, bucket_name=bucket_name)


def minio_client():
    hmac_keys = get_hmac_keys()
    access_key = hmac_keys["access_key"]
    secret_key = hmac_keys["secret_key"]
    endpoint = hmac_keys["endpoint"]
    return MinioClient(
        access_key=access_key,
        secret_key=secret_key,
        bucket_name=bucket_name,
        endpoint=endpoint,
    )


if __name__ == "__main__":
    google_client = google_client()
    google_client.download_folder("test", "gtest1")
    google_client.upload_folder("gtest1", "gtest2")

    minio_client = minio_client()
    minio_client.download_folder("test", "mtest1")
    minio_client.upload_folder("mtest1", "mtest2")
