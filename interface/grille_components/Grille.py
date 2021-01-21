from PyQt5.QtWidgets import QWidget, QGridLayout
from interface.grille_components.Cellule import Cellule
from interface.tools.Dimensions import Dimensions
from interface.tools.theme import Theme
import math

class Grille(QWidget):
    selected_cell = None

    def __init__(self, data, theme=Theme(), dim=Dimensions()):
        super().__init__()

        self.n = data["n"]
        self.divider = data["divider"]
        self.grille = data["grille"]

        self.setFixedSize(dim.grille[str(self.n)], dim.grille[str(self.n)])
        self.theme = theme

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)
        self.setLayout(self.grid_layout)

        self.cells = []
        self.initialiseGrille()

    def initialiseGrille(self):
        for i in range(0, self.divider):
            for y in range(0, self.divider):
                inner_layout = QGridLayout()
                inner_layout.setContentsMargins(0, 0, 0, 0)
                inner_layout.setSpacing(1)
                self.grid_layout.addLayout(inner_layout, i, y)

        for i in range(0, self.n):
            for y in range(0, self.n):
                inner_layout = self.grid_layout.itemAtPosition(i // self.divider, y // self.divider)
                cell = Cellule(self.grille[i][y], self.divider)
                cell.selected_signal.connect(self.unselectCell)
                inner_layout.addLayout(cell, i % self.divider, y % self.divider)
                self.cells.append(cell)

    def toggleCellsDisplay(self):
        for cell in self.cells:
            cell.toggleCellDisplay()

    def unselectCell(self):
        if self.selected_cell is not None:
            self.selected_cell.unselect()

        self.selected_cell = next((cell for cell in self.cells if cell.selected), None)

    def updateCellValue(self, valeur):
        if self.selected_cell is not None:
            self.selected_cell.updateValue(int(valeur))



