from PyQt5.QtCore import QSize, QTimer, QTime
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton, QVBoxLayout, QStyle, QLabel

from interface.styles.Theme import Theme


class Timer(QWidget):
    paused = False

    def __init__(self, timer_data, theme=Theme()):
        super().__init__()
        self.theme = theme
        self.box_layout = QHBoxLayout()
        self.box_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.box_layout)

        self.label = QLabel()
        self.label.setStyleSheet(self.theme.timer_label)
        self.label.setText("00:00:00")
        self.box_layout.addWidget(self.label)

        self.button = QPushButton()
        self.button.setIconSize(QSize(50, 50))
        self.button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPause")))
        self.button.setStyleSheet(self.theme.timer_button)
        self.button.clicked.connect(self.btnClicked)
        self.box_layout.addWidget(self.button)

        self.curr_time = QTime(timer_data[0], timer_data[1], timer_data[2])
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)

    def updateTime(self):
        self.curr_time = self.curr_time.addSecs(1)
        self.label.setText(self.curr_time.toString("hh:mm:ss"))

    def btnClicked(self):
        if self.paused:
            self.timer.start()
            self.paused = False
            self.button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPause")))
        else:
            self.timer.stop()
            self.paused = True
            self.button.setIcon(self.style().standardIcon(getattr(QStyle, "SP_MediaPlay")))


    #TODO disable controls on paused


