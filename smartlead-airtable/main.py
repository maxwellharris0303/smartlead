import requests

url = "https://api.airtable.com/v0/appHdom1GelRjJdR5/Campaign"
headers = {
    "Authorization": "Bearer patB17ZsXMc93ffTb.9a0fe5dad27b67ce5c3379da07954b10722a7f3a6dce1ae2e238bfbdeb05c7c8",
    "Content-Type": "text/csv"
}
data = '''First,column2
row1-column1,row1-column2
row2-column1,row2-column2'''

response = requests.post(url, headers=headers)

# Check the response status code
if response.status_code == 200:
    print("Request successful")
else:
    print("Request failed with status code:", response.status_code)
