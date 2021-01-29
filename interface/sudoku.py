import sys
from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu

from interface.popups.PopupDifficulty import PopupDifficulty
from interface.services.GridGeneratorService import GridGeneratorService
from interface.pages.HomeWidget import HomeWidget
from interface.pages.GameWidget import GameWidget
from interface.popups.PopupFileName import PopupFileName
from interface.popups.PopupInfo import PopupInfo
from interface.services.SaveService import SaveService
from interface.styles.Style import Style


class MainWindow(QMainWindow):
    """
    This class is the programm's main window. It contains either the home widget or the game widget
    It connects diffents widgets and services to play the game
    """

    game_widget = None
    save_service = SaveService()
    file_name = ""

    def __init__(self, style=Style()):
        """
        Initializes styles and displays the home widget
        """

        super().__init__()
        self.style = style

        self.setFixedSize(700, 550)
        self.setWindowTitle('Sudoku')
        self.setWindowIcon(QIcon("../images/logo_base.png"))
        self.setStyleSheet(self.style.main_background)

        self.initHome()
        self.initMenu()

    def initHome(self):
        """
        Initializes the home widget then displays it
        """

        self.home_widget = HomeWidget()
        self.setCentralWidget(self.home_widget)
        self.connectHomeControls()

    def connectHomeControls(self):
        """
        Connects the home buttons to their callbacks
        """

        self.home_widget.btn_9x9.clicked.connect(partial(self.newGameCallback, 9))
        self.home_widget.btn_16x16.clicked.connect(partial(self.newGameCallback, 16))
        self.home_widget.btn_load_game.clicked.connect(self.loadGameCallback)

    def initMenu(self):
        """
        Initializes the menu bar.
        Connects each action with its callback
        """

        self.bar = self.menuBar()
        self.bar.setStyleSheet(self.style.menu_bar)

        # Game menu
        game_menu = self.bar.addMenu("Partie")

        home_action = QAction("Accueil", self)
        home_action.triggered.connect(self.displayHomeCallback)
        game_menu.addAction(home_action)

        new_game_menu = QMenu("Nouvelle partie", self)
        new_game_menu.setStyleSheet(self.style.menu_bar)
        game_menu.addMenu(new_game_menu)

        nine_by_nine_action = QAction("9x9", self)
        nine_by_nine_action.triggered.connect(partial(self.newGameCallback, 9))
        new_game_menu.addAction(nine_by_nine_action)

        sixteen_by_sixteen_action = QAction("16x16", self)
        sixteen_by_sixteen_action.triggered.connect(partial(self.newGameCallback, 16))
        new_game_menu.addAction(sixteen_by_sixteen_action)

        save_game_action = QAction("Sauvegarder", self)
        save_game_action.triggered.connect(self.saveGameCallback)
        game_menu.addAction(save_game_action)

        quit_action = QAction("Quitter", self)
        quit_action.triggered.connect(qApp.quit)
        game_menu.addAction(quit_action)

        # Solver menu
        solver_menu = self.bar.addMenu("Solveur")
        solver_menu.setStyleSheet(self.style.menu_bar)

        check_grid = QAction("Vérifier la grille", self)
        check_grid.triggered.connect(self.checkGridCallback)
        solver_menu.addAction(check_grid)

        brute_foce = QAction("Brute Force", self)
        brute_foce.triggered.connect(self.bruteForceCallback)
        solver_menu.addAction(brute_foce)

        back_track = QAction("Back Track", self)
        back_track.triggered.connect(self.backTrackCallback)
        solver_menu.addAction(back_track)

        self.bar.setVisible(False)

    def displayHomeCallback(self):
        """
        Returns to the home page
        """

        self.setFixedSize(700, 550)
        self.home_widget = HomeWidget()
        self.connectHomeControls()
        self.setCentralWidget(self.home_widget)
        self.bar.setVisible(False)

    def newGameCallback(self, n):
        """
        Starts a new game
        :param n: 9 or 16 (starts either a 9x9 or 16x16 game)
        """

        popup_difficulty = PopupDifficulty()
        if popup_difficulty.exec_() == QtWidgets.QDialog.Accepted:
            generator = GridGeneratorService(n)
            data = generator.generate(popup_difficulty.textValue())
            self.setFixedSize(self.style.window_w[str(n)], self.style.window_h[str(n)])
            self.startGame(data)
        else:
            return

    def saveGameCallback(self):
        """
        Saves the game
        """

        # If it's a new games, asks for the name
        if self.file_name == "":
            popup_file_name = PopupFileName()
            if popup_file_name.exec_() == QtWidgets.QDialog.Accepted:
                self.file_name = popup_file_name.textValue()
            else:
                return

        # Then, save it
        try:
            self.save_service.saveData(self.file_name, self.game_widget)
            self.file_name = ""
            PopupInfo(True, "Partie sauvegardée avec succès")
        except EnvironmentError:
            PopupInfo(False, "Une erreur est survenue lors de la sauvegarde")

    def loadGameCallback(self):
        """
        Load data from the chosen file by the combo box
        """

        self.file_name = self.home_widget.combo_files.currentText()
        if self.file_name == "":
            PopupInfo(False, "Aucun fichier sélectionné")
        else:
            data = self.save_service.getData(self.file_name)
            self.startGame(data)

    def checkGridCallback(self):
        """
        Check each cell in the grid then display the number of valid cells
        """

        success, fails = self.game_widget.grid.solver.checkGrid()
        PopupInfo(True, "Résultat : %d succès et %d erreurs" % (success, fails))

    def bruteForceCallback(self):
        """
        Solves the grid using the brute force agorithm
        """

        self.game_widget.grid.solver.loadGridData()
        self.game_widget.grid.solver.solveByBruteForce()

    def backTrackCallback(self):
        """
        Solves the grid using the back track agorithm
        """

        self.game_widget.grid.solver.loadGridData()
        self.game_widget.grid.solver.solveByBackTracking()

    def startGame(self, data):
        """
        Starts the game
        """

        if self.game_widget is not None:
            del self.game_widget

        self.game_widget = GameWidget(data)
        self.setCentralWidget(self.game_widget)
        self.bar.setVisible(True)


def main():
    """
    Entry point
    """

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
