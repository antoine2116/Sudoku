from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLineEdit

from interface.styles.Dimensions import Dimensions
from interface.styles.Theme import Theme


class CelluleValeur(QLineEdit):
    selected_signal = pyqtSignal()
    value = 0

    def __init__(self, fixed, valeur, verifie=False, theme=Theme(), dim=Dimensions()):
        super(QLineEdit, self).__init__()
        self.theme = theme
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(dim.cellule_valeur, dim.cellule_valeur)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.fixed = fixed
        self.verifie = verifie
        self.setValue(valeur)

        self.updateTextColor()

    def keyPressEvent(self, event):
        return

    def focusInEvent(self, event):
        if not self.fixed:
            self.selected_signal.emit()

    def setValue(self, valeur):
        if valeur == self.value:
            valeur = 0
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        self.setText(symbols[valeur])
        self.value = valeur

    def updateTextColor(self):
        if self.fixed:
            self.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_fixed)
            if self.verifie:
                self.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_verifie)
        else:
            self.setStyleSheet(self.theme.cellule_valeur)



