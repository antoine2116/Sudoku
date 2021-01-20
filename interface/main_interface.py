import sys
import json

from PyQt5.QtWidgets import QApplication

from interface.GenerateurGrille import GenerateurGrille
from interface.MainWindow import MainWindow


def main():
    with open("storage/grille.json", "r") as file:
        m = json.load(file)

    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
