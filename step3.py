# Step III: Needle in a haystack

# Abdul Ali

import requests
import json

url = "http://challenge.code2040.org/api/haystack"
url2 = "http://challenge.code2040.org/api/haystack/validate"
token = '34698de496bdc62158739a8db87da501'

# Retrieve needle(a string) and haystack(an array of strings) from the API

payload = {'token':token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
r = requests.post(url,json=payload,headers=headers)

dictionary = r.content
dictionary = json.loads(dictionary)
needle = dictionary["needle"]
haystack = dictionary["haystack"]


index = 0
i= 0

# Loop through array until needle is found
# Set index equal to the 'index' in the array at which needle is found

while i < len(haystack):
    if haystack[i] == needle:
        index = i
        break
    else:
        i+=1

# Return index

payload2 = {'token':token, 'needle':index}          
r2 = requests.post(url2,json=payload2,headers=headers)

print r2.content

