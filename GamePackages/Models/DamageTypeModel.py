# DamageTypeModel.py
# DamageTypeModel.py is an enum class that defines the different types of damage in the game.

from enum import Enum

class DamageType(Enum):
    FORCE = 1 # This is the default damage type / Physical damage type
    ARCANE = 2 # This is the default damage type for Wielders / Magical damage type
    DIVINE = 3 # This is the default damage type for Priests / Magical damage type
    HEAT = 4 # Fire damage type / Check for damage over time
    COLD = 5 # Ice damage type / Check for damage over time
    ELECTRIC = 6 # Lightning damage type
    TOXIC = 7 # Poison damage type / Check for damage over time
    PSYCHIC = 8 # Mental damage type
    SONIC = 9 # Sound damage type
    DISEASE = 10 # Disease damage type / Check for damage over time
    RADIANT = 11 # Holy damage type
    NECROTIC = 12 # Unholy damage type
    ACID = 13 # Acid damage type / Check for damage over time
    DRAIN = 14 # Drain damage type / Special damage type
    FANTACITE = 15 # Fantacite damage type / Special damage type

    def __str__(self):
        if self == DamageType.FORCE:
            return "force"
        elif self == DamageType.ARCANE:
            return "arcane"
        elif self == DamageType.DIVINE:
            return "divine"
        elif self == DamageType.HEAT:
            return "heat"
        elif self == DamageType.COLD:
            return "cold"
        elif self == DamageType.ELECTRIC:
            return "electric"
        elif self == DamageType.TOXIC:
            return "toxic"
        elif self == DamageType.PSYCHIC:
            return "psychic"
        elif self == DamageType.SONIC:
            return "sonic"
        elif self == DamageType.DISEASE:
            return "disease"
        elif self == DamageType.RADIANT:
            return "radiant"
        elif self == DamageType.NECROTIC:
            return "necrotic"
        elif self == DamageType.ACID:
            return "acid"
        elif self == DamageType.DRAIN:
            return "drain"
        elif self == DamageType.FANTACITE:
            return "fantacite"
        else:
            return "unknown"
        
    @staticmethod
    def from_string(damageType):
        if damageType == "force":
            return DamageType.FORCE
        elif damageType == "arcane":
            return DamageType.ARCANE
        elif damageType == "divine":
            return DamageType.DIVINE
        elif damageType == "heat":
            return DamageType.HEAT
        elif damageType == "cold":
            return DamageType.COLD
        elif damageType == "electric":
            return DamageType.ELECTRIC
        elif damageType == "toxic":
            return DamageType.TOXIC
        elif damageType == "psychic":
            return DamageType.PSYCHIC
        elif damageType == "sonic":
            return DamageType.SONIC
        elif damageType == "disease":
            return DamageType.DISEASE
        elif damageType == "radiant":
            return DamageType.RADIANT
        elif damageType == "necrotic":
            return DamageType.NECROTIC
        elif damageType == "acid":
            return DamageType.ACID
        elif damageType == "drain":
            return DamageType.DRAIN
        elif damageType == "fantacite":
            return DamageType.FANTACITE
        else:
            return None