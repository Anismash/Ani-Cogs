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
    
    @commands.command(name="retrosign")
    async def retrosign(self, *, content : str):
        """Make a retrosign with 3 words seperated by ';' or one word in the middle"""
        texts = [t.strip() for t in content.split(';')]
        if len(texts) < 3 and not len(texts) > 1:
            lenstr = len(texts[0])
            if lenstr <= 12:
                    data = dict(
                      bcg=choice([1, 2, 3, 4, 5]),
                      txt=choice([1, 2, 3, 4]),
                      text1="",
                      text2=texts[0],
                      text3=""
                    )
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
            else:
                await self.bot.say("\N{CROSS MARK} too many characters for one line")
                return
        elif len(texts) != 3:
            await self.bot.say("\N{CROSS MARK} please provide three words seperated by ';' or one word")
            return
        elif len(texts[0]) <= 12
            await self.bot.say("\N{CROSS MARK} Your First Word(s) is/are too long")
            return
        elif len(texts[1]) <= 12:
            await self.bot.say("\N{CROSS MARK} Your Second Word(s) is/are too long")
            return
        elif len(texts[2]) <= 12:
            await self.bot.say("\N{CROSS MARK} Your Third Word(s) is/are too long")
            return
        else:
            data = dict(
              bcg=choice([1, 2, 3, 4, 5]),
              txt=choice([1, 2, 3, 4]),
              text1=texts[0],
              text2=texts[1],
              text3=texts[2]
            )
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
        
        
                    
    @commands.command(name="retrotopsign")
    async def _top_(self, *, content : str):
        """Make a retrosign with top and middle text"""
        texts = [t.strip() for t in content.split(';')]
        if len(texts) != 2:
            await self.bot.say("\N{CROSS MARK} please provide two words seperated by ';'")
            return
        else:
            data = dict(
              bcg=choice([1, 2, 3, 4, 5]),
              txt=choice([1, 2, 3, 4]),
              text1=texts[0],
              text2=texts[1],
              text3=""
            )
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
            
    @commands.command(name="retrobottomsign")
    async def _bottom_(self, *, content : str):
        """Make a retrosign with middle and bottom text"""
        texts = [t.strip() for t in content.split(';')]
        if len(texts) != 2:
            await self.bot.say("\N{CROSS MARK} please provide two words seperated by ';'")
            return
        else:
            data = dict(
              bcg=choice([1, 2, 3, 4, 5]),
              txt=choice([1, 2, 3, 4]),
              text1="",
              text2=texts[0],
              text3=texts[1]
            )
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
                  
def setup(bot):
  n = retrosign(bot)
  bot.add_cog(n)
