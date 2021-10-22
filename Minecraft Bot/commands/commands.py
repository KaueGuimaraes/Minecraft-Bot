import discord
from discord.ext import commands
from arquivo import *


mod_list = ['Blood Magic', 'Draconic Evolution', 'Ore Seeds', 'Chickens', 'Vatonage Magic', 'Survival Guns',
        'Power Generators+', "Tinkers' ReAwakening", 'More TNT', 'CustomEnchantments', 'Item Exchange Balanced',
        'Ore Trees', 'Advanced Machinery', 'Baubles', 'Loots Bags', 'Android Infusion', 'Weapon Cases',
        'Lucky Blocks']


class Commands(commands.Cog):
    '''Commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'mods', help = 'Mostra os Mods ativos em um servidor.')
    async def mods(self, ctx):
        msg = lerArquivo('mods.txt')
        
        await ctx.channel.send(msg)
    
    @commands.command(name = 'servers', help = 'Mostra os servidores disponíveis.')
    async def servers(self, ctx):
        msg = lerArquivo('servers.txt')
        
        await ctx.channel.send(msg)
    
    @commands.command(name = 'add', help = 'Adiciona um server a lista de servidores.')
    async def add(self, ctx, nome, link, ip, porta, version):
        try:
            arquivoExiste('servers.txt')
        except:
            print('Erro ao ler o arquivo.')
        else:
            try:
                cadastrar('servers.txt', nome, link, ip, porta, version)
            except:
                print('Erro ao cadastrar servidor.')
            else:
                await ctx.channel.send('Servidor adicionado com sucesso.')
    
    @commands.command(name = 'addMod', help = 'Adiciona um mod a lista de mods.')
    async def add_mod(self, ctx, mod):
        try:
            arquivoExiste('mods.txt')
        except:
            print('Erro ao ler o arquivo.')
        else:
            try:
                cadastrarMod('mods.txt', mod)
            except:
                print('Erro ao cadastrar Mod.')
            else:
                await ctx.channel.send('Mod adicionado com sucesso.')
    
    @commands.command(name = 'remove')
    async def remove(self, ctx):
        await ctx.channel.send('Somente o meu criador pode remover um servidor.')
    
    @commands.command(name = 'removeMod')
    async def removeMod(self, ctx):
        await ctx.channel.send('Somente o meu criador pode remover um mod.')



def setup(bot):
    bot.add_cog(Commands(bot))
