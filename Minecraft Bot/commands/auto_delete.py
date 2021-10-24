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
        auto_delete_words = auto_delete_words.split('\n')

        description = ''
        for c in auto_delete_words: #Para cada palavra banida
            if c == '': #Se a palavra for uma linha vazia
                continue #Irei ignorar
            else: #Senão
                description += f'• {c}\n' #Adicionarei o valor formatado a descrição

        embed = discord.Embed(
            title = 'Palavra banidas',
            description = description,
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

        escrever('auto_delete_words.txt', f'{msg}\n') #Logo depois adicionarei a palavra no arquivo auto_delete_words.txt
        await ctx.channel.send(f'"{msg}" foi banido com sucesso.') #E informarei ao usuário
    
    @commands.command(name = 'addPhrase', help = 'Adiciona uma frase para ser mostrada ao deletar uma mensagem contendo uma palvra banida. É importante que contenha "[nome]" na frase para conseguir identificar quando falar o nome do autor da mensagem ofensiva. !addPhrase <frase>')
    async def add_phrase(self, ctx, *phrase):
        msg = ''
        for c in phrase: #Pra cada coisa nas frases
            msg += f' {c}' #Irei adiciona-la na mensagem
        msg = msg.strip() #Depois irei remover os espaços no início e no final da string msg

        escrever('auto_delete_phrases.txt', f'{msg}\n') #Irei escrever a mensagem no arquivo auto_delete_phrases.txt
        await ctx.channel.send(f'"{msg}" foi adicionado com sucesso.') #Por último informarei o usuário que eu adicionei a mensagem
    
    @commands.command(name = 'unbanWord', help = 'Desbane uma palvra. !unbanWord <palavra>')
    async def unban_word(self, ctx, *word):
        msg = ''
        for c in word: #Para cada item no objeto word
            msg += f' {c}' #Adicionarei na variável msg
        msg = msg.lower().strip() #Transformarei a variável msg em minusculo e removerei os espaços do início e final

        try: #Tentarei
            auto_delete_words = lerArquivo('auto_delete_words.txt') #Ler o arquivo auto_delete_words.txt
            auto_delete_words = auto_delete_words.split('\n') #E separarei o mesmo por linha

            exist = False
            new_auto_delete_words = ''
            for c in auto_delete_words: #Para cada palavra banida
                if c == '': #Se for uma linha vazia
                    continue #Irei ignorar
                elif c == msg.lower().strip(): #Senão se for igual a palavra informada pelo usuário
                    print('igual')
                    exist = True #Irei anotar que a palavra solicitava realmente existe
                    continue #Continuarei
                else: #senão
                    new_auto_delete_words += f'{c}\n' #Adicionarei na variável new_auto_delete_words
            
            criarArquivo('auto_delete_words.txt') #Limparei o arquivo auto_delete_words.txt
            escrever('auto_delete_words.txt', new_auto_delete_words) #E adicionarei as novas informações formatadas

            if exist: #Se a palavra solicitada a remoção existir na lista
                await ctx.channel.send(f'**{msg}** foi desbanido com sucesso.') #Informarei o usuário que a tarefa solicitada foi concluida com sucesso
            else: #Se não
                await ctx.channel.send(f'{msg} já está desbanido. Use **!banWord {msg}** caso queira banir a palavra. !help para mais informações') #Informarei que a tarefa solicitada pelo usuário não tem a mínima necessidade de ser concluida
        except: #Se eu falhar
            await ctx.chanenl.send(f'Não foi possível desbanir **"{msg}"**') #Informarei o usuário que não foi possível concluir a tarefa solicitada


def setup(bot):
    bot.add_cog(AutoDelete(bot))
