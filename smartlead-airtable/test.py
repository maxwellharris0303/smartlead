import requests
apikey = '21e10585-811e-41f2-9061-459df29737ae_292f3uj'
campaignid = '268763'
url = f'https://server.smartlead.ai/api/v1/campaigns/{campaignid}/leads?api_key={apikey}'
leadlist = [{
    'first_name': 'Cristiano',
    'last_name': 'Ronaldo',
    'email': 'cristiano@mufc.com',
    'phone_number': "239392029",
    'company_name': 'Manchester United',
    'website': 'mufc.com',
    'linkedin_profile': 'http://www.linkedin.com/in/cristianoronaldo',
    'location': 'London',
}]

response = requests.post(url, json={
        'lead_list': leadlist,
        "settings": {
            "ignore_global_block_list": True, 
            "ignore_unsubscribe_list": True,
            "ignore_duplicate_leads_in_other_campaign": False
        }
    })
print(response.json())