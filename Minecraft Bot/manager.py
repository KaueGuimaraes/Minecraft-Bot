import discord
from discord.ext import commands

from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound, CommandInvokeError

from random import randint


auto_delete_words = ['fdp', 'filho da puta', 'boquete', 'puta que paril', 'pqp',
                    'punheta', 'xoxota', 'siririca', 'bicha']
auto_delete_phrases = ['Por favor. [name] não ofenda os demais usuários',
                        'Manere no palavreado [name]',
                        '[name] cuidado com o que diz...',
                        'Não seja ofensivo [name]']


class Manager(commands.Cog):
    '''Manage the Bot'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Estou pronto. Estou conectado como {self.bot.user}')
    
    @commands.Cog.listener()
    async def on_message(self, message):
        name = message.author.name
        if message.author == self.bot.user:
            return
        
        if message.content in auto_delete_words:
            await message.channel.send(auto_delete_phrases[0].replace('[name]', f'**{name}**'))

            await message.delete()
    
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, (MissingRequiredArgument, CommandInvokeError)):
            await ctx.send(f'Por favor envie todos os argumentos necessários. Digite !help para ver os parâmetros de cada comando.')
        elif isinstance(error, CommandNotFound):
            await ctx.send('Esse comando não existe. Digite !help para ver todos os comandos.')
        else:
            raise error



def setup(bot):
    bot.add_cog(Manager(bot))
