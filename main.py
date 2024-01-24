import os
import requests

api_token = "btjZHTwIomIDkazihXanMyPwZaDKDzJX"


api_endpoint = "https://www.ncei.noaa.gov/cdo-web/api/v2/"
url = api_endpoint + "data?datasetid=GHCND"
headers = {'token': api_token}
params = {'datasetid': "GHCND"}
r = requests.get(url = url, headers=headers)
if r.status_code == 200:
    json = r.json()
    print(json)
else:
    print("not a valid endpoint")
    print(r)