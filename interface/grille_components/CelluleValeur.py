from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLineEdit

from interface.tools.theme import Theme


class CelluleValeur(QLineEdit):
    selected_signal = pyqtSignal()
    value = ""

    def __init__(self, fixed, valeur, theme=Theme()):
        super(QLineEdit, self).__init__()
        self.theme = theme
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(60, 60)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.fixed = fixed
        self.value = "" if valeur == 0 else str(valeur)
        self.setText(self.value)

        self.updateTextColor()

    def focusInEvent(self, event):
        if not self.fixed:
            self.selected_signal.emit()

    def setValue(self, valeur):
        valeur = "" if valeur == 0 else valeur
        if valeur != self.value:
            self.setText(str(valeur))
            self.value = str(valeur)
        else:
            self.setText("")
            self.value = ""

    def updateTextColor(self):
        style = self.theme.cellule_valeur
        if self.fixed:
            self.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_fixed)
        else:
            self.setStyleSheet(self.theme.cellule_valeur)



