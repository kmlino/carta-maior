import random


class Baralho:

    def __init__(self):
        self.naipes = ['C', 'E', 'O', 'P']
        self.valores = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cartas = [(x+y) for x in self.naipes for y in self.valores]

    # def get_cartas(self):
    #     return self.cartas

    def embaralha(self):
        random.shuffle(self.cartas)
        c = [i for i in self.cartas]
        return c[:5]

    def distribui(self):
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        val_inv = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        lista_ordenada = []
        resultado = []

        for i in self.embaralha():
            num = val[i[1:]] if i[1:] in val else int(i[1:])
            lista_ordenada.append((num, i[0]))
        for j in sorted(lista_ordenada):
            char = val_inv[j[0]] if j[0] in val_inv else str(j[0])
            resultado.append(j[-1] + char)
        return resultado
