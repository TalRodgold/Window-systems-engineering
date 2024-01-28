import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QWidget,QVBoxLayout,QPushButton

from frame1 import *
from frame2 import *

from PySide6.QtGui import QAction
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the menu bar
        menubar = self.menuBar()

        # Create a menu
        menu = menubar.addMenu('MyMenu')

        # Create actions for the menu options
        action_s1 = QAction('Option S1', self)
        action_s2 = QAction('Option S2', self)

        # Connect actions to functions
        action_s1.triggered.connect(self.option_s1_selected)
        action_s2.triggered.connect(self.option_s2_selected)

        # Add actions to the menu
        menu.addAction(action_s1)
        menu.addAction(action_s2)

        # Set the menu bar
        self.setMenuBar(menubar)

    def option_s1_selected(self):
        print("Option S1 Selected")
        frame=CustomFrame1()
        self.change_widget(frame)
        
    def option_s2_selected(self):
        print("Option S2 Selected")
        frame=CustomFrame2()
        self.change_widget(frame)
       
     
    def change_widget(self,currentframe):
        # Create a new central widget
        new_widget = QWidget(self)
        new_layout = QVBoxLayout(new_widget)

        # Add content to the new widget
        new_layout.addWidget(currentframe)
    
        # Set the new widget as the central widget
        self.setCentralWidget(new_widget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MyMainWindow()
    main_window.show()
    sys.exit(app.exec())
