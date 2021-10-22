import os

from decouple import config
from discord.ext import commands


bot = commands.Bot('!')

bot.load_extension('commands.commands')
bot.load_extension('manager')

TOKEN = config('TOKEN')
bot.run(TOKEN)