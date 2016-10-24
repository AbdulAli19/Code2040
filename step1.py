# Step I: Registration

# Abdul Ali

import requests
import json

url = "http://challenge.code2040.org/api/register"
token = '34698de496bdc62158739a8db87da501'
github = "https://github.com/AbdulAli19/Code2040"

# Connect to the registration endpoint

payload = {'token': token, 'github': github}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
response = requests.post(url,json=payload, headers=headers)

print response.content
