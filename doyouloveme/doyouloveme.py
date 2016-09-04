from discord.ext import commands
import os
import random
import discord

class doyouloveme:
    """Do the Bot loves You?"""

    def __init__(self, bot):
        self.bot = bot
        self.love = ["Yes, I do! :heart: http://i.imgur.com/cRfX87T.gif",
                     "Die! http://i.imgur.com/QzfBdVe.gif",
                     "I-It's not that I like you or anything... http://i.imgur.com/b0RWwM2.gif",
                     "If you bow down and kiss my feet, {} http://i.imgur.com/gD2w8oV.gif",
                     "Nope. http://i.imgur.com/yqKQTef.gif",
                     "That's funny, {} http://i.imgur.com/ZnmFUhR.gif",
                     "You are scaring me http://i.imgur.com/fEurqrT.gif",
                     "I don't care what you feel http://i.imgur.com/VhZZUH0.gif",
                     "We will have much fun http://i.imgur.com/QY5zTs0.gif",
                     "What is love? http://i.imgur.com/GCLzjTO.gif",
                     "I will crush your nuts http://i.imgur.com/zCRMpX7.gif",
                     "Yes... I love you ~ http://i.imgur.com/KKjHhUV.gif",
                     "B-Baka! Stop asking this! http://i.imgur.com/zde7L1w.gif"]
        self.loveothers = ["Yes, {} loves you :heart:",
                           "No, {} doesn't loves you :broken_heart:"]
        self.loveanismash = ["Of course I love you because you are my BF, {} :heart:"]

    @commands.command(pass_context=True)
    async def doyouloveme(self, ctx, *, user : discord.Member=None):
        """Random Love Answer"""
        if user == None:
            user = ctx.message.author
            await self.bot.say(random.choice(self.love).format(user.mention))
        elif ctx.message.author.id == "114338628695621634":
            await self.bot.say("Of course I love you because you are my BF, {} :heart:".format(user.mention))
        else: 
            await self.bot.say(random.choice(self.loveothers).format(user.mention))
        

def setup(bot):
    bot.add_cog(doyouloveme(bot))
