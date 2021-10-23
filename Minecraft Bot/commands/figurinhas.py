import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Figurinhas(commands.Cog):
    '''Figurinhas commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'fs', help = 'Mostra todas as figurinhas adicionadas. !fs')
    async def figurinhas(self, ctx):
        figurinhas = lerArquivo('figurinhas.txt') #Lê o arquivo figurinhas.txt

        msg = ''
        figurinhas = figurinhas.split('\n') #Separa por linha
        for c in figurinhas: #Pra cada coisa nas figurinhas
            c = c.split('===') #Separa usando de referência os caractéres '==='
            msg += f'**{c[0]}**  adicionado por {c[2]}\n' #Adiciona o nome e crédito ao msg
        
        embed = discord.Embed(
            title = 'Figurinhas',
            description = msg,
            colour = colour
        )
        
        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/7/77/Enchanting_Table_JE4_BE2.png/revision/latest?cb=20200315175031')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'f', help = 'Usa alguma figurinha. !f <figurinha>')
    async def figurinha(self, ctx, *figurinha):
        msg = ''
        for c in figurinha: #Junta os caractéres separados do elemento figurinha
            msg += f'{c} '
        
        figurinhas = lerArquivo('figurinhas.txt') #Lê o arquivo figurinhas
        figurinhas = figurinhas.split('\n') #Separa por linha para facilitar identificação

        for c in figurinhas: #Para cada coisa nos figurinhas
            c = c.split('===') #Separa usando de referência o caractére '==='
            if c[0] == msg.strip().lower(): #Se o nome da figurinha for igual a figurinha que o usuário solicitou
                name = c[0] #Será salvo o nome da imagem
                image = c[1] #Será salvo a imagem da figurinhas
        
        await ctx.channel.send(f'{image}') #Mensagem que informa quem usou o emoji **{ctx.author.name}** usou {name}\n
    
    @commands.command(name = 'addFigurinha', help = 'Adiciona uma figurinha. !addFigurinha <nome>=<imagem url>')
    async def add_figurinha(self, ctx, *figurinha):
        msg = ''
        for c in figurinha: #Junta os caractéres separados do elemento figurinha
            msg += f'{c} '
        
        msg = msg.split('=')
        autor_mention = f'<@!{ctx.author.id}>'
        
        try: #Vou tentar escrever a nova figurinha
            escrever('figurinhas.txt', f'\n{msg[0].lower().strip()}==={msg[1].strip()}==={autor_mention}')
        except: #Se eu não conseguir
            await ctx.channel.send('Não foi possível adicionar a sua figurinha')
        else: #Mas se eu conseguir
            await ctx.channel.send('Figurinha adicionada com sucesso.')


def setup(bot):
    bot.add_cog(Figurinhas(bot))
