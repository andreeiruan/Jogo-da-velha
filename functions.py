def att_tab(tabuleiro=None, jogada=None, quem=None):
    """
    :param jogada: Recebe a opção que o jogador escolheu para marcar no tabuleiro
    :param quem: Recebe quem fez a jogada
    :param tabuleiro: Recebe o tabuleiro
    :return: Retorna a atualização do tabuleiro a cada rodada
    """
    for item in tabuleiro:
        if item == jogada:
            tabuleiro.remove(item)
            tabuleiro.insert(jogada-1, quem)
    return f'''
            \t {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} 
            \t---|---|---
            \t {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}   
            \t---|---|---
            \t {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}'''


def verificar(t):
    """
    A função verificara as posiçoes das jogadas e se tiver uma combinação para vitoria
    :param t: O tabuleiro do jogo que esta em uma lista.
    :return: variavel ok para dar o fim do jogo quando houver um ganhador retornando ok = true,
     ou ok=false enquanto não houver a combinação de vitoria
    """
    if t[0] == t[1] and t[1] == t[2]:
        ok = True
        print(f'"{t[0]}" GANHOU!')
        return ok
    elif t[3] == t[4] and t[4] == t[5]:
        ok = True
        print(f'"{t[3]}" GANHOU!')
        return ok
    elif t[6] == t[7] and t[7] == t[8]:
        ok = True
        print(f'"{t[6]}" GANHOU!')
        return ok
    elif t[0] == t[3] and t[3] == t[6]:
        ok = True
        print(f'"{t[0]}" GANHOU!')
        return ok
    elif t[1] == t[4] and t[4] == t[7]:
        ok = True
        print(f'"{t[1]}" GANHOU!')
        return ok
    elif t[2] == t[5] and t[5] == t[8]:
        ok = True
        print(f'"{t[2]}" GANHOU!')
        return ok
    elif t[2] == t[4] and t[4] == t[6]:
        ok = True
        print(f'"{t[2]}" GANHOU!')
        return ok
    elif t[0] == t[4] and t[4] == t[8]:
        ok = True
        print(f'"{t[0]}" GANHOU!')
        return ok
    else:
        ok = False
        return ok
