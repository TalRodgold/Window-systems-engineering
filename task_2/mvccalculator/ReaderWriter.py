import os
import csv

class readwrite():
    def __init__(self):
        self.filename="history.csv"
        self.createfile()       
        
    def createfile(self):
        if not os.path.isfile(self.filename):        
            with open(self.filename, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(["Saved Calculations"])    
                
    def save(self,newrow):    
        newrow=[newrow]          
        with open(self.filename, 'a', newline='') as csv_file:
          csv_writer = csv.writer(csv_file)
          csv_writer.writerow(newrow)        
    
    def load(self):
        result=None
        with open(self.filename, 'r', newline='') as csv_file:
          csv_reader = csv.reader(csv_file)          
          lines = list(csv_reader)         
          text=str(lines[-1][0])
        
          if not (text.__contains__("Saved")):            
              return text
        
   