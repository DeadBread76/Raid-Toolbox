import sys
import discord
token = sys.argv[1]
client = discord.Client()
@client.event
async def on_ready():
    for server in client.guilds:
        await server.leave()
    await client.close()
client.run(token, bot=False)
