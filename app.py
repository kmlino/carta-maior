import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from Jogador import *
from Baralho import *


class Tab(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.jogadas = []
        self.naipe_da_vez = ''
        self.vencedor_atual = 0
        self.baralho = Baralho()
        # self.cartas = self.baralho.distribui()
        self.jogador1 = Jogador()
        self.cartas = self.baralho.distribui()
        self.jogador2 = Jogador()
        self.cartas_p2 = self.baralho.distribui()
        self.distribuir()
        self.restart.clicked.connect(self.recomecar)
        self.btn_carta_1.clicked.connect(lambda: self.clicar_btn(self.carta_1.text()))
        self.btn_carta_2.clicked.connect(lambda: self.clicar_btn(self.carta_2.text()))
        self.btn_carta_3.clicked.connect(lambda: self.clicar_btn(self.carta_3.text()))
        self.btn_carta_4.clicked.connect(lambda: self.clicar_btn(self.carta_4.text()))
        self.btn_carta_5.clicked.connect(lambda: self.clicar_btn(self.carta_5.text()))
        self.pushButton_2.clicked.connect(self.comecar)

    def comecar(self):
        msg = QMessageBox()
        msg.setText('Testando pop up!')
        msg.setWindowTitle('Pop Up')
        msg.show()
        msg.exec_()

    def recomecar(self):
        self.jogadas.clear()
        self.jogada_p1.clear()
        self.jogada_p2.clear()
        self.cartas = baralho.distribui()
        self.distribuir()

    def clicar_btn(self, carta):
        if not carta:
            return
        self.jogadas.append(carta)
        for c in range(len(self.cartas)):
            if carta == self.cartas[c]:
                self.cartas[c] = None
        self.jogada_p1.setText(carta)
        carta_p2 = self.joga_p2(carta)
        self.jogada_p2.setText(carta_p2)
        self.distribuir()

    def distribuir(self):
        self.carta_1.setText(self.cartas[0])
        self.carta_2.setText(self.cartas[1])
        self.carta_3.setText(self.cartas[2])
        self.carta_4.setText(self.cartas[3])
        self.carta_5.setText(self.cartas[4])

    def joga_p2(self, carta_p1):
        c = self.cartas_p2.copy()
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
                if x[0] == carta_p1[0]:
                    equal.append([x[0], int(x[1:])])
                else:
                    diff.append([x[0], int(x[1:])])

        res = max(equal) if carta_p1[0] in naipe else min(diff)
        st = res[0]
        it = str(res[1])
        for k, y in val.items():
            if it == str(y):
                it = k

        carta_p2 = str(st) + it

        for c in range(len(self.cartas_p2)):
            if carta_p2 == self.cartas_p2[c]:
                self.cartas_p2[c] = None

        return carta_p2

    # def verifica_vencedor_rodada(self, jogada_p1, jogada_p2, naipe):
    #     val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    #     p1 = int(jogada_p1[1:]) if jogada_p1[1:] not in val else val[jogada_p1[1:]]
    #     p2 = int(jogada_p2[1:]) if jogada_p2[1:] not in val else val[jogada_p2[1:]]
    #
    #     if jogada_p1[0] == jogada_p2[0]:
    #         return True if p1 > p2 else False
    #     else:
    #         return True if naipe == jogada_p1[0] else False


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tab = Tab()
    tab.show()
    qt.exec_()
    b = baralho
