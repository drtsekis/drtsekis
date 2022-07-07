import discord,asyncio,os
from discord.ext import  commands

#	----------------------------------------------------
#	               BOT DEFINATION
#	----------------------------------------------------

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

#	----------------------------------------------------
#	                  ON READY
#	----------------------------------------------------

@bot.event
async def on_ready():          
    print("Online")

bot.run("Nzc0ODUyMTY0ODI0NDY1NDI4.Gcda3t.hdak7iyoJ8BeAMlEBXJK7o8FIcQ-ArxmZ26nOQ", reconnect=True)