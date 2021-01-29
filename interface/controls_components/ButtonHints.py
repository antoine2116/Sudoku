from interface.controls_components.Button import Button


class ButtonHints(Button):
    """
    Togglable button.
    Enable: display hints
    Disabled : display value
    """

    enabled = False

    def __init__(self):
        """
        Initialize styling and text
        """

        super().__init__()

        # Styling
        self.setText("Aff. Indices")
        self.setStyleSheet(self.style.controls_button + self.style.controls_button_smaller)

    def toggleClicked(self):
        """
        Enable or disable the button depending of the button's status
        """

        if self.enabled:
            self.enabled = False
            self.setStyleSheet(self.style.controls_button + self.style.controls_button_smaller)
        else:
            self.enabled = True
            self.setStyleSheet(self.style.controls_button + self.style.controls_button_smaller + self.style.controls_button_enabled)
