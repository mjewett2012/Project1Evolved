import random
from Models import RoomModel, ThemeModel
from DatabaseHandler import DatabaseHandler
from TextGenerator import text_generate  # Assuming text_generate is in TextGenerator

class RoomFactory:
    room_grid = {}
    current_coordinates = (0, 0)
    db_handler = DatabaseHandler()

    @staticmethod
    def get_room(x, y):
        if (x, y) in RoomFactory.room_grid:
            return RoomFactory.room_grid[(x, y)]
        
        # Check the database if the room exists
        room_data = RoomFactory.db_handler.fetch_room_by_location(f"{x},{y}")
        if room_data:
            room = RoomModel.Room()
            room.rNumber = room_data["roomNum"]
            room.name = room_data["name"]
            room.description = room_data["description"]
            room.x, room.y = map(int, room_data["location"].split(","))
            # ... load other attributes as necessary
            RoomFactory.room_grid[(x, y)] = room
            return room

        # If room doesn't exist in memory or database, generate a new one
        return RoomFactory.generate_room(x, y)

    @staticmethod
    def generate_room(x, y):
        theme = random.choice(list(ThemeModel.Theme))
        size = random.randint(20, 50)
        RoomFactory.generate_theme_area(theme, size)
        return RoomFactory.room_grid.get((x, y))

    @staticmethod
    def generate_theme_area(theme, size):
        for i in range(size):
            for j in range(size):
                x = RoomFactory.current_coordinates[0] + i
                y = RoomFactory.current_coordinates[1] + j
                if (x, y) not in RoomFactory.room_grid:
                    room = RoomModel.Room()
                    room.name, room.description = text_generate(RoomModel.Room, theme)  # Using text_generate to get the room name and description
                    room.theme = theme
                    room.x = x
                    room.y = y
                    RoomFactory.room_grid[(x, y)] = room
                    RoomFactory.db_handler.save_room(room)  # Save the room to the database
