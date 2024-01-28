from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QGridLayout, QLineEdit

class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("O.O.Calculator")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        self.result_display = QLineEdit(self)
        self.layout.addWidget(self.result_display)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        self.create_buttons(buttons)

    def create_buttons(self, buttons):
        grid_layout = QGridLayout()
        self.layout.addLayout(grid_layout)

        row = 0
        col = 0

        for button_text in buttons:
            button = QPushButton(button_text, self)
            button.clicked.connect(self.on_button_click)
            grid_layout.addWidget(button, row, col)

            col += 1
            if col > 3:
                col = 0
                row += 1

    def on_button_click(self):
        # get a pointer to the pressed button
        button = self.sender()
        current_text = self.result_display.text()

        if button.text() == '=':
            try:
                result = eval(current_text)
                self.result_display.setText(str(result))
            except Exception as e:
                self.result_display.setText("Error")

        else:
            new_text = current_text + button.text()
            self.result_display.setText(new_text)


