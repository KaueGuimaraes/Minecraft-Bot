import discord
from discord.ext import commands

from arquivo import *


colour = 1015823


class Profiles(commands.Cog):
    '''Players commands'''
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name = 'perfil', help = '(BETA) Mostra o perfil do usuário. !perfil')
    async def profile(self, ctx):
        name = ctx.author.name
        embed = discord.Embed(
            title = name,
            description = 'Informações',
            colour = colour
        )

        await ctx.channel.send(embed = embed)

    @commands.command(name = 'players', help = 'Mostra todos os jogadores registrados. !players')
    async def players(self, ctx):
        if arquivoExiste('players.txt'):
            msg = lerArquivo('players.txt')
            msg = msg.split('\n')

            description = ''
            for c in msg:
                if c == '':
                    continue
                else:
                    description += f'• {c}\n'

            embed = discord.Embed(
                title = 'Players',
                description = description,
                colour = colour
            )

            embed.set_author(name = 'Minecraft Bot', icon_url = 'https://cdn.discordapp.com/avatars/900889967604158464/eda53038817044cf685215dde7cdff30.png?size=160')
            embed.set_thumbnail(url = 'https://i.pinimg.com/564x/fa/9b/60/fa9b6028ba671d619781059653299849.jpg')

            await ctx.channel.send(embed = embed)
        else:
            criarArquivo('players.txt')
            await ctx.channel.send('Tente novamente.')
    
    @commands.command(name = 'addPlayer', help = 'Adiciona um jogador a lista de jogadores. !addPlayers <nome no minecraft> <menção no discord>')
    async def add_player(self, ctx, player, nick):
        try: #Tenta
            escrever('players.txt', f'{player} **{nick}**\n') #Adicionar player
        except: #Se não conseguir
            await ctx.channel.send('Não foi possível adicionar o jogador.') #Informa
        else: #Se conseguir
            await ctx.channel.send('Player adicionado com sucesso.') #Informa
    
    @commands.command(name = 'removePlayer', help = 'Remove um jogador da lista de jogadores. !removePlayer <nome> ou !removePlayer <menção> ou !removePlayer <número do player>')
    async def remove_player(self, ctx, player):
        players = lerArquivo('players.txt') #Ler o arquivo players.txt e anota-lo na variável players
        players = players.split('\n') #Separar a variáevel players por linha
        
        try: #Tentarei
            player = int(player) #Transformar a variável player de string para int
        except: #Se eu não conseguir
            for c in range(0, len(players)): #Usando a variável c começando do 0 até o tamanho da lista players
                if players[c] == '': #Se o jogador for uma linha vazia
                    continue #Ignoro
                elif player in players[c]: #Senão se o jogador informado pelo usuário for o jogador atual
                    remove = c #Irei anotar
        else: #Se eu conseguir
            for c in range(0, len(players)): #Usando a variável c começando do 0 até o tamanho da lista players
                if players[c] == '': #Se o jogador for uma linha vazio
                    continue #Ignoro
                elif c + 1 == player: #Se não se o número do jogar for igual ao valor informado pelo usuário
                    remove = c #Irei anotar
        finally: #Por último
            try: #Tentarei
                new_players = ''
                for c in players: #Para cada valor na lista players
                    if c == '': #Se for uma linha vazia
                        continue #Ignoro
                    elif c == players[remove]: #Senão se for o que eu anotei
                        continue #Ignoro
                    else: #Senão
                        new_players += f'{c}\n' #Adiciono o jogador a variável new_players
                
                criarArquivo('players.txt') #Limpo o arquivo players.txt
                escrever('players.txt', new_players) #Envio as informações formatadas para o arquivo players.txt

                await ctx.channel.send(f'Player {player} removido(a) com sucesso.') #Informo o usuário de que a tarefa solicitada foi realizada com sucesso
            except: #Se eu não conseguir
                await ctx.channel.send(f'Não foi possível remover o player {player}.') #Informo o usuário de que não consegui realizar a tarefa solicitada


def setup(bot):
    bot.add_cog(Profiles(bot))
