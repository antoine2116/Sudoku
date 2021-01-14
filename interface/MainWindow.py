from PyQt5.QtWidgets import QWidget, QHBoxLayout

from interface.controls_components.Controls import Controls
from interface.grille_components.Grille import Grille
from interface.tools.theme import Theme


class MainWindow(QWidget):
    def __init__(self, matrix, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.setStyleSheet(self.theme.main_background)
        self.setFixedSize(900, 600)
        self.setWindowTitle('ZEBI LE SUDOKU')

        self.box_layout = QHBoxLayout()
        self.setLayout(self.box_layout)

        self.controls = Controls()
        self.grille = Grille(matrix)

        self.box_layout.addWidget(self.grille)
        self.box_layout.addWidget(self.controls)

        self.connectControls()

    def connectControls(self):
        # Button d'affichage des indices
        self.controls.btn_aff_indice.clicked.connect(self.grille.toggleCellsDisplay)
        self.controls.btn_aff_indice.clicked.connect(self.controls.btn_aff_indice.toggleClicked)

        # Pavé numérique
        for button_valeur in self.controls.btns_numero:
            button_valeur.clicked.connect(
                lambda ignore, x=button_valeur.valeur: self.grille.updateCellValue(str(x)))






