from PyQt5.QtWidgets import QMessageBox


class PopupInfo(QMessageBox):
    def __init__(self, success, message):
        super().__init__()
        self.setFixedSize(80, 120)
        self.setText(message)
        self.setWindowTitle("Information")

        icon = QMessageBox.Information if success else QMessageBox.Critical
        self.setIcon(icon)
        self.exec_()
