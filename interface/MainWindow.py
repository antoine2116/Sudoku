from PyQt5.QtWidgets import QMainWindow

from interface.MainWidget import MainWidget
from interface.tools.theme import Theme


class MainWindow(QMainWindow):
    def __init__(self, matrix, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.setFixedSize(900, 600)
        self.setWindowTitle('ZEBI LE SUDOKU')
        self.setStyleSheet(self.theme.main_background)

        self.main_widget = MainWidget(matrix)
        self.setCentralWidget(self.main_widget)

        self.initMenu()

    def initMenu(self):
        bar = self.menuBar()
        bar.setStyleSheet(self.theme.menu_bar)

        partie = bar.addMenu("Partie")
        partie.addAction("Nouvelle Partie")
        partie.addAction("Sauvegarder")
        partie.addAction("Quitter")

        resoudre = bar.addMenu("Résoudre")
        resoudre.addAction("Brute Force")
        resoudre.addAction("Back Track")


