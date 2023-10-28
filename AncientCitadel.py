# Filename: AncientCitadel.py
from GamePackages.GUIFunctions import init_gui, display_title_graphics
from GamePackages.DatabaseHandler import DatabaseHandler
from GamePackages.Factories.RoomFactory import RoomFactory
from GamePackages.Models.ThemeModel import Theme

def main():
    display_title_graphics()
    db = DatabaseHandler()
    if (db.check_for_room_one() == False):
        # generate a themed area of rooms
        RoomFactory.generate_theme_area(Theme.PLAINS, 50)
    init_gui()

if __name__ == "__main__":
    main()