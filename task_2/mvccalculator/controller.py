# מנתב את הקוד בהתאם לצורך ולמצב
class CalculatorController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
    def run(self):    
        self.view.show()
