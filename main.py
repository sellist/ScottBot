import os
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

"""
https://discordpy.readthedocs.io/en/stable/ext/commands/commands.html
for switching to .bot
"""

for x in ['DISCORD_TOKEN', 'ADMIN_ID']:
    while True:
        try:
            _ = str(os.environ[x])
            print('Token retrieved')
            break
        except KeyError:
            print(f"Enter {x}: ")
            os.environ[x] = input()

TOKEN = str(os.environ['DISCORD_TOKEN'])
ADMIN_ID = int(os.environ['ADMIN_ID'])


# log in event
@bot.event
async def on_ready():
    print("Successfully loaded vars from env")
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

bot.run(TOKEN)
