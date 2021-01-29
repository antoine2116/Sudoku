from os import listdir
from os.path import isfile, join

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QGridLayout, QPushButton, QComboBox

from interface.styles.Style import Style


class HomeWidget(QWidget):
    """
    Entry point of the suduku.
    Two main choices : start a new game or resume a previous one
    """

    def __init__(self, style=Style()):
        """
        Creates all the components (logo, label, buttons and combo files)
        :param style: styling object
        """

        super().__init__()
        vbox_layout = QVBoxLayout()
        self.setLayout(vbox_layout)

        logo = QLabel()
        logo.setPixmap(QPixmap("../images/logo_smaller.png"))
        logo.setStyleSheet(style.home_logo)
        logo.setAlignment(Qt.AlignCenter)
        vbox_layout.addWidget(logo)

        titre = QLabel()
        titre.setText("SUDOKU")
        titre.setStyleSheet(style.home_title)
        titre.setAlignment(Qt.AlignCenter)
        vbox_layout.addWidget(titre)

        grid_layout = QGridLayout()
        vbox_layout.addLayout(grid_layout)
        new_game_label = QLabel()
        new_game_label.setText("Nouvelle Partie")
        new_game_label.setStyleSheet(style.home_label)
        grid_layout.addWidget(new_game_label, 0, 0)

        self.btn_9x9 = QPushButton()
        self.btn_9x9.setStyleSheet(style.home_button)
        self.btn_9x9.setText("9 x 9")
        grid_layout.addWidget(self.btn_9x9, 0, 1)

        self.btn_16x16 = QPushButton()
        self.btn_16x16.setStyleSheet(style.home_button)
        self.btn_16x16.setText("16 x 16")
        grid_layout.addWidget(self.btn_16x16, 0, 2)

        load_game_label = QLabel()
        load_game_label.setText("Charger une partie")
        load_game_label.setStyleSheet(style.home_label)
        grid_layout.addWidget(load_game_label, 1, 0)

        self.combo_files = QComboBox()
        self.combo_files.setStyleSheet(style.combo_file)
        # Gets the all the stored games
        files = [f.replace(".json", "") for f in listdir("./storage/") if isfile(join("./storage/", f))]
        self.combo_files.addItems(files)
        grid_layout.addWidget(self.combo_files, 1, 1)

        self.btn_load_game = QPushButton()
        self.btn_load_game.setText("Ok")
        self.btn_load_game.setStyleSheet(style.home_button)
        grid_layout.addWidget(self.btn_load_game, 1, 2)




