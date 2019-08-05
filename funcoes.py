def att_tab(jogada, quem, tabuleiro):
    """
    Função para atualizar o tabuleiro a cada jogada
    :param jogada: Recebe o numero da jogada
    :param quem: Recebe quem fez a jogada
    :param tabuleiro: Recebe o tabuleiro da partida
    :return:
    """
    for item in tabuleiro:
        if item == jogada:
            tabuleiro.remove(item)
            tabuleiro.insert(jogada-1, quem)


def tab(tabuleiro):
    """
    Uma simples função para mostrar o tabuleiro da partida em forma de jogo da velha
    :param tabuleiro: Recebe o tabuleiro da partida
    :return:
    """
    print(f'''\n
            \n
            \t\t\t {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} 
            \t\t\t---|---|---
            \t\t\t {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}   
            \t\t\t---|---|---
            \t\t\t {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
            \n
            \n''')


def verificar(t):
    """
    Função para verificar o tabueleiro, se há ou não um ganhador
    :param t: Recebe o tabuleiro como parametro para analise das jogadas
    :return: Ok recebe true caso haja um ganhador e encerrar a partida
    """
    if (t[0] == t[1] and t[1] == t[2]) or (t[0] == t[3] and t[3] == t[6]) or (t[0] == t[4] and t[4] == t[8]):
        ok = True
        print(f'"{t[0]}" GANHOU!')
        return ok
    elif (t[2] == t[5] and t[5] == t[8]) or (t[2] == t[4] and t[4] == t[6]):
        ok = True
        print(f'"{t[2]}" GANHOU!')
        return ok
    elif t[3] == t[4] and t[4] == t[5]:
        ok = True
        print(f'"{t[3]}" GANHOU!')
        return ok
    elif t[6] == t[7] and t[7] == t[8]:
        ok = True
        print(f'"{t[6]}" GANHOU!')
        return ok
    elif t[1] == t[4] and t[4] == t[7]:
        ok = True
        print(f'"{t[1]}" GANHOU!')
        return ok
    else:
        ok = False
        return ok
