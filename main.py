from datetime import date
import discord
from discord.ext import commands

def time_before_christmas(christmas_day, actual_date):
    return christmas_day - actual_date

"""
---------------
     BOT
---------------
"""

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '!', intents = intents)

@bot.command()
async def days(ctx):

    actual_date = date.today()
    
    christmas_day = date(actual_date.year, 12, 25)
    
    days_before_christmas = time_before_christmas(christmas_day, actual_date)
    
    await ctx.send("Faltan " + str(days_before_christmas.days) + " días para navidad!")
    
@bot.event
async def on_ready():
    print("READY")
    
bot.run("token")