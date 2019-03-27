import sys
import requests

token = sys.argv[1]
house = sys.argv[2]

apilink = 'https://discordapp.com/api/v6/hypesquad/online'
headers = {'Authorization': token, 'Content-Type': 'application/json'}
payload = {'house_id': int(house)}
"""
bravery = 1
brilliance = 2
ballance = 3
"""
requests.post(apilink, headers=headers, json=payload)
