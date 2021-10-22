import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Commands(commands.Cog):
    '''Commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'botInfo', help = 'Mostra informações do Bot como criador e etc.')
    async def info(self, ctx):
        embed = discord.Embed(
            description = 'Bot código aberto criado pelo usuário Kauê Guimarães Programador#7894\n\nhttps://github.com/KaueGuimaraes/Minecraft-Bot',
            colour = colour
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://avatars.githubusercontent.com/u/76141331?v=4')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'guia', help = 'Mostra todos os objetivos do mundo Stone Block')
    async def objetivos(self, ctx):
        if arquivoExiste('objetivos.txt'):
            msg = lerArquivo('objetivos.txt')

            embed = discord.Embed(
                tile = 'Objetivos',
                description = msg,
                colour = colour
            )

            embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
            embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/50/Book_JE2_BE2.png/revision/latest?cb=20210427032255')

            await ctx.channel.send(embed = embed)
        else:
            criarArquivo('objetivos.txt')
            await ctx.channel.send('Tente novamente.')
    
    @commands.command(name = 'report', help = 'Envie uma mensagem privada para meu criador')
    async def report(self, ctx, *report):
        msg = ''
        for c in report: #Para cada coisa no elemento report
            msg += f'{c} ' #Irei anotar no elemento msg
        msg += '\n\n' #E no final pularei 2 linhas

        autor_id = ctx.author.id
        autor_name = ctx.author.name

        if arquivoExiste('report.txt'):
            escrever('report.txt', f'Name: {autor_name}\nID: <@!{autor_id}>\n{msg}')
            await ctx.channel.send('Feedback enviado com sucesso.')
        else:
            criarArquivo('report.txt')
            await ctx.channel.send('Tente novamente.')


def setup(bot):
    bot.add_cog(Commands(bot))
