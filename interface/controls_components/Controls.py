from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout

from interface.controls_components.Button import Button
from interface.controls_components.ButtonIndice import ButtonIndice
from interface.controls_components.ButtonValeur import ButtonValeur
from interface.controls_components.Timer import Timer
from interface.tools.theme import Theme


class Controls(QWidget):
    def __init__(self, n, theme=Theme()):
        super().__init__()
        self.theme = theme
        v_boxlayout = QVBoxLayout()
        self.setLayout(v_boxlayout)
        self.timer = Timer()
        v_boxlayout.addWidget(self.timer)

        grid_layout = QGridLayout()
        v_boxlayout.addLayout(grid_layout)

        self.btns_numero = []
        cpt = 1
        for i in range(0, n):
            for y in range(0, n):
                button = ButtonValeur(cpt)
                self.btns_numero.append(button)
                grid_layout.addWidget(button, i, y)
                cpt = cpt + 1

        self.btn_aff_indice = ButtonIndice()
        v_boxlayout.addWidget(self.btn_aff_indice)


