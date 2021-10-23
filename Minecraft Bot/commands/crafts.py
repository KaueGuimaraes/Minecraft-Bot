import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Crafts(commands.Cog):
    '''Minecraft Crafts commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'crafts', help = 'Mostra crafts adicionados. !crafts')
    async def crafts(self, ctx):
        crafts = lerArquivo('crafts.txt') #Lê o arquivo crafts.txt

        msg = ''
        crafts = crafts.split('\n') #Separa por linha
        for c in crafts: #Pra cada coisa nos crafts
            c = c.split('===') #Separa usando de referência os caractéres '==='
            msg += f'**{c[0]}** adicionado por {c[2]}\n' #Adiciona o nome e crédito ao msg
        
        embed = discord.Embed(
            title = 'Crafts',
            description = msg,
            colour = colour
        )
        
        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b7/Crafting_Table_JE4_BE3.png/revision/latest?cb=20191229083528')

        await ctx.channel.send(embed = embed)

    @commands.command(name = 'craft', help = 'Mostra como crafitar um item. !craft <item>')
    async def craft(self, ctx, *craft):
        msg = ''
        for c in craft: #Junta os caractéres separados do elemento craft
            msg += f'{c} '
        
        crafts = lerArquivo('crafts.txt') #Lê o arquivo craft
        crafts = crafts.split('\n') #Separa por linha para facilitar identificação

        for c in crafts: #Para cada coisa nos crafts
            c = c.split('===') #Separa usando de referência os caractéres '==='
            if c[0] == msg.strip().lower(): #Se o nome do craft for igual ao craft que o usuário solicitou
                image = c[1] #Será salvo a imagem do craft
                description = c[3]

        embed = discord.Embed(
            title = msg,
            description = description,
            colour = colour
        )

        embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
        embed.set_thumbnail(url = 'https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b7/Crafting_Table_JE4_BE3.png/revision/latest?cb=20191229083528')
        embed.set_image(url = image)

        await ctx.channel.send(embed = embed)
    
    @commands.command(name = 'addCraft', help = 'Adiciona um craft a lista de crafts. !addCraft <nome>$<imagem url> ou !addCraft <nome>$<imagem url>$<descrição>')
    async def add_craft(self, ctx, *craft):
        msg = ''
        for c in craft: #Junta os caractéres separados do elemento craft
            msg += f'{c} '
        
        autor_id = ctx.author.id
        msg = msg.split('$')

        try: #Vou tentar escrever o novo craft
            try:
                escrever('crafts.txt', f'\n{msg[0].lower().strip()}==={msg[1].strip()}===<@!{autor_id}>==={msg[2]}')
            except:
                escrever('crafts.txt', f'\n{msg[0].lower().strip()}==={msg[1].strip()}===<@!{autor_id}>===')
        except: #Se eu não conseguir
            await ctx.channel.send('Não foi possível adicionar o seu Craft')
        else: #Mas se eu conseguir
            await ctx.channel.send('Craft adicionado com sucesso.')
    



def setup(bot):
    bot.add_cog(Crafts(bot))
