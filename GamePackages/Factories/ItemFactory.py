# ItemFactory.py
# ItemFactory.py is a factory class that creates Item objects.  
# It is used by the RoomFactory and the MobFactory to create Item objects
# that are added to the roomInventory of a Room object or the inventory of a Mob object.
#
# Parameters: None
#
# Return: None
#
# Example:
# itemFactory = ItemFactory()
import random
import os
import pickle
from GamePackages.Data import Data
from GamePackages.Models.GameItems import ItemModel
from Factories import TextGenerator
from GamePackages.Calculators import ValueCalc
from GamePackages.Calculators import WeightCalc

def Item_create(material, rarity):
    # Create an Item object based on the material and rarity
    # 
    # Parameters:
    #     material:  The material of the item
    #     rarity:  The rarity of the item
    # 
    # Return:
    #     item:  An Item object
    # 
    # Example:
    #     item = Item_create("iron", "common")
    # 
    # Note:  Handle Keys and Quest Items differently based on item name and description
    item = ItemModel()
    item.material = material
    item.rarity = rarity
    item.name = TextGenerator.generate_item_name(material, rarity)
    item.description = TextGenerator.generate_item_description(material, rarity)
    item.weight = ValueCalc.calculate_weight(item)
    item.value = ValueCalc.calculate_value(item)
    return item

def Item_create_from_string(itemString):
    # Create an Item object from a string
    # 
    # Parameters:
    #     itemString:  A string representation of an Item object
    # 
    # Return:
    #     item:  An Item object
    # 
    # Example:
    #     item = Item_create_from_string("iron,common,iron sword,an iron sword,3.0,3.0")
    # 
    # Check the name and description of the item and pull keywords to determine their class, 
    # type, material, and rarity

    # Split the string into a list
    itemList = itemString.split(",")
    # Create an Item object
    item = ItemModel()
    # find and set the material
    
    
