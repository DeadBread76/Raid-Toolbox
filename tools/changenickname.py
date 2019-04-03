import discord
import sys

client = discord.Client()
token = sys.argv[1]
SERVER = sys.argv[2]
nick = sys.argv[3]

@client.event
async def on_ready():
    server = client.get_guild(int(SERVER))
    try:
        await server.me.edit(nick=str(nick))
    except Exception:
        pass
    await client.close()
try:
    client.run(token, bot=False)
except Exception as c:
    print (c)
