from PyQt5.QtWidgets import QWidget, QGridLayout
from interface.grille_components.Cellule import Cellule
from interface.tools.theme import Theme
import math

class Grille(QWidget):
    def __init__(self, matrix, theme=Theme()):
        super().__init__()

        self.matrix = matrix
        self.n = len(self.matrix)
        self.divider = math.isqrt(self.n)

        self.setFixedSize(600, 600)
        self.theme = theme

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(1)
        self.setLayout(self.grid_layout)

        self.cells = []
        self.initialise_grille()

    def initialise_grille(self):
        for i in range(0, self.divider):
            for y in range(0, self.divider):
                inner_layout = QGridLayout()
                inner_layout.setContentsMargins(0, 0, 0, 0)
                inner_layout.setSpacing(1)
                self.grid_layout.addLayout(inner_layout, i, y)

        for i in range(0, self.n):
            for y in range(0, self.n):
                inner_layout = self.grid_layout.itemAtPosition(i // self.divider, y // self.divider)
                cell = Cellule(self.matrix[i][y])
                inner_layout.addLayout(cell, i % self.divider, y % self.divider)
                self.cells.append(cell)


