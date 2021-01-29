from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog

from interface.styles.Style import Style


class PopupDifficulty(QInputDialog):
    """
    Dialog allowing the user to choose the game diffuclty
    """

    def __init__(self, style=Style()):
        """
        Initializes style and content
        :param style: styling object
        """

        super().__init__()

        self.setStyleSheet(style.popup)

        self.setWindowIcon(QIcon("../images/logo_base.png"))
        self.setWindowTitle("Difficulté")

        self.setLabelText("Choisir la difficulté")
        self.setComboBoxItems(("Normal", "Difficile"))
        self.setCancelButtonText("Annuler")
