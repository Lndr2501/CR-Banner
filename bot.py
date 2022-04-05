from asyncio import tasks
import nextcord
from nextcord.ext import commands, tasks
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

intents = nextcord.Intents.default()
intents.members = True
intents.presences = True
bot = commands.Bot(command_prefix="!", help_command=None, intents=intents)

@bot.event
async def on_ready():
    print(f"Eingeloggt {bot.user}, mit Bewerbungen")
    print("Ver:" + nextcord.__version__)
    bannner.start()
    
@tasks.loop(minutes=5)
async def bannner():

    members = [member for member in bot.get_guild(898766854552690789).members if member.status != nextcord.Status.offline]
    
    img = Image.open("Banner.png")
    
    draw = ImageDraw.Draw(img)
    draw.text((52, 180), f"{len(members)}", fill=(255, 255, 255), font=ImageFont.truetype("AmsiPro-Black.ttf", 32))
    draw.text((213, 180), f"{bot.get_guild(898766854552690789).member_count}", fill=(255, 255, 255), font=ImageFont.truetype("AmsiPro-Black.ttf", 32))
    
    buffer = BytesIO()
    img.save(buffer, "png")
    buffer.seek(0)
    
    await bot.get_guild(898766854552690789).edit(banner=buffer.read())
     
bot.run("OTU5Nzc4NTU4MzgzODk4NjM0.Ykg1cA._R2M3JYP4MDEVOqM8MRCN_GU4LE")