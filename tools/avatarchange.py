import sys
import requests
import discord
from base64 import b64encode

# Ripped from Discord.py
def get_mime(data):
    if data.startswith(b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A'):
        return 'image/png'
    elif data[6:10] in (b'JFIF', b'Exif'):
        return 'image/jpeg'
    elif data.startswith((b'\x47\x49\x46\x38\x37\x61', b'\x47\x49\x46\x38\x39\x61')):
        return 'image/gif'
    elif data.startswith(b'RIFF') and data[8:12] == b'WEBP':
        return 'image/webp'
# Ripped from Discord.py
def bytes_to_base64_data(data):
    fmt = 'data:{mime};base64,{data}'
    mime = get_mime(data)
    b64 = b64encode(data).decode('ascii')
    return fmt.format(mime=mime, data=b64)

client = discord.Client()
token = sys.argv[1]
avatarfile = sys.argv[2]
with open(avatarfile, "rb") as avatar_handle:
    encoded = bytes_to_base64_data(avatar_handle.read())

@client.event
async def on_ready():
    apilink = 'https://discordapp.com/api/v6/users/@me'
    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    payload = {'avatar': encoded, 'email': client.user.email, 'password': "", 'username': client.user.name}
    src = requests.patch(apilink, headers=headers, json=payload)
    await client.close()

client.run(token, bot=False)
