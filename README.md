# Google Cloud Storage Client

### Summary:

This is simple Google Cloud storage client which performs download/upload operations from the Google Cloud.

---

### Requirements:
* Python (3.10+ recommended)

### How to Run:

First, open `auth.py` and edit `service_account` for google client or `hmac_keys` for minio client.  
Also edit `bucket_name` for both.  
Upload a `test` folder with files to your google cloud storage.  
Then run this commands:

```
pip install -r requirements.txt
python main.py
```

---

**Alperen Cubuk**