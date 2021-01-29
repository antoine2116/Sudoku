from PyQt5 import QtCore
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QPushButton

from interface.styles.Style import Style


class Button(QPushButton):
    """
    Parent class for all the game buttons
    """

    def __init__(self, style=Style()):
        super().__init__()

        # Styling
        self.style = style
        self.setStyleSheet(self.style.controls_button)
        self.setCursor(QCursor(QtCore.Qt.PointingHandCursor))


