import sys
from design import *
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from Jogador import *
from Baralho import *


class Tab(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.jogadas = []
        self.baralho = Baralho()
        self.vitorias_p1 = 0
        self.vitorias_p2 = 0
        self.cartas = baralho.distribui()
        self.cartas_p2 = baralho.distribui()
        self.vencedor_atual = 2
        self.restart.clicked.connect(self.recomecar)
        self.btn_carta_1.clicked.connect(lambda: self.clicar_btn(self.carta_1.text(), self.jogada_p2.text()))
        self.btn_carta_2.clicked.connect(lambda: self.clicar_btn(self.carta_2.text(), self.jogada_p2.text()))
        self.btn_carta_3.clicked.connect(lambda: self.clicar_btn(self.carta_3.text(), self.jogada_p2.text()))
        self.btn_carta_4.clicked.connect(lambda: self.clicar_btn(self.carta_4.text(), self.jogada_p2.text()))
        self.btn_carta_5.clicked.connect(lambda: self.clicar_btn(self.carta_5.text(), self.jogada_p2.text()))
        self.distribuir()

    def limitador(self):
        if self.vitorias_p1 >= 3 or self.vitorias_p2 >= 3:
            msg = QMessageBox()
            msg.setWindowTitle('OVER')
            msg.setText('Fim de jogo!')
            msg.show()
            msg.exec_()
            self.close()

    def recomecar(self):
        self.jogadas.clear()
        self.jogada_p1.clear()
        self.jogada_p2.clear()
        self.cartas = baralho.distribui()
        self.cartas_p2 = baralho.distribui()
        self.distribuir()

    def clicar_btn(self, carta, carta_p2=None):
        if not carta:
            return
        self.cartas[self.cartas.index(carta)] = None
        if not carta_p2:
            self.jogadas.append(carta)
            self.jogada_p1.setText(carta)
            self.joga_p2(carta)
            self.distribuir()
        else:
            self.jogadas.append(carta)
            self.jogada_p1.setText(carta)
            if self.verifica_vencedor_rodada(carta, carta_p2, carta_p2[0]):
                self.vitorias_p1 += 1
                self.score.setText(f'{self.vitorias_p1} x '
                                   f'{self.vitorias_p2} ')
                self.resultado.setText('Jogador 1 ganhou')
            else:
                self.vitorias_p2 += 1
                self.score.setText(f'{self.vitorias_p1} x '
                                   f'{self.vitorias_p2} ')
                self.resultado.setText('Jogador 2 ganhou')

            self.distribuir()
            self.limitador()

    def distribuir(self):
        self.carta_1.setText(self.cartas[0])
        self.carta_2.setText(self.cartas[1])
        self.carta_3.setText(self.cartas[2])
        self.carta_4.setText(self.cartas[3])
        self.carta_5.setText(self.cartas[4])

    def joga_p2(self, carta_p1=None):
        c = self.cartas_p2.copy()
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        equal = []
        diff = []
        new = {}

        if not carta_p1:
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
            self.jogada_p2.setText(res)
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
                    if x[0] == carta_p1[0]:
                        # Se sim, o naipe e o valor numérico serão armazenados numa lista com naipes iguais
                        equal.append([x[0], int(x[1:])])
                    else:
                        # Se não, o naipe e o valor numérico serão armazenados numa lista com naipes diferentes
                        diff.append([x[0], int(x[1:])])

            # Essa variável pegará a minha maior carta com o mesmo naipe, ou, se não houver naipe iguala, a menor carta
            res = max(equal) if carta_p1[0] in naipes else min(diff)

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
            for c in range(len(self.cartas_p2)):
                if carta_p2 == self.cartas_p2[c]:
                    self.cartas_p2[c] = None
            self.jogada_p2.setText(carta_p2)
            if self.verifica_vencedor_rodada(carta_p1, carta_p2, carta_p1[0]):
                self.vitorias_p1 += 1
                self.score.setText(f'{self.vitorias_p1} x '
                                   f'{self.vitorias_p2} ')
                self.resultado.setText('Jogador 1 ganhou')
            else:
                self.vitorias_p2 += 1
                self.score.setText(f'{self.vitorias_p1} x '
                                   f'{self.vitorias_p2} ')
                self.resultado.setText('Jogador 2 ganhou')
            self.limitador()
            self.distribuir()
            return carta_p2

    def verifica_vencedor_rodada(self, jogada_p1, jogada_p2, naipe):
        val = {'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        p1 = int(jogada_p1[1:]) if jogada_p1[1:] not in val else val[jogada_p1[1:]]
        p2 = int(jogada_p2[1:]) if jogada_p2[1:] not in val else val[jogada_p2[1:]]

        if jogada_p1[0] == jogada_p2[0]:
            return True if p1 > p2 else False
        else:
            return True if naipe == jogada_p1[0] else False


if __name__ == '__main__':
    qt = QApplication(sys.argv)
    tab = Tab()
    tab.show()
    qt.exec_()
