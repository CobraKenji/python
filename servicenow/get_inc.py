##Sample HTTP GET Request to ServiceNow
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("admin", "adminpass")
uri = https://dev11235.service-now.com/api/now/table/incident?sysparm_limit=1&sysparm_query=active%3Dtrue%5EstateIN1%2C2%2C-1%2C-3%2C-2%2C5"
headers = {
    "accept": "application/json;charset=utf-8",
    "Content-Type": "application/json",
}

response = requests.get(url=uri, auth=auth, verify=False, headers=headers)
content = response.json()
print "Response Status Code: " + str(r.status_code)
print(content)
