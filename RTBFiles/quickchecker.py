import sys
import json
import requests
from colorama import init
from termcolor import colored
init()
token = sys.argv[1]
apilink = 'https://discordapp.com/api/v6/users/@me'
headers = {'Authorization': token, 'Content-Type': 'application/json'}
src = requests.get(apilink, headers=headers)
if "401: Unauthorized" in str(src.content):
    print(colored(token + " Invalid","red"))
else:
    response = json.loads(src.content.decode())
    if response["verified"]:
        print(colored(token + " Valid","green"))
        with open ("quick_checked_tokens_verified.txt", "a+") as handle:
            handle.write(token+"\n")
    else:
        print(colored(token + " Unverified","yellow"))
        with open ("quick_checked_tokens_unverified.txt", "a+") as handle:
            handle.write(token+"\n")
