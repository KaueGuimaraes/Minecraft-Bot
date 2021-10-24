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
        mods = lerArquivo('mods.txt')
        mods = mods.split('\n')
        
        description = ''
        cont = 1
        for c in mods:
            if c == '':
                continue
            else:
                description += f'{cont}. {c}\n'
                cont += 1

        embed = discord.Embed(
            title = 'Minecraft Mods',
            description = description,
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
    
    @commands.command(name = 'removeMod', help = 'Remove um mod da lista de mods. !removeMod <nome> ou !removeMod <número do mod>')
    async def remove_mod(self, ctx, *mod):
        msg = ''
        for c in mod: #Para cada item no objeto mod
            msg += f' {c}' #Adicionarei o mesmo no objeto msg
        msg.strip() #No final removerei os espaços do inicio e do final

        mods = lerArquivo('mods.txt') #Irei ler os mods registrados no arquivo mods.txt
        mods = mods.split('\n') #Irei separar cada linha para facilitar a leitura
        try: #Tentarei
            msg = int(msg) #Transformar a variável msg de string para int
        except: #Se não funcionar significa que é uma string
            for c in range(0, len(mods)): #Usando a variável c começando do 0 até o tamanho da lista mods
                if mods[c].lower().strip() == msg.lower().strip(): #Se o mod for igual ao mod solicitado pelo usuário
                    remove = c #Anotarei o mesmo usando a variável remove
                    return #E retornarei
        else: #Se funcionar significa que é um número
            for c in range(0, len(mods)): #Usando a variável c começando do 0 até o tamanho da lista mods
                if c + 1 == msg: #Se a ordem do mod for igual ao número informado pelo usuário:
                    remove = c #Anotarei o mesmo usando a variável remove
                    return #E retornarei
        finally: #Por último
            try: #Tentarei
                new_mods = ''
                for c in mods: #Para cada item na variável mods
                    if c == mods[remove]:
                        name = mods[remove]
                        continue
                    else:
                        if c == '': #Se for uma linha vazia
                            continue #Irei ignora-lo
                        else:
                            new_mods += f'{c}\n' #Adicionarei o mesmo na variável new_mods
                print('o')
                criarArquivo('mods.txt') #Limparei o arquivo
                escrever('mods.txt', new_mods) #Adicionarei a nova lista atualizada

                await ctx.channel.send(f'O mod **{name}** foi removido com sucesso.') #Informarei ao usuário que a tarefa foi realizada com sucesso
            except: #Se não conseguir
                await ctx.channel.send(f'Não foi possível remover o mod {msg}.') #Infomarei ao usuário que eu não fui capaz de realizar a tarefa como solicitado


def setup(bot):
    bot.add_cog(Mods(bot))
