import json

class ShoppingListModel:
    def __init__(self, filename):
        self.filename = filename
        self.load_data()

    def load_data(self):
        try:
            with open(self.filename, 'r') as file:
                data = file.read()
                if data:
                    self.data = json.loads(data)
                else:
                    self.data = []
        except FileNotFoundError:
            self.data = []

    def save_data(self):
        with open(self.filename, 'w') as file:
            json.dump(self.data, file)

    def add_item(self, item_text, checked=False):
        if item_text:
            self.data.append({"text": item_text, "checked": checked})
            self.save_data()

    def update_checked_status(self, index, checked):
        if 0 <= index < len(self.data):
            self.data[index]["checked"] = checked
            self.save_data()

    def get_items(self):
        return self.data
