import os
import requests

api_token = "btjZHTwIomIDkazihXanMyPwZaDKDzJX"


api_endpoint = "https://www.ncei.noaa.gov/cdo-web/api/v2/"
url = api_endpoint + "data"
headers = {'token': api_token}
PARAMS = {'datasetid': "GHCND", 'startdate': "2020-01-01", 'enddate': "2020-06-01", 'locationid': 'ZIP:43338'}
r = requests.get(url = url, headers=headers, params=PARAMS)
if r.status_code == 200:
    json = r.json()
    print(json)
else:
    print("not a valid endpoint")
    print(r.content)