import os
from .GUIFunctions import display_text_in_gui

def display_main_menu():
    #clear_text("main")  # Clear the main text output first

    menu_text = """
        Welcome to the Citadel of the Ancients!
        ======================================
        GAME MENU
        =========
        start - Begin your adventure
        list  - List all Characters
        add   - Add a Character
        del   - Delete a Character
        quit  - Exit World
        ======================================
        """
    display_text_in_gui(menu_text, target="main", format_type="menu")
# def display_main_menu():
#     os.system('cls')
#     print("Welcome to the Citadel of the Ancients!")
#     print("    ==============================")
#     print("    |        GAME MENU           |")
#     print("    ==============================")
#     print("    |start - Begin your adventure|")
#     print("    |list  - List all Characters |")
#     print("    |add   - Add a Character     |")
#     print("    |del   - Delete a Character  |")
#     print("    |quit  - Exit World          |")
#     print("    ==============================")
#     print()    

def display_class_select():
    os.system('cls')
    print("    Choose your class:")
    print("    ==============================")
    print("    |        CLASS SELECT        |")
    print("    ==============================")
    print("    |Warrior - A skilled fighter |")
    print("    |Rogue   - A gifted thief    |")
    print("    |Priest  - A true believer of|")
    print("    |          of ancient Gods   |")
    print("    |Wielder - A powerful wielder|")
    print("    |          of ancient magic  |")
    print("    ==============================")
    print()    

def run_menu():
    print("Fare thee well!")

def town_menu():
        print("You are in the town of Duskwood. You are standing in the town square. There is a tavern to the north, a blacksmith to the east, and a general store to the west.")
        print("What would you like to do?")
        print("1. Visit the tavern")
        print("2. Visit the blacksmith")
        print("3. Visit the general store")
        print("4. Explore the forest")
        print("5. Enter the citadel")
        print("6. Go to the castle")
        print("7. Visit the temple")
        print("8. Visit the wizard's tower")
        print("9. Visit the alchemist")

# display the title graphics from title.txt

def display_title_graphics():
    with open("title.txt", "r") as file:
        title = file.read()
        display_text_in_gui(title, target="main")

# def display_title_graphics():
#     with open("title.txt", "r") as file:
#         title = file.read()
#         print(title)
    
