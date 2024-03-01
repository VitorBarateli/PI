import time
import math
import random as rnd
from pyfiglet import Figlet

from jogo import AbaloneGrid
import config as config
import minimax as algs

custom_fig = Figlet(font='big')

while True:
    pontuacao_preto = 0
    pontuacao_branco = 0
    profundidade = 3
    rnd.seed(4106)

    posicao_inicial = config.initialize('mini')
    tabuleiro = AbaloneGrid(posicao_inicial)

    escolher = print("Selecione o Algortimo:\n(1) MiniMax \n(2) Alpha-Beta")
    alg = input("\nSelecione o numero: ")
    print("__________________________________________")
    print("\n Branco: ", pontuacao_branco, "\t\tPreto: ", pontuacao_preto)
    print("\n")
    print(tabuleiro.display)
    print("\n")

    start = time.time()
    while True:
        numero_de_brancas = tabuleiro.query.marbles(tabuleiro.WHITE, True)
        moves = list(tabuleiro.moves(tabuleiro.BLACK, rnd=True, seed=rnd.seed))
        block, direction = moves[rnd.randint(0, len(moves) - 1)]
        tabuleiro.move(block, direction)

        print("__________________________________________")
        print("\n Branco: ", pontuacao_branco, "\t\tPreto: ", pontuacao_preto)
        print("\n")
        print(tabuleiro.display)
        print("__________________________________________")
        print("\nPreto move: ", (block, direction))
        print("__________________________________________\n\n")

        if tabuleiro.query.check_win(tabuleiro.BLACK):
            print("Preto ganhou!")
            print("Duração: ", time.time() - start)
            print("______________________________________\n\n")
            break

        pontuacao_preto += numero_de_brancas - tabuleiro.query.marbles(tabuleiro.WHITE, True)
        numero_de_brancas = tabuleiro.query.marbles(tabuleiro.WHITE, True)

        move = None
      
        numero_de_pretas = tabuleiro.query.marbles(tabuleiro.BLACK, True)
        if alg == "1":
            _, move = algs.minimax(tabuleiro, profundidade, tabuleiro.WHITE)
        elif alg == "2":
            _, move = algs.alphabeta(tabuleiro, profundidade, tabuleiro.WHITE, -math.inf, math.inf)

        tabuleiro.move(move[0], move[1])

        print("__________________________________________")
        print("\n Branco: ", pontuacao_branco, "\t\tPreto: ", pontuacao_preto)
        print("__________________________________________\n")
        print(tabuleiro.display)
        print("______________________________________")
        print("\nBranco move: ", move, sep="")
        print("______________________________________\n\n")
        print("\n")

        if tabuleiro.query.check_win(tabuleiro.WHITE):
            print("Branco ganhou!")
            print("Duração: ", time.time() - start)
            print("______________________________________\n\n")
            break

        pontuacao_branco += numero_de_pretas - tabuleiro.query.marbles(tabuleiro.BLACK, True)
        numero_de_pretas = tabuleiro.query.marbles(tabuleiro.BLACK, True)
