# Step IV: Prefix

# Abdul Ali

import requests
import json
from collections import Counter

url = "http://challenge.code2040.org/api/prefix"
url2 = "http://challenge.code2040.org/api/prefix/validate"
token = '34698de496bdc62158739a8db87da501'

# Retrieve prefix and array from the API

payload = {'token':token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
r = requests.post(url,json=payload,headers=headers)

dictionary = r.content
dictionary = json.loads(dictionary)
prefix = dictionary["prefix"]
array = dictionary["array"]

prefixlength = len(prefix)
newarray = []

# Loop through array while checking if a given string begins with the given prefix.
# If it doesn't, append the string to our new array. If it does, do nothing.

for str in array:
    if(Counter(prefix) != Counter(str[0:prefixlength])):
       newarray.append(str)

# Return array containing only the strings that don't begin with prefix

payload2 = {'token':token, 'array':newarray}
r2 = requests.post(url2,json=payload2,headers=headers)

print r2.content

