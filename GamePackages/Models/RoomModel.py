# RoomModel.py
# The Room class is the parent class for all rooms in the game.  It contains the basic attributes
# and methods that all rooms will have.
#
# Parameters: None
#
# Return: None
#
# Example:
# room = Room()

class Room:
    def __init__(self):
        self.rNumber = None
        self.name = ""
        self.description = ""
        self.theme = None
        self.x = 0
        self.y = 0
        self.exits = {}  # Dictionary to store exits. e.g., {"north": 2, "west": 3}
        self.mobs = []   # List to store mob IDs present in the room
        self.inventory = []  # List to store item IDs present in the room

