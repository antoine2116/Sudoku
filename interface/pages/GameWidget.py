from functools import partial

from PyQt5.QtWidgets import QWidget, QHBoxLayout

from interface.controls_components.Controls import Controls
from interface.grid_components.Grid import Grid
from interface.styles.Style import Style


class GameWidget(QWidget):
    """
    Contains the sudoku grid and the control panel
    """
    def __init__(self, data, style=Style()):
        """
        Initializes styles and create its two components : the grid and the controls
        :param data: JSON data from the save or the generator
        :param style: styling object
        """

        super().__init__()

        # Styling and main layout
        self.style = style
        self.box_layout = QHBoxLayout()
        self.setLayout(self.box_layout)

        # Components
        self.controls = Controls(data["divider"], data["timer"])
        self.grid = Grid(data)

        # Adding components to the main layout
        self.box_layout.addWidget(self.grid)
        self.box_layout.addWidget(self.controls)

        self.connectControls()

    def connectControls(self):
        """
        Connects the buttons of the control panel to their callbacks declared in the grid class
        """

        # Button delete
        self.controls.btn_delete.clicked.connect(partial(self.grid.updateCellValue, 0))

        # Numeric keypad
        for btn_value in self.controls.btns_value:
            btn_value.clicked.connect(
                lambda ignore, x=btn_value.value: self.grid.updateCellValue(x))

        # Bouton pause
        self.controls.timer.button.clicked.connect(self.grid.pause)

        # Button possibilites
        self.controls.btn_possibilities.clicked.connect(self.grid.displayPossibilitiesCallback)

        # Button hints
        self.controls.btn_hints.clicked.connect(self.grid.toggleCellsDisplay)
        self.controls.btn_hints.clicked.connect(self.controls.btn_hints.toggleClicked)
