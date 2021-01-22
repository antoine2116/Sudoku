import sys

from PyQt5.QtWidgets import QApplication

from functools import partial

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu

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
        self.setWindowTitle('Soduku')
        self.setStyleSheet(self.theme.main_background)

        self.initAccueil()
        self.initMenu()

    def initAccueil(self):
        self.accueil_widget = AccueilWidget()
        self.setCentralWidget(self.accueil_widget)
        self.accueil_widget.btn_9x9.clicked.connect(partial(self.nouvellePartieCallback, 9))
        self.accueil_widget.btn_16x16.clicked.connect(partial(self.nouvellePartieCallback, 16))
        self.accueil_widget.btn_charger.clicked.connect(self.chargerPartieCallback)

    def initMenu(self):
        self.bar = self.menuBar()
        self.bar.setStyleSheet(self.theme.menu_bar)

        # Menu Partie
        partie_menu = self.bar.addMenu("Partie")

        accueil_action = QAction("Accueil", self)
        accueil_action.triggered.connect(self.initAccueil)
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
        resoudre = self.bar.addMenu("Résoudre")
        resoudre.addAction("Brute Force")
        resoudre.addAction("Back Track")

        self.bar.setVisible(False)

    def accueilCallback(self):
        self.accueil_widget = AccueilWidget()
        self.setCentralWidget(self.accueil_widget)
        self.bar.setVisible(False)

    def nouvellePartieCallback(self, n):
        generateur = GenerateurGrilleService(n)
        data = generateur.generate()
        self.setFixedSize(self.dim.window_w[str(n)], self.dim.window_h[str(n)])
        self.startJeuWidget(data)

    def sauvegarderCallback(self):
        if self.file_name == "":
            popup_file_name = PopupFileName()
            if popup_file_name.exec_() == QtWidgets.QDialog.Accepted:
                self.file_name = popup_file_name.textValue()
            else:
                return
        try:
            self.save_service.saveData(self.file_name, self.jeu_widget)
            popup = PopupInfo(True, "Partie sauvegardée avec succès")
        except EnvironmentError:
            popup = PopupInfo(False, "Une erreur est survenue lors de la sauvegarde")

    def chargerPartieCallback(self):
        self.file_name = self.accueil_widget.combo_files.currentText()
        if self.file_name == "":
            popup = PopupInfo(False, "Aucun fichier sélectionné")
        else:
            data = self.save_service.getData(self.file_name)
            self.startJeuWidget(data)

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
