"""
                                        PROGRAMADO POR ANDREI RUÃ
                                                03/07/2019
"""
import functions
from random import randint
from time import sleep

fim = True
totjog = totcomp = empate = 0

while True:
    # Criei uma lista para simular o tabuleiro, a cada jogada, o valor é substituido pelo simbolo do jogador
    tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # Essa lista salvara as posições que ja foram jogadas, para não ter problema de repetir uma jogada
    # e tambem para verificar o fim do jogo
    jogadas = []
    comp = ganhador = ''

    while True:
        play = str(input('Digite X ou O e pressione Enter para escolher com qual você quer jogar: ')).strip().upper()
        if play not in 'XO':
            print('Opção invalida')
        else:
            if play == 'X':
                comp = 'O'
            elif play == 'O':
                comp = 'X'
            break

    print(f'Você escolheu {play} para jogar')
    print('Vamos ao jogo!')
    sleep(0.5)

    print(functions.att_tab(tabuleiro))

    while True:
        while True:
            try:
                print()
                print()
                jogador = int(input(f'Sua vez de marcar "{play}": '))
                print()
            except ValueError:
                print('Jogada Invalida!')
            else:
                if jogador not in tabuleiro:
                    print('jogada invalida ou Campo ja foi preenchido!')
                else:
                    jogadas.append(jogador)
                    break

        sleep(0.5)
        print(functions.att_tab(tabuleiro, jogador, play))
        sleep(0.5)

        if functions.verificar(tabuleiro) == fim:
            totjog += 1
            ganhador = 'JOGADOR'
            break
        if len(jogadas) == 9:
            empate += 1
            ganhador = 'EMPATE'
            break

        print()
        print()
        print(f'Agora minha vez "{comp}"! ')
        sleep(1)
        print()
        while True:
            computador = int(randint(0, 8)) + 1
            if computador not in jogadas:
                jogadas.append(computador)
                break
        print(functions.att_tab(tabuleiro, computador, comp))
        sleep(2)

        if functions.verificar(tabuleiro) == fim:
            totcomp += 1
            ganhador = 'COMPUTADOR'
            break
    sleep(1)
    print('Final de jogo')
    sleep(0.5)
    print(f'Quem ganhou foi o {ganhador}!')
    while True:
        continuar = str(input('Quer jogar outra partida [S/N]? ')).strip().upper()[0]
        if continuar not in 'SN':
            print('Apenas SIM ou NÃO!')
        else:
            break
    if continuar == 'N':
        break
print('-' * 50)
sleep(0.5)
print(f'Jogador ganhou {totjog} vezes.')
sleep(0.5)
print(f'Computador ganhou {totcomp} vezes.')
sleep(0.5)
print(f'Deu empate {empate} vezes.')
