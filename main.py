from Tabuleiro import *
from Jogador import *

# Variáveis locais e objetos necessários
jogador1 = Jogador()
jogador2 = Jogador()
vencedor_atual = 0
naipe_da_vez = ''
t = Tabuleiro()

# Não permite cartas repetidas entre os dois jogadores
while set(jogador1.get_cartas()) & set(jogador2.get_cartas()):
    jogador2 = Jogador()

# Inicia o jogo
print('***JOGO DE COPAS***'.rjust(30))

while jogador1.get_vitorias() < 3 and jogador2.get_vitorias() < 3:

    t.imprime_tabuleiro(jogador1.get_cartas(), jogador2.get_cartas())

    # O vencedor da rodada passada inicia. Caso seja a primeira, o jogador 1 inicia
    if vencedor_atual == 1:
        print('Jogador 1, sua vez!')
        jogada1 = jogador1.joga_humano()
        jogador1.set_jogada(jogada1)
        print('Jogador 2, sua vez!')
        jogada2 = jogador2.joga_cpu(jogada1)
        jogador2.set_jogada(jogada2)
        print('Jogador 2 jogou a carta: {0}'.format(jogada2))
        naipe_da_vez = jogada1[0]

    elif vencedor_atual == 2:
        print('Jogador 2, sua vez!')
        jogada2 = jogador2.joga_cpu(' ')
        jogador2.set_jogada(jogada2)
        print('Jogador 2 jogou a carta: {0}'.format(jogada2))
        print('Jogador 1, sua vez!')
        jogada1 = jogador1.joga_humano()
        jogador1.set_jogada(jogada1)
        naipe_da_vez = jogada2[0]

    else:
        print('Jogador 1, sua vez!')
        jogada1 = jogador1.joga_humano()
        jogador1.set_jogada(jogada1)
        print('Jogador 2, sua vez!')
        jogada2 = jogador2.joga_cpu(jogada1)
        jogador2.set_jogada(jogada2)
        print('Jogador 2 jogou a carta: {0}'.format(jogada2))
        naipe_da_vez = jogada1[0]

    # Imprime a carta escolhida por cada um e as cartas disponíveis
    t.imprime_restante(jogador1.get_cartas(), jogador2.get_cartas(), jogada1, jogada2)

    # Verifica o vencedor de cada rodada
    if t.verifica_vencedor_rodada(jogada1, jogada2, naipe_da_vez):
        print('Vencedor da rodada: Jogador 1!')
        jogador1.set_vitoria(1)
        vencedor_atual = 1
    else:
        print('Vencedor da rodada: Jogador 2!')
        jogador2.set_vitoria(1)
        vencedor_atual = 2

    # Imprime o placar do jogo no final de cada rodada
    print('Placar: Jogador 1= \'{0}\' | Jogador 2= \'{1}\''.format(jogador1.get_vitorias(), jogador2.get_vitorias()))
    t.verifica_vencedor_partida(jogador1.get_cartas(), jogador2.get_cartas(),
                                jogador1.get_vitorias(), jogador2.get_vitorias())

    # Permite o jogador analisar a rodada e só prossegue quando Enter for pressionado
    cls = input('Pressione \'Enter\' para prosseguir')
    print('\n\n')
