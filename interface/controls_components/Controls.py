from PyQt5.QtWidgets import QWidget, QGridLayout

from interface.controls_components.Button import Button
from interface.controls_components.ButtonIndice import ButtonIndice
from interface.controls_components.ButtonValeur import ButtonValeur
from interface.tools.theme import Theme


class Controls(QWidget):
    def __init__(self, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.setFixedSize(300, 300)
        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.btns_numero = []
        cpt = 1
        for i in range(0, 3):
            for y in range(0, 3):
                button = ButtonValeur(cpt)
                self.btns_numero.append(button)
                self.grid_layout.addWidget(button, i, y)
                cpt = cpt + 1

        self.btn_aff_indice = ButtonIndice()
        self.grid_layout.addWidget(self.btn_aff_indice, 3, 0)


