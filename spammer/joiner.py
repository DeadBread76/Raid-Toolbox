import sys
import requests

token = sys.argv[1]
link = sys.argv[2]
apilink = "https://discordapp.com/api/v6/invite/" + str(link)
headers={
    'Authorization': token
}
requests.post(apilink, headers=headers)
