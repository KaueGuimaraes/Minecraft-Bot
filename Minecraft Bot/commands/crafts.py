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
        cont = 1
        crafts = crafts.split('\n') #Separa por linha
        for c in crafts: #Pra cada coisa nos crafts
            if c == '': #Se for uma linha vazia
                continue #Irei ignora-lo
            else: #Se não
                c = c.split('===') #Separa usando de referência os caractéres '==='
                msg += f'{cont}. **{c[0]}** adicionado por {c[2]}\n' #Adiciona o nome e crédito ao msg
                cont += 1
        
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

        try:
            msg = int(msg)
        except:
            for c in crafts: #Para cada coisa nos crafts
                c = c.split('===') #Separa usando de referência os caractéres '==='
                if c[0] == msg.strip().lower(): #Se o nome do craft for igual ao craft que o usuário solicitou
                    title = msg #Salva o nome do craft
                    image = c[1] #Será salvo a imagem do craft
                    description = c[3]
        else:
            cont = 1
            for c in crafts: #Para cada coisa nos crafts
                c = c.split('===') #Separa usando de referência os caractéres '==='
                if cont == msg: #Se o nome do número for igual ao número que o usuário solicitou
                    title = c[0] #Salva o nome do craft
                    image = c[1] #Será salvo a imagem do craft
                    description = c[3]
                
                cont += 1

        embed = discord.Embed(
            title = title,
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
                escrever('crafts.txt', f'{msg[0].lower().strip()}==={msg[1].strip()}===<@{autor_id}>==={msg[2]}\n')
            except:
                escrever('crafts.txt', f'{msg[0].lower().strip()}==={msg[1].strip()}===<@{autor_id}>===\n')
        except: #Se eu não conseguir
            await ctx.channel.send('Não foi possível adicionar o seu Craft')
        else: #Mas se eu conseguir
            await ctx.channel.send('Craft adicionado com sucesso.')
    
    @commands.command(name = 'removeCraft', help = 'Remove um craft da lista de crafts. !removeCraft <nome> ou !removeCraft <número do craft>')
    async def remove_mod(self, ctx, *craft):
        msg = ''
        for c in craft: #Para cada coisa no objeto craft
            msg += f' {c}' #Adicionarei no objeto msg
        msg = msg.strip().lower() #Transformarei a string msg em minúsculo e tirarei os espaços do início e final

        crafts = lerArquivo('crafts.txt') #Irei ler o arquivo crafts.txt
        crafts = crafts.split('\n') #Irei separar os crafts por linha
        for c in range(0, len(crafts)): #Usando o objeto c do 0 até o tamanho da lista crafts
            if crafts[c] == '': #Se for uma linha vasia
                continue #Ignoro
            else: #Senão
                crafts[c] = crafts[c].split('===') #Irei separar usando de referência "==="
        
        try: #Tentarei
            msg = int(msg) #Transformar o objeto msg de string para int
        except: #Se não conseguir é porque é uma string
            for c in range(0, len(crafts)): #Usando a variável c começando do 0 até o tamanho da lista craft
                if crafts[c][0].lower().strip() == msg: #Se o craft for igual ao craft solicitado pelo usuário
                    remove = c #Anotarei o mesmo
                    return #E retornarei
        else: #Se conseguir é porque é um valor inteiro
            for c in range(0, len(crafts)): #Usando a variável c começando do 0 até o tamanho da lista craft
                if c + 1 == msg: #Se o número do craft for igual ao valor informado pelo usuário
                    remove = c #Anotarei o mesmo
                    return #E retornarei
        finally: #Por último
            try: #Tentarei
                new_crafts = ''
                for c in range(0, len(crafts)): #Usando a variável c começando do 0 até o tamanho da lista crafts
                    if crafts[c] == '': #Se o craft for uma linha vazia
                        continue #Ignoro
                    elif crafts[c][0] == crafts[remove][0]: #Senão se o nome do craft for igual ao nome do craft anotado
                        name = crafts[remove][0] #Irei anotar o nome do mesmo
                        continue #E continar
                    else: #Se não
                        new_crafts += f'{crafts[c][0]}==={crafts[c][1]}==={crafts[c][2]}==={crafts[c][3]}\n' #Irei adicionar o craft a variável new_crafts
                
                if crafts[remove][2].strip() == ctx.author.mention:
                    criarArquivo('crafts.txt') #Limparei o arquivo crafts.txt
                    escrever('crafts.txt', new_crafts) #Adicionarei os novos crafts com o valor formatado

                    await ctx.channel.send(f'Craft **{name}** removido com sucesso.') #Informarei o usuário que a tarefa solicitadaa foi realizada com sucesso
                else:
                    await ctx.channel.send('Somente o autor do craft pode remove-lo.')
            except: #Se eu não conseguir
                await ctx.channel.send(f'Não foi possível remover **{msg}**.') #Informarei o usuário que eu falhei na tentativa de realizar a tarefa solicitada


def setup(bot):
    bot.add_cog(Crafts(bot))
