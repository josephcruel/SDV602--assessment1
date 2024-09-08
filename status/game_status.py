# game_status.py
points = 0
health = 100
inventory = []

def get_points():
    return points

def set_points(pValue):
    global points
    points += pValue

def get_health():
    return health

def set_health(pValue):
    global health
    health += pValue
    if health < 0:  # Prevent health from going below 0
        health = 0

def show_status():
    result = f"Points: {points}, Health: {health}\n"
    result += f"Inventory: {', '.join(inventory) if inventory else 'Empty'}\n"
    if health <= 0:
        result += "\nYou are dead. Game over.\n"
    return result

# Inventory functions
def add_item(item):
    inventory.append(item)

def remove_item(item):
    if item in inventory:
        inventory.remove(item)

def get_inventory():
    return inventory

def show_inventory():
    return f"Inventory: {', '.join(inventory) if inventory else 'Empty'}"
