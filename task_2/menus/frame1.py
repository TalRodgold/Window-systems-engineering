import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QLineEdit, QPushButton, QWidget

class CustomFrame1(QFrame):
    def __init__(self):
        super().__init__()

        # Create three QLineEdit widgets
        self.edit_box1 = QLineEdit(self)
        self.edit_box2 = QLineEdit(self)
        self.edit_box3 = QLineEdit(self)

        # Create an "OK" button
        self.ok_button = QPushButton("OK", self)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.edit_box1)
        layout.addWidget(self.edit_box2)
        layout.addWidget(self.edit_box3)
        layout.addWidget(self.ok_button)

    def on_ok_button_clicked(self):
        # Handle the OK button click event
        text1 = self.edit_box1.text()
        text2 = self.edit_box2.text()
        text3 = self.edit_box3.text()

        print(f"Edit Box 1: {text1}")
        print(f"Edit Box 2: {text2}")
        print(f"Edit Box 3: {text3}")


