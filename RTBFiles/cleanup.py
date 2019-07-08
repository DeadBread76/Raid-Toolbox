import discord
import sys
import psutil

token = sys.argv[1]
SERVER = sys.argv[2]
parentprocess = sys.argv[3]
client = discord.Client(status=discord.Status.offline)


@client.event
async def on_ready():
    server = client.get_guild(int(SERVER))
    for channel in server.text_channels:
        myperms = channel.permissions_for(server.get_member(client.user.id))
        if not myperms.send_messages:
            continue
        async for message in channel.history(limit=9999):
            if not psutil.pid_exists(int(parentprocess)):
                await client.logout()
                sys.exit()
            if message.author == client.user:
                await message.delete()
    await client.close()

try:
    client.run(token, bot=False)
except Exception:
    pass
