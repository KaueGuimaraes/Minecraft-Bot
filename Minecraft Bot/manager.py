import discord
from discord.ext import commands

from discord.ext.commands.errors import MissingRequiredArgument, CommandNotFound, CommandInvokeError

from random import randint

from arquivo import *


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
        if message.author == self.bot.user: #Se o autor for um bot
            return #Vou ignora-lo
        
        auto_delete_phrases = lerArquivo('auto_delete_phrases.txt').split('\n') #Leio as frases para usar quando deletar uma mensagem
        auto_delete_words = lerArquivo('auto_delete_words.txt').split('\n') #Leio as palavras banidas

        for word in auto_delete_words: #Para cada palavra nas palavras banidas
            if word.strip() == '': #Se a palavra for uma linha vazia
                continue #Irei ignorar
            elif word.strip().lower() in message.content.lower(): #Senão se a palavra banida estiver na mensagem do usuário
                num = randint(0, len(auto_delete_phrases)) #irei pegar uma frase aleatória da lista auto_delete_phrases

                await message.channel.send(auto_delete_phrases[num].replace('[name]', f'**{name}**')) #Irei avisa-lo para não usar esse tipo de palavreado

                await message.delete() #E deletarei a mensagem ofensiva do mesmo
    
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
