def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print('Arquivo criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
        return 'Algum erro aconteceu por favor contate o criador do bot e reporte o erro. Kauê Guimarães Programador#7894'
    else:
        ret = '' #Valor a retornar
        for linha in a:
            ret += linha
        
        return ret
    finally:
        a.close()


def cadastrar(arquivo, nome, link, ip, porta, version):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mOcorreu um ao o tentar cadastrar o usuário!\033[m')
    else:
        try:
            a.write(f'\n**{nome}**\nLink: {link}\nIP: {ip}\nPorta: {porta}\nVersion: {version}\n')
        except:
            print('\033[31mOcorreu um erro ao tentar cadastrar o usuário!\033[m')
        else:
            print(f'cadastrado com sucesso!')
    finally:
        a.close()


def cadastrarMod(arquivo, mod):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mOcorreu um ao o tentar cadastrar o usuário!\033[m')
    else:
        try:
            a.write(f'- {mod}\n')
        except:
            print('\033[31mOcorreu um erro ao tentar cadastrar o usuário!\033[m')
        else:
            print(f'cadastrado com sucesso!')
    finally:
        a.close()


def escrever(arquivo, texto):
    try:
        a = open(arquivo, 'at')
    except:
        print('\033[31mOcorreu um ao o tentar escrever no arquivo!\033[m')
    else:
        try:
            a.write(f'{texto}')
        except:
            print('\033[31mOcorreu um erro ao tentar escrever no arquivo!\033[m')
        else:
            print(f'escrito com sucesso!')
    finally:
        a.close()