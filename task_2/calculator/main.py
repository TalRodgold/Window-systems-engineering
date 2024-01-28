import sys
from PySide6.QtWidgets import QApplication
from calculator import *

def main():
    app = QApplication([])
    calculator = CalculatorApp()
    calculator.show()
    app.exec()

if __name__ == "__main__":
    main()
