import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

url = f"https://server.smartlead.ai/api/v1/campaigns/create?api_key={API_KEY}"

headers = {"accept": "application/json"}

data = {
    "name": "My Campaign",
}

response = requests.post(url, headers=headers, json=data)

print(response.text)