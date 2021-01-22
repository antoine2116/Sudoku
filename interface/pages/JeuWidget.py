from PyQt5.QtWidgets import QWidget, QHBoxLayout, QMainWindow

from interface.controls_components.Controls import Controls
from interface.grille_components.Grille import Grille
from interface.styles.Theme import Theme


class JeuWidget(QWidget):
    def __init__(self, data, theme=Theme()):
        super().__init__()
        self.theme = theme

        self.box_layout = QHBoxLayout()
        self.setLayout(self.box_layout)

        self.controls = Controls(data["divider"], data["timer"])
        self.grille = Grille(data)

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






