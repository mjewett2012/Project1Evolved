# ValueCalc.py
# Calculate values of items

from GamePackages.Models.GameItems import ItemModel

# Default material values
# 
# Material values are used to calculate the value of an item based on the material it is made of.
# 
# Example:  A sword made of steel is worth more than a sword made of wood.
# 
# The value of an item is calculated by adding the value of the item to the value of the material 
# it is made of multiplied by its weight. The value of the material is determined by the material's rarity. 
#     

# Materials
GLASSVALUE = 0.5
CLOTHVALUE = 0.7
LEATHERVALUE = 1.1
WOODVALUE = 1.3
STONEVALUE = 0.9
IRONVALUE = 3
STEELVALUE = 5
MITHRILVALUE = 8.5
FANTACITEVALUE = 15

# ITEM BY RARITY

# Common
COMMONVALUE = 1
UNCOMMONVALUE = 1.5
RAREVALUE = 2
ELITEVALUE = 3
LEGENDARYVALUE = 5
ANCIENTVALUE = 8
UNIQUEVALUE = 13

# calculate the value of an item based on its material, weight, and rarity
# Note: This is a very basic calculation.  It will be improved later to include enchantments, etc.
def calculate_value(item):
    value = 0
    if item.material == ItemModel.Material.GLASS:
        value = GLASSVALUE
    elif item.material == ItemModel.Material.CLOTH:
        value = CLOTHVALUE
    elif item.material == ItemModel.Material.LEATHER:
        value = LEATHERVALUE
    elif item.material == ItemModel.Material.WOOD:
        value = WOODVALUE
    elif item.material == ItemModel.Material.STONE:
        value = STONEVALUE
    elif item.material == ItemModel.Material.IRON:
        value = IRONVALUE
    elif item.material == ItemModel.Material.STEEL:
        value = STEELVALUE
    elif item.material == ItemModel.Material.MITHRIL:
        value = MITHRILVALUE
    elif item.material == ItemModel.Material.FANTACITE:
        value = FANTACITEVALUE
    else:
        value = 0
    return value * item.weight * item.rarity
