from discord.ext import commands
import os
import random
import discord

class doyouloveme:
    """Do the Bot loves You?"""

    def __init__(self, bot):
        self.bot = bot
        self.love = ["Yes, I do!","Die!","I-It's not that I like you or anything...","If you bow down and kiss my feet, {}"]

    @commands.command(pass_context=True)
    async def doyouloveme(self, ctx):
        """Random Love Answer"""
        user = ctx.message.author
        #Your code will go here
        await self.bot.say(random.choice(self.love).format(user.mention))

def setup(bot):
    bot.add_cog(doyouloveme(bot))