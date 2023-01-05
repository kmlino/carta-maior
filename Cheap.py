import random


class Cheap:

    def __init__(self):
        self.suits = ['C', 'E', 'O', 'P']
        self.values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [(x + y) for x in self.suits for y in self.values]

    def cards_shuffle(self):
        random.shuffle(self.cards)
        c = [i for i in self.cards]
        return c[:5]

    def to_distribute(self):
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        val_inv = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}
        ordered_list = []
        result = []

        for i in self.cards_shuffle():
            num = val[i[1:]] if i[1:] in val else int(i[1:])
            ordered_list.append((num, i[0]))
        for j in sorted(ordered_list):
            char = val_inv[j[0]] if j[0] in val_inv else str(j[0])
            result.append(j[-1] + char)
        return result
