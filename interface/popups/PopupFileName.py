from PyQt5.QtWidgets import QInputDialog

from interface.styles.Theme import Theme


class PopupFileName(QInputDialog):
    def __init__(self, theme=Theme()):
        super().__init__()
        self.setLabelText("Entrer un nom de sauvegarde")
        self.setWindowTitle("Sauvegarder")
        self.setTextValue("Sauvegarde1")
        self.setStyleSheet(theme.popup_file_name)
