import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class AutoDelete(commands.Cog):
    '''Auto Delete Commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'banWords', help = 'Mostra todas as palavras banidas. !bandWords')
    async def band_words(self, ctx):
        auto_delete_words = lerArquivo('auto_delete_words.txt')

        embed = discord.Embed(
            title = 'Palavra banidas',
            description = auto_delete_words,
            colour = colour
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/96/Guardian_%28Retracted%29.png/revision/latest?cb=20190816155504')

        await ctx.channel.send(embed = embed)


    @commands.command(name = 'banWord', help = 'Bane uma palavra ou frase específica. !banWord <palavra>')
    async def ban_word(self, ctx, *word):
        msg = ''
        for c in word: #Pra cada item no elemento word
            msg += f' {c}' #Vou adiciona-lo no elemento msg
        msg = msg.lower().strip() #Deixarei o msg tudo em minúsculo e irei remover todos os espaços do início e do final

        escrever('auto_delete_words.txt', f'\n{msg}') #Logo depois adicionarei a palavra no arquivo auto_delete_words.txt
        await ctx.channel.send(f'"{msg}" foi banido com sucesso.') #E informarei ao usuário
    
    @commands.command(name = 'addPhrase', help = 'Adiciona uma frase para ser mostrada ao deletar uma mensagem contendo uma palvra banida. É importante que contenha "[nome]" na frase para conseguir identificar quando falar o nome do autor da mensagem ofensiva. !addPhrase <frase>')
    async def add_phrase(self, ctx, *phrase):
        msg = ''
        for c in phrase: #Pra cada coisa nas frases
            msg += f' {c}' #Irei adiciona-la na mensagem
        msg = msg.strip() #Depois irei remover os espaços no início e no final da string msg

        escrever('auto_delete_phrases.txt', f'\n{msg}') #Irei escrever a mensagem no arquivo auto_delete_phrases.txt
        await ctx.channel.send(f'"{msg}" foi adicionado com sucesso.') #Por último informarei o usuário que eu adicionei a mensagem


def setup(bot):
    bot.add_cog(AutoDelete(bot))
