import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Mods(commands.Cog):
    '''Minecraft Mods Commands'''
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name = 'mods', help = 'Mostra os Mods adicionado. !mods')
    async def mods(self, ctx):
        embed = discord.Embed(
            title = 'Minecraft Mods',
            description = lerArquivo('mods.txt'),
            colour = colour
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/99/Furnace_%28S%29_JE4.png/revision/latest?cb=20210111063232')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'addMod', help = 'Adiciona um mod a lista de mods. !addMod <mod>')
    async def add_mod(self, ctx, *mod):
        msg = ''
        for c in mod: #Junta os caractéres separados do elemento mod
            msg += f'{c} '

        if arquivoExiste('mods.txt'):
            try:
                cadastrarMod('mods.txt', msg)
            except:
                print('Erro ao cadastrar Mod.')
            else:
                await ctx.channel.send('Mod adicionado com sucesso.')
        else:
            await ctx.channel.send('Não foi possível adicionar o mod.')
    
    '''@commands.command(name = 'removeMod', help = 'Remove mod da lista de mod (não funciona muito bem)')
    async def remove_mod(self, ctx, num):
        if arquivoExiste('mods.txt'): #Verifica se o arquivo mods.txt existe
            mods = lerArquivo('mods.txt') #Se existir lê o arquivo
            mods = mods.split('\n') #Divide com linha
            removido = mods[int(num) - 1]
            del(mods[int(num) - 1]) #Remove item por número informado pelo usuário
            
            save = ''
            for c in mods:
                save += f'{c}\n' #Junta todos os mods pra salvar novamente sem o mod retirado
            print(save)

            criarArquivo('mods.txt')
            escrever('mods.txt', save) #Salva sem o mod retirado

            await ctx.channel.send(f'Mod removido com sucesso ({removido.replace("- ", "")})')
        else:
            print('O arquivo não existe.')'''


def setup(bot):
    bot.add_cog(Mods(bot))
