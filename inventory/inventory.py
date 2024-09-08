# inventory.py

class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def list_items(self):
        return [item.name for item in self.items]

class Item:
    def __init__(self, name, attack_bonus=0):
        self.name = name
        self.attack_bonus = attack_bonus

    def __repr__(self):
        return f"{self.name} (Attack Bonus: {self.attack_bonus})"
