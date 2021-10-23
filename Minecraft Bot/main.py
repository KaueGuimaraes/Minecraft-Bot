import os

from decouple import config
from discord.ext import commands


bot = commands.Bot('!')

bot.load_extension('commands.commands')
bot.load_extension('commands.mods')
bot.load_extension('commands.servers')
bot.load_extension('commands.crafts')
bot.load_extension('commands.figurinhas')
bot.load_extension('commands.profiles')
bot.load_extension('commands.auto_delete')

bot.load_extension('manager')

TOKEN = config('TOKEN')
bot.run(TOKEN)