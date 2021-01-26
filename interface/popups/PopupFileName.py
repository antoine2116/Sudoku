from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QInputDialog

from interface.styles.Theme import Theme


class PopupFileName(QInputDialog):
    def __init__(self, theme=Theme()):
        super().__init__()
        self.setLabelText("Entrer un nom de sauvegarde")
        self.setWindowIcon(QIcon("../images/logo_base.png"))
        self.setWindowTitle("Sauvegarder")
        self.setCancelButtonText("Annuler")
        self.setTextValue("Sauvegarde1")
        self.setStyleSheet(theme.popup_file_name)
