import math

def minimax(tabuleiro, profundidade, maximizar):
    if tabuleiro.query.check_win(not maximizar):
        return -math.inf if maximizar else math.inf, -1
    elif profundidade == 0:
        return heuristica(tabuleiro), -1

    if maximizar:
        pontuacao = -math.inf

        def substituir(x):
            return x > pontuacao
    else:
        pontuacao = math.inf

        def substituir(x):
            return x < pontuacao

    mover = -1

    sucessores = tabuleiro.moves(maximizar)

    for sucessor in sucessores:
        acao = sucessor
        estado = tabuleiro.deep_copy()
        estado.move(*acao)

        temp = minimax(estado, profundidade - 1, not maximizar)[0]
        if substituir(temp):
            pontuacao = temp
            mover = acao

    return pontuacao, mover


def alphabeta(tabuleiro, profundidade, maximizar, alpha, beta):
    if tabuleiro.query.check_win(maximizar):
        return math.inf if maximizar else -math.inf, -1
    elif profundidade == 0:
        return heuristica(tabuleiro), -1

    if maximizar:
        pontuacao = -math.inf

        def substituir(x):
            return x > pontuacao
    else:
        pontuacao = math.inf

        def substituir(x):
            return x < pontuacao

    mover = -1

    sucessores = list(tabuleiro.moves(maximizar))

    for sucessor in sucessores:
        acao = sucessor
        estado = tabuleiro.deep_copy()
        estado.move(*acao)

        temp = alphabeta(estado, profundidade - 1, not maximizar, alpha, beta)[0]

        if substituir(temp):
            pontuacao = temp
            mover = acao
        if maximizar:
            alpha = max(alpha, temp)
        else:
            beta = min(beta, temp)
        if alpha >= beta:
            break

    return pontuacao, mover


def heuristica(tabuleiro):
    proximidade_centro = tabuleiro.query.center_proximity(False) - tabuleiro.query.center_proximity(True)

    coesao = 0
    if abs(proximidade_centro) > 2:
      coesao = len(list(tabuleiro.query.populations(False))) - len(list(tabuleiro.query.populations(True)))

    bolas = 0
    if abs(proximidade_centro) < 1.8:
        bolas = tabuleiro.query.marbles(True, True) * 100 - tabuleiro.query.marbles(False, True) * 100

    return proximidade_centro + coesao + bolas
