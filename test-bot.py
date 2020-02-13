# permissions integer : 330816

import discord
import config

token = config.token # put your bot token in a config.py file and add this file to the .gitignore

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$about'):
        await message.channel.send('Hello ! I am a work-in-progress bot for vote automation. ')
        await message.channel.send('One of my planned features is to automatize server-related decisions decided by these votes. ')
        await message.channel.send('Right now I cannot do any of this yet, but be on the lookout for updates !')

client.run(token)