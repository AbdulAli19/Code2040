# Step II: Reverse a string

# Abdul Ali

import requests
import json

url = "http://challenge.code2040.org/api/reverse"
url2 = "http://challenge.code2040.org/api/reverse/validate"
token = '34698de496bdc62158739a8db87da501'

# Retrieve string from the API

payload = {'token':token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
r = requests.post(url,json=payload, headers=headers)
originalstr = r.content

# Reverse original string

reversedstr = originalstr[::-1]

# Return reversed string

payload2 = {'token': token, 'string':reversedstr}
r2 = requests.post(url2,json=payload2, headers=headers)
print r2.content
