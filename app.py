import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from Cheap import *


class Tab(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.plays = []
        self.cheap = Cheap()
        self.p1_wins = 0
        self.p2_wins = 0
        self.p1_cards = self.cheap.to_distribute()
        self.p2_cards = self.cheap.to_distribute()
        self.current_winner = 2
        self.restart.clicked.connect(self.restart)
        self.btn_card_1.clicked.connect(lambda: self.clicar_btn(self.card_1.text(), self.p2_move.text()))
        self.btn_card_2.clicked.connect(lambda: self.clicar_btn(self.card_2.text(), self.p2_move.text()))
        self.btn_card_3.clicked.connect(lambda: self.clicar_btn(self.card_3.text(), self.p2_move.text()))
        self.btn_card_4.clicked.connect(lambda: self.clicar_btn(self.card_4.text(), self.p2_move.text()))
        self.btn_card_5.clicked.connect(lambda: self.clicar_btn(self.card_5.text(), self.p2_move.text()))
        self.to_distribute_main()

    # Responsible for counting the rounds and ending the game
    def limiter(self):
        if self.p1_wins >= 3 or self.p2_wins >= 3:
            msg = QMessageBox()
            msg.setWindowTitle('OVER')
            msg.setText('Fim de jogo!')
            msg.show()
            msg.exec_()
            self.close()

    # Responsible for clearing all the fields
    def restart(self):
        self.plays.clear()
        self.p1_move.clear()
        self.p2_move.clear()
        self.p1_cards = self.cheap.to_distribute()
        self.p2_cards = self.cheap.to_distribute()
        self.to_distribute_main()

    # Responsible for controlling the action on click the buttons of the cards
    # 'p2_card' parameter is None when the first player is the player 1
    def clicar_btn(self, card, p2_card=None):
        # If there is no value, none action is taken
        if not card:
            return
        # If there is, the value will be removed from the list 'p1_cards' and printed in the field
        self.p1_cards[self.p1_cards.index(card)] = None
        if not p2_card:
            # If there is no card in the field of player 2, I am the first
            self.plays.append(card)
            self.p1_move.setText(card)
            self.p2_plays(card)
            self.to_distribute_main()
        else:
            self.plays.append(card)
            self.p1_move.setText(card)
            if self.round_winner_check(card, p2_card, p2_card[0]):
                self.p1_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Jogador 1 ganhou')
            else:
                self.p2_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Jogador 2 ganhou')
            self.limiter()
            self.to_distribute_main()

    def to_distribute_main(self):
        self.card_1.setText(self.p1_cards[0])
        self.card_2.setText(self.p1_cards[1])
        self.card_3.setText(self.p1_cards[2])
        self.card_4.setText(self.p1_cards[3])
        self.card_5.setText(self.p1_cards[4])

    def p2_plays(self, p1_cards=None):
        c = self.p2_cards.copy()
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        equal = []
        diff = []
        new = {}

        if not p1_cards:
            for k, v in val.items():
                for i in c:
                    if i is not None:
                        if i[1:] == k:
                            c[c.index(i)] = i[0] + str(v)  # Ex: OJ -> O10
            for i in c:
                if i is not None:
                    new = {i[1:]: i[0]}

            menor = min(new.items())
            res = menor[1] + menor[0]
            self.p2_move.setText(res)
            return res
        else:
            #  Trasnforma os valores não numéricos em numéricos
            for k, v in val.items():
                for i in c:
                    if i is not None:
                        if i[1:] == k:
                            c[c.index(i)] = i[0] + str(v)  # Ex: OJ -> O10

            # Armazena os naipes do jogador em uma lista
            naipes = [x[0] if x is not None else None for x in c]

            # Confere se o naipe da carta adversária existe entre as minhas cartas
            for x in c:
                if x is not None:
                    if x[0] == p1_cards[0]:
                        # Se sim, o naipe e o valor numérico serão armazenados numa lista com naipes iguais
                        equal.append([x[0], int(x[1:])])
                    else:
                        # Se não, o naipe e o valor numérico serão armazenados numa lista com naipes diferentes
                        diff.append([x[0], int(x[1:])])

            # Essa variável pegará a minha maior carta com o mesmo naipe, ou, se não houver naipe igual, a menor carta
            res = max(equal) if p1_cards[0] in naipes else min(diff)

            # Retorna os valores acima de 9 para letras
            st = res[0]
            it = str(res[1])

            # Caso o valor seja igual a umas das chaves, será substituido pela chave correspondente
            for k, y in val.items():
                if it == str(y):
                    it = k

            # Variável recebe a carta pronta para o 'return'
            carta_p2 = str(st) + it

            # Anula o valor na lista depois que a carta for usada
            for c in range(len(self.p2_cards)):
                if carta_p2 == self.p2_cards[c]:
                    self.p2_cards[c] = None

            # Realiza a jogada
            self.p2_move.setText(carta_p2)

            #  Verifica qual é a maior carta e imprime o vencedor no campo 'resultado'
            if self.round_winner_check(p1_cards, carta_p2, p1_cards[0]):
                self.p1_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Jogador 1 ganhou')
            else:
                self.p2_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Jogador 2 ganhou')
            self.limiter()
            self.to_distribute_main()
            return carta_p2

    def round_winner_check(self, move_p1, move_p2, suit):
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        p1 = int(move_p1[1:]) if move_p1[1:] not in val else val[move_p1[1:]]
        p2 = int(move_p2[1:]) if move_p2[1:] not in val else val[move_p2[1:]]

        if move_p1[0] == move_p2[0]:
            return True if p1 > p2 else False
        else:
            return True if suit == move_p1[0] else False


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tab = Tab()
    tab.show()
    qt.exec_()
