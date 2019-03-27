import sys
import requests
import random
token = sys.argv[1]
userid = sys.argv[2]
useproxies = sys.argv[3]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()

def proxyfriend():
    try:
        proxy = random.choice(proxy_list)
        requests.put(apilink, headers=headers, proxies={"http": proxy, "https": proxy})
    except Exception:
        proxyfriend()

apilink = 'https://discordapp.com/api/v6/users/@me/relationships/'+ str(userid)

headers={
    'Authorization': token,
    'Content-Type': 'application/json'
}
if useproxies == 'True':
    proxyfriend()
else:
    requests.put(apilink, headers=headers)
