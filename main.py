import discord
import os
import random

client = discord.Client()
TOKEN = str(os.environ['DISCORD_TOKEN'])
ADMIN_ID = int(os.environ['ADMIN_ID'])
NAMES_FILE = 'names.txt'


# log in event
@client.event
async def on_ready():
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
        print('is admin')
        is_admin = True

    # !test
    """
    Checks if user who put !test is an admin, and returns their ID number
    """
    if message.content.startswith('!test'):
        if is_admin:
            await message.channel.send(f'I saw an admin say {message.content} from {message.author.id}')
        else:
            await message.channel.send(f'I saw a non admin say {message.content} from {message.author.id}')

    # !addname
    """
    Takes in name from user input, and updates names.txt with it
    """
    if message.content.startswith('!addname'):
        name = message.content.split()
        count = 0

        with open(NAMES_FILE, 'r') as names:
            namelist = names.read().splitlines()

        if len(name) > 10:
            if is_admin:
                print("admin added more than 10 names")
            else:
                await message.channel.send("Too many names at once! Please limit to under 10")
                return

        for x in name[1:]:
            if x not in namelist or len(x) < 20:
                with open(NAMES_FILE, 'a') as names:
                    names.write('\n' + x.title())
                    count += 1

        if count >= 1:
            await message.channel.send("Names added!")
            return
        else:
            await message.channel.send("Name already in names list!")
            return

    # !name
    """
    Generates a random two word name from names.txt
    """
    if message.content.startswith('!name'):
        with open(NAMES_FILE, 'r') as names:
            names_list = names.read().splitlines()
            line_count = len(names_list)

        firstname = random.randint(0, line_count - 1)
        lastname = random.randint(0, line_count - 1)

        await message.channel.send(f"{names_list[firstname]} {names_list[lastname]}")

    # !help
    """
    Returns how to use !addname and !name
    """
    if message.content.startswith('!help'):
        await message.channel.send(
            """Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")


if __name__ == "__main__":
    client.run(TOKEN)