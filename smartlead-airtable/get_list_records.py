import requests
import json

base_id = "app6PVvXIzXHyBHLd"
table_name = "Campaign"

url = f"https://api.airtable.com/v0/{base_id}/{table_name}"
headers = {"Authorization": "Bearer patB17ZsXMc93ffTb.9a0fe5dad27b67ce5c3379da07954b10722a7f3a6dce1ae2e238bfbdeb05c7c8"}

response = requests.get(url, headers=headers)

json_data = response.json()['records'][1]
# Prettify the JSON
prettified_json = json.dumps(json_data, indent=4)

print(prettified_json)