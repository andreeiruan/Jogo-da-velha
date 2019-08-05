"""
                                        PROGRAMADO POR ANDREI RUÃ
                                                03/07/2019
"""

import funcoes
from random import randint
from time import sleep

while True:

    print('[1] PLAY VS COMP')
    print('[2] PLAY VS PLAY')
    print('[0] SAIR')

    while True:
        try:
            partida = int(input())
        except ValueError:
            print('Digite um número valido para sua opção!')
        else:
            if partida not in (0, 1, 2):
                print('Digite uma opção valida!')
            else:
                break

    if partida is 1:
        totjog = totcomp = empate = 0
        while True:
            tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            jogadas = []
            comp = ganhador = ''

            while True:
                play = str(input('Digite X ou O e pressione Enter para escolher '
                                 'com qual você quer jogar: ')).strip().upper()
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
            funcoes.tab(tabuleiro)

            while True:
                while True:
                    try:
                        sleep(0.5)
                        jogador = int(input(f'Sua vez de marcar "{play}": '))

                    except ValueError:
                        print('Jogada Invalida!')
                    else:
                        if jogador not in tabuleiro:
                            print('jogada invalida ou Campo ja foi preenchido!')
                        else:
                            jogadas.append(jogador)
                            funcoes.att_tab(jogador, play, tabuleiro)
                            break
                sleep(1)
                funcoes.tab(tabuleiro)
                sleep(2)

                if funcoes.verificar(tabuleiro) is True:
                    totjog += 1
                    ganhador = 'JOGADOR'
                    break

                if len(jogadas) is 9:
                    empate += 1
                    ganhador = 'EMPATE'
                    break

                print(f'Agora minha vez "{comp}"! ')
                sleep(0.5)
                while True:
                    computador = int(randint(0, 8)) + 1
                    if computador not in jogadas:
                        jogadas.append(computador)
                        break
                funcoes.att_tab(computador, comp, tabuleiro)
                sleep(2)

                funcoes.tab(tabuleiro)
                sleep(2)

                if funcoes.verificar(tabuleiro) is True:
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

    if partida is 2:
        totjog1 = totjog2 = empate = 0

        while True:
            jogador1 = jogador2 = ''
            tabuleiro = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            jogadas = []
            while True:
                jogador1 = str(input('Jogador 1: Você quer X ou O para jogar? ')).upper().strip()
                if jogador1 not in 'XO':
                    print('Escolha X ou O para jogar')
                else:
                    if jogador1 == 'X':
                        jogador2 = 'O'
                        break
                    else:
                        jogador2 = 'X'
                        break
            sleep(0.5)
            print(f'Jogador 1 será {jogador1} e jogador 2 será {jogador2}')
            sleep(0.5)
            print('COMEÇA A PARTIDA!!!!!')
            print('-' * 50)
            sleep(0.5)
            funcoes.tab(tabuleiro)
            sleep(0.5)
            while True:
                while True:
                    try:
                        jog_jogador1 = int(input(f'Sua vez de marcar Jogador 1"{jogador1}": '))
                    except ValueError:
                        print('Digite um numero para sua jogada!')
                    else:
                        if jog_jogador1 not in tabuleiro:
                            print('Jogada invalida ou campo ja preenchido!')
                        else:
                            jogadas.append(jog_jogador1)
                            funcoes.att_tab(jog_jogador1, jogador1, tabuleiro)
                            break

                if funcoes.verificar(tabuleiro) is True:
                    totjog1 += 1
                    print('JOGADOR 1 GANHOU!!!')
                    break

                if len(jogadas) is 9:
                    empate += 1
                    print('Deu empate!')
                    break

                funcoes.tab(tabuleiro)

                while True:
                    try:
                        jog_jogador2 = int(input(f'Sua vez de marcar jogador 2 "{jogador2}": '))
                    except ValueError:
                        print('Digite um numero para sua jogada!')
                    else:
                        if jog_jogador2 not in tabuleiro:
                            print('Jogada invalida ou campo ja preenchido!')
                        else:
                            jogadas.append(jog_jogador2)
                            funcoes.att_tab(jog_jogador2, jogador2, tabuleiro)
                            break

                if funcoes.verificar(tabuleiro) is True:
                    totjog2 += 1
                    print('JOGADOR 2 GANHOU!!!')
                    break

                funcoes.tab(tabuleiro)

            while True:
                continuar = str(input('Jogar mais? ')).strip().upper()[0]
                if continuar not in 'SN':
                    print('Apenas SIM ou NÃO!')
                else:
                    break
            if continuar is 'N':
                break

        print('-' * 50)
        print(f'Jogador 1 ganhou {totjog1} vezes!')
        sleep(0.5)
        print(f'Jogador 2 ganhou {totjog2} vezes!')
        sleep(0.5)
        print(f'Empatou {empate} vezes!')

    if partida is 0:
        sleep(0.5)
        print('FINALIZANDO...')
        sleep(1)
        print('ADEUS!')
        break
