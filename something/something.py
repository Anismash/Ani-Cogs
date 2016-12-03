import discord, aiohttp, re
from bs4 import BeautifulSoup as b_s
from io import BytesIO
from discord.ext import commands
import os
import random


class something:
    """Some Commands"""
    def __init__(self, bot):
      self.bot = bot
    
    @commands.command(pass_context=True)
    async def _retro_(self, *, content : str):
        """retro"""
        texts = [t.strip() for t in content.split('|')]
        if len(texts) != 3:
          await self.bot.say("\N{CROSS MARK} please provide three strings seperated by `|`")
          return

        await self.bot.type()

        data = dict(
          bcg=choice([1, 2, 3, 4]),
          txt=choice([1, 2, 3, 4]),
          text1=texts[0],
          text2=texts[1],
          text3=texts[2]
        )

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
  n = something(bot)
  bot.add_cog(n)
