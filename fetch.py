#MOVE KEY TO STREAMLIT SECRETS BEFORE COMMITING
import os
import requests
API_KEY = os.environ.get("NASA_API_KEY","DEMO_KEY")
url = "https://api.nasa.gov/neo/rest/v1/feed"
params = {
    "start_date": "2026-06-16"
    "end_date": "2026-06-23"
    "api_key": API_KEY
}

response = requests.get(url, params=params)
print(response.json)
