import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
HF_API_KEY = os.getenv("HF_API_KEY")

if not HF_API_KEY:
    print("HF_API_KEY not found in .env file")
    exit()

# HuggingFace Router API
API_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}",
    "Content-Type": "application/json"
}

def extract_final_answer(text: str):
    # Remove thinking tags if model outputs them
    text = text.replace("<think>", "").replace("</think>", "").strip()

    # Split into paragraphs and return the last meaningful one
    parts = [p.strip() for p in text.split("\n\n") if p.strip()]
    return parts[-1]

def generate_text(prompt):
    payload = {
        "model": "katanemo/Arch-Router-1.5B",
        "messages": [
            {
                "role": "system",
                "content": "Write a professional resume summary in 2–3 sentences. Only give the final answer."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        "max_tokens": 160,
        "temperature": 0.6
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    print("Status Code:", response.status_code)

    if response.status_code != 200:
        print("Error Response:")
        print(response.text)
        return None

    data = response.json()
    raw_text = data["choices"][0]["message"]["content"]

    # Clean output
    final_text = extract_final_answer(raw_text)
    return final_text


if __name__ == "__main__":
    prompt = "Write a professional resume summary for a Python developer."
    result = generate_text(prompt)

    print("\nFinal Generated Text:\n")
    print(result)
