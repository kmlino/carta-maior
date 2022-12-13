class Tabuleiro:

    def __init__(self):
        self.s = '''
        {0} | {1} | {2} | {3} | {4}
        --------------------------
             {10}    |    {11}
        --------------------------
        {5} | {6} | {7} | {8} | {9}
        '''

    def imprime_tabuleiro(self, cartas_p1, cartas_p2):
        t = cartas_p1 + cartas_p2
        t.append(' ')
        t.append(' ')
        print(self.s.format(*t))

    def imprime_restante(self, cartas_p1, cartas_p2, jogada_p1, jogada_p2):
        t = cartas_p1 + cartas_p2
        t.append(jogada_p1)
        t.append(jogada_p2)
        print(self.s.format(*t))

    def verifica_vencedor_rodada(self, jogada_p1, jogada_p2, naipe):
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        p1 = int(jogada_p1[1:]) if jogada_p1[1:] not in val else val[jogada_p1[1:]]
        p2 = int(jogada_p2[1:]) if jogada_p2[1:] not in val else val[jogada_p2[1:]]

        if jogada_p1[0] == jogada_p2[0]:
            return True if p1 > p2 else False
        else:
            return True if naipe == jogada_p1[0] else False

    def verifica_vencedor_partida(self, cartas_p1, cartas_p2, win_p1, win_p2):
        if (cartas_p1.count(None) >= 5 and cartas_p2.count(None) >= 5) or (win_p1 >= 3 or win_p2 >= 3):
            print('Vencedor da partida: Jogador 1!!!' if win_p1 > win_p2 else 'Vencedor da partida: Jogador 2!!!')
        else:
            pass
