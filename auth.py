def get_service_account() -> dict:
    return {
        "type": "service_account",
        "project_id": "project_id",
        "private_key_id": "private_key_id",
        "private_key": "----BEGIN PRIVATE KEY----\nKEY\n----END PRIVATE KEY----\n",
        "client_email": "project-service@project_id.iam.gserviceaccount.com",
        "client_id": "client_id",
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/",
    }


def get_hmac_keys() -> dict:
    return {
        "access_key": "access_key",
        "secret_key": "secret_key",
        "endpoint": "storage.googleapis.com",
    }


def get_bucket_name() -> str:
    return "your-bucket-name"
