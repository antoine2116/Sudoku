from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLineEdit

from interface.tools.theme import Theme


class CelluleValeur(QLineEdit):
    def __init__(self, value, theme=Theme()):
        super(QLineEdit, self).__init__()
        self.theme = theme
        self.setStyleSheet(self.theme.cellule)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(60, 60)
        self.setMouseTracking(True)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)

        self.setValue(value)

    def focusInEvent(self, event):
        self.selected = True

    def setValue(self, value):
        self.value = str(value)
        if self.value == "0":
            self.setText("")
        else:
            self.setText(self.value)

