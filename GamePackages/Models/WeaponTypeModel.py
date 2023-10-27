# WeaponTypeModel.py
# WeaponTypeModel.py is an enum class that defines the different types of weapons in the game.

from enum import Enum

class DamageType(Enum):
    BLUDGEONING = 1
    PIERCING = 2
    SLASHING = 3

    def __str__(self):
        if self == DamageType.BLUDGEONING:
            return "bludgeoning"
        elif self == DamageType.PIERCING:
            return "piercing"
        elif self == DamageType.SLASHING:
            return "slashing"
        else:
            return "unknown"

    @staticmethod
    def from_string(DamageType):
        if DamageType == "bludgeoning":
            return DamageType.BLUDGEONING
        elif DamageType == "piercing":
            return DamageType.PIERCING
        elif DamageType == "slashing":
            return DamageType.SLASHING
        else:
            return None    
        
class WeaponType(Enum):
    DAGGER = 1
    SHORTSWORD = 2
    SWORD = 3
    FALCHION = 4
    AXE = 5
    MACE = 6
    STAFF = 7
    SLINGSHOT = 8
    BOW = 9
    JAVALIN = 10
    CROSSBOW = 11
    TWOHANDED = 12
    CLUB = 13
    SLING = 14
    RAPIER = 15
    GLAIVE = 16
    TRIDENT = 17
    SPEAR = 18
    SCIMITAR = 19
    FLAIL = 20
    MORNINGSTAR = 21    
    SICKLE = 22
    SAI = 23
    KATANA = 24
    NUNCHUCKS = 25
    KAMA = 26
    BOOMERANG = 27
    SABER = 28

    def __str__(self):
        if self == WeaponType.DAGGER:
            return "dagger"
        elif self == WeaponType.SHORTSWORD:
            return "shortsword"
        elif self == WeaponType.SWORD:
            return "sword"
        elif self == WeaponType.FALCHION:
            return "falchion"
        elif self == WeaponType.AXE:
            return "axe"
        elif self == WeaponType.MACE:
            return "mace"
        elif self == WeaponType.STAFF:
            return "staff"
        elif self == WeaponType.SLINGSHOT:
            return "slingshot"
        elif self == WeaponType.BOW:
            return "bow"
        elif self == WeaponType.JAVALIN:
            return "javalin"
        elif self == WeaponType.CROSSBOW:
            return "crossbow"
        elif self == WeaponType.TWOHANDED:
            return "two handed"
        elif self == WeaponType.CLUB:
            return "club"
        elif self == WeaponType.SLING:
            return "sling"
        elif self == WeaponType.RAPIER:
            return "rapier"
        elif self == WeaponType.GLAIVE:
            return "glaive"
        elif self == WeaponType.TRIDENT:
            return "trident"
        elif self == WeaponType.SPEAR:
            return "spear"
        elif self == WeaponType.SCIMITAR:
            return "scimitar"
        elif self == WeaponType.FLAIL:
            return "flail"
        elif self == WeaponType.MORNINGSTAR:
            return "morningstar"
        elif self == WeaponType.SICKLE:
            return "sickle"
        elif self == WeaponType.SAI:
            return "sai"
        elif self == WeaponType.KATANA:
            return "katana"
        elif self == WeaponType.NUNCHUCKS:
            return "nunchucks"
        elif self == WeaponType.KAMA:
            return "kama"
        elif self == WeaponType.BOOMERANG:
            return "boomerang"
        elif self == WeaponType.SABER:
            return "saber"
        else:
            return "unknown"
        
    @staticmethod
    def from_string(weaponType):
        if weaponType == "dagger":
            return WeaponType.DAGGER
        elif weaponType == "shortsword":
            return WeaponType.SHORTSWORD
        elif weaponType == "sword":
            return WeaponType.SWORD
        elif weaponType == "falchion":
            return WeaponType.FALCHION
        elif weaponType == "axe":
            return WeaponType.AXE
        elif weaponType == "mace":
            return WeaponType.MACE
        elif weaponType == "staff":
            return WeaponType.STAFF
        elif weaponType == "slingshot":
            return WeaponType.SLINGSHOT
        elif weaponType == "bow":
            return WeaponType.BOW
        elif weaponType == "javalin":
            return WeaponType.JAVALIN
        elif weaponType == "crossbow":
            return WeaponType.CROSSBOW
        elif weaponType == "two handed":
            return WeaponType.TWOHANDED
        elif weaponType == "club":
            return WeaponType.CLUB
        elif weaponType == "sling":
            return WeaponType.SLING
        elif weaponType == "rapier":
            return WeaponType.RAPIER
        elif weaponType == "glaive":
            return WeaponType.GLAIVE
        elif weaponType == "trident":
            return WeaponType.TRIDENT
        elif weaponType == "spear":
            return WeaponType.SPEAR
        elif weaponType == "scimitar":
            return WeaponType.SCIMITAR
        elif weaponType == "flail":
            return WeaponType.FLAIL
        elif weaponType == "morningstar":
            return WeaponType.MORNINGSTAR
        elif weaponType == "sickle":
            return WeaponType.SICKLE
        elif weaponType == "sai":
            return WeaponType.SAI
        elif weaponType == "katana":
            return WeaponType.KATANA
        elif weaponType == "nunchucks":
            return WeaponType.NUNCHUCKS
        elif weaponType == "kama":
            return WeaponType.KAMA
        elif weaponType == "boomerang":
            return WeaponType.BOOMERANG
        elif weaponType == "saber":
            return WeaponType.SABER
        else:
            return None
        
    @staticmethod
    def get_damage_type(weaponType):
        if weaponType == WeaponType.DAGGER:
            return DamageType.PIERCING
        elif weaponType == WeaponType.SHORTSWORD:
            return DamageType.PIERCING
        elif weaponType == WeaponType.SWORD:
            return DamageType.SLASHING
        elif weaponType == WeaponType.FALCHION:
            return DamageType.SLASHING
        elif weaponType == WeaponType.AXE:
            return DamageType.SLASHING
        elif weaponType == WeaponType.MACE:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.STAFF:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.SLINGSHOT:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.BOW:
            return DamageType.PIERCING
        elif weaponType == WeaponType.JAVALIN:
            return DamageType.PIERCING
        elif weaponType == WeaponType.CROSSBOW:
            return DamageType.PIERCING
        elif weaponType == WeaponType.TWOHANDED:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.CLUB:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.SLING:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.RAPIER:
            return DamageType.PIERCING
        elif weaponType == WeaponType.GLAIVE:
            return DamageType.SLASHING
        elif weaponType == WeaponType.TRIDENT:
            return DamageType.PIERCING
        elif weaponType == WeaponType.SPEAR:
            return DamageType.PIERCING
        elif weaponType == WeaponType.SCIMITAR:
            return DamageType.SLASHING
        elif weaponType == WeaponType.FLAIL:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.MORNINGSTAR:
            return DamageType.PIERCING
        elif weaponType == WeaponType.SICKLE:
            return DamageType.SLASHING
        elif weaponType == WeaponType.SAI:
            return DamageType.PIERCING
        elif weaponType == WeaponType.KATANA:
            return DamageType.SLASHING
        elif weaponType == WeaponType.NUNCHUCKS:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.KAMA:
            return DamageType.SLASHING
        elif weaponType == WeaponType.BOOMERANG:
            return DamageType.BLUDGEONING
        elif weaponType == WeaponType.SABER:
            return DamageType.SLASHING
        else:
            return None

        