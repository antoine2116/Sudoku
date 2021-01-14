from interface.controls_components.Button import Button
from interface.tools.theme import Theme


class ButtonValeur(Button):
    def __init__(self, valeur, theme=Theme()):
        super().__init__()
        self.valeur = (str(valeur))
        self.setText(self.valeur)
