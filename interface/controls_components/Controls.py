from PyQt5.QtWidgets import QWidget, QGridLayout, QVBoxLayout, QHBoxLayout, QStyle

from interface.controls_components.Button import Button
from interface.controls_components.ButtonHints import ButtonHints
from interface.controls_components.ButtonValue import ButtonValue
from interface.controls_components.Timer import Timer
from interface.styles.Style import Style


class Controls(QWidget):
    def __init__(self, n, timer_data, style=Style()):
        """
        Initialize all the components of the controls panel

        :param n: size of the grid (9 or 16)
        :param timer_data: timer value from JSON
        :param style: styling object
        """

        # Styling and main layout
        super().__init__()
        self.styles = style
        self.setFixedHeight(400)
        v_boxlayout = QVBoxLayout()
        self.setLayout(v_boxlayout)

        # Timer
        self.timer = Timer(timer_data)
        v_boxlayout.addWidget(self.timer)

        # Button Delete
        self.btn_delete = Button()
        self.btn_delete.setStyleSheet(self.styles.controls_button + self.styles.controls_button_delete)
        self.btn_delete.setIcon(self.style().standardIcon(getattr(QStyle, "SP_TitleBarCloseButton")))
        v_boxlayout.addWidget(self.btn_delete)

        # Nurmeric keypad
        grid_layout = QGridLayout()
        v_boxlayout.addLayout(grid_layout)
        self.btns_value = []
        i = 1
        for r in range(1, n + 1):
            for c in range(1, n + 1):
                button = ButtonValue(i)
                self.btns_value.append(button)
                grid_layout.addWidget(button, r, c)
                i = i + 1

        h_boxlayout = QHBoxLayout()
        v_boxlayout.addLayout(h_boxlayout)

        # Button hints
        self.btn_hints = ButtonHints()
        h_boxlayout.addWidget(self.btn_hints)

        # Button possiblities
        self.btn_possibilities = Button()
        self.btn_possibilities.setText("Possibilités")
        self.btn_possibilities.setStyleSheet(self.styles.controls_button + self.styles.controls_button_smaller)
        h_boxlayout.addWidget(self.btn_possibilities)


