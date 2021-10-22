import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Servers(commands.Cog):
    '''Minecraft Servers commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'servers', help = 'Mostra os servidores disponíveis.')
    async def servers(self, ctx):
        embed = discord.Embed(
            title = 'Minecraft Worlds',
            description = lerArquivo('servers.txt'),
            colour = colour
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://cdn.icon-icons.com/icons2/3053/PNG/512/minecraft_macos_bigsur_icon_189943.png')
        #embed.set_image(url = 'https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png')
        #embed.set_footer(text = 'Teste', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'add', help = 'Adiciona um server a lista de servidores.')
    async def add(self, ctx, nome, link, ip, porta, version):
        if arquivoExiste('servers.txt'):
            try:
                cadastrar('servers.txt', nome, link, ip, porta, version)
            except:
                await ctx.channel.send('Erro ao cadastrar servidor.')
            else:
                await ctx.channel.send('Servidor adicionado com sucesso.')
        else:
            await ctx.channel.send('Erro ao cadastrar servidor.')


def setup(bot):
    bot.add_cog(Servers(bot))
