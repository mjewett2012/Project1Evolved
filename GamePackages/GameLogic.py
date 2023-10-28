# GameLogic.py
import GamePackages.GUIFunctions
from GamePackages.DatabaseHandler import DatabaseHandler

def main_game_loop(character):
    while True:
        # clear the screen
        GamePackages.GUIFunctions.clear_text()

        # Display the current room or situation
        display_current_room(character)

        # Get player input
        player_input = get_player_input()

        # Process player input and update game state
        process_input(player_input, character)

        # Check game-ending conditions, if any
        if game_over_condition():
            break

def display_current_room(character):
    db = DatabaseHandler()
    room_data = db.fetch_room_by_id(character['currentRoomLocation'])
    db.close()
    room_info = f"{room_data['name']}\n\n{room_data['description']}\n"
    GamePackages.GUIFunctions.display_text_in_gui(room_info, target="main")

    # Initialize exits_info with a default message
    exits_info = "No visible exits"

    # Displaying exits
    exits = room_data.get('exits', [])
    if exits:
        exits_info = "Exits: "
        for exit in exits:
            exits_info += f"{exit}, "
        exits_info = exits_info.strip(", ")  # Remove trailing comma

    GamePackages.GUIFunctions.display_text_in_gui(exits_info, target="main")


def get_player_input():
    # This can be a simple input box or a more complex GUI input method
    return input("What do you want to do? ")

def process_input(player_input, character):
    # Here, you'll handle various commands like "move north", "take item", etc.
    # Update the character's state, room location, inventory, etc. based on the command
    pass

def game_over_condition():
    # Check conditions like player choosing to exit, character death, etc.
    # Return True if the game should end, otherwise return False
    pass