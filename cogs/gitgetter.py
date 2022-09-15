import datetime
import feedparser
from discord.ext import commands
import asyncio


class GitGetter(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.current_local_timestamp = 0
        self.current_remote_timestamp = 0
        self.rss_feed = ''
        self.gitlab_rss = ''
        print("test")

    @commands.command()
    async def setupgit(self, ctx):
        message = ctx.message.content.split(" ")
        print(message)
        try:
            self.gitlab_rss = message[1]
            self.rss_feed = feedparser.parse(self.gitlab_rss)
            last_updated = self.rss_feed.entries[0]['updated']
            year, month, day = last_updated.split("T")[0].split("-")
            hour, minute, second = last_updated.split("T")[1].split("-")[0].split(":")
            self.current_remote_timestamp = datetime.datetime(int(year), int(month), int(day),
                                                              int(hour), int(minute), int(second))
            self.current_local_timestamp = self.current_remote_timestamp
        except Exception as e:
            print(e)
        await self.loopcheck(ctx)
        print("setup successful")

    def check_repo(self):
        """
        get the newest timestamp from latest rss feed and update current_remote_timestamp
        :return: None
        """
        self.rss_feed = feedparser.parse(self.gitlab_rss)
        last_updated = self.rss_feed.entries[0]['updated']
        year, month, day = last_updated.split("T")[0].split("-")
        hour, minute, second = last_updated.split("T")[1].split("-")[0].split(":")
        self.current_remote_timestamp = datetime.datetime(int(year), int(month), int(day),
                                                          int(hour), int(minute), int(second))
        print("Checking repo....")

    async def difference_check(self, ctx):
        self.check_repo()
        testing_channel = self.bot.get_channel(961494473676840970)
        if self.current_local_timestamp != self.current_remote_timestamp:
            print("A change!")
            await testing_channel.send(f"@everyone Something happened to Gitlab!")
            self.current_local_timestamp = self.current_remote_timestamp
        else:
            print("no change.....")

    @commands.command()
    async def currenttimestamp(self, ctx):
        await ctx.message.channel.send(self.current_local_timestamp)

    async def loopcheck(self, ctx):
        while True:
            await self.difference_check(ctx)
            await asyncio.sleep(60)


def setup(bot):
    bot.add_cog(GitGetter(bot))


if __name__ == "__main__":
    print("Please run me through discord!")
