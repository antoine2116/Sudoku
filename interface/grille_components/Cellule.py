from PyQt5.QtWidgets import QGridLayout

from interface.grille_components.CelluleValeur import CelluleValeur
from interface.grille_components.CelluleIndice import CelluleIndice
from interface.tools.theme import Theme

class Cellule(QGridLayout):
    def __init__(self, cell_data, theme=Theme()):
        super(QGridLayout, self).__init__()
        self.setSpacing(0)
        self.data = cell_data

        if len(self.data["indices"]) > 0:
            self.generateIndices()
        else:
            self.displayValeur()

    def generateIndices(self):
        i = 0
        for x in range(0, 3):
            for y in range(0, 3):
                if i in self.data["indices"]:
                    self.addWidget(CelluleIndice(i), x, y)
                else:
                    self.addWidget(CelluleIndice(0), x, y)
                i = i + 1


    def displayValeur(self):
        if self.data["afficher_solution"]:
            self.addWidget(CelluleValeur(self.data["solution"]), 0, 0)
        else:
            self.addWidget(CelluleValeur(0), 0, 0)
