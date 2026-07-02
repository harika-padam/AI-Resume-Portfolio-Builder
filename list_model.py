import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

url = "https://router.huggingface.co/v1/models"
headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.text)
