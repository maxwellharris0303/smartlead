import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')

url = "https://api.airtable.com/v0/meta/bases"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}"
}

response = requests.get(url, headers=headers)

# Prettify the JSON
prettified_json = json.dumps(response.json(), indent=4)

print(prettified_json)