from PyQt5 import QtCore
from PyQt5.QtGui import QCursor

from interface.controls_components.Button import Button
from interface.tools.theme import Theme


class ButtonIndice(Button):
    isClicked = False

    def __init__(self, theme=Theme()):
        super().__init__()
        self.setText("Indices")
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.setStyleSheet(self.theme.button + self.theme.button_indice)

    def toggleClicked(self):
        if self.isClicked:
            self.isClicked = False
            self.setStyleSheet(self.theme.button + self.theme.button_indice)
        else:
            self.isClicked = True
            self.setStyleSheet(self.theme.button + self.theme.button_indice + self.theme.button_indice_selected)

