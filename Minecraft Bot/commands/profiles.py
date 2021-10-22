import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Profiles(commands.Cog):
    '''Players commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'perfil', help = 'Mostra o perfil de um usuário')
    async def profile(self, ctx):
        name = ctx.author.name
        embed = discord.Embed(
            title = name,
            description = 'Informações',
            colour = colour
        )

        await ctx.channel.send(embed = embed)

    @commands.command(name = 'players', help = 'Mostra todos players registrados')
    async def players(self, ctx):
        if arquivoExiste('players.txt'):
            msg = lerArquivo('players.txt')

            embed = discord.Embed(
                title = 'Players',
                description = msg,
                colour = colour
            )

            embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
            embed.set_thumbnail(url = 'https://i.pinimg.com/564x/fa/9b/60/fa9b6028ba671d619781059653299849.jpg')

            await ctx.channel.send(embed = embed)
        else:
            criarArquivo('players.txt')
            await ctx.channel.send('Tente novamente.')
    
    @commands.command(name = 'addPlayer', help = 'Adiciona um jogador a lista de jogadores')
    async def add_player(self, ctx, player, nick):
        try: #Tenta
            escrever('players.txt', f'{player} **{nick}**\n') #Adicionar player
        except: #Se não conseguir
            await ctx.channel.send('Não foi possível adicionar o jogador.') #Informa
        else: #Se conseguir
            await ctx.channel.send('Player adicionado com sucesso.') #Informa


def setup(bot):
    bot.add_cog(Profiles(bot))
