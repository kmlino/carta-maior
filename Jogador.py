from Baralho import *
baralho = Baralho()


class Jogador:

    def __init__(self):
        #self.cartas_jogador = baralho.distribui()
        self.vitorias = 0

    # def get_cartas(self):
    #     return self.cartas_jogador

    def get_vitorias(self):
        return self.vitorias

    def set_vitoria(self, vencedor):
        self.vitorias += vencedor

    # def set_jogada(self, jogada):
    #     self.cartas_jogador[self.cartas_jogador.index(jogada)] = None

    def joga_humano(self):
        jogada = input('Escolha sua carta: ').upper()
        while jogada not in self.cartas_jogador:
            jogada = input('Carta inválida, tent novamente: ').upper()
        return jogada

    def joga_cpu(self, jogada_adv):
        c = self.cartas_jogador.copy()
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        equal = []
        diff = []
        for k, v in val.items():
            for i in c:
                if i is not None:
                    if i[1:] == k:
                        c[c.index(i)] = i[0] + str(v)

        naipe = [x[0] if x is not None else None for x in c]

        for x in c:
            if x is not None:
                if x[0] == jogada_adv[0]:
                    equal.append([x[0], int(x[1:])])
                else:
                    diff.append([x[0], int(x[1:])])

        res = max(equal) if jogada_adv[0] in naipe else min(diff)
        st = res[0]
        it = str(res[1])
        for k, y in val.items():
            if it == str(y):
                it = k
        return st + it
