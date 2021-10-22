import discord
from discord.ext import commands
from arquivo import *


class Commands(commands.Cog):
    '''Commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'mods', help = 'Mostra os Mods ativos em um servidor.')
    async def mods(self, ctx):
        embed = discord.Embed(
            title = 'Minecraft Mods',
            description = lerArquivo('mods.txt'),
            colour = 11598249
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/99/Furnace_%28S%29_JE4.png/revision/latest?cb=20210111063232')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'servers', help = 'Mostra os servidores disponíveis.')
    async def servers(self, ctx):
        embed = discord.Embed(
            title = 'Minecraft Worlds',
            description = lerArquivo('servers.txt'),
            colour = 11598249
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://cdn.icon-icons.com/icons2/3053/PNG/512/minecraft_macos_bigsur_icon_189943.png')
        #embed.set_image(url = 'https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png')
        #embed.set_footer(text = 'Teste', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'removeMod', help = 'Remove mod da lista de mod (não funciona muito bem)')
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
            print('O arquivo não existe.')
    
    @commands.command(name = 'botInfo', help = 'Mostra informações do Bot como criador e etc.')
    async def info(self, ctx):
        embed = discord.Embed(
            description = 'Bot código aberto criado pelo usuário Kauê Guimarães Programador#7894\n\nhttps://github.com/KaueGuimaraes/Minecraft-Bot',
            colour = 11598249
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://avatars.githubusercontent.com/u/76141331?v=4')

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'craft', help = 'Mostra craft de itens')
    async def craft(self, ctx, *craft):
        msg = ''
        for c in craft: #Junta os caractéres separados do elemento craft
            msg += f'{c} '
        
        crafts = lerArquivo('crafts.txt') #Lê o arquivo craft
        crafts = crafts.split('\n') #Separa por linha para facilitar identificação

        for c in crafts: #Para cada coisa nos crafts
            c = c.split('=') #Separa usando de referência o caractére '='
            if c[0] == msg.strip().lower(): #Se o nome do craft for igual ao craft que o usuário solicitou
                image = c[1] #Será salvo a imagem do craft

        embed = discord.Embed(
            title = msg,
            colour = 11598249
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b7/Crafting_Table_JE4_BE3.png/revision/latest?cb=20191229083528')
        embed.set_image(url = image)

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'crafts', help = 'Mostra todos os crafts adicionados')
    async def crafts(self, ctx):
        crafts = lerArquivo('crafts.txt') #Lê o arquivo crafts.txt

        msg = ''
        crafts = crafts.split('\n') #Separa por linha
        for c in crafts: #Pra cada coisa nos crafts
            c = c.split('=') #Separa usando de referência o caractére '='
            msg += f'{c[0]}\n' #Adiciona o nome ao msg
        
        embed = discord.Embed(
            title = 'Crafts',
            description = msg,
            colour = 11598249
        )
        
        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b7/Crafting_Table_JE4_BE3.png/revision/latest?cb=20191229083528')

        await ctx.channel.send(embed = embed)

    @commands.command(name = 'addCraft', help = 'Adiciona um craft a lista de crafts')
    async def add_craft(self, ctx, *craft):
        msg = ''
        for c in craft: #Junta os caractéres separados do elemento craft
            msg += f'{c} '
        
        try: #Vou tentar escrever o novo craft
            escrever('crafts.txt', f'\n{msg.lower().strip()}')
        except: #Se eu não conseguir
            await ctx.channel.send('Não foi possível adicionar o seu Craft')
        else: #Mas se eu conseguir
            await ctx.channel.send('Craft adicionado com sucesso.')
    
    @commands.command(name = 'addMod', help = 'Adiciona um mod a lista de mods.')
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
    
    @commands.command(name = 'remove')
    async def remove(self, ctx):
        await ctx.channel.send('Somente o meu criador pode remover um servidor.')
        



def setup(bot):
    bot.add_cog(Commands(bot))
