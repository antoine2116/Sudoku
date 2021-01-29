from interface.controls_components.Button import Button


class ButtonValue(Button):
    """"
    Button of the numeric keypad
    """

    def __init__(self, value):
        """
        :param value: (int) from 1 to 16
        """

        super().__init__()

        # Initialize text
        symbols = ["", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G"]
        self.setText(symbols[value])
        self.value = value
