import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QPixmap
from Jogador import *
from Baralho import *


class Tab(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.jogadas = []
        self.baralho = Baralho()
        #self.cartas = self.baralho.distribui()
        self.jogador = Jogador()
        self.distribuir()
        self.restart.clicked.connect(self.recomecar)
        self.btn_carta_1.clicked.connect(lambda: self.clicar_btn(self.carta_1.text()))
        self.btn_carta_2.clicked.connect(lambda: self.clicar_btn(self.carta_2.text()))
        self.btn_carta_3.clicked.connect(lambda: self.clicar_btn(self.carta_3.text()))
        self.btn_carta_4.clicked.connect(lambda: self.clicar_btn(self.carta_4.text()))
        self.btn_carta_5.clicked.connect(lambda: self.clicar_btn(self.carta_5.text()))

    def recomecar(self):
        self.jogadas.clear()
        self.jogada.clear()
        self.distribuir()

    def clicar_btn(self, carta):
        self.jogadas.append(carta)
        self.jogada.setText(carta)

    def distribuir(self):
        cartas = self.baralho.distribui()
        self.carta_1.setText(cartas[0])
        self.carta_2.setText(cartas[1])
        self.carta_3.setText(cartas[2])
        self.carta_4.setText(cartas[3])
        self.carta_5.setText(cartas[4])


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tab = Tab()
    tab.show()
    qt.exec_()
    b = baralho
