from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QLineEdit

from interface.styles.Style import Style


class CellValue(QLineEdit):
    """
    Cell that contains the value
    """

    selected_signal = pyqtSignal()
    value_changed_signal = pyqtSignal()
    value = 0

    def __init__(self, fixed, valeur, checked=False, style=Style()):
        """
        Initializes style and properties
        :param fixed: propertie from JSON
        :param valeur: propertie from JSON
        :param checked: propertie from JSON
        :param style: styling object
        """

        super(QLineEdit, self).__init__()

        # Style
        self.style = style
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(style.cell_value_side, style.cell_value_side)
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setContextMenuPolicy(Qt.NoContextMenu)

        # Properties

        # A fixed cell is a unselectable cell (value from the initial grid or checked by the solver)
        self.fixed = fixed

        # A check cell is a fixed cell, it has been checked by the solver
        self.checked = checked

        self.setValue(valeur)

        self.updateStyle()

    def keyPressEvent(self, event):
        """
        Detects the key pressed to update the cell value
        :param event: key event
        """
        allowed_keys = [Qt.Key_1, Qt.Key_2, Qt.Key_3, Qt.Key_4, Qt.Key_5, Qt.Key_6, Qt.Key_7,
                        Qt.Key_8, Qt.Key_9, Qt.Key_A, Qt.Key_B, Qt.Key_C, Qt.Key_D, Qt.Key_E,
                        Qt.Key_F, Qt.Key_G]

        if event.key() not in allowed_keys:
            return
        elif not self.fixed:
            self.setValue(allowed_keys.index(event.key()) + 1)

    def focusInEvent(self, event):
        """
        Overide of PyQt method, emits a signal to unselect the current selected cell
        and to select to cell
        """

        if not self.fixed:
            self.selected_signal.emit()

    def setValue(self, new_value):
        """
        Updates the cell value and display
        :param new_value: incoming value
        """

        if new_value == self.value:
            new_value = 0

        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        self.setText(symbols[new_value])
        self.value = new_value
        self.value_changed_signal.emit()

    def updateStyle(self):
        """
        Updates the color of the display depending its status (fixed, checked, none)
        """

        if self.fixed:
            self.setStyleSheet(self.style.cell_value + self.style.cell_value_fixed)
            if self.checked:
                self.setStyleSheet(self.style.cell_value + self.style.cell_value_checked)
        else:
            self.setStyleSheet(self.style.cell_value)

