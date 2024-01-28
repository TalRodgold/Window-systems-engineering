from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QGridLayout

# אחראי על התצוגה והאינטראקציה עם המשתמש
class CalculatorView(QMainWindow):
    def __init__(self, model):
        super().__init__()

        self.model = model

        self.setWindowTitle("Calculator")
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
        #add save 
        button = QPushButton("save", self)
        button.clicked.connect(self.on_button_click)
        grid_layout.addWidget(button, 5,1)        
        
        #add show
        button = QPushButton("show", self)
        button.clicked.connect(self.on_button_click)
        grid_layout.addWidget(button, 5,2)        
        
    def on_button_click(self):
        #איתור הכפתור שהפעיל את האירוע 
        button = self.sender()
        button_text = button.text()
        print(button_text)
        if button_text == '=':
            result = self.model.evaluate_expression()
            self.result_display.setText(result)
        elif button_text =="show":
            self.model.load()             
            self.result_display.setText(str(self.model.expression))                        
        elif button_text =="save":            
            self.model.save()
        else:
            self.model.update_expression(button_text)
            self.result_display.setText(self.model.expression)
