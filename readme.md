This is an incredibly simple bot (at time of this readme's commit) that takes a list of words/names, simply formats
them and then stores them in names.txt.

On start-up, program will prompt for the bot's token found in Discord's dev portal, and the user id of the owner.
Currently, all the user id requirement does is bypass the limit of adding names (limit of 10 for normal users), but more
features are planned.

5/3/2022 Update: Pushed rewrite from using discord.Client to discord.Bot.
