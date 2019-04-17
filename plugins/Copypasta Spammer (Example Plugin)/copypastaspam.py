import discord
import sys

# make sure you use the order of when subprocess opens this file with sys.argv
token = sys.argv[1]
tokenno = sys.argv[2]
text = sys.argv[3]
textchan = sys.argv[4]
client = discord.Client()
wordList = text.split()
@client.event
async def on_ready():
    txtchan = client.get_channel(int(textchan))
    while not client.is_closed():
        for word in wordList:
            await txtchan.send(word)
try:
    client.run(token, bot=False)
except Exception as c:
    print(c)
