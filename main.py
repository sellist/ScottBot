import discord
import os
from name import Names

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
    # self check
    if message.author == client.user:
        return

    # admin check
    is_admin = False
    if message.author.id == ADMIN_ID:
        is_admin = True

    # !test
    # Checks if user who put !test is an admin, and returns their ID number
    if message.content.startswith('!test'):
        if is_admin:
            await message.channel.send(f'I saw an admin say {message.content} from {message.author.id}')
        else:
            await message.channel.send(f'I saw a non admin say {message.content} from {message.author.id}')

    # !addname
    # Takes in name from user input, and updates names.txt with it, reacts if successful or not
    if message.content.startswith('!addname'):
        count = 0
        for x in message.content.split()[1:]:
            if names.check_if_valid(x):
                count += 1

        if count >= 1:
            names.add_name(message.content)
            await message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            await message.add_reaction('\N{THUMBS DOWN SIGN}')
            return

    # !name
    # Generates a random two word name from names.txt
    if message.content.startswith('!name'):
        await message.channel.send(names.create_name())

    # !help
    # Returns how to use !addname and !name
    if message.content.startswith('!help'):
        await message.channel.send(
            """Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")

if __name__ == "__main__":
    client.run(TOKEN)
