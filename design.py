# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(652, 455)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.score = QtWidgets.QLineEdit(self.centralwidget)
        self.score.setEnabled(False)
        self.score.setStyleSheet("")
        self.score.setObjectName("score")
        self.gridLayout_2.addWidget(self.score, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 6, 5, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.restart = QtWidgets.QPushButton(self.centralwidget)
        self.restart.setObjectName("restart")
        self.gridLayout_2.addWidget(self.restart, 6, 4, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.gridLayout.setContentsMargins(-1, 0, 0, -1)
        self.gridLayout.setHorizontalSpacing(10)
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.carta_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.carta_5.setEnabled(False)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carta_5.sizePolicy().hasHeightForWidth())
        self.carta_5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.carta_5.setFont(font)
        self.carta_5.setStyleSheet("height: 140;")
        self.carta_5.setObjectName("carta_5")
        self.gridLayout.addWidget(self.carta_5, 0, 4, 1, 1)
        self.btn_carta_1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carta_1.setObjectName("btn_carta_1")
        self.gridLayout.addWidget(self.btn_carta_1, 1, 0, 1, 1)
        self.btn_carta_2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carta_2.setObjectName("btn_carta_2")
        self.gridLayout.addWidget(self.btn_carta_2, 1, 1, 1, 1)
        self.btn_carta_5 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carta_5.setObjectName("btn_carta_5")
        self.gridLayout.addWidget(self.btn_carta_5, 1, 4, 1, 1)
        self.carta_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.carta_3.setEnabled(False)
        self.carta_3.setStyleSheet("height: 140;")
        self.carta_3.setObjectName("carta_3")
        self.gridLayout.addWidget(self.carta_3, 0, 2, 1, 1)
        self.carta_1 = QtWidgets.QLineEdit(self.centralwidget)
        self.carta_1.setEnabled(False)
        self.carta_1.setStyleSheet("height: 140 px;")
        self.carta_1.setObjectName("carta_1")
        self.gridLayout.addWidget(self.carta_1, 0, 0, 1, 1)
        self.carta_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.carta_4.setEnabled(False)
        self.carta_4.setStyleSheet("height: 140;")
        self.carta_4.setObjectName("carta_4")
        self.gridLayout.addWidget(self.carta_4, 0, 3, 1, 1)
        self.btn_carta_4 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carta_4.setObjectName("btn_carta_4")
        self.gridLayout.addWidget(self.btn_carta_4, 1, 3, 1, 1)
        self.carta_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.carta_2.setEnabled(False)
        self.carta_2.setStyleSheet("height: 140;")
        self.carta_2.setReadOnly(False)
        self.carta_2.setObjectName("carta_2")
        self.gridLayout.addWidget(self.carta_2, 0, 1, 1, 1)
        self.btn_carta_3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_carta_3.setObjectName("btn_carta_3")
        self.gridLayout.addWidget(self.btn_carta_3, 1, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 6)
        self.jogada_p1 = QtWidgets.QLineEdit(self.centralwidget)
        self.jogada_p1.setEnabled(False)
        self.jogada_p1.setPlaceholderText("")
        self.jogada_p1.setObjectName("jogada_p1")
        self.gridLayout_2.addWidget(self.jogada_p1, 1, 1, 1, 1)
        self.rodada = QtWidgets.QLineEdit(self.centralwidget)
        self.rodada.setEnabled(False)
        self.rodada.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.rodada.setObjectName("rodada")
        self.gridLayout_2.addWidget(self.rodada, 0, 1, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_1.setObjectName("label_1")
        self.gridLayout_2.addWidget(self.label_1, 1, 3, 1, 1)
        self.resultado = QtWidgets.QLineEdit(self.centralwidget)
        self.resultado.setEnabled(False)
        self.resultado.setObjectName("resultado")
        self.gridLayout_2.addWidget(self.resultado, 2, 1, 1, 1)
        self.jogada_p2 = QtWidgets.QLineEdit(self.centralwidget)
        self.jogada_p2.setEnabled(False)
        self.jogada_p2.setObjectName("jogada_p2")
        self.gridLayout_2.addWidget(self.jogada_p2, 1, 4, 1, 1)
        self.melhor = QtWidgets.QLineEdit(self.centralwidget)
        self.melhor.setEnabled(False)
        self.melhor.setObjectName("melhor")
        self.gridLayout_2.addWidget(self.melhor, 3, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 3, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Jogada P1:"))
        self.label_4.setText(_translate("MainWindow", "Score:"))
        self.label_3.setText(_translate("MainWindow", "Resultado:"))
        self.pushButton_2.setText(_translate("MainWindow", "Sair"))
        self.label.setText(_translate("MainWindow", "Rodada:"))
        self.restart.setText(_translate("MainWindow", "Restart"))
        self.btn_carta_1.setText(_translate("MainWindow", "Escolher"))
        self.btn_carta_2.setText(_translate("MainWindow", "Escolher"))
        self.btn_carta_5.setText(_translate("MainWindow", "Escolher"))
        self.btn_carta_4.setText(_translate("MainWindow", "Escolher"))
        self.btn_carta_3.setText(_translate("MainWindow", "Escolher"))
        self.label_1.setText(_translate("MainWindow", "Jogada P2:"))
        self.label_5.setText(_translate("MainWindow", "Melhor:"))
