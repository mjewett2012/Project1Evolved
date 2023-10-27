# ThemeModel.py
# Enum for the different themes in the game

from enum import Enum

class Theme(Enum):
    PLAINS = 1
    FOREST = 2
    MOUNTAIN = 3
    DESERT = 4
    SWAMP = 5
    OCEAN = 6
    RIVER = 7
    LAKE = 8
    CAVE = 9

    def __str__(self):
        if self == Theme.PLAINS:
            return "plains"
        elif self == Theme.FOREST:
            return "forest"
        elif self == Theme.MOUNTAIN:
            return "mountain"
        elif self == Theme.DESERT:
            return "desert"
        elif self == Theme.SWAMP:
            return "swamp"
        elif self == Theme.OCEAN:
            return "ocean"
        elif self == Theme.RIVER:
            return "river"
        elif self == Theme.LAKE:
            return "lake"
        elif self == Theme.CAVE:
            return "cave"
        else:
            return "unknown"
        
    @staticmethod
    def from_string(theme):
        if theme == "plains":
            return Theme.PLAINS
        elif theme == "forest":
            return Theme.FOREST
        elif theme == "mountain":
            return Theme.MOUNTAIN
        elif theme == "desert":
            return Theme.DESERT
        elif theme == "swamp":
            return Theme.SWAMP
        elif theme == "ocean":
            return Theme.OCEAN
        elif theme == "river":
            return Theme.RIVER
        elif theme == "lake":
            return Theme.LAKE
        elif theme == "cave":
            return Theme.CAVE
        else:
            return None