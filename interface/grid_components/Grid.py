from PyQt5.QtWidgets import QWidget, QGridLayout

from interface.grid_components.Cell import Cell
from interface.popups.PopupInfo import PopupInfo
from interface.services.SolverService import SolverService
from interface.styles.Style import Style


class Grid(QWidget):
    """
    Central widget that contains all the sudoku
    """

    selected_cell = None
    paused = False

    def __init__(self, data, style=Style()):
        """
        Initializes general styling and creates the cells
        :param data: JSON data from the save or the generator
        :param style: styling object
        """

        super().__init__()

        # Grid properties
        self.n = data["n"]
        self.divider = data["divider"]
        self.grid = data["grid"]

        # Style and main layout
        self.style = style
        self.setFixedSize(self.style.grid_side[str(self.n)], self.style.grid_side[str(self.n)])
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)
        self.setLayout(self.grid_layout)

        self.initGrid()

        self.solver = SolverService(self)

    def initGrid(self):
        """
        Creates the sudoku cells
        """
        self.cells = []

        # Generate several grids layout acting as sudoku block
        for r in range(0, self.divider):
            for c in range(0, self.divider):
                inner_layout = QGridLayout()
                inner_layout.setContentsMargins(0, 0, 0, 0)
                inner_layout.setSpacing(1)
                self.grid_layout.addLayout(inner_layout, r, c)

        # Fill the blocks with cells
        for r in range(0, self.n):
            for c in range(0, self.n):
                inner_layout = self.grid_layout.itemAtPosition(r // self.divider, c // self.divider)
                cell = Cell(self.grid[r][c], self.divider, r, c)
                cell.cell_value.value_changed_signal.connect(self.autoComplete)

                cell.selected_signal.connect(self.unselectCell)
                inner_layout.addLayout(cell, r % self.divider, c % self.divider)
                self.cells.append(cell)

    def toggleCellsDisplay(self):
        """
        Toggles each cell display in order to display either values or hints
        """

        for cell in [cell for cell in self.cells if not cell.cell_value.fixed]:
            cell.toggleCellDisplay()

    def unselectCell(self):
        """
        Unselected the current selected cell
        """

        if self.selected_cell is not None:
            self.selected_cell.unselect()
        self.selected_cell = next((cell for cell in self.cells if cell.selected), None)

    def updateCellValue(self, new_value):
        """
        Updates the cell value or add a hint
        :param new_value: incoming value
        """

        if self.paused:
            PopupInfo(False, "Le jeu est en pause")
        elif self.selected_cell is not None:
            self.selected_cell.updateValue(new_value)

    def pause(self):
        """
        Pauses the game
        """

        self.paused = not self.paused

    def displayPossibilitiesCallback(self):
        """
        Opens a popup that displays all possibles values in a cell (triggered by the possibilites button)
        """

        self.solver.loadGridData()
        possibilities = self.solver.getPossibilities(self.selected_cell.r, self.selected_cell.c)
        if not possibilities:
            message = "Aucune possibilité trouvée"
        else:
            symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
            str_poss = [symbols[s] for s in possibilities]
            message = "Possiblités dans cette cellule : " + ", ".join(str_poss)
        PopupInfo(True, message)

    def autoComplete(self):
        """
        Triggered when a value is changed
        """

        self.solver.autoComplete(self.selected_cell)
