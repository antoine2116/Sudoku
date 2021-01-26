from interface.controls_components.Button import Button


class ButtonIndices(Button):
    isClicked = False

    def __init__(self):
        super().__init__()
        self.setText("Aff. Indices")
        self.setStyleSheet(self.theme.button + self.theme.button_font_smaller)

    def toggleClicked(self):
        if self.isClicked:
            self.isClicked = False
            self.setStyleSheet(self.theme.button + self.theme.button_font_smaller)
        else:
            self.isClicked = True
            self.setStyleSheet(self.theme.button + self.theme.button_font_smaller + self.theme.button_indice_selected)

