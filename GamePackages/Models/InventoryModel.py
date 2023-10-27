# InventoryModel.py

class Inventory:
    def __init__(self, capacity=None):
        self.items = []
        self.capacity = capacity

    def add_item(self, item):
        if self.capacity and len(self.items) >= self.capacity:
            print("Inventory full!")
            return False
        self.items.append(item)
        return True

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            return True
        print(f"{item.name} not found in inventory!")
        return False

    def list_items(self):
        for item in self.items:
            print(item.name)

    def item_exists(self, item_name):
        for item in self.items:
            if item.name == item_name:
                return True
        return False