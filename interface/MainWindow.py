from functools import partial

from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QMenu

from interface.GenerateurGrille import GenerateurGrille
from interface.pages.AccueilWidget import AccueilWidget
from interface.pages.JeuWidget import JeuWidget
from interface.tools.theme import Theme


class MainWindow(QMainWindow):
    def __init__(self, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.setFixedSize(900, 600)
        self.setWindowTitle('Soduku')
        self.setStyleSheet(self.theme.main_background)

        self.accueil_widget = AccueilWidget()
        self.setCentralWidget(self.accueil_widget)
        self.initAccueilEvents()

    def initAccueilEvents(self):
        self.accueil_widget.btn_9x9.clicked.connect(partial(self.nouvellePartieCallback, 9))
        #self.accueil_widget.btn_16x16.clicked.connect(partial(self.nouvellePartieCallback, 16))

    def initMenu(self):
        bar = self.menuBar()
        bar.setStyleSheet(self.theme.menu_bar)

        # Menu Partie
        partie_menu = bar.addMenu("Partie")
        nouvelle_partie_menu = QMenu("Nouvelle partie", self)
        nouvelle_partie_menu.setStyleSheet(self.theme.menu_bar)

        partie_menu.addMenu(nouvelle_partie_menu)
        neufparneuf_action = QAction("9x9", self)
        neufparneuf_action.triggered.connect(self.nouvellePartieCallback)
        nouvelle_partie_menu.addAction(neufparneuf_action)
        seizparseize_action = QAction("16x16", self)
        seizparseize_action.triggered.connect(self.nouvellePartieCallback)
        nouvelle_partie_menu.addAction(seizparseize_action)

        sauvegarder_action = QAction("Sauvegarder", self)
        sauvegarder_action.triggered.connect(self.sauvegarderCallback)
        partie_menu.addAction(sauvegarder_action)

        quitter_action = QAction("Quitter", self)
        quitter_action.triggered.connect(qApp.quit)
        partie_menu.addAction(quitter_action)

        # Menu resoudre
        resoudre = bar.addMenu("Résoudre")
        resoudre.addAction("Brute Force")
        resoudre.addAction("Back Track")

    def nouvellePartieCallback(self, n):
        generateur = GenerateurGrille(n)
        grille = generateur.generate()
        self.startJeuWidget(grille)

    def sauvegarderCallback(self):
        print("aaaa")

    def startJeuWidget(self, grille):
        self.jeu_widget = JeuWidget(grille)
        self.setCentralWidget(self.jeu_widget)
        self.initMenu()
