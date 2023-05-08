import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDialog, QPushButton, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QBrush, QFont
from PyQt5.QtCore import *

class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super(CircleWidget, self).__init__(parent)

    def paintEvent(self, event):
        qp = QPainter(self)
        qp.setRenderHint(QPainter.Antialiasing)
        qp.setPen(QColor(0, 0, 0))
        qp.setBrush(QBrush(QColor(255, 255, 255)))

        # Set circle position and size
        x = 50
        y = 50
        w = 100
        h = 100

        qp.drawEllipse(int(x), int(y), int(w), int(h))

        # Add text to the circle
        qp.setFont(QFont("Arial", 16))
        qp.drawText(int(x + w/4), int(y + h/3 +5), "Logo")
        qp.drawText(int(x + w/4 +3), int(y + h/1.5 +5), "BCA")
        qp.setFont(QFont("Arial", 16))
        qp.drawText(int(x + 1.1*w), int(y + h / 1.5), "Identification Card Assesment")
        qp.drawText(int(x + 1.1*w), int(y + h / 1.4), "________________________")
        qp.drawText(int(x + 1.1*w), int(y + h / 1), "Công cụ giám định CCCD")

    def open_new_window(self):
        # Create a new dialog window
        new_window = QDialog(self)
        new_window.setWindowTitle("New Window")

        # Create a label and OK button for the new window
        message_label = QLabel("This is a new window.")
        ok_button = QPushButton("OK")

        # Connect the OK button to the new window's accept() slot
        ok_button.clicked.connect(new_window.accept)

        # Add the label and OK button to a layout
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(ok_button)

        # Set the layout for the new window
        new_window.setLayout(layout)

        # Show the new window
        new_window.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CircleWidget()
    btn1 = QPushButton(w)
    btn1.setText("Lấy mẫu")
    btn1.move(100, 200)
    btn1.setFont(QFont("Arial", 16))
    btn2 = QPushButton(w)
    btn2.setText("Giám định nhanh")
    btn2.move(100,250)
    btn2.setFont(QFont("Arial", 16))
    w.setGeometry(0, 0, 500, 500)
    w.show()
    sys.exit(app.exec_())