from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog

from interface.styles.Style import Style


class PopupFileName(QInputDialog):
    """
    Dialog allowing the user to enter a name for his save
    """

    def __init__(self, style=Style()):
        """
        Initializes style and content
        :param style: styling object
        """

        super().__init__()

        self.setStyleSheet(style.popup)
        self.setWindowIcon(QIcon("../images/logo_base.png"))
        self.setWindowTitle("Sauvegarder")

        self.setLabelText("Entrer un nom de sauvegarde")
        self.setCancelButtonText("Annuler")
