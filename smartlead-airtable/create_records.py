import requests
import json
import pandas as pd

# Read the CSV file
data = pd.read_csv('1.csv')

# Convert the data into a list of dictionaries
records = data.to_dict(orient='records')

# Create the final JSON structure
json_data = {"records": [{"fields": record} for record in records]}

# Print the generated JSON data
print(json_data)

baseId = "appiIOZWlRqEb3y8v"
tableIdOrName = "Campaign"

url = f"https://api.airtable.com/v0/{baseId}/{tableIdOrName}"
headers = {
    "Authorization": "Bearer patB17ZsXMc93ffTb.9a0fe5dad27b67ce5c3379da07954b10722a7f3a6dce1ae2e238bfbdeb05c7c8",
    "Content-Type": "application/json"
}
# data = {
#     "records": [
#         {
#             "fields": {
#                 "First Name": "Michelle",
#                 "Last Name": "Merrigan",
#                 "Email Address": "michelle@ajparkes.com.au",
#                 "Phone Number": "--",
#                 "Company Name": "aj parkes & co pty ltd",
#                 "Website": "ajparkes.com.au",
#                 "LinkedIn Profile": "--",
#                 "Location": "--"
#             }
#         }
#     ]
# }

response = requests.post(url, headers=headers, data=json.dumps(json_data))
print(response)
print(response.json())