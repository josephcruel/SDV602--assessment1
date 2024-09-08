from fights.monster import fight as monster_fight
from fights.second_monster import fight as second_monster_fight
from status.game_status import get_health, show_status

# Game state and status
game_state = 'Forest'
game_prev = 'Forest'
game_mode = 'exploring'  # Can be 'exploring' or 'fighting'
monster_defeated = False
second_monster_defeated = False

def move_prev():
    """Move the player back to the previous location (when running)."""
    global game_state, game_prev, game_mode
    game_state = game_prev  # Return to the previous location
    game_mode = 'exploring'  # Switch back to exploring mode

    # Return a message saying you've successfully run away
    return f"You have fled back to the {game_state}.\n"

def move_fight(monster='first'):
    """Handle fighting a monster."""
    global game_mode, monster_defeated, second_monster_defeated
    game_mode = 'fighting'

    if monster == 'first' and get_health() > 0 and not monster_defeated:
        fight_result = monster_fight()  # Fight the first monster
        if "You have defeated the monster!" in fight_result:
            monster_defeated = True
        return fight_result

    elif monster == 'second' and get_health() > 0 and not second_monster_defeated:
        fight_result = second_monster_fight()  # Fight the second monster
        if "You have defeated the second monster!" in fight_result:
            second_monster_defeated = True
        return fight_result

    elif get_health() <= 0:
        return "You are dead. Game over.\n"

    else:
        return "There are no monsters left to fight here."

def get_move_command(pDirection, monster='first'):
    """Return the appropriate move function."""
    if pDirection == 'prev':
        return move_prev
    elif pDirection == 'fight':
        return lambda: move_fight(monster)  # Pass the monster type

# Define the game places and story
game_places = {
    'Forest': {
        'Story': 'You are in the forest.\nTo the north is a cave.\nTo the south is a castle.\nA goblin stands in your way!',
        'North': 'Cave', 'South': 'Castle', 'Fight': 'Fight Monster', 'Image': 'forest.png'
    },
    'Cave': {
        'Story': 'You are in a cave.\nTo the south is a forest.',
        'South': 'Forest', 'Image': 'cave.png'
    },
    'Castle': {
        'Story': 'You are in a castle.\nNorth leads to the forest,\nSouth leads to the Swamp.',
        'North': 'Forest', 'South': 'Swamp', 'Image': 'castle.png'
    },
    'Swamp': {
        'Story': 'You are in a swamp.\nA Zombie is lurking here!',
        'North': 'Castle', 'Fight': 'Fight Second Monster', 'Image': 'swamp.png'
    },
    'Fight Monster': {
        'Story': 'You encounter the goblin!\nFight or Run?',
        'Run': get_move_command('prev'),  # Now allows running back to the previous location
        'Fight': get_move_command('fight', 'first'), 
        'Image': 'goblin.png'
    },
    'Fight Second Monster': {
        'Story': 'You encounter the zombie!\nFight or Run?',
        'Run': get_move_command('prev'),  # Now allows running back to the previous location
        'Fight': get_move_command('fight', 'second'), 
        'Image': 'zombie.png'
    },
}


def show_current_place():
    """Show the story at the current game state."""
    return game_places[game_state]['Story']

def game_play(direction):
    """Handle game logic for movement and actions."""
    global game_state, game_prev, game_mode

    if get_health() <= 0:
        return "You are dead. Game over.\n"

    direction = direction.capitalize()

    # Handle movement
    if direction in game_places[game_state]:
        proposed_state = game_places[game_state][direction]

        if callable(proposed_state):
            # This is a command like "Fight" or "Run"
            game_mode = 'fighting'  # Switch to fighting mode
            return proposed_state()  # Return the result of the fight or run command

        else:
            game_prev = game_state
            game_state = proposed_state
            game_mode = 'exploring'  # Switch back to exploring mode
            return game_places[game_state]['Story']  # Return the location story

    else:
        return f"You can't go that way.\n{game_places[game_state]['Story']}"
