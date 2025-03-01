import sys
import random
from typing import Optional
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPaintEvent
from PyQt6 import uic


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.add_circle)
        self.circles: list[tuple[int, int, int]] = []

    def add_circle(self):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        diameter = random.randint(20, 100)
        self.circles.append((x, y, diameter))
        self.update()

    def paintEvent(self, a0: Optional[QPaintEvent]):
        painter = QPainter(self)
        painter.setBrush(QColor("yellow"))
        painter.setPen(QColor("yellow"))
        for x, y, diameter in self.circles:
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
