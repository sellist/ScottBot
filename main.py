import sys
import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio

from cogs import on_messages
from cogs import gitgetter

try:
    TOKEN = sys.argv[1]
    print(f'Token retrieved = {TOKEN}')
    intents = discord.Intents.default()
    intents.message_content = True
    intents.messages = True
    bot_instance = commands.Bot(intents=intents, command_prefix="!")
except IndexError:
    exit("No arg detected, please enter Discord token as argument when running")


async def main():

    @bot_instance.command()
    async def on_message(message):
        print(message)
        await bot_instance.process_commands(message)




    async with bot_instance:
        await bot_instance.add_cog(on_messages.NameCommands(bot_instance))
        await bot_instance.add_cog(gitgetter.GitGetter(bot_instance))
        await bot_instance.start(TOKEN)

asyncio.run(main())