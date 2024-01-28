from ReaderWriter import readwrite

#זוכר את הנתונים ומבצע חישובים ולוגיקה עבורם 
class CalculatorModel:
    def __init__(self):
        self.expression = ""
        self.readwrite=readwrite()

    def update_expression(self, value):
        self.expression += str(value)

    def evaluate_expression(self):
        try:
            result = eval(self.expression)
            self.expression=""
            return str(result)
        except Exception as e:
            return "Error"
        
    def save(self):       
        self.readwrite.save(self.expression)   
    
    def load(self): 
        self.expression=self.readwrite.load()
      
       
       

