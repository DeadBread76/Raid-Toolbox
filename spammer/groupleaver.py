import sys
import requests

token = sys.argv[1]
ID = sys.argv[2]

apilink = "https://discordapp.com/api/v6/channels/" + str(ID)

headers={
'Authorization': token
}

requests.delete(apilink, headers=headers)
