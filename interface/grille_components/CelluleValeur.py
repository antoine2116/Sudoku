from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLineEdit
from interface.tools.theme import Theme


class CelluleValeur(QLineEdit):
    selected_signal = pyqtSignal()
    value = ""

    def __init__(self, fixed, valeur, verifie=False, theme=Theme()):
        super(QLineEdit, self).__init__()
        self.theme = theme
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(60, 60)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.fixed = fixed
        self.verifie = verifie
        self.value = "" if valeur == 0 else str(valeur)
        self.setText(self.value)

        self.updateTextColor()

    def keyPressEvent(self, event):
        return

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
        if self.fixed:
            self.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_fixed)
            if self.verifie:
                self.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_verifie)
        else:
            self.setStyleSheet(self.theme.cellule_valeur)



