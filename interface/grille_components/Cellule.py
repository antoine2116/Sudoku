from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QGridLayout

from interface.grille_components.CelluleValeur import CelluleValeur
from interface.grille_components.CelluleIndice import CelluleIndice
from interface.tools.theme import Theme

class Cellule(QGridLayout):
    selected = False
    selected_signal = pyqtSignal()

    def __init__(self, cell_data, theme=Theme()):
        super(QGridLayout, self).__init__()
        self.setSpacing(0)
        self.theme = theme
        self.data = cell_data
        self.fixed = self.data["afficher_solution"]
        self.generateComponents()
        self.displayValeur()

    def generateComponents(self):
        if self.fixed:
            self.cell_valeur = CelluleValeur(True, self.data["solution"])
        else:
            self.cell_valeur = CelluleValeur(False, self.data["joueur"])
        self.cell_valeur.selected_signal.connect(self.selectCell)

        self.cells_indices = []

        if not self.fixed:
            cpt = 1
            for i in range(0, 3):
                li = []
                for y in range(0, 3):
                    if i in self.data["indices"]:
                        cell_indice = CelluleIndice(cpt)
                    else:
                        cell_indice = CelluleIndice()
                    cell_indice.selected_signal.connect(self.selectCell)
                    li.append(cell_indice)
                    cpt = cpt + 1
                self.cells_indices.append(li)

    def displayValeur(self):
        self.removeAllWidgets()
        self.addWidget(self.cell_valeur, 0, 0)

    def displayIndices(self):
        if not self.fixed:
            self.removeAllWidgets()
            for i in range(0, 3):
                for y in range(0, 3):
                    self.addWidget(self.cells_indices[i][y], i, y)

    def toggleCellDisplay(self):
        if self.count() == 1 and self.cell_valeur.value == "":
            self.displayIndices()
        else:
            self.displayValeur()

    def removeAllWidgets(self):
        for i in reversed(range(self.count())):
            self.itemAt(i).widget().setParent(None)

    def selectCell(self):
        self.selected = True
        self.cell_valeur.setStyleSheet(self.theme.cellule_valeur + self.theme.cellule_valeur_focused)
        for i in range(0, 3):
            for y in range(0, 3):
                self.cells_indices[i][y].setStyleSheet(self.theme.cellule_indice + self.theme.cellule_indice_focused)
        self.selected_signal.emit()

    def unselect(self):
        self.selected = False
        self.cell_valeur.setStyleSheet(self.theme.cellule_valeur)
        for i in range(0, 3):
            for y in range(0, 3):
                self.cells_indices[i][y].setStyleSheet(self.theme.cellule_indice)

    def updateValue(self, valeur):
        if self.count() == 1:
            self.cell_valeur.setValue(valeur)
        else:
            cpt = 1
            for i in range(0, 3):
                for y in range(0, 3):
                    if str(cpt) == valeur:
                        if self.cells_indices[i][y].text == valeur:
                            self.cells_indices[i][y].setValue("")
                        else:
                            self.cells_indices[i][y].setValue(valeur)
                    cpt = cpt + 1



