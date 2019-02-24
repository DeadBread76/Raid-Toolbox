import sys
import requests

token = sys.argv[1]
userid = sys.argv[2]

apilink = 'https://discordapp.com/api/v6/users/@me/relationships/'+ str(userid)

headers={
    'Authorization': token,
    'Content-Type': 'application/json'
}

requests.put(apilink, headers=headers)
