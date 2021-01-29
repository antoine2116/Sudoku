from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QMessageBox


class PopupInfo(QMessageBox):
    """
    Dialog informing the user
    """

    def __init__(self, success, message):
        """
        Initializes style and content
        :param success:(bool) type of the information
        :param message:(str) message to display
        """

        super().__init__()

        # Style
        self.setFixedSize(80, 120)
        self.setWindowTitle("Information")
        self.setWindowIcon(QIcon("../images/logo_base.png"))

        # Icon
        icon = QMessageBox.Information if success else QMessageBox.Critical
        self.setIcon(icon)

        # Text
        self.setText(message)

        # Open
        self.exec_()
