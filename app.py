import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
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
        self.btn_restart.clicked.connect(self.restart)
        self.btn_card_1.clicked.connect(lambda: self.click_btn(self.card_1.text(), self.p2_move.text()))
        self.btn_card_2.clicked.connect(lambda: self.click_btn(self.card_2.text(), self.p2_move.text()))
        self.btn_card_3.clicked.connect(lambda: self.click_btn(self.card_3.text(), self.p2_move.text()))
        self.btn_card_4.clicked.connect(lambda: self.click_btn(self.card_4.text(), self.p2_move.text()))
        self.btn_card_5.clicked.connect(lambda: self.click_btn(self.card_5.text(), self.p2_move.text()))
        self.to_distribute_main()

    # Responsible for counting the rounds and ending the game
    def limiter(self):
        if self.p1_wins >= 3 or self.p2_wins >= 3:
            msg = QMessageBox()
            msg.setWindowTitle('GAME OVER!!!')
            msg.setText('Player 1 won!') if self.p1_wins > 3 else msg.setText('Player 2 won!')
            msg.setStandardButtons(QMessageBox.Close)
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
    def click_btn(self, card, p2_card=None):
        # If there is no value, none action is taken
        if not card:
            return
        # If there is, the value will be removed from the list 'p1_cards' and printed in the field
        self.p1_cards[self.p1_cards.index(card)] = None
        if not p2_card:
            # If there is no card in the field of player 2, I am the first, and then he plays
            self.plays.append(card)
            self.p1_move.setText(card)
            self.p2_plays(card)
            self.to_distribute_main()
        else:
            # If there is, my card will be compared with p2's card
            self.plays.append(card)
            self.p1_move.setText(card)
            # Define the winner
            if self.round_winner_check(card, p2_card, p2_card[0]):
                self.p1_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Player 1 Won!')
            else:
                self.p2_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Player 2 Won!')
            self.limiter()
            self.to_distribute_main()

    # Distribute the cards according to the lists
    def to_distribute_main(self):
        self.card_1.setText(self.p1_cards[0])
        self.card_2.setText(self.p1_cards[1])
        self.card_3.setText(self.p1_cards[2])
        self.card_4.setText(self.p1_cards[3])
        self.card_5.setText(self.p1_cards[4])

    # Responsible to move the player 2
    def p2_plays(self, p1_card=None):
        p2_card_list = self.p2_cards.copy()
        # Dictionary used to replace the letters to numbers
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        equal = []
        diff = []
        new_dict = {}

        # If there isn't my card on the field, player 2 starts, and play your smaller card
        if not p1_card:
            for k, v in val.items():
                for i in p2_card_list:
                    if i:
                        if i[1:] == k:
                            # If there's a letter in the values, here it's replaced to number
                            p2_card_list[p2_card_list.index(i)] = i[0] + str(v)  # Ex: OJ -> O10
            for i in p2_card_list:
                if i:
                    new_dict = {i[1:]: i[0]}
            # The number is replaced to letter
            smaller = min(new_dict.items())
            res = smaller[1] + smaller[0]
            self.p2_move.setText(res)
            return res
        # If so, the player 2 try his highest card
        else:
            for k, v in val.items():
                for i in p2_card_list:
                    if i:
                        if i[1:] == k:
                            p2_card_list[p2_card_list.index(i)] = i[0] + str(v)  # Ex: OJ -> O10

            # Stores player suits in a list
            suits = [x[0] if x is not None else None for x in p2_card_list]

            # Checks if the opponent's card suit exists among my cards
            for x in p2_card_list:
                if x is not None:
                    if x[0] == p1_card[0]:
                        # If so, the suit and value will be stored in a suited list
                        equal.append([x[0], int(x[1:])])
                    else:
                        # If not, the suit and value will be stored in a list with different suits
                        diff.append([x[0], int(x[1:])])

            # This variable will take the highest card of the same suit, or, if there is no matching suit, the lowest
            res = max(equal) if p1_card[0] in suits else min(diff)
            st = res[0]
            it = str(res[1])

            # If the value is equal to one of the keys, it will be replaced by the corresponding key
            for k, y in val.items():
                if it == str(y):
                    it = k

            p2_card = str(st) + it

            # Null the value in the list after the card is used
            for p2_card_list in range(len(self.p2_cards)):
                if p2_card == self.p2_cards[p2_card_list]:
                    self.p2_cards[p2_card_list] = None

            # Plays
            self.p2_move.setText(p2_card)

            # Checks which is the highest card and prints the winner in the 'result' field
            if self.round_winner_check(p1_card, p2_card, p1_card[0]):
                self.p1_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Player 1 Won')
            else:
                self.p2_wins += 1
                self.score.setText(f'{self.p1_wins} x '
                                   f'{self.p2_wins} ')
                self.result.setText('Player 1 Won')
            self.limiter()
            self.to_distribute_main()
            return p2_card

    # Responsible for checking the winner of the round
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
