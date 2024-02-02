from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QLineEdit, QCheckBox

class ShoppingListView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.setWindowTitle("MY SHOPPING LIST")
        self.setGeometry(100, 100, 400, 200)

        self.controller = controller

        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout(central_widget)

        self.item_input = QLineEdit(self)
        layout.addWidget(self.item_input)

        add_button = QPushButton("Add Item", self)
        add_button.clicked.connect(self.add_item)
        layout.addWidget(add_button)

        layout.addStretch()

        self.checkboxes = []

    def add_item(self):
        item_text = self.item_input.text()
        self.controller.add_item(item_text)
        self.update_view()

    def update_checked_status(self, index, checked):
        self.controller.update_checked_status(index, checked)

    def update_view(self):
        for checkbox in self.checkboxes:
            checkbox.setParent(None)

        items = self.controller.get_items()

        for index, item in enumerate(items):
            checkbox = QCheckBox(item["text"], self)
            checkbox.setChecked(item["checked"])
            checkbox.stateChanged.connect
