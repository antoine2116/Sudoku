from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout

from interface.grille_components.CelluleValeur import CelluleValeur
from interface.grille_components.CelluleIndice import CelluleIndice
from interface.styles.Theme import Theme


class Cellule(QGridLayout):
    selected = False
    selected_signal = pyqtSignal()

    def __init__(self, cell_data, divider, r, c, theme=Theme()):
        super(QGridLayout, self).__init__()
        self.setSpacing(0)
        self.theme = theme
        self.cell_data = cell_data
        self.divider = divider
        self.r = r
        self.c = c

        self.fixed = self.cell_data["afficher_solution"] or self.cell_data["verifie"]
        self.verifie = self.cell_data["verifie"]
        self.generateComponents()
        self.displayValeur()

    def generateComponents(self):
        if self.fixed and not self.verifie:
            self.cell_valeur = CelluleValeur(True, self.cell_data["solution"], False)
        elif self.verifie:
            self.cell_valeur = CelluleValeur(True, self.cell_data["joueur"], True)
        else:
            self.cell_valeur = CelluleValeur(False, self.cell_data["joueur"], False)
        self.cell_valeur.selected_signal.connect(self.selectCell)

        self.cells_indices = []
        if not self.fixed:
            cpt = 0
            for r in range(0, 3):
                for c in range(0, 3):
                    if cpt < len(self.cell_data["indices"]):
                        cell_indice = CelluleIndice(cpt + 1)
                    else:
                        cell_indice = CelluleIndice()
                    cell_indice.selected_signal.connect(self.selectCell)
                    self.cells_indices.append(cell_indice)
                    cpt = cpt + 1

    def displayValeur(self):
        self.removeAllWidgets()
        self.addWidget(self.cell_valeur, 0, 0)

    def displayIndices(self):
        if not self.fixed:
            self.removeAllWidgets()
            cpt = 0
            for r in range(0, 3):
                for c in range(0, 3):
                    self.addWidget(self.cells_indices[cpt], r, c)
                    cpt = cpt + 1

    def toggleCellDisplay(self):
        if self.count() == 1 and self.cell_valeur.value == 0:
            self.displayIndices()
        else:
            self.displayValeur()

    def removeAllWidgets(self):
        for i in reversed(range(self.count())):
            self.itemAt(i).widget().setParent(None)

    def selectCell(self):
        self.selected = True
        self.cell_valeur.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_focused)
        for cell_indice in self.cells_indices:
            cell_indice.setStyleSheet(self.theme.cellule_indice + self.theme.cellule_indice_focused)
        self.selected_signal.emit()

    def unselect(self):
        self.selected = False
        self.cell_valeur.updateTextColor()
        for cell_indice in self.cells_indices:
            cell_indice.setStyleSheet(self.theme.cellule_indice)

    def updateValue(self, valeur):
        if self.count() == 1:
            self.cell_valeur.setValue(valeur)
        else:
            existing_indice = next((cell for cell in self.cells_indices if cell.value == valeur), None)
            if existing_indice is not None:
                existing_indice.setValue(0)
            else:
                empty_indice = next((cell for cell in self.cells_indices if cell.value == 0), None)
                if empty_indice is not None:
                    empty_indice.setValue(valeur)




