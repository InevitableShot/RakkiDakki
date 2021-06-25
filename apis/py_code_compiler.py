import json 
import requests

with open('config.json') as config:
    data = json.load(config)
    client_id = data['CLIENTID']
    client_secret = data['CLIENTSECRET']

def compiler(code):
    post_url = 'https://api.jdoodle.com/v1/execute'

    return json.loads(requests.post(
        post_url,
        json={
            "script": f"{code}",
            "language": "python3",
            "versionIndex": "3",
            "clientId": f"{client_id}",
            "clientSecret": f"{client_secret}"
        }
    ).content)