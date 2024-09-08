# monster.py
from status.game_status import show_status, get_health, set_health, add_item

monster_health = 10  # Monster starts with 10 health points
item_drop = 'Sword'  # Example of an item that could be dropped

def fight():
    global monster_health

    if get_health() <= 0:
        return "You are dead. Game over.\n"

    if monster_health > 0:
        set_health(-1)  # Player takes damage
        monster_health -= 3  # Deal damage to the monster

        # If the monster's health reaches or drops below 0, defeat the monster
        if monster_health <= 0:
            monster_health = 0  # Ensure health is not negative
            result = "\nYou have defeated the monster!\n"
            result += f"The monster dropped a {item_drop}!\n"
            add_item(item_drop)  # Add the item to the player's inventory
            return result

        # If the monster is not defeated yet, show its health
        result = f"Monster Health: {monster_health}\n"
        result += show_status()  # Show player's current status
        return result

    else:
        return "\nThe monster is already defeated.\n"
