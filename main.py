import discord
import logging
from discord.ext import commands
import json
import os


class RakkiDakkiBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Connect
    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'Bot is working.\nHello! I\'m called {self.bot.user}, my ID is {self.bot.user.id}.')

    # Reconnect
    @commands.Cog.listener()
    async def on_resumed(self):
        print('Bot has reconnected!')

    # Error handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send('Invalid command, for valid commands check .help.')
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('Bot doesn\'t have permission to do that.')


# Intents !!!
intents = discord.Intents.all()
#intents.members = True
#intents.presences = True

# Loading data from json file
with open('config.json') as config:
    data = json.load(config)
    token = data['TOKEN']
    prefix = data['PREFIX']

# Bot settings
bot = commands.Bot(command_prefix=commands.when_mentioned_or(
    prefix), description='There is a description of the bot. (to be added later)', intents=intents)

# Logs
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(
    filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter(
    '%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@bot.event
# Greets new member of the server on the 'rakkidakki' text channel
# TO DO:
# - add more greetings and randomize them
async def on_member_join(member):
    channel = bot.get_channel(856558594518548500)
    await channel.send(f'Hello {member}! Nice to see you ;) ')
    #print(f"Member '{member.name}' has joined the server.")


@bot.event
# Sends message to the 'rakkidakki' text channel on who has left the server
async def on_member_remove(member):
    channel = bot.get_channel(856558594518548500)
    await channel.send(f'Member {member} has left the server.')
    #print(f"Member '{member.name}' has left the server.")


if __name__ == '__main__':
    # Loading extensions
    for filename in os.listdir('./commands'):
        if filename.endswith('.py'):
            bot.load_extension(f'commands.{filename[: -3]}')

    bot.add_cog(RakkiDakkiBot(bot))
    bot.run(token, reconnect=True)
