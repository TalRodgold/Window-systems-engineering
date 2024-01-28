import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFrame, QVBoxLayout, QDial, QSlider, QPushButton
from PySide6.QtCore import Qt

class CustomFrame2(QFrame):
    def __init__(self):
        super().__init__()

        # Create a QDial
        self.dial = QDial(self)
        self.dial.setRange(0, 100)

        # Create a QSlider
        self.slider = QSlider(self)
        self.slider.setOrientation(Qt.Horizontal)  # Use Qt.Horizontal instead of integer
        self.slider.setRange(0, 100)

        # Create buttons
        self.increase_button = QPushButton("Increase", self)
        self.decrease_button = QPushButton("Decrease", self)

        # Connect buttons to functions
        self.increase_button.clicked.connect(self.on_increase_button_clicked)
        self.decrease_button.clicked.connect(self.on_decrease_button_clicked)

        # Set up the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.dial)
        layout.addWidget(self.slider)
        layout.addWidget(self.increase_button)
        layout.addWidget(self.decrease_button)

    def on_increase_button_clicked(self):
        # Increase values of the dial and slider
        self.dial.setValue(self.dial.value() + 10)
        self.slider.setValue(self.slider.value() + 10)

    def on_decrease_button_clicked(self):
        # Decrease values of the dial and slider
        self.dial.setValue(self.dial.value() - 10)
        self.slider.setValue(self.slider.value() - 10)

