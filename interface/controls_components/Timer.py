from PyQt5.QtCore import QSize, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QStyle, QLabel

from interface.styles.Style import Style


class Timer(QWidget):
    """
    Timer component. Contains a label and a button
    """
    paused = False

    def __init__(self, timer_data, style=Style()):
        """
        Initialize styling and create its components
        :param timer_data: timer value from JSON
        :param style: styling object
        """

        super().__init__()

        # Styling and main layout
        self.styles = style
        self.box_layout = QHBoxLayout()
        self.box_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.box_layout)

        # Label (displays the timer value)
        self.label = QLabel()
        self.label.setStyleSheet(self.styles.timer_label)
        self.label.setText("00:00:00")
        self.box_layout.addWidget(self.label)

        # Button pause/continue
        self.button = QPushButton()
        self.button.setIconSize(QSize(50, 50))
        self.button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPause")))
        self.button.setStyleSheet(self.styles.timer_button)
        self.button.clicked.connect(self.btnClicked)
        self.box_layout.addWidget(self.button)

        # Initialize the clock
        self.curr_time = QTime(timer_data[0], timer_data[1], timer_data[2])
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def updateTime(self):
        """
        Timers callback (called every second to update the timer value)
        """

        self.curr_time = self.curr_time.addSecs(1)
        self.label.setText(self.curr_time.toString("hh:mm:ss"))

    def btnClicked(self):
        """
        Pause or continue the timer depending of its status
        """

        if self.paused:
            self.timer.start()
            self.paused = False
            self.button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPause")))
        else:
            self.timer.stop()
            self.paused = True
            self.button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPlay")))
