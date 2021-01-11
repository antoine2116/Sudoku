from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton

from interface.tools.theme import Theme


class Button(QPushButton):
    def __init__(self, value, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.setText(value)
        self.setStyleSheet(self.theme.button)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
