# WeightCalc.py
# Calculate the weight of an item based on its material and type
#

import random
from GamePackages.Models.GameItems import ItemModel

# Default material weights

GLASSWEIGHT = 0.5
CLOTHWEIGHT = 0.7
LEATHERWEIGHT = 1.1
WOODWEIGHT = 1.3
STONEWEIGHT = 0.9
IRONWEIGHT = 3
STEELWEIGHT = 5
MITHRILWEIGHT = 8.5
FANTACITEWEIGHT = 15

# Default type weights

CONSUMABLEWEIGHT = 0.2
DAGGERWEIGHT = 0.3
SHORTSWORDWEIGHT = 0.6
SWORDWEIGHT = 1
FALCHIONWEIGHT = 1.5
AXEWEIGHT = 1.5
MACEWEIGHT = 3.0
STAFFWEIGHT = 1.5
SLINGSHOTWEIGHT = 0.2
BOWWEIGHT = 1.5
JAVALINWEIGHT = 0.5
CROSSBOWWEIGHT = 2
TWOHANDEDWEIGHT = 3.5
CLUBWEIGHT = 2.5
SLINGWEIGHT = 0.5
KEYWEIGHT = 0.1
QUESTITEMWEIGHT = 0.1
COINWEIGHT = 0.1
CURRENCYWEIGHT = 0.1

ARMORROBEWEIGHT = 0.5
ARMORLEATHERWEIGHT = 3.5
ARMORCHAINMAILWEIGHT = 15
ARMORIRONPLATEWEIGHT = 35
ARMORSTEELPLATEWEIGHT = 70
ARMORMITHRILCHAINWEIGHT = 20
ARMORMITHRILPLATEWEIGHT = 40
ARMORDRAGONSCALEWEIGHT = 50
ARMORFANTACITECHAINWEIGHT = 15
ARMORFANTACITEPLATEWEIGHT = 30

# Determine the Item material

def calculate_material(item):
    if item.material == ItemModel.Material.GLASS:
        item.weight = GLASSWEIGHT
    elif item.material == ItemModel.Material.CLOTH:
        item.weight = CLOTHWEIGHT
    elif item.material == ItemModel.Material.LEATHER:
        item.weight = LEATHERWEIGHT
    elif item.material == ItemModel.Material.WOOD:
        item.weight = WOODWEIGHT
    elif item.material == ItemModel.Material.STONE:
        item.weight = STONEWEIGHT
    elif item.material == ItemModel.Material.IRON:
        item.weight = IRONWEIGHT
    elif item.material == ItemModel.Material.STEEL:
        item.weight = STEELWEIGHT
    elif item.material == ItemModel.Material.MITHRIL:
        item.weight = MITHRILWEIGHT
    elif item.material == ItemModel.Material.FANTACITE:
        item.weight = FANTACITEWEIGHT
    else:
        item.weight = 0
    return item.weight

# Determine the Item type

def calculate_type(item):
    if item.type == ItemModel.ItemType.CONSUMABLE:
        item.weight = CONSUMABLEWEIGHT
    elif item.type == ItemModel.ItemType.DAGGER:
        item.weight = DAGGERWEIGHT
    elif item.type == ItemModel.ItemType.SHORTSWORD:
        item.weight = SHORTSWORDWEIGHT
    elif item.type == ItemModel.ItemType.SWORD:
        item.weight = SWORDWEIGHT
    elif item.type == ItemModel.ItemType.FALCHION:
        item.weight = FALCHIONWEIGHT
    elif item.type == ItemModel.ItemType.AXE:
        item.weight = AXEWEIGHT
    elif item.type == ItemModel.ItemType.MACE:
        item.weight = MACEWEIGHT
    elif item.type == ItemModel.ItemType.STAFF:
        item.weight = STAFFWEIGHT
    elif item.type == ItemModel.ItemType.SLINGSHOT:
        item.weight = SLINGSHOTWEIGHT
    elif item.type == ItemModel.ItemType.BOW:
        item.weight = BOWWEIGHT
    elif item.type == ItemModel.ItemType.JAVALIN:
        item.weight = JAVALINWEIGHT
    elif item.type == ItemModel.ItemType.CROSSBOW:
        item.weight = CROSSBOWWEIGHT
    elif item.type == ItemModel.ItemType.TWOHANDED:
        item.weight = TWOHANDEDWEIGHT
    elif item.type == ItemModel.ItemType.KEY:
        item.weight = KEYWEIGHT
    elif item.type == ItemModel.ItemType.QUESTITEM:
        item.weight = QUESTITEMWEIGHT
    elif item.type == ItemModel.ItemType.COIN:
        item.weight = COINWEIGHT
    elif item.type == ItemModel.ItemType.CURRENCY:
        item.weight = CURRENCYWEIGHT
    elif item.type == ItemModel.ItemType.ARMOR:
        if item.material == ItemModel.Material.CLOTH:
            item.weight = ARMORROBEWEIGHT
        elif item.material == ItemModel.Material.LEATHER:
            item.weight = ARMORLEATHERWEIGHT
        elif item.material == ItemModel.Material.IRON:
            item.weight = ARMORIRONPLATEWEIGHT
        elif item.material == ItemModel.Material.STEEL:
            item.weight = ARMORSTEELPLATEWEIGHT
        elif item.material == ItemModel.Material.MITHRIL:
            item.weight = ARMORMITHRILPLATEWEIGHT
        elif item.material == ItemModel.Material.FANTACITE:
            item.weight = ARMORFANTACITEPLATEWEIGHT
        else:
            item.weight = 0
    else:
        item.weight = 0
    return item.weight

# Calculate the weight of an item based on its material and type with a small random variation
# Note: This is a very basic calculation.  It will be improved later to include enchantments, etc.

def calculate_weight(item):
    item.weight = calculate_material(item) + calculate_type(item)
    item.weight = item.weight * random.uniform(0.9, 1.1)
    return item.weight



