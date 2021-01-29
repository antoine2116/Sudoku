from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal

from interface.styles.Style import Style


class CellHint(QLineEdit):
    """
    Cell that contains a hint
    """

    value = 0
    selected_signal = pyqtSignal()

    def __init__(self, value=0, style=Style()):
        """
        Initializes style and its value
        :param value: value from JSON data
        :param style: styling object
        """

        super(QLineEdit, self).__init__()

        # Styling
        self.style = style
        self.setStyleSheet(self.style.cell_hint)
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(style.cell_hint_side, style.cell_hint_side)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)

        # Initialize value
        self.setValue(value)

    def setValue(self, new_value):
        """
        Updates the cell value and display
        :param new_value: incoming value
        """

        # Value
        self.value = new_value

        # Display
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        self.setText(symbols[new_value])

    def focusInEvent(self, event):
        """
        Overides PyQt method, emits a signal to unselect the current selected cell
        and to select this cell
        """

        self.selected_signal.emit()
