from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout

from interface.styles.Style import Style
from interface.grid_components.CellValue import CellValue
from interface.grid_components.CellHint import CellHint


class Cell(QGridLayout):
    """
    Contains a cell value and 9 cell hints
    """

    cell_value = None
    selected = False
    selected_signal = pyqtSignal()

    def __init__(self, cell_data, divider, r, c, style=Style()):
        """
        Initializes styles and generate its components
        :param cell_data: JSON data
        :param divider: size of a block
        :param r: row number
        :param c: col number
        :param style: styling object
        """

        super(QGridLayout, self).__init__()

        # Styling
        self.style = style
        self.setSpacing(0)

        # Propeties
        self.cell_data = cell_data
        self.divider = divider
        self.r = r
        self.c = c
        self.fixed = self.cell_data["display_solution"] or self.cell_data["checked"]
        self.checked = self.cell_data["checked"]

        self.generateComponents()
        self.displayValue()

    def generateComponents(self):
        """
        Generates cell value and the cell hints
        """

        # Create cell_value
        if self.fixed and not self.checked:
            self.cell_value = CellValue(True, self.cell_data["solution"], False)
        elif self.checked:
            self.cell_value = CellValue(True, self.cell_data["player"], True)
        else:
            self.cell_value = CellValue(False, self.cell_data["player"], False)
        self.cell_value.selected_signal.connect(self.selectCell)

        # Create 9 clel_hints
        self.cells_hints = []
        if not self.fixed:
            i = 0
            for r in range(0, 3):
                for c in range(0, 3):
                    if i < len(self.cell_data["hints"]):
                        cell_hint = CellHint(i + 1)
                    else:
                        cell_hint = CellHint()
                    cell_hint.selected_signal.connect(self.selectCell)
                    self.cells_hints.append(cell_hint)
                    i = i + 1

    def displayValue(self):
        """
        Clears the widget, then displays the cell value
        """

        self.removeAllWidgets()
        self.addWidget(self.cell_value, 0, 0)

    def displayHints(self):
        """
        Clears the widget, then display the 9 cell hints
        """

        if not self.cell_value.fixed:
            self.removeAllWidgets()
            i = 0
            for r in range(0, 3):
                for c in range(0, 3):
                    self.addWidget(self.cells_hints[i], r, c)
                    i = i + 1

    def toggleCellDisplay(self):
        """
        Switches the display (value/hints)
        """

        if self.count() == 1 and self.cell_value.value == 0:
            self.displayHints()
        else:
            self.displayValue()

    def removeAllWidgets(self):
        """
        Tool method for cleaning the layout
        """

        for i in reversed(range(self.count())):
            self.itemAt(i).widget().setParent(None)

    def selectCell(self):
        """
        Selects a cell
        """

        self.selected = True

        # Cell value
        self.cell_value.setStyleSheet(self.style.cell_value + self.style.cell_value_selected)

        # Cells hints
        for cell_hint in self.cells_hints:
            cell_hint.setStyleSheet(self.style.cell_hint + self.style.cell_value_selected)

        # Emit a signal to its parent (the grid), in order to unselect the current selected cell
        self.selected_signal.emit()

    def unselect(self):
        """
        Unselects a cell
        """

        self.selected = False
        # Cell value
        self.cell_value.updateStyle()

        # Cells hints
        for cell_hint in self.cells_hints:
            cell_hint.setStyleSheet(self.style.cell_hint)

    def updateValue(self, new_value):
        """
        Updates the cell value or add a hint
        :param new_value: incoming value
        """

        # Cell value
        if self.count() == 1:
            self.cell_value.setValue(new_value)

        # Cells hints
        else:
            if new_value != 0:
                existing_hint = next((cell for cell in self.cells_hints if cell.value == new_value), None)
                if existing_hint is not None:
                    existing_hint.setValue(0)
                else:
                    empty_hint = next((cell for cell in self.cells_hints if cell.value == 0), None)
                    if empty_hint is not None:
                        empty_hint.setValue(new_value)
            else:
                for cell_hint in self.cells_hints:
                    cell_hint.setValue(0)