from dotenv import load_dotenv
import game
import os
import discord
from discord.ext import commands

load_dotenv() # take environment variables from .env.
token = os.getenv("TOKEN") # get the token from .env

def printRule():
        return """===================
Rock Paper Scissors Lizard Spock
===================
  1) 🤚
  2) ✊
  3) ✌️
  4) 🦎
  5) 🖖"""


class MyClient(commands.Bot):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('/rule'):
            await message.channel.send(printRule()) # print the rules
        if message.content.startswith('/play'):
            userC=int(message.content[6]) # get the user choice
            if userC<1 or userC>5:
                await message.channel.send("Invalid choice")
            else:
                start=game.Game(userC)
                await message.channel.send(start.printC())
                await message.channel.send(start.result())


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(command_prefix='/', intents=intents) # create a new client instance
client.run(token) 