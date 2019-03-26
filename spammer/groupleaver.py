import sys
import requests
import random

token = sys.argv[1]
ID = sys.argv[2]
useproxies = sys.argv[3]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()

def proxyleave():
    try:
        proxy = random.choice(proxy_list)
        requests.delete(apilink, headers=headers, proxies={"http": proxy, "https": proxy})
    except Exception:
        proxyleave()
apilink = "https://discordapp.com/api/v6/channels/" + str(ID)
headers = {
    'Authorization': token
}
if useproxies == 'True':
    proxyleave()
else:
    requests.delete(apilink, headers=headers)
