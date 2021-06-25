from discord.ext import commands
import discord
import time
import requests
import random
import aiohttp


class StandardCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    # Lists all of the commands and explains them
    async def helpme(self, ctx):
        await ctx.send(f"""Helping hand is here my friend!\n
Standard commands:
helpme - shows the message you're reading right now
ping - tells you the latency of the bot
purge - deletes as many messages as you insert
quote - gives you a random quote
todays_quote - gives you the quote of the day
meme - gives you random meme from reddit/r/memes\n
Music commands:
join - bot joins your channel, remember to be in one
leave - bot leaves your channel
play - bot plays some music for ya, give him a name of the song or simply paste youtube link
queue - shows you queue of the songs
search - you can search for the song, bot will search and give you 5 youtube videos
skip - let you skip a song, remember 80% of the people in channel have to agree on the skip\n
Compilers:
run_python - lets you run python script
run_cpp - lets you run c++ code
""")

    @commands.command()
    # Shows latency of the bot
    async def ping(self, ctx):
        await ctx.send(f'My latency is {round(self.bot.latency * 1000)}ms.')

    @commands.command()
    # Prints a random quote
    # Quotes API - link: https://zenquotes.io/
    async def quote(self, ctx):
        response = requests.get('https://zenquotes.io/api/random').json()
        await ctx.send(f"'{response[0]['q']}'\n~ {response[0]['a']}")

    @commands.command()
    # Prints quote of the day
    # Quotes API - link: https://zenquotes.io/
    async def todays_quote(self, ctx):
        response = requests.get('https://zenquotes.io/api/today').json()
        await ctx.send(f"'{response[0]['q']}'\n~ {response[0]['a']}")

    @commands.command()
    # Deletes n messages
    async def purge(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send(f'Deleted {amount} messages :)')
        time.sleep(5)
        await ctx.channel.purge(limit=1)

    @commands.command()
    # Posts a random meme from reddit/r/memes
    async def meme(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/memes.json') as reddit:
                memes = await reddit.json()
                embed = discord.Embed(
                    color=discord.Color.purple()
                )
                embed.set_image(
                    url=memes["data"]["children"][random.randint(0, 25)]["data"]["url"])
                embed.set_footer(
                    text=f"Source: reddit/r/memes | Meme requested by {ctx.author}")
                await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(StandardCommands(bot))
