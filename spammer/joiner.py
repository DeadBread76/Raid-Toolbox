import sys
import requests
import random

token = sys.argv[1]
link = sys.argv[2]
useproxies = sys.argv[3]

if useproxies == 'True':
    proxy_list = open("proxies.txt").read().splitlines()
    
def proxyjoin():
    try:
        proxy = random.choice(proxy_list)
        requests.post(apilink, headers=headers, proxies={"http": proxy, "https": proxy})
    except Exception:
        proxyjoin()

apilink = "https://discordapp.com/api/v6/invite/" + str(link)
headers={
    'Authorization': token
}
if useproxies == 'True':
    proxyjoin()
else:
    requests.post(apilink, headers=headers)
