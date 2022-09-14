from utils.name import Names
from discord.ext import commands


class NameCommands(commands.Cog):
    """
    Organization of events that will trigger using ! commands
    """

    def __init__(self, bot):
        self.bot = bot
        self.names = Names('names.txt', 'teams.txt')

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f'I saw someone say {ctx.message.content} from {ctx.message.author.id}')

    @commands.command()
    async def addname(self, ctx):

        """
        TO DO:
        Merge addname and addteam into one command after json switch
        ex:
        if !addname_var (!add name, second word is category now) is in supported_types:
            category = json[!addname_var]
        else:
            return not supported type

        remove check valid name outside of being a word without numbers


        :param ctx: message
        :return: none
        """
        count = 0
        name = []
        print(ctx.message.content)
        for x in ctx.message.content.split()[1:]:
            if self.names.check_valid_name(x):
                print(f"{x} is valid")
                name.append(x)
                count += 1
            else:
                print(f"{x} isn't valid")

            with open('names.txt', 'a') as names:
                for x in name:
                    names.write('\n' + x.title())

        if count >= 1:
            await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')

    @commands.command()
    async def addteam(self, ctx):
        count = 0
        team = []
        print(ctx.message.content)
        for x in ctx.message.content.split()[1:]:
            if self.names.check_valid_team(x):
                print(f"{x} is valid")
                team.append(x)
                count += 1
            else:
                print(f"{x} isn't valid")

            with open('teams.txt', 'a') as teams:
                for x in team:
                    teams.write('\n' + x.title())

        if count >= 1:
            await ctx.message.add_reaction('\N{THUMBS UP SIGN}')
        else:
            await ctx.message.add_reaction('\N{THUMBS DOWN SIGN}')

    @commands.command()
    async def name(self, ctx):
        await ctx.message.channel.send(self.names.create_name())

    @commands.command()
    async def namehelp(self, ctx):
        await ctx.send(
            """Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")

    @commands.command()
    async def namecount(self, ctx):
        name_count = self.names.name_count()
        await ctx.message.channel.send(f" There are {name_count} names, with {name_count * name_count} possible names!")

    @commands.command()
    async def team(self, ctx):
        await ctx.message.channel.send(self.names.create_team())

    @commands.command()
    async def purgenamedupes(self, ctx):
        difference = self.names.remove_dupes()
        await ctx.message.channel.send(f"{difference} duplicated removed.")


def setup(bot):
    bot.add_cog(NameCommands(bot))


if __name__ == '__main__':
    print("This is the on_messages module in the on_events package")
