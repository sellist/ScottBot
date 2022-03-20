import discord
import os
import random
import linecache

client = discord.Client()
TOKEN = os.environ['OAtoken']
admin_id = 139160626902728704

def admin_check(message):
  if message.author.id == admin_id:
    return True
  else:
    return False

#log in event
@client.event
async def on_ready():
  print(f"Logged in as {client.user}")

#messages
@client.event
async def on_message(message):
  #self check
  if message.author == client.user:
    return

  #!test
  if message.content.startswith('!test'):
    if admin_check(message):
      await message.channel.send(f'i saw an admin say {message.content} from {message.author.id}')
    else:
       await message.channel.send(f'i saw a non admin say {message.content} from {message.author.id}')

  #!addname
  if message.content.startswith('!addname'):
    name = message.content.split()
    with open('names.txt','r') as names:
      namelist = names.read()

    if len(name) > 2 or len(name[1]) > 15:
      await message.channel.send("name 2 long")
      
    if name[1] in namelist:
      await message.channel.send("name already in names list")
    else:
      with open('names.txt','a+') as names:
        names.write('\n' + name[1])
        await message.channel.send("name added")
      

  #!name
  if message.content.startswith('!name'):
    with open('names.txt','r') as names:
        nameslist = names.read().splitlines() 
        linecount = len(nameslist)
      
    firstname = random.randint(0,linecount-1)
    lastname = random.randint(0,linecount-1)
    
    await message.channel.send(f"{nameslist[firstname]} {nameslist[lastname]}")

  #!howname
  if message.content.startswith('!help'):
    await message.channel.send("""Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")
      
client.run(TOKEN)