import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QCheckBox, QLineEdit
from PySide6.QtGui import QFont, QColor

from model import ShoppingListModel

class MyMainWindow(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.setWindowTitle("MY SHOPPING LIST")
        self.setGeometry(100, 100, 400, 200)

        self.model = model

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)

        # Text input box
        self.text_input = QLineEdit(self)
        self.text_input.setPlaceholderText("Enter item")
        self.text_input.setStyleSheet("color: #333; background-color: #eee; border: 1px solid #ccc; border-radius: 5px;")
        self.layout.addWidget(self.text_input)

        # Add item button
        add_button = QPushButton("Add Item")
        add_button.setStyleSheet("background-color: #4CAF50; color: white; border: none; padding: 8px 16px; text-align: center; text-decoration: none; display: inline-block; font-size: 14px;")
        add_button.clicked.connect(self.add_item)
        self.layout.addWidget(add_button)

        # Load existing checkboxes
        self.load_existing_checkboxes()

    def load_existing_checkboxes(self):
        for item in self.model.get_items():
            self.add_checkbox(item["text"], item["checked"])

    def add_checkbox(self, text, checked):
        checkbox = QCheckBox(text)
        checkbox.setChecked(checked)
        checkbox.setStyleSheet("color: #333; font-family: Arial, sans-serif; font-size: 12px;")
        checkbox.stateChanged.connect(lambda state, text=text: self.checkbox_state_changed(state, text))
        self.layout.addWidget(checkbox)

    def checkbox_state_changed(self, state, text):
        index = next((i for i, checkbox in enumerate(self.findChildren(QCheckBox)) if checkbox.text() == text), -1)
        if index != -1:
            self.model.update_checked_status(index, state == 2)

    def add_item(self):
        item_text = self.text_input.text()
        if item_text:
            self.model.add_item(item_text)
            self.add_checkbox(item_text, False)
            self.text_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    model = ShoppingListModel("task_3/shopping_list.json")
    main_window = MyMainWindow(model)
    main_window.show()
    sys.exit(app.exec())
