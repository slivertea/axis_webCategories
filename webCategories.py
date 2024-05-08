import requests
import json
import os
import csv

#Define static values
TOKEN = os.getenv('AXIS_TOKEN')
path = "https://admin-api.axissecurity.com/api/v1.0/webcategories"
getUri = path+"?pageSize=500&pageNumber=1"
postUri = path+"/"
apiToken = 'Bearer '+TOKEN
payload = ""
headers = {
    'Authorization': apiToken,
    'Content-Type': 'application/json'
}


zoneIdPublic='d2031599-31d9-4f75-9753-20929d0cf6a1'
zoneIdNew='82025e12-a263-406e-95ca-451cadadc94a'


responseCategories = (requests.request("GET", getUri, headers=headers, data=payload).json())
dataCategories = responseCategories['data']

#print (json.dumps(dataCategories[0]))

# Change Zone Id 1:1
payloadPut = dataCategories[0]
payloadPut["connectorZoneId"] = zoneIdNew
responsePut = requests.request("PUT", postUri+payloadPut["id"], headers=headers, data=json.dumps(payloadPut))
print ("Response code:", responsePut.status_code, '|', payloadPut["name"])


for category in dataCategories:
    payloadPut = category
    payloadPut["connectorZoneId"] = zoneIdPublic
    responsePut = requests.request("PUT", postUri+payloadPut["id"], headers=headers, data=json.dumps(payloadPut))
    print ("Response code:", responsePut.status_code, '|', payloadPut["name"])
