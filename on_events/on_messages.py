import discord
from on_events.name import Names


def messages(message, client, ADMIN_ID: int, is_admin=False):
    """
    Organization of events that will trigger using ! commands
    """
    names = Names('names.txt')

    # self check
    if message.author == client.user:
        return

    # admin check
    if message.author.id == ADMIN_ID:
        is_admin = True

    # !test
    if message.content.startswith('!test'):
        if is_admin:
            return message.channel.send(f'I saw an admin say {message.content} from {message.author.id}')
        else:
            return message.channel.send(f'I saw a non admin say {message.content} from {message.author.id}')

    # !addname
    # Takes in name from user input, and updates names.txt with it, reacts if successful or not
    if message.content.startswith('!addname'):
        count = 0
        for x in message.content.split()[1:]:
            if names.check_if_valid(x):
                count += 1

        if count >= 1:
            names.add_name(message.content)
            return message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            return message.add_reaction('\N{THUMBS DOWN SIGN}')

    # !name
    if message.content.startswith('!name'):
        return message.channel.send(names.create_name())

    # !help
    if message.content.startswith('!help'):
        return message.channel.send(
            """Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")
