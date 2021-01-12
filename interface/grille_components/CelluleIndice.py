from PyQt5.QtWidgets import QLabel
from interface.tools.theme import Theme
from PyQt5.QtCore import Qt


class CelluleIndice(QLabel):
    def __init__(self, value=0, theme=Theme()):
        super(QLabel, self).__init__()
        self.theme = theme
        self.setStyleSheet(self.theme.indice)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(20, 20)

        self.value = str(value)
        if self.value == "0":
            self.setText("")
        else:
            self.setText(self.value)