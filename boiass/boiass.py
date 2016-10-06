from discord.ext import commands
import os
import random
import discord

class boiass:
    """Random Male Ass"""

    def __init__(self, bot):
        self.bot = bot
        self.mass = ["http://rs909.pbsrc.com/albums/ac298/ironicirony/Shirtless/1509.jpg?w=480&h=480&fit=clip",
                     "https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcQAoU9d-ojkjklLZH1FjjZoM1DvXeD0humI0YjLmoZBBWOMwXrp",
                     "http://img2.izismile.com/img/img3/20100820/640/sexy_shirtless_men_640_09.jpg",
                     "http://img2.izismile.com/img/img3/20100820/640/sexy_shirtless_men_640_10.jpg",
                     "http://img2.izismile.com/img/img3/20100820/640/sexy_shirtless_men_640_39.jpg",
                     "http://img2.izismile.com/img/img3/20100820/640/sexy_shirtless_men_640_31.jpg",
                     "http://img2.izismile.com/img/img3/20100820/640/sexy_shirtless_men_640_32.jpg",
                     "http://img2.izismile.com/img/img3/20100820/640/sexy_shirtless_men_640_51.jpg",
                     "http://65.media.tumblr.com/42c3b10cae36bee5ad92e6ed79b275be/tumblr_o74o12Jxuc1sl7p6vo1_540.jpg",
                     "http://66.media.tumblr.com/d32c97c2a71e8765293d111de4b7dbf4/tumblr_oe48qprT151u1rnafo1_1280.jpg",
                     "http://67.media.tumblr.com/992f6a4182f91cbd17ab82cd2fb96f73/tumblr_oc6djhWLK61tuh4e9o1_1280.jpg",
                     "http://66.media.tumblr.com/98dd7f674ca13971b1c2a74faa272e07/tumblr_nk6disG9jA1rcrcdeo1_1280.jpg",
                     "http://65.media.tumblr.com/268e1d10d27615f8f7f849a911947885/tumblr_odeg6jz3TF1sbydeco1_1280.jpg",
                     "http://66.media.tumblr.com/492193c3d59863bc7b538f4fec5aa813/tumblr_od8v6oCG791rphqceo1_1280.jpg",
                     "http://67.media.tumblr.com/060f766b2d60adaa0327880f1c818e45/tumblr_n45stxBuNg1qg22hlo1_1280.jpg",
                     "http://66.media.tumblr.com/4bc5879d6eb069692dffedf8bd268fa2/tumblr_o9wt6zRwQa1rphqceo1_1280.jpg",
                     "http://66.media.tumblr.com/25a692e3003853e2a808346fc68f5d87/tumblr_odn13jnP7m1tuh4e9o1_1280.jpg",
                     "http://66.media.tumblr.com/3744ec65bccab8c2a6c6d971bb8bee43/tumblr_od4l1y8KY41tuh4e9o1_1280.jpg",
                     "http://66.media.tumblr.com/1d77dda5bbe165cfbfdf3a47a997f98d/tumblr_oe489nxSF91t85cnmo1_500.jpg",
                     "http://66.media.tumblr.com/0d01e60980a6fd003d97e216761ed590/tumblr_od9vahZoPA1t85cnmo1_540.jpg",
                     "http://67.media.tumblr.com/7cfb7ed5639bf5bb1fe6ceee388ad1df/tumblr_ocphq1BK9r1t85cnmo1_500.jpg",
                     "http://67.media.tumblr.com/3bf735b297d7529554e32d8d4b445478/tumblr_oclqubcH0M1t85cnmo1_540.jpg",
                     "http://67.media.tumblr.com/70f3f07b1d1adaa194924d81541ae8a0/tumblr_octx8t1SJ21u1rnafo1_1280.jpg",
                     "http://66.media.tumblr.com/0f55ff69bfa70b703938cc77fd78f493/tumblr_ob64fvFDRB1tg3ktao1_1280.jpg",
                     "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSTd-Uez6FcF1qXfYQJ389Ilur0puI7s_pa1B4srP1hWPeXqt7P",
                     "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSkwBjNUDJ9K2L6sEM9XTREuatvM-UG07q6N2JN2qhX84Xh0E-S",
                     "http://66.media.tumblr.com/763aeccfa171d5371deed4df1bcebdce/tumblr_mzgvbhUmEo1r0hac5o1_1280.jpg",
                     "https://shechive.files.wordpress.com/2015/05/shirtless-friday-24.jpg?quality=100&strip=info&w=640",
                     "https://shechive.files.wordpress.com/2015/05/shirtless-friday-17.jpg?quality=100&strip=info&w=640",
                     "https://67.media.tumblr.com/2316dbd4176eecf7f5af76d93fb97131/tumblr_mz7jeaHWfv1rtiyedo1_400.png",
                     "https://scontent-fra3-1.xx.fbcdn.net/v/t1.0-9/fr/cp0/e15/q65/14022090_1047208378720777_7706775770404465799_n.jpg?oh=1e80d700bb827895cbe43819750329d0&oe=586DDBC7",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233642267049590784/IMG_20161006_193059_836.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233642306501214208/IMG_20161006_193046_241.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233642379519852545/IMG_20161006_192504_671.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233642445802438660/IMG_20161006_192451_968.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233642491637661696/IMG_20161006_192408_87.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233642582033432586/IMG_20161006_193037_580.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233643498040066049/IMG_20161006_193544_140.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233643535272771585/IMG_20161006_193556_765.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233644686730985472/IMG_20161006_193932_848.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233644717563183104/IMG_20161006_194003_682.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233644759502028800/IMG_20161006_194022_424.jpg",
                     "https://cdn.discordapp.com/attachments/231758338948464640/233644808101560320/IMG_20161006_194034_288.jpg",
                     "http://www.pride.com/sites/www.pride.com/files/2016/07/01/stock20.jpg",
                     "http://www.pride.com/sites/www.pride.com/files/2016/07/01/stock29.jpg",
                     "http://www.pride.com/sites/www.pride.com/files/2016/07/01/stock19.jpg",
                     "https://67.media.tumblr.com/a57e2bc555f776b9af33127c572ee442/tumblr_nzlntgen0N1uvd18yo1_400.png",
                     "https://66.media.tumblr.com/c575475120572f1870e5fe9220ed7a52/tumblr_o8k8fbyVqm1r7eta3o1_400.jpg",
                     "https://66.media.tumblr.com/b50a443a4f99515c4c93cee9ccfd0818/tumblr_o2jqwzTVF81udbqfoo1_400.jpg",
                     "https://67.media.tumblr.com/0d2902883d1b85a628f93d449853367a/tumblr_nz89bpViDH1u03v7lo1_400.jpg",
                     "https://66.media.tumblr.com/e67b43a934266dc88c6493b3549b7f2f/tumblr_n1fx9oaNuY1ssvhcyo1_400.jpg",
                     "http://67.media.tumblr.com/60e3f0d40269c20ec64155c9dd68dd75/tumblr_odvdm0roJ71qju1v8o1_500.png",
                     "http://67.media.tumblr.com/9007dd3d9a8d66850a6577e7dd1cb897/tumblr_nh1gdcuTkv1rtkr1co1_500.jpg",
                     "http://66.media.tumblr.com/3ee24ed05490d34d53947feadaa777c2/tumblr_nrwah6KrTp1rwdv3lo1_1280.jpg",
                     "http://66.media.tumblr.com/179fdc581d992a28c37d4f106aff0ac0/tumblr_nrl0vhRfph1rwdv3lo1_1280.jpg",
                     "http://67.media.tumblr.com/690f8b092fc0f312f1726f6777899a07/tumblr_nqco7cM4cT1rwdv3lo1_1280.jpg",
                     "http://67.media.tumblr.com/5b4dc6ae936fce497d1dc922290b0970/tumblr_npuavzV0AG1rwdv3lo1_1280.jpg",
                     "http://66.media.tumblr.com/77f1c96ef320b603a8a11a01ed96f01e/tumblr_np1rx3FStQ1rwdv3lo1_1280.jpg",
                     "http://66.media.tumblr.com/9a66635fd55a45a937e51dc1cbc3c4a3/tumblr_nnprt4AMsu1rwdv3lo1_1280.jpg",
                     "http://67.media.tumblr.com/4261a4cc506120e44aac173946093041/tumblr_nloca4IRgR1rwdv3lo1_1280.jpg",
                     "http://67.media.tumblr.com/3576e364dd3702687f00002db7bf4f22/tumblr_nks3zh6jQk1rwdv3lo1_1280.jpg",
                     "http://65.media.tumblr.com/35aa9966e075ee4694bc3b328cb3ab15/tumblr_nibef29d0z1rwdv3lo1_1280.jpg"]

    @commands.command(pass_context=True)
    async def boiass(self):
        """Random Ass Answer"""
        await self.bot.say(random.choice(self.mass))

def setup(bot):
    bot.add_cog(boiass(bot))
