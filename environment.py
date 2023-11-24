import os
from dotenv import load_dotenv

load_dotenv()

# AWS
access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_access_key = os.environ.get("AWS_SECRET_ACCESS_KEY")


# Flask variables
secret_key = os.environ.get("SECRET_KEY")



