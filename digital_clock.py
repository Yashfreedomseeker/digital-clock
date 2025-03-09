import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTime, QTimer, Qt
from PyQt5.QtGui import QFont, QFontDatabase

class DigitalClock(QWidget):
    def __init__(self): #designing entities for the clock
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUi()

    def initUi(self): #layout for the digital clock
        self.setWindowTitle("Digital Clock")
        self.setGeometry(680, 400, 500, 200)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignCenter)

        self.time_label.setStyleSheet("font-size: 120px;"
                                      "color: aqua;"
                                      "font-weight: bold;")

        self.setStyleSheet("background-color: black;")

        font_id = QFontDatabase.addApplicationFont("DS-DIGI.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        myFont = QFont(font_family,150)
        self.time_label.setFont(myFont)

        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.updateTime()

    def updateTime(self):
        current_time = QTime.currentTime().toString("hh:mm:ss A")
        self.time_label.setText(current_time)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())