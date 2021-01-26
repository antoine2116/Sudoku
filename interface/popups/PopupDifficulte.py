from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog

from interface.styles.Theme import Theme


class PopupDifficulte(QInputDialog):
    def __init__(self, theme=Theme()):
        super().__init__()
        self.setLabelText("Choisir la difficulté")
        self.setWindowIcon(QIcon("../images/logo_base.png"))
        self.setWindowTitle("Difficulté")
        self.setCancelButtonText("Annuler")
        self.setComboBoxItems(("Normal", "Difficile"))
        self.setStyleSheet(theme.popup_file_name)
