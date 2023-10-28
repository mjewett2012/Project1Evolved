# Description: This file contains the GameItems class and its subclasses Weapon and Armor
#              The GameItems class is used to create objects that represent items in the game
#              The Weapon and Armor classes are subclasses of GameItems and are used to create
#              objects that represent weapons and armor in the game
#              The GameItems class has a subclass called Consumable that is used to create objects
#              that represent consumable items in the game
#              The GameItems class has a subclass called Container that is used to create objects
#              that represent containers in the game
#              The GameItems class has a subclass called Key that is used to create objects
#              that represent keys in the game
#              The GameItems class has a subclass called QuestItem that is used to create objects
#              that represent quest items in the game
#              The GameItems class has a subclass called Currency that is used to create objects
#              that represent currency in the game

from .CharacterModel import playerCharacter
from .InventoryModel import Inventory
from .ThemeModel import Theme
from .DamageTypeModel import DamageType
from .EffectModel import Effect
from .ArmorTypeModel import ArmorType
from .WeaponTypeModel import WeaponType

class GameItems:
    def __init__(self, iNumber, name, description, price, quantity, material, weight, image, worldTheme, rarity):
        self.iNumber = iNumber
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.material = material
        self.weight = weight
        self.image = image # This is the image that will be displayed when the item is displayed in the game
        self.worldTheme = ThemeModel.Theme(worldTheme)
        self.rarity = rarity

    # __str__ is used to print the object in a more readable format
    # This is what is printed when you print the object
    # Example: print(item)
    # Output:
    #         Name: Health Potion
    #         Description: Restores 10 health
    #         Price: 10
    #         Quantity: 1

    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPrice: {self.price}\nQuantity: {self.quantity}"

# Weapon class
# This class is used to create objects that represent weapons in the game
# Weapons are a subclass of GameItems
# Weapons have a damage attribute that is used to determine how much damage the weapon does
# Weapons have a durability attribute that is used to determine how much durability the weapon has
# Weapons have an attackType attribute that is used to determine what type of attack the weapon has
# Weapons are usually found in containers or on enemies
    
class Weapon(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, damage, durability, attackType):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        self.damage = damage
        self.durability = durability
        self.attackType = attackType
        self.bonus_damage = 0
        self.bonus_to_hit = 0
        self.effect = None

    def __str__(self):
        return super().__str__() + f"\nDamage: {self.damage}\nDurability: {self.durability}\nAttack Type: {self.attackType}"

# Armor class
# This class is used to create objects that represent armor in the game
# Armor is a subclass of GameItems
# Armor has a defense attribute that is used to determine how much defense the armor provides
# Armor has a durability attribute that is used to determine how much durability the armor has
# Armor has an armorType attribute that is used to determine what type of armor it is
# Armor is usually found in containers or on enemies
# Armor is usually used to increase defense
    
class Armor(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, defense, durability, armorType):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        self.defense = defense
        self.durability = durability
        self.armorType = armorType
        self.hp_add = 0
        self.mp_add = 0
        self.effect = None

    def __str__(self):
        return super().__str__() + f"\nDefense: {self.defense}\nDurability: {self.durability}\nArmor Type: {self.armorType}"

# Consumable class
# This class is used to create objects that represent consumable items in the game
# Consumable items are items that can be used to restore health, mana, etc.
# Consumable items are usually found in containers or on enemies
# Consumable items are a subclass of GameItems
# Consumable items have an effect attribute that is used to determine what effect the item has

class Consumable(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, effect):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        self.effect = effect

    def __str__(self):
        return super().__str__() + f"\nEffect: {self.effect}"
    
# Container class
# This class is used to create objects that represent containers in the game
# Containers are objects that can hold other objects
# Containers are usually found in the game world
# Containers are a subclass of GameItems
# Containers have an inventory attribute that is used to store items
# Containers have a capacity attribute that is used to determine how many items can be stored
# Containers have an isLocked attribute that is used to determine if the container is locked
# Containers have a keyNumber attribute that is used to determine which key unlocks the container
# Containers have an isTrapped attribute that is used to determine if the container is trapped
# Containers have a trapType attribute that is used to determine what type of trap the container has
# Containers have a trapDamage attribute that is used to determine how much damage the trap does
# Containers have a trapEffect attribute that is used to determine what effect the trap has
# Containers have a trapDuration attribute that is used to determine how long the trap lasts
# Containers have a trapDC attribute that is used to determine the DC of the trap
# Containers have a state attribute that is used to determine if the container is open or closed
# Containers have a mobile attribute that is used to determine if the container can be moved
# Containers have an open method that is used to open the container
# Containers have a close method that is used to close the container
# Containers have a lock method that is used to lock the container
# Containers have an unlock method that is used to unlock the container
# Containers have an item_to_container method that is used to add an item to the container from the player's inventory
# Containers have an item_from_container method that is used to remove an item from the container and add it to the player's inventory

class Container(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, capacity=None, 
                 isLocked=False, keyNumber=0, isTrapped=False, trapType=None, trapDamage=0, 
                 trapEffect=None, trapDuration=0, trapDC=0, state="Closed", mobile=False):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        
        self.inventory = Inventory(capacity)
        self.isLocked = isLocked
        self.keyNumber = keyNumber
        self.isTrapped = isTrapped
        self.trapType = trapType
        self.trapDamage = trapDamage
        self.trapEffect = trapEffect
        self.trapDuration = trapDuration
        self.trapDC = trapDC
        self.state = state
        self.mobile = mobile

    def item_to_container(self, item):
        if self.state == "Open":
            result = self.inventory.add_item(item)
            if result:
                print(f"You put the {item.name} in the {self.name}.")
            else:
                print(f"Couldn't put the {item.name} in the {self.name}. Maybe it's full?")
            return result
        else:
            print(f"The {self.name} is closed.")
            return False
        
    def item_from_container(self, item):
        if self.state == "Open":
            result = self.inventory.remove_item(item)
            if result:
                print(f"You take the {item.name} from the {self.name}.")
                # If you still want to add the item to character inventory when removing from container:
                playerCharacter.add_to_inventory(item)
            else:
                print(f"{item.name} not found in {self.name}.")
            return result
        else:
            print(f"The {self.name} is closed.")
            return False
    def open(self):
        if self.state == "Closed":
            if self.isLocked:
                print(f"The {self.name} is locked.")
            else:
                print(f"You open the {self.name}.")
                self.state = "Open"
        else:
            print(f"The {self.name} is already open.")
    def close(self):
        if self.state == "Open":
            print(f"You close the {self.name}.")
            self.state = "Closed"
        else:
            print(f"The {self.name} is already closed.")
    def lock(self):
        if self.isLocked:
            # Check if the player has the key
            if playerCharacter.check_for_item(self.keyNumber):
                print(f"You lock the {self.name}.")
                self.isLocked = False
            print(f"The {self.name} is already locked.")
        else:
            print(f"You lock the {self.name}.")
            self.isLocked = True
    def unlock(self):
        if self.isLocked:
            # Check if the player has the key
            if playerCharacter.check_for_item(self.keyNumber):
                print(f"You unlock the {self.name}.")
                self.isLocked = False
            print(f"You unlock the {self.name}.")
            self.isLocked = False
        else:
            print(f"The {self.name} is already unlocked.")

# Key class
# This class is used to create objects that represent keys in the game
# Keys are used to unlock containers
# Keys are usually found in containers or on enemies
# Keys are a subclass of GameItems
# Keys have a keyNumber attribute that is used to determine which container the key unlocks

class Key(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, keyNumber):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        self.keyNumber = keyNumber

    def __str__(self):
        return super().__str__() + f"\nKey Type: {self.keyNumber}"

# QuestItem class
# This class is used to create objects that represent quest items in the game
# Quest items are items that are used to complete quests
# Quest items are usually found in containers or on enemies
# Quest items are usually used to complete quests
# Quest items are a subclass of GameItems
# Quest items have a quest attribute that is used to determine which quest the item is used for
    
class QuestItem(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, quest):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        self.quest = quest

    def __str__(self):
        return super().__str__() + f"\nQuest: {self.quest}"

# Currency class
# This class is used to create objects that represent currency in the game
# Currency is a subclass of GameItems

class Currency(GameItems):
    def __init__(self, iNumber, name, description, price, quantity, worldTheme, currencyType):
        super().__init__(iNumber, name, description, price, quantity, worldTheme)
        self.currencyType = currencyType

    def __str__(self):
        return super().__str__() + f"\nCurrency Type: {self.currencyType}"

# This is a test to see if the classes work
# If you run this file, it will print the object
# If you import this file into another file, it will not print the object
# This is because the code below is only run when this file is run
# If you import this file into another file, the code below is not run
if __name__ == "__main__":

    # Create a character object
    character = playerCharacter("Bob", "Warrior", 10, 10, 10, 10, 10, "Sword", "Shield", 10, 10, 10, 10, 1, 0, 0, "password")

    # Create a weapon object
    weapon = Weapon(1, "Sword", "A sword", 10, 1, "Fantasy", 10, 100, "Slash")
    # add the weapon to the character's inventory
    character.add_to_inventory(weapon)
    print(weapon.__str__() + "\n")
    print()

    # Create an armor object
    armor = Armor(2, "Shield", "A shield", 10, 1, "Fantasy", 10, 100, "Slash")
    # add the armor to the character's inventory
    character.add_to_inventory(armor)
    print(armor.__str__() + "\n")
    print()

    # Create a consumable object
    consumable = Consumable(3, "Health Potion", "Restores 10 health", 10, 1, "Fantasy", "Heal")
    # add the consumable to the character's inventory
    character.add_to_inventory(consumable)
    print(consumable.__str__() + "\n")
    print()

    # Create a container object
    container = Container(4, "Chest", "A chest", 10, 1, "Fantasy", 10, False, 0, False, None, 0, None, 0, 0, "Closed", False)
    # add the container to the character's inventory
    character.add_to_inventory(container)
    print(container.__str__() + "\n")
    print()

    # Create a key object
    key = Key(5, "Key", "A key", 10, 1, "Fantasy", 1)
    # add the key to the character's inventory
    character.add_to_inventory(key)
    print(key.__str__() + "\n")
    print()

    # Create a quest item object
    questItem = QuestItem(6, "Quest Item", "A quest item", 10, 1, "Fantasy", "Quest")
    # add the quest item to the character's inventory
    character.add_to_inventory(questItem)
    print(questItem.__str__() + "\n")
    print()

    # Create a currency object
    currency = Currency(7, "Gold", "Gold", 10, 1, "Fantasy", "Gold")
    # add the currency to the character's inventory
    character.add_to_inventory(currency)
    print(currency.__str__() + "\n")
    print()

    # print character object
    print(character.print_character())
    print()

    # remove the weapon from the character's inventory
    print("(1) Removing sword...\n\n")
    character.remove_from_inventory(weapon)
    input("Press Enter to continue...\n\n")

    # print the character's inventory
    print("(2) Listing inventory...\n\n")
    print(character.inventory.list_items())
    input("Press Enter to continue...\n\n")

    # add the weapon to the character's inventory
    print("(3) Adding sword...\n\n")
    character.add_to_inventory(weapon)
    input("Press Enter to continue...\n\n")

    # print the character's inventory
    print("(4) Listing inventory...\n\n")
    print(character.inventory.list_items()) 
    input("Press Enter to continue...\n\n")

    # check if the character has the weapon in their inventory
    print(f"Character has sword: {character.inventory.item_exists(weapon.name)}")

    # check if the character has the armor in their inventory
    print(f"Character has armor: {character.inventory.item_exists(armor.name)}")

    # check if the character has the consumable in their inventory
    print(f"Character has potion: {character.inventory.item_exists(consumable.name)}")

    # check if the character has the container in their inventory
    print(f"Character has chest: {character.inventory.item_exists(container.name)}")

    # check if the character has the key in their inventory
    print(f"Character has Key: {character.inventory.item_exists(key.name)}")

    # check if the character has the quest item in their inventory
    print(f"Character has Quest Item: {character.inventory.item_exists(questItem.name)}")

    # check if the character has the currency in their inventory
    print(f"Character has Currency: {character.inventory.item_exists(currency.name)}")

    # open the container
    print("(5) Opening container...\n\n")
    container.open()
    input("Press Enter to continue...\n\n")

    # print the character's inventory
    print("(6) Listing inventory...\n\n")
    print(character.inventory.list_items())
    input("Press Enter to continue...\n\n")

    # add the sword to the container from the player's inventory
    print("(7) Add sword to container...\n\n")
    character.add_item_to_container(weapon, container)
    input("Press Enter to continue...\n\n")

    # print the character's inventory
    print("(8) Listing inventory...\n\n")
    print(character.inventory.list_items())
    input("Press Enter to continue...\n\n")

    # print the container's contents
    print("(9) Listing container contents...\n\n")
    print(container.inventory.list_items())
    input("Press Enter to continue...\n\n")

    # remove the sword from the container
    print("(10) Removing sword from container...\n\n")
    character.remove_item_from_container(weapon, container)
    input("Press Enter to continue...\n\n")

    # print the character's inventory
    print("(11) Listing inventory...\n\n")
    print(character.inventory.list_items())
    input("Press Enter to continue...\n\n")

    # print the container's contents
    print("(12) Listing container contents...\n\n")
    print(container.inventory.list_items())
    input("Press Enter to continue...\n\n")

