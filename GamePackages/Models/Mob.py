# Mob.py
# The Mob class is the parent class for all monsters in the game.  It contains the basic attributes 
# and methods that all monsters will have.

# Parameters: name - The name of the monster.
#             strength - The strength of the monster.
#             dexterity - The dexterity of the monster.
#             intelligence - The intelligence of the monster.
#             wisdom - The wisdom of the monster.
#             constitution - The constitution of the monster.
#             weapon - The weapon of the monster.
#             armor - The armor of the monster.
#             hitPoints - The hit points of the monster.
#             magicPoints - The magic points of the monster.
#             level - The level of the monster.
#             experience - The experience of the monster.
#             gold - The gold of the monster.
 
# Return: None

# Example:
# monster = Mob("Goblin", 5, 5, 5, 5, 5, "Dagger", "Leather Armor", 10, 10, 1, 0, 0)
import pickle
from GamePackages.Models.InventoryModel import Inventory
from GamePackages.Models.ThemeModel import Theme
class Mob:
    def __init__(self, mobNum, name, strength, dexterity, intelligence, wisdom, constitution, 
                 weapon, armor, hitPoints, maxHitPoints, magicPoints, maxMagicPoints, level,
                    experience, gold, worldTheme, currentRoomLocation):
        self.mobNum = mobNum
        self.name = name
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution
        self.weapon = weapon
        self.armor = armor
        self.hitPoints = hitPoints
        self.maxHitPoints = maxHitPoints
        self.magicPoints = magicPoints
        self.maxMagicPoints = maxMagicPoints
        self.level = level
        self.experience = experience
        self.gold = gold
        self.worldTheme = ThemeModel.Theme(worldTheme)
        self.currentRoomLocation = currentRoomLocation
        self.inventory = InventoryModel()
        self.skills = []
    
    @classmethod
    def from_list(cls, mob_list):
        return cls(*mob_list)
    
    @staticmethod
    def xp_needed_for_next_level(current_level):
        if current_level <= 50:
            return 150 + 10 * current_level
        else:
            return int(100 * (current_level - 50) ** 2)
    
    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= Mob.xp_needed_for_next_level(self.level):
            self.level += 1
            self.experience -= Mob.xp_needed_for_next_level(self.level - 1)
            self.check_skill_upgrade()

    def check_skill_upgrade(self):
        # This method should be overridden by subclasses to upgrade skills
        pass
    
    def add_to_inventory(self, item):
        self.inventory.add_item(item)

    def remove_from_inventory(self, item):
        self.inventory.remove_item(item)
    
    def add_item_to_container(self, item, container):
        container.inventory.add_item(item)
        self.remove_from_inventory(item)

    def remove_item_from_container(self, item, container):
        container.inventory.remove_item(item)
        
    # save the mob to a binary file containing all mobs in the game, also save the mob as an active instance of the mob with current stats and location
                