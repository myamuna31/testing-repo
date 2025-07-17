# vulnerable_sample.py

import requests

# Hardcoded API key (security vulnerability)
API_KEY = "sk_test_51H8s2..."

def send_data(payload):
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.post("https://api.example.com/data", headers=headers, json=payload)
    return response.status_code

# Sample usage
send_data({"email": "user@example.com", "amount": 100})
