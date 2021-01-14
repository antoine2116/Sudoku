from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import *

from interface.tools.theme import Theme


class Button(QPushButton):
    def __init__(self, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.setStyleSheet(self.theme.button)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


