import sys
import random
from typing import Optional
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtGui import QPainter, QColor, QPaintEvent

from ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button = self.findChild(QPushButton, "pushButton")
        self.button.clicked.connect(self.add_circle)
        self.circles: list[tuple[int, int, int, QColor]] = []

    def add_circle(self):
        x = random.randint(0, self.width())
        y = random.randint(0, self.height())
        diameter = random.randint(20, 100)
        color = QColor(random.randint(0, 255),
                       random.randint(0, 255),
                       random.randint(0, 255))
        self.circles.append((x, y, diameter, color))
        self.update()

    def paintEvent(self, a0: Optional[QPaintEvent]):
        painter = QPainter(self)
        for x, y, diameter, color in self.circles:
            painter.setBrush(color)
            painter.setPen(color)
            painter.drawEllipse(x, y, diameter, diameter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
