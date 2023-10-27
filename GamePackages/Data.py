import csv
import pickle
import sys

FILENAME = "character_data.csv"

def load_characters():
    try:
        characters = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                characters.append(row)
        return characters
    except FileNotFoundError as e:
        return characters
    except Exception as e:
        print(type(e), e)
        sys.exit()

def save_characters(characters):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(characters)
    except OSError as e:
        print(type(e), e)
        sys.exit()
    except Exception as e:
        print(type(e), e)
        sys.exit()

    # Save item to binary file containing all items in the game
    def save_item(self):
        with open("items.bin", "ab") as file:
            pickle.dump(self, file)

    # Save item as an active instance of the item with current stats and location
    def save_item_as_instance(self):
        with open("active_items.bin", "ab") as file:
            pickle.dump(self, file)

    # Save mob to binary file containing all mobs in the game
    def save_mob(self):
        with open("mobs.bin", "ab") as file:
            pickle.dump(self, file)

    # Save mob as an active instance of the mob with current stats and location
    def save_mob_as_instance(self):
        with open("active_mobs.bin", "ab") as file:
            pickle.dump(self, file)

    # Load all items from binary file containing all items and subclasses in the game
    def load_items():
        items = []
        with open("items.bin", "rb") as file:
            while True:
                try:
                    items.append(pickle.load(file))
                except EOFError:
                    break
        return items

    # Load all active items from binary file containing all active items in the game
    def load_active_items():
        items = []
        with open("active_items.bin", "rb") as file:
            while True:
                try:
                    items.append(pickle.load(file))
                except EOFError:
                    break
        return items
    
    # Load all mobs from binary file containing all mobs in the game
    def load_mobs():
        mobs = []
        with open("mobs.bin", "rb") as file:
            while True:
                try:
                    mobs.append(pickle.load(file))
                except EOFError:
                    break
        return mobs
    
    # Load all active mobs from binary file containing all active mobs in the game
    def load_active_mobs():
        mobs = []
        with open("active_mobs.bin", "rb") as file:
            while True:
                try:
                    mobs.append(pickle.load(file))
                except EOFError:
                    break
        return mobs
    
