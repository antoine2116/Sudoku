from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class PopupInfo(QMessageBox):
    def __init__(self, success, message):
        super().__init__()
        self.setFixedSize(80, 120)
        self.setText(message)
        self.setWindowTitle("Information")
        self.setWindowIcon(QIcon("../images/logo_base.png"))

        icon = QMessageBox.Information if success else QMessageBox.Critical
        self.setIcon(icon)

        self.exec_()
