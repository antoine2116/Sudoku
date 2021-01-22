from os import listdir
from os.path import isfile, join
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QComboBox

from interface.styles.Theme import Theme


class AccueilWidget(QWidget):
    def __init__(self, theme=Theme()):
        super().__init__()
        vbox_layout = QVBoxLayout()
        self.setLayout(vbox_layout)

        titre = QLabel()
        titre.setText("SODUKU")
        titre.setStyleSheet(theme.accueil_titre)
        titre.setAlignment(Qt.AlignCenter)
        vbox_layout.addWidget(titre)

        grid_layout = QGridLayout()
        vbox_layout.addLayout(grid_layout)
        nouvelle_partie_label = QLabel()
        nouvelle_partie_label.setText("Nouvelle Partie")
        nouvelle_partie_label.setStyleSheet(theme.accueil_label)
        grid_layout.addWidget(nouvelle_partie_label, 0, 0)

        self.btn_9x9 = QPushButton()
        self.btn_9x9.setStyleSheet(theme.nouvelle_partie_button)
        self.btn_9x9.setText("9 x 9")
        grid_layout.addWidget(self.btn_9x9, 0, 1)

        self.btn_16x16 = QPushButton()
        self.btn_16x16.setStyleSheet(theme.nouvelle_partie_button)
        self.btn_16x16.setText("16 x 16")
        grid_layout.addWidget(self.btn_16x16, 0, 2)

        charger_partie = QLabel()
        charger_partie.setText("Charger une partie")
        charger_partie.setStyleSheet(theme.accueil_label)
        grid_layout.addWidget(charger_partie, 1, 0)

        self.combo_files = QComboBox()
        self.combo_files.setStyleSheet(theme.combo_files)
        files = [f.replace(".json", "") for f in listdir("./storage/") if isfile(join("./storage/", f))]
        self.combo_files.addItems(files)
        grid_layout.addWidget(self.combo_files, 1, 1)

        self.btn_charger = QPushButton()
        self.btn_charger.setText("Ok")
        self.btn_charger.setStyleSheet(theme.nouvelle_partie_button)
        grid_layout.addWidget(self.btn_charger, 1, 2)




