import requests
import json

"""https://gorest.co.in/public-api/users"""

accessToken = "GIY2lCXbfiBPzIZ05-Va2qZwIn3mxd_Ew1pU"
website="https://gorest.co.in"
uri = "/public-api/users"
form ="?_format=json"
auth=("GIY2lCXbfiBPzIZ05-Va2qZwIn3mxd_Ew1pU")

PARAMS = {'auth':auth}

url = website+uri+form+"&"+accessToken
url1 = "https://gorest.co.in/public-api/users/1164?_format=json&access-token=GIY2lCXbfiBPzIZ05-Va2qZwIn3mxd_Ew1pU"
print(url)

data = requests.get(url1).json()
data1 = requests.get(url,params=PARAMS)
print(data)
data1 = json.loads(data)
print(json.dumps(data1,indent=2,sort_keys=True))


#print(data1)


