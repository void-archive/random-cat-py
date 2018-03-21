import discord
import asyncio
import requests

prefix = "test!"

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
            
        if message.content.startswith(prefix + 'cat'):
            response = requests.get('https://aws.random.cat/meow')
            data = response.json()
            await message.channel.send(data['file'])

client = MyClient()
client.run('bot_token')
