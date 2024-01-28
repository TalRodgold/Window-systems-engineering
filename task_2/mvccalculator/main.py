import sys
from PySide6.QtWidgets import QApplication

from model import CalculatorModel
from view import CalculatorView
from controller import CalculatorController
    
def main():    
    app = QApplication()
    model = CalculatorModel()
    view = CalculatorView(model)
    controller = CalculatorController(model, view)
    controller.run()
    app.exec()
    
if __name__ == "__main__":
    main()    
