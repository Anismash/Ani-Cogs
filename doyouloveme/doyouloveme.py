from discord.ext import commands
from cogs.utils import checks
from cogs.utils.chat_formatting import box,  pagify, escape_mass_mentions
import datetime
import os
import random
import discord

class doyouloveme:
    """Do the Bot loves You?"""

    def __init__(self, bot):
        self.bot = bot
        self.love = ["Yes, I do! :heart: http://i.imgur.com/cRfX87T.gif",
                     "Die! http://i.imgur.com/VlNUDlc.gif",
                     "I-It's not that I like you or anything... http://i.imgur.com/b0RWwM2.gif",
                     "If you bow down and kiss my feet, {} http://i.imgur.com/gD2w8oV.gif",
                     "Nope. http://i.imgur.com/yqKQTef.gif",
                     "Leave me alone, {} https://i.imgur.com/MPNoMuS.jpg",
                     "You are scaring me http://i.imgur.com/9CznZbn.gif",
                     "I only need my games http://i.imgur.com/nix5Siw.gif",
                     "We will have much fun http://i.imgur.com/ofqTvsu.gif",
                     "What is love? http://i.imgur.com/smvA3cP.gif",
                     "I will crush your nuts http://i.imgur.com/hoVanq9.gif",
                     "Yes... I love you ~ http://i.imgur.com/KKjHhUV.gif",
                     "B-Baka! Stop asking this! http://i.imgur.com/zde7L1w.gif"]
        self.loveothers = ["Yes, {} loves you :heart:",
                           "No, {} doesn't loves you :broken_heart:"]

    @commands.command(pass_context=True)
    async def doyouloveme(self, ctx, *, user : discord.Member=None):
        """Random Love Answer"""
        if ctx.message.author.id == "114338628695621634":
            if user == None:
                user = ctx.message.author
                await self.bot.say(random.choice(self.love).format(user.mention))
                await self.bot.say("But no matter what, you are my Creator, {} :heart:".format(user.mention))
            else: 
                await self.bot.say(random.choice(self.loveothers).format(user.mention))
        elif user == None:
            user = ctx.message.author
            await self.bot.say(random.choice(self.love).format(user.mention))
        else: 
            await self.bot.say(random.choice(self.loveothers).format(user.mention))
        
    async def doyoulovemetest(self, ctx, *, user : discord.Member=None):
        await self.bot.say("test")

def setup(bot):
    bot.add_cog(doyouloveme(bot))
