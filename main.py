import discord
import os
from on_events.name import Names
import on_events

client = discord.Client()
names = Names('names.txt')

try:
    TOKEN = str(os.environ['DISCORD_TOKEN'])
    print('Token retrieved')
    ADMIN_ID = int(os.environ['ADMIN_ID'])
    print('Admin_id retrieved')
except KeyError:
    print("Enter discord token: ")
    os.environ['DISCORD_TOKEN'] = input()
    print("Enter admin_id: ")
    os.environ['ADMIN_ID'] = input()
    TOKEN = str(os.environ['DISCORD_TOKEN'])
    ADMIN_ID = int(os.environ['ADMIN_ID'])


# log in event
@client.event
async def on_ready():
    print("Successfully loaded vars from env")
    print(f"Logged in as {client.user}")


# messages
@client.event
async def on_message(message):
    try:
        await on_events.on_messages.messages(message, client, ADMIN_ID)
    except TypeError:
        return

if __name__ == "__main__":
    client.run(TOKEN)
