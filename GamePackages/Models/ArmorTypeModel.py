# ArmorTypeModel.py
# ArmorTypeModel.py is an enum class that defines the different types of armor in the game.

from enum import Enum

class ArmorType(Enum):
    CLOTH = 1 # This is the default armor type / Common armor type
    ROBES = 2 # This is the default armor type for Wielders / Common armor type
    LEATHER = 3 # This is the default armor type for Rogues / Common armor type
    CHAINMAIL = 4 # This is the default armor type for Warriors / Common armor type
    IRONPLATE = 5 # This is an uncommon armor type
    STEELPLATE = 6 # This is a rare armor type
    MITHRILCHAIN = 7 # This is a rare armor type
    MITHRILPLATE = 8 # This is a  very rare armor type
    DRAGONSCALE = 9 # This is a incredibly rare armor type
    FANTACITECHAIN = 10 # This is an almost impossible armor type to get
    FANTACITEPLATE = 11 # This is an almost impossible armor type to get


    def __str__(self):
        if self == ArmorType.CLOTH:
            return "cloth"
        elif self == ArmorType.ROBES:
            return "robes"
        elif self == ArmorType.LEATHER:
            return "leather"
        elif self == ArmorType.CHAINMAIL:
            return "chainmail"
        elif self == ArmorType.IRONPLATE:
            return "iron plate"
        elif self == ArmorType.STEELPLATE:
            return "steel plate"
        elif self == ArmorType.MITHRILCHAIN:
            return "mithril chain"
        elif self == ArmorType.MITHRILPLATE:
            return "mithril plate"
        elif self == ArmorType.DRAGONSCALE:
            return "dragon scale"
        elif self == ArmorType.FANTACITECHAIN:
            return "fantacite chain"
        elif self == ArmorType.FANTACITEPLATE:
            return "fantacite plate"
        else:
            return "unknown"
        
    @staticmethod
    def from_string(armorType):
        if armorType == "cloth":
            return ArmorType.CLOTH
        elif armorType == "robes":
            return ArmorType.ROBES
        elif armorType == "leather":
            return ArmorType.LEATHER
        elif armorType == "chainmail":
            return ArmorType.CHAINMAIL
        elif armorType == "iron plate":
            return ArmorType.IRONPLATE
        elif armorType == "steel plate":
            return ArmorType.STEELPLATE
        elif armorType == "mithril chain":
            return ArmorType.MITHRILCHAIN
        elif armorType == "mithril plate":
            return ArmorType.MITHRILPLATE
        elif armorType == "dragon scale":
            return ArmorType.DRAGONSCALE
        elif armorType == "fantacite chain":
            return ArmorType.FANTACITECHAIN
        elif armorType == "fantacite plate":
            return ArmorType.FANTACITEPLATE
        else:
            return None