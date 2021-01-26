from PyQt5.QtWidgets import QWidget, QGridLayout
from interface.grille_components.Cellule import Cellule
from interface.popups.PopupInfo import PopupInfo
from interface.services.SolveurService import SolveurService
from interface.styles.Dimensions import Dimensions
from interface.styles.Theme import Theme


class Grille(QWidget):
    selected_cell = None
    paused = False

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
        self.solveur = SolveurService(self)

    def initialiseGrille(self):
        for r in range(0, self.divider):
            for c in range(0, self.divider):
                inner_layout = QGridLayout()
                inner_layout.setContentsMargins(0, 0, 0, 0)
                inner_layout.setSpacing(1)
                self.grid_layout.addLayout(inner_layout, r, c)

        for r in range(0, self.n):
            for c in range(0, self.n):
                inner_layout = self.grid_layout.itemAtPosition(r // self.divider, c // self.divider)
                cell = Cellule(self.grille[r][c], self.divider, r, c)
                cell.cell_valeur.value_changed_signal.connect(self.autoComplete)

                cell.selected_signal.connect(self.unselectCell)
                inner_layout.addLayout(cell, r % self.divider, c % self.divider)
                self.cells.append(cell)

    def toggleCellsDisplay(self):
        for cell in [cell for cell in self.cells if not cell.fixed]:
            cell.toggleCellDisplay()

    def unselectCell(self):
        if self.selected_cell is not None:
            self.selected_cell.unselect()
        self.selected_cell = next((cell for cell in self.cells if cell.selected), None)

    def updateCellValue(self, valeur):
        if self.paused:
            PopupInfo(False, "Le jeu est en pause")
        elif self.selected_cell is not None:
            self.selected_cell.updateValue(valeur)

    def pause(self):
        self.paused = not self.paused

    def displayPossibilitesCallback(self):
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        possibilites = self.solveur.getPossibilites(self.selected_cell)
        str_poss = [symbols[s] for s in possibilites]
        PopupInfo(True, "Possiblité dans cette case : " + ", ".join(str_poss))

    def autoComplete(self):
        self.solveur.autoComplete(self.selected_cell)