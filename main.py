import os
import sys
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

"""
https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
for switching to .bot
"""

try:
    TOKEN = sys.argv[1]
    print(f'Token retrieved')
except IndexError:
    exit(print("No arg detected, please enter Discord token as argument when running"))


# log in event
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


# messages
@bot.event
async def on_message(message):
    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    latency = bot.latency
    await ctx.send(latency)


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

try:
    print("Logging in...")
    bot.run(TOKEN)
except Exception as e:
    print('Error raised on login')
    print(e)
    exit(print("Exiting"))
