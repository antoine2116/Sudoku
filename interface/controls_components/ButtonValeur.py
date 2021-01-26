from interface.controls_components.Button import Button


class ButtonValeur(Button):
    def __init__(self, valeur):
        super().__init__()
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        self.setText(symbols[valeur])
        self.valeur = valeur