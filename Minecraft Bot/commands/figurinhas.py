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
        cont = 1
        figurinhas = figurinhas.split('\n') #Separa por linha
        for c in figurinhas: #Pra cada coisa nas figurinhas
            if c == '': #Se for uma linha vazia
                continue #Irei ignora-lo
            else: #Senão
                c = c.split('===') #Separa usando de referência os caractéres '==='
                msg += f'{cont}. **{c[0]}**  adicionado por {c[2]}\n' #Adiciona o nome e crédito ao msg
                cont += 1
        
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

        try: #Tentarei
            msg = int(msg) #Tranformar a variável msg de string para int
        except: #Se não conseguir significa que é uma string
            for c in figurinhas: #Para cada coisa nos figurinhas
                c = c.split('===') #Separa usando de referência o caractére '==='
                if c[0] == msg.strip().lower(): #Se o nome da figurinha for igual a figurinha que o usuário solicitou
                    name = c[0] #Será salvo o nome da imagem
                    image = c[1] #Será salvo a imagem da figurinha
                    return #Retornarei
        else: #Mas se eu conseguir significa que é um valor inteiro
            for c in range(0, len(figurinhas)): #Usando a variável c começando do 0 até o tamanho da lista figurinhas
                if figurinhas[c] == '': #Se a figurinha for uma linha vazia
                    continue #Simplismente irei ignorar

                figurinhas[c] = figurinhas[c].split('===') #Irei separar usando de referência '==='
                if c + 1 == msg: #se o número da figurinha for igual ao número enviado pelo usuário
                    name = figurinhas[c][0] #Será salvo o nome da image
                    image = figurinhas[c][1] #Será salvo a imagem da figurinha
        finally:
            try:
                await ctx.channel.send(f'{image}') #Envio a figurinha
            except:
                await ctx.channel.send(f'Não existe')
    
    @commands.command(name = 'addFigurinha', help = 'Adiciona uma figurinha. !addFigurinha <nome>=<imagem url>')
    async def add_figurinha(self, ctx, *figurinha):
        msg = ''
        for c in figurinha: #Junta os caractéres separados do elemento figurinha
            msg += f'{c} '
        
        msg = msg.split('=')
        autor_mention = ctx.author.mention
        
        try: #Vou tentar escrever a nova figurinha
            escrever('figurinhas.txt', f'{msg[0].lower().strip()}==={msg[1].strip()}==={autor_mention}\n')
        except: #Se eu não conseguir
            await ctx.channel.send('Não foi possível adicionar a sua figurinha')
        else: #Mas se eu conseguir
            await ctx.channel.send('Figurinha adicionada com sucesso.')
    
    @commands.command(name = 'removeFigurinha', help = 'Remove uma figurinha. !removeFigurinha <nome> ou !removeFigurinha <número da Figurinha>')
    async def remove_figurinha(self, ctx, *figurinha):
        msg = ''
        for c in figurinha: #Para cada item no objeto figurinha
            msg += f' {c}' #Adicionarei o mesmo no objeto msg
        msg = msg.strip().lower() #Deixarei a string msg em minúsculo e tirarei os espaços do começo e do final

        figurinhas = lerArquivo('figurinhas.txt') #Ler arquivo figurinhas.txt e anotar no objeto figurinhas
        figurinhas = figurinhas.split('\n') #Separar figurinhas por linha
        for c in range(0, len(figurinhas)): #Usando o elemento c começando do 0 até o tamanho da lista figurinhas
            if figurinhas[c] == '': #Se for uma linha vazia
                continue #Irei ignorar
            else: #Senão
                figurinhas[c] = figurinhas[c].split('===') #Irei separa-lo usando de referência "---"
        
        try: #Tentarei
            msg = int(msg) #Transformar a string msg em um valor inteiro
        except: #Se eu não conseguir
            for c in range(0, len(figurinhas)): #Usando a variável c começando do 0 até o tamanho da lista figurinhas
                if figurinhas[c][0].strip() == msg: #Se a figurinha for igual a figurinha solicitada pelo usuário
                    remove = c #Irei anotar o mesmo
                    return #E retornarei
        else: #Se eu conseguir
            for c in range(0, len(figurinhas)): #Usando a variável c começando do 0 até o tamanho da lista figurinhas
                if c + 1 == msg: #Se o número da figurinha for igual ao número solicitado pelo usuário
                    remove = c #Irei anota-lo
                    return #E retornarei
        finally: #E por último
            try: #Tentarei
                new_figurinhas = ''
                for c in range(0, len(figurinhas)): #Usando a variável c do 0 até o tamanho da lista figurinhas
                    if figurinhas[c] == '': #Se for uma linha vazia
                        continue #Irei ignorar
                    elif figurinhas[c][0] == figurinhas[remove][0]: #Senão se a figurinha for igual a figurinha anotada
                        name = figurinhas[remove][0] #Irei anotar o nome
                        continue #E continuarei
                    else: #Senão
                        new_figurinhas += f'{figurinhas[c][0]}==={figurinhas[c][1]}==={figurinhas[c][2]}\n' #Adicionarei a figurinha a variável new_figurinhas
                
                if figurinhas[remove][2] == ctx.author.mention:
                    criarArquivo('figurinhas.txt') #Limparei o arquivo figurinhas.txt
                    escrever('figurinhas.txt', new_figurinhas) #Enviarei as informações formatadas para o arquivo figurinhas.txt

                    await ctx.channel.send(f'Figurinha {name} removida com sucesso.') #Informarei o usuário que o proceso solicitado foi realizado com sucesso
                else:
                    await ctx.channel.send('Somente o autor da figurinha pode remove-la.')
            except: #Se eu não conseguir
                await ctx.channel.send(f'Não foi possível remover {msg}.') #Informarei o usuário que não foi possível realizar o processo solicitado


def setup(bot):
    bot.add_cog(Figurinhas(bot))
