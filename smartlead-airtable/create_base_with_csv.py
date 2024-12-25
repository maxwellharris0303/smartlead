import requests
import json
import os
import pandas as pd
from dotenv import load_dotenv

CSV_FILE_NAME = "1.csv"

data = pd.read_csv(CSV_FILE_NAME)
# Get the headers
headers = data.columns.tolist()

fields = []
for header in headers:
    fields.append({
        "name": header,
        "type": "singleLineText"
    })

load_dotenv()
ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
WORK_SAPCE_ID = os.getenv('WORK_SAPCE_ID')

url = "https://api.airtable.com/v0/meta/bases"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
json_data = {
    "name": "Smartlead Campaign 1",
    "tables": [
        {
            "description": "Lead list",
            "fields": fields,
            "name": "Campaign"
        },
    ],
    "workspaceId": WORK_SAPCE_ID
}

response = requests.post(url, headers=headers, json=json_data)
print(response.json())
print(f"Base ID: {response.json()['id']}")
print(f"Table Name & ID: {response.json()['tables'][0]['name']} & {response.json()['tables'][0]['id']}")

baseId = response.json()['id']
tableIdOrName = response.json()['tables'][0]['name']

data = pd.read_csv(CSV_FILE_NAME)

# Convert the data into a list of dictionaries
records = data.to_dict(orient='records')

# Create the final JSON structure
json_data = {"records": [{"fields": record} for record in records]}

# Print the generated JSON data
print(json_data)

url = f"https://api.airtable.com/v0/{baseId}/{tableIdOrName}"
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}
response = requests.post(url, headers=headers, data=json.dumps(json_data))
print(response.json())
if response.status_code == 200:
    print("Success")
else:
    print(f"Failed: {response.status_code}")

