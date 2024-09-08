"""fight module for the second monster"""
from status.game_status import show_status, get_health, set_health, set_points

monster_health = 18 # Monster starts with 10 health points

def fight():
    global monster_health

    if get_health() <= 0:
        return "You are dead. Game over.\n"

    if monster_health > 0:
        set_health(-1)  # Player takes damage
        monster_health -= 3  # Deal damage to the monster

        # Cap monster's health at 0
        if monster_health < 0:
            monster_health = 0

        result = f"Monster Health: {monster_health}\n"
        result += show_status()  # Show player's current status

        if monster_health <= 0:
            result += "\nYou have defeated the monster!\n"
    else:
        result = "\nThe monster is already defeated.\n"

    return result
