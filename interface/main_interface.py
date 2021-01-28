import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication

from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu

from interface.popups.PopupDifficulte import PopupDifficulte
from interface.services.GenerateurGrilleService import GenerateurGrilleService
from interface.pages.AccueilWidget import AccueilWidget
from interface.pages.JeuWidget import JeuWidget
from interface.popups.PopupFileName import PopupFileName
from interface.popups.PopupInfo import PopupInfo
from interface.services.SauvegardeService import SauvegardeService
from interface.styles.Dimensions import Dimensions
from interface.styles.Theme import Theme


class MainWindow(QMainWindow):
    save_service = SauvegardeService()
    file_name = ""

    def __init__(self, theme=Theme(), dim=Dimensions()):
        super().__init__()
        self.theme = theme
        self.dim = dim
        self.setFixedSize(700, 550)
        self.setWindowTitle('Sudoku')
        self.setWindowIcon(QIcon("../images/logo_base.png"))
        self.setStyleSheet(self.theme.main_background)

        self.initAccueil()
        self.initMenu()

    def initAccueil(self):
        self.accueil_widget = AccueilWidget()
        self.setCentralWidget(self.accueil_widget)
        self.connectControlsAccueil()

    def connectControlsAccueil(self):
        self.accueil_widget.btn_9x9.clicked.connect(partial(self.nouvellePartieCallback, 9))
        self.accueil_widget.btn_16x16.clicked.connect(partial(self.nouvellePartieCallback, 16))
        self.accueil_widget.btn_charger.clicked.connect(self.chargerPartieCallback)

    def initMenu(self):
        self.bar = self.menuBar()
        self.bar.setStyleSheet(self.theme.menu_bar)

        # Menu Partie
        partie_menu = self.bar.addMenu("Partie")

        accueil_action = QAction("Accueil", self)
        accueil_action.triggered.connect(self.accueilCallback)
        partie_menu.addAction(accueil_action)

        nouvelle_partie_menu = QMenu("Nouvelle partie", self)
        nouvelle_partie_menu.setStyleSheet(self.theme.menu_bar)
        partie_menu.addMenu(nouvelle_partie_menu)

        neufparneuf_action = QAction("9x9", self)
        neufparneuf_action.triggered.connect(partial(self.nouvellePartieCallback, 9))
        nouvelle_partie_menu.addAction(neufparneuf_action)
        seizparseize_action = QAction("16x16", self)
        seizparseize_action.triggered.connect(partial(self.nouvellePartieCallback, 16))
        nouvelle_partie_menu.addAction(seizparseize_action)

        sauvegarder_action = QAction("Sauvegarder", self)
        sauvegarder_action.triggered.connect(self.sauvegarderCallback)
        partie_menu.addAction(sauvegarder_action)

        quitter_action = QAction("Quitter", self)
        quitter_action.triggered.connect(qApp.quit)
        partie_menu.addAction(quitter_action)

        # Menu resoudre
        solver_menu = self.bar.addMenu("Solveur")
        solver_menu.setStyleSheet(self.theme.menu_bar)

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

    def accueilCallback(self):
        self.setFixedSize(700, 550)
        self.accueil_widget = AccueilWidget()
        self.connectControlsAccueil()
        self.setCentralWidget(self.accueil_widget)
        self.bar.setVisible(False)

    def nouvellePartieCallback(self, n):
        popup_difficulte = PopupDifficulte()
        if popup_difficulte.exec_() == QtWidgets.QDialog.Accepted:
            generateur = GenerateurGrilleService(n)
            data = generateur.generate(popup_difficulte.textValue())
            self.setFixedSize(self.dim.window_w[str(n)], self.dim.window_h[str(n)])
            self.startJeuWidget(data)
        else:
            return

    def sauvegarderCallback(self):
        if self.file_name == "":
            popup_file_name = PopupFileName()
            if popup_file_name.exec_() == QtWidgets.QDialog.Accepted:
                self.file_name = popup_file_name.textValue()
            else:
                return
        try:
            self.save_service.saveData(self.file_name, self.jeu_widget)
            self.file_name = ""
            PopupInfo(True, "Partie sauvegardée avec succès")
        except EnvironmentError:
            PopupInfo(False, "Une erreur est survenue lors de la sauvegarde")

    def chargerPartieCallback(self):
        self.file_name = self.accueil_widget.combo_files.currentText()
        if self.file_name == "":
            PopupInfo(False, "Aucun fichier sélectionné")
        else:
            data = self.save_service.getData(self.file_name)
            self.startJeuWidget(data)

    def checkGridCallback(self):
        success, fails = self.jeu_widget.grille.solveur.checkGrille()
        PopupInfo(True, "Résultat : %d succès et %d erreurs" % (success, fails))

    def bruteForceCallback(self):
        self.jeu_widget.grille.solveur.loadGrilleData()
        self.jeu_widget.grille.solveur.solveByBruteForce()

    def backTrackCallback(self):
        self.jeu_widget.grille.solveur.loadGrilleData()
        self.jeu_widget.grille.solveur.solveByBackTracking()

    def startJeuWidget(self, data):
        self.jeu_widget = JeuWidget(data)
        self.setCentralWidget(self.jeu_widget)
        self.bar.setVisible(True)


def main():
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
