import discord
from discord.ext import commands
import json
import requests

# Parameters
description = '''
    There is a description of the bot. (to be added later)
'''
with open('config.json') as config:
    data = json.load(config)
    token = data['TOKEN']
    prefix = data['PREFIX']
intents = discord.Intents(messages=True, guilds=True,
                          reactions=True, members=True, presences=True)
bot = commands.Bot(command_prefix=prefix, intents=intents)
ctx = commands.Context
# ------------------------------------------------------------ #


@bot.event
async def on_ready():
    print(
        f'Bot is working.\nHello! I\'m called {bot.user.name}, my ID is {bot.user.id}.')


@bot.event
# Greets new member of the server on the 'rakkidakki' text channel
# TO DO:
# - add more greetings and randomize them
# - after testing change channel from 'rakkidakki' to 'log'
async def on_member_join(member):
    channel = bot.get_channel(824820147722256454)
    await channel.send(f'Hello {member}! Nice to see you ;) ')
    print(f"Member '{member.name}' has joined the server.")


@bot.event
# Sends message to the 'rakkidakki' text channel on who has left the server
async def on_member_remove(member):
    channel = bot.get_channel(824820147722256454)
    await channel.send(f"Member {member} has left the server.")
    print(f"Member '{member.name}' has left the server.")


@bot.command()
async def ping(ctx):
    await ctx.send(f'My latency is {round(bot.latency * 1000)}ms.')


@bot.command()
async def quote(ctx):
    # Quotes API - link: https://goquotes.docs.apiary.io/#
    url = 'https://goquotes-api.herokuapp.com/api/v1/random?count=1'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers).json()
    await ctx.send(f"'{response['quotes'][0]['text']}'\n~ {response['quotes'][0]['author']}\ntag: {response['quotes'][0]['tag']}")


bot.run(token)
