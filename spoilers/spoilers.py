import discord
import os
from discord.ext import commands
from cogs.utils.dataIO import dataIO

class Spoilers:
    """A cog for spoilers"""

    def __init__(self, bot):
        self.bot = bot
        self.spoilers = dataIO.load_json("data/spoilers/spoilers.json")

    @commands.group(name="spoiler", pass_context=True, invoke_without_command=True)
    async def spoiler(self, ctx, tag : str, *, content : str):
        """Adds a spoiler"""
        message = ctx.message
        author = message.author
        try:
            await self.bot.delete_message(message)
        except discord.errors.Forbidden:
            await self.bot.say("I lack the permissions to delete that message!")
            return
        spoiler, spoiler_id = self.add_spoiler(ctx, tag, content)
        await self.bot.say("Spoiler about {} by {}. Do ``{}spoiler show {}`` "
                           "to see it!"
                           "".format(tag, author.display_name, ctx.prefix, spoiler_id))

    @spoiler.command(pass_context=True, name="show")
    async def _show_spoiler(self, ctx, spoiler_id : int):
        """Shows the specified spoiler"""
        server = ctx.message.server
        try:
            spoiler = self.spoilers[server.id][spoiler_id]
        except IndexError:
            await self.bot.say("Invalid ID.")
            return
        msg = "Spoiler about {} from <@{}>\n\n{}".format(spoiler["tag"], spoiler["author"], spoiler["content"])
        await self.bot.whisper(msg)

    def add_spoiler(self, ctx, tag, content):
        message = ctx.message
        author = message.author
        server = author.server
        spoiler = {
            "author"  : author.id,
            "tag"     : tag,
            "content" : content
        }
        if server.id not in self.spoilers:
            self.spoilers[server.id] = [spoiler]
        else:
            self.spoilers[server.id].append(spoiler)
        dataIO.save_json("data/spoilers/spoilers.json", self.spoilers)
        return spoiler, len(self.spoilers[server.id])-1

    @spoiler.command(pass_context=True, name="list")
    async def list_last_ten_spoilers(self, ctx):
        """Lists last 10 spoilers"""
        try:
            last_ten = self.spoilers[ctx.message.server.id][:-11:-1]
        except KeyError:
            await self.bot.say("No spoiler have been added in this server.")
            return
        i = len(self.spoilers[ctx.message.server.id])
        msg = "Last 10 spoilers:\n\n"
        for spoiler in last_ten:
            msg += "{} - {}\n".format(i-1, spoiler["tag"])
            i -= 1
        if msg != "Last 10 spoilers:\n":
            await self.bot.say(msg)
        else:
            await self.bot.say("No spoiler have been added in this server.")

def check_folders():
    if not os.path.exists("data/spoilers"):
        print("Creating spoilers folder...")
        os.makedirs("data/spoilers")

def check_files():
    if not os.path.isfile("data/spoilers/spoilers.json"):
        print("Creating empty spoilers.json...")
        dataIO.save_json("data/spoilers/spoilers.json", {})

def setup(bot):
    check_folders()
    check_files()
    bot.add_cog(Spoilers(bot))
