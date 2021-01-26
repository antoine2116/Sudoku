from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QStyle

from interface.controls_components.Button import Button
from interface.controls_components.ButtonIndices import ButtonIndices
from interface.controls_components.ButtonValeur import ButtonValeur
from interface.controls_components.Timer import Timer
from interface.styles.Theme import Theme


class Controls(QWidget):
    def __init__(self, n, timer_data, theme=Theme()):
        super().__init__()
        self.theme = theme
        v_boxlayout = QVBoxLayout()
        self.setFixedHeight(400)
        self.setLayout(v_boxlayout)
        self.timer = Timer(timer_data)
        v_boxlayout.addWidget(self.timer)

        self.btn_supprimer = Button()
        self.btn_supprimer.setStyleSheet(self.theme.button + self.theme.button_supprimer)
        self.btn_supprimer.setIcon(self.style().standardIcon(getattr(QStyle, "SP_TitleBarCloseButton")))
        v_boxlayout.addWidget(self.btn_supprimer)

        grid_layout = QGridLayout()
        v_boxlayout.addLayout(grid_layout)

        self.btns_numero = []
        cpt = 1
        for x in range(1, n + 1):
            for y in range(1, n + 1):
                button = ButtonValeur(cpt)
                self.btns_numero.append(button)
                grid_layout.addWidget(button, x, y)
                cpt = cpt + 1

        h_boxlayout = QHBoxLayout()
        v_boxlayout.addLayout(h_boxlayout)

        self.btn_aff_indice = ButtonIndices()
        h_boxlayout.addWidget(self.btn_aff_indice)

        self.btn_possibilites = Button()
        self.btn_possibilites.setText("Possibilités")
        self.btn_possibilites.setStyleSheet(self.theme.button + self.theme.button_font_smaller)
        h_boxlayout.addWidget(self.btn_possibilites)


