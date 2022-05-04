from name import Names
from discord.ext import commands


class NameCommands(commands.Cog):
    """
    Organization of events that will trigger using ! commands
    """

    def __init__(self, bot):
        self.bot = bot
        self.names = Names('names.txt')
        pass

    @commands.command()
    async def test(self, ctx):
        await ctx.send(f'I saw someone say {ctx.message.content} from {ctx.message.author.id}')

    @commands.command()
    async def addname(self, ctx):
        count = 0
        name = []
        print(ctx.message.content)
        for x in ctx.message.content.split()[1:]:
            if self.names.check_if_valid(x):
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
    async def name(self, ctx):
        await ctx.message.channel.send(self.names.create_name())

    @commands.command()
    async def namehelp(self, ctx):
        await ctx.send(
            """Use !name to generate a name \nUse !addname to add a name to the list of names to be generated from""")


def setup(bot):
    bot.add_cog(NameCommands(bot))


if __name__ == '__main__':
    print("This is the on_messages module in the on_events package")
