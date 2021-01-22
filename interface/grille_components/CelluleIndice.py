from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLabel, QLineEdit

from interface.styles.Dimensions import Dimensions
from interface.styles.Theme import Theme
from PyQt5.QtCore import Qt, pyqtSignal


class CelluleIndice(QLineEdit):
    value = 0
    selected_signal = pyqtSignal()

    def __init__(self, valeur=0, theme=Theme(), dim=Dimensions()):
        super(QLineEdit, self).__init__()
        self.theme = theme
        self.setStyleSheet(self.theme.cellule_indice)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(dim.cellule_indice, dim.cellule_indice)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setValue(valeur)

    def setValue(self, valeur):
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        self.setText(symbols[valeur])
        self.value = valeur

    def focusInEvent(self, event):
        self.selected_signal.emit()

