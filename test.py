from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QVBoxLayout, QLabel, QPushButton


class MainWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Set the window title
        self.setWindowTitle("Main Window")

        # Create a label to display a message
        message_label = QLabel("This is the main window.")

        # Create a button to open a new window
        button1 = QPushButton("Lấy mẫu")
        button1.move(100,100)
        button2 = QPushButton("Giám định nhanh")
        button2.move(100,200)

        # Connect the button to a slot function
        button1.clicked.connect(self.open_new_window)
        button2.clicked.connect(self.open_new_window)

        # Add the label and button to a layout
        layout = QVBoxLayout()
        layout.addWidget(message_label)
        layout.addWidget(button1)
        layout.addWidget(button2)

        # Set the layout for the window
        self.setLayout(layout)

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
    app = QApplication([])
    main_window = MainWindow()
    main_window.setGeometry(0,0,500,500)
    main_window.show()
    app.exec_()