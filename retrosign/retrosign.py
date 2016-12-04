import discord, aiohttp, re
from bs4 import BeautifulSoup as b_s
from io import BytesIO
from discord.ext import commands
import os
import random
from random import choice
import lxml    

class retrosign:
    def __init__(self, bot):
      self.bot = bot
    
    async def do_it():
        await self.bot.type() 

        with aiohttp.ClientSession() as session:
          async with session.post("http://photofunia.com/effects/retro-wave", data=data) as response:
            if response.status == 200:
              soup = b_s(await response.text(), "lxml")
              download_url = soup.find("div", class_="downloads-container").ul.li.a["href"]
              async with session.get(download_url) as image_response:
                if image_response.status == 200:
                  image_data = await image_response.read()
                  with BytesIO(image_data) as temp_image:
                    await self.bot.upload(temp_image, filename="retro.jpg")
    
    @commands.group(pass_context=True)
    async def retrosign(self, content : str):
        """Make a Retrosign"""
        texts = [t.strip() for t in content.split('|')]
        if len(texts) < 3:
            lenstr = len(texts[0])
            await self.bot.say(lenstr)
            if lenstr <= 12:
                    global data
                    data = dict(
                      bcg=choice([1, 2, 3, 4, 5]),
                      txt=choice([1, 2, 3, 4]),
                      text1="",
                      text2=texts[0],
                      text3=""
                    )
                    do_it()
            else:
                await self.bot.say("\N{CROSS MARK} too many Characters for one Line")
                return
        elif len(texts) != 3:
            await self.bot.say("\N{CROSS MARK} please provide three strings seperated by `|`")
            return
        else:
            global data
            data = dict(
              bcg=choice([1, 2, 3, 4, 5]),
              txt=choice([1, 2, 3, 4]),
              text1=texts[0],
              text2=texts[1],
              text3=texts[2]
            )
            do_it()
        
        
                    
    @retrosign.command(pass_context=True)
    async def top(self, content : str):
        """Make a Retrosign with top and middle Text"""
        texts = [t.strip() for t in content.split('|')]
        if len(texts) != 2:
            await self.bot.say("\N{CROSS MARK} please provide two strings seperated by `|`")
            return
        else:
            global data
            data = dict(
              bcg=choice([1, 2, 3, 4, 5]),
              txt=choice([1, 2, 3, 4]),
              text1=texts[0],
              text2=texts[1],
              text3=""
            )
            do_it()
            
    @retrosign.command(pass_context=True)
    async def bottom(self, content : str):
        """Make a Retrosign with middle and bottom Text"""
        texts = [t.strip() for t in content.split('|')]
        if len(texts) != 2:
            await self.bot.say("\N{CROSS MARK} please provide two strings seperated by `|`")
            return
        else:
            global data
            data = dict(
              bcg=choice([1, 2, 3, 4, 5]),
              txt=choice([1, 2, 3, 4]),
              text1="",
              text2=texts[0],
              text3=[1]
            )
            do_it()
                  
def setup(bot):
  n = retrosign(bot)
  bot.add_cog(n)
