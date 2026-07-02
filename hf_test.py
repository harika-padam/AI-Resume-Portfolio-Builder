import requests
import os
from dotenv import load_dotenv

load_dotenv()

HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    print("HF_API_KEY not found. Check your .env file.")
    exit()

API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def generate_text(prompt):
    payload = {
        "model": "HuggingFaceTB/SmolLM3-3B",
        "messages": [
            {"role": "system", "content": "You are a professional resume writer."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 150,
        "temperature": 0.7
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("Status Code:", response.status_code)
    print("Raw Response:")
    print(response.text)

    if response.status_code == 200:
        return response.json()
    else:
        return None


result = generate_text("Write a professional resume summary for a Python developer.")
print("\nParsed Result:")
print(result)

if result:
    print("\nFinal Generated Text:")
    print(result["choices"][0]["message"]["content"])


