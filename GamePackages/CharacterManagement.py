import os
from GamePackages.Models.CharacterModel import playerCharacter
from GamePackages.Menu import display_main_menu, display_class_select
from GamePackages.Data import save_characters
from GamePackages.Utility import dice_roller, exit_program
from datetime import date
from DatabaseHandler import DatabaseHandler



# Incorporate later

# def weapon_choice(myClass):
#     if myClass == "Warrior":
#         weapon = "Wooden Sword"
#     elif myClass == "Rogue":
#         weapon = "Wooden Dagger"
#     elif myClass == "Priest":
#         weapon = "Wooden Staff"
#     elif myClass == "Wielder":
#         weapon = "Wooden Wand"
#     return weapon

# def armor_choice(myClass):
#     if myClass == "Warrior":
#         armor = "Leather Armor"
#     elif myClass == "Rogue":
#         armor = "Leather Armor"
#     elif myClass == "Priest":
#         armor = "Acolyte Robes"
#     elif myClass == "Wielder":
#         armor = "Simple Robes"
#     return armor

def get_password():
    while True:
        password = input("Enter a password for your character: ")
        password2 = input("Re-enter your password: ")
        if password == password2:
            os.system('cls')
            return password
        else:
            os.system('cls')
            print("Passwords do not match. Please try again.\n")




def format_character_line(index, name, ordinal, type_name):
    # Create the string
    content_str = f"{index}. {name} the {ordinal} Level {type_name}"
    # Center the string within the WIDTH, between the bars
    print(f"|{content_str.center(WIDTH - 2)}|")

    
def create_character(characters):
    display_class_select()
    myClass = class_choice()
    myName = name_choice(characters)
    strength, dexterity, intelligence, wisdom, constitution = stat_roller(myClass)
    weapon = weapon_choice(myClass)
    armor = armor_choice(myClass)
    defense, attack, hitPoints, magicPoints = stat_calculator(myClass, strength, dexterity, intelligence, wisdom, constitution)
    maxHitPoints = hitPoints
    maxMagicPoints = magicPoints
    level = 1
    experience = 0
    gold = 0
    pWord = get_password()
    currentPlayerNum = len(characters) + 1
    character = [currentPlayerNum, myName, myClass, strength, dexterity, intelligence, wisdom, constitution, 
                 weapon, armor, defense, attack, hitPoints, maxHitPoints, magicPoints, maxMagicPoints, level, 
                 experience, gold, pWord]
    characters.append(character)
    save_characters(characters)
    print(f"{myName} the {myClass} has been created.\n")
    print()
    input("Press Enter to continue...")
    display_main_menu()

def select_character(characters):
    list_characters(characters)
    print()
    print("Enter the number of the character you wish to play as.")
    print("Or enter 0 to return to the main menu.")
    while True:
        selection = int(input("Selection: "))
        try:
            if selection == 0:
                display_main_menu()
                return
            elif selection < 0 or selection > len(characters):
                print("Not a valid selection. Please try again.\n")
                continue
            else:
                break
        except ValueError:
            print("Not a valid selection. Please try again.\n")
            continue

    character = characters[selection - 1]
    print("You have selected {} the {}.".format(character[0], character[1]))
    print("Enter the password for this character.")
    while True:
        password = input("Password: ")
        if password == str(character[19]):
            print(f"Welcome back, {character[0]}!\nYour adventure continues...")
            selectedCharacter = playerCharacter.from_list(character)
            return selectedCharacter
        else:
            print("Incorrect password. Please try again.")
            continue



