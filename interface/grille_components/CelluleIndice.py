from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLabel, QLineEdit
from interface.tools.theme import Theme
from PyQt5.QtCore import Qt, pyqtSignal


class CelluleIndice(QLineEdit):
    value = ""
    selected_signal = pyqtSignal()

    def __init__(self, valeur="", theme=Theme()):
        super(QLineEdit, self).__init__()
        self.theme = theme
        self.setStyleSheet(self.theme.cellule_indice)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(20, 20)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)
        self.setValue(valeur)

    def setValue(self, valeur):
        if valeur != self.value:
            self.setText(str(valeur))
            self.value = str(valeur)
        else:
            self.setText("")
            self.value = ""

    def focusInEvent(self, event):
        self.selected_signal.emit()

