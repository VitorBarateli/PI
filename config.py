TAMANHO_TABULEIRO = 5
NUMERO_MAX_BOLAS_ATAQUE = range(1, 4)
BRANCO = False
PRETO = True

def initialize(tabuleiro):
  return POSICAO_INICIAL[tabuleiro]

POSICAO_INICIAL = {
    'mini': {
        BRANCO: [
                         (1, -4), (2, -4), (3, -4),
                              (1, -3), (2, -3),
                                 (1, -2),
        ],
        PRETO: [
                                 (-1, 2),
                              (-2, 3), (-1, 3),
                         (-3, 4), (-2, 4), (-1, 4),
        ],
    },
}
