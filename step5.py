# Step V: The dating game

# Abdul Ali

import requests
import json
import datetime
from datetime import timedelta


url = "http://challenge.code2040.org/api/dating"
url2 = "http://challenge.code2040.org/api/dating/validate"
token = '34698de496bdc62158739a8db87da501'

# Retrieving datestamp and interval from the API

payload = {'token':token}
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache"
    }
r = requests.post(url,json=payload,headers=headers)

dictionary = r.content
dictionary = json.loads(dictionary)
datestamp = dictionary["datestamp"]
interval = dictionary["interval"]

# Convert datestamp to a datetime object
# Add interval to datetime object
# Convert back into an ISO 8601 datestamp

inputDate = datetime.datetime.strptime( datestamp, "%Y-%m-%dT%H:%M:%SZ" )
interval = datetime.timedelta(seconds = interval)
newdate = inputDate + interval
newdate = newdate.isoformat() +'Z'


# Return date

payload2 = {'token':token, 'datestamp':newdate}        
r2 = requests.post(url2,json=payload2,headers=headers)

print r2.content

