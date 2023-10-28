# EffectModel.py
# EffectModel.py is a class that defines the Effect object.  An Effect object 
# is used to define the effects of an Item object.  For example, a Potion of
# Healing would have an Effect object that heals the player when the Potion of
# Healing is used.  A Potion of Poison would have an Effect object that poisons
# the player when the Potion of Poison is used. A Potion of Strength would have
# an Effect object that increases the player's strength when the Potion of 
# Strength is used.  A Potion of Dexterity would have an Effect object that
# increases the player's dexterity when the Potion of Dexterity is used, etc. 
import enum

class Effect(enum.Enum):
    # CONSUMABLE EFFECTS
    HEAL = 1
    POISON = 2
    STRENGTH = 3
    DEXTERITY = 4
    INTELLIGENCE = 5
    WISDOM = 6
    MAGICREGEN = 7
    CONSTITUTION = 8
    ARMOR = 9
    DAMAGE = 10
    SPEED = 11
    SIGHT = 12
    INVISIBILITY = 13
    FLYING = 14
    WATER_BREATHING = 15
    # ARMOR EFFECTS
    FIRE_RESISTANCE = 16
    COLD_RESISTANCE = 17
    ELECTRIC_RESISTANCE = 18
    TOXIC_RESISTANCE = 19
    PSYCHIC_RESISTANCE = 20
    SONIC_RESISTANCE = 21
    DISEASE_RESISTANCE = 22
    RADIANT_RESISTANCE = 23
    NECROTIC_RESISTANCE = 24
    ACID_RESISTANCE = 25
    DRAIN_RESISTANCE = 26
    # WEAPON EFFECTS
    FLAMING = 27 # May cause burn status
    FROSTED = 28 # May cause slow status
    SHOCKING = 29 
    POISONED = 30 # May cause poison status
    PSYCHIC = 31 # May cause stun status
    SONIC = 32 
    DISEASED = 33 # May cause disease status
    RADIANT = 34 # extra damage to undead
    NECROTIC = 35 # extra damage to living
    ACID = 36 # May cause acid status
    DRAINING = 37 # Drains life from the target and gives it to the wielder / VERY RARE
    # MOB EFFECTS
    PROTECTED = 38 # Mob takes half damage
    STRENGTHENEDMOB = 39 # Mob deals extra damage
    FORTIFIED = 40 # Mob has extra health
    ENRAGED = 41 # Mob has extra speed
    INVISIBLE = 42 # Mob is invisible
    FLYINGMOB = 43 # Mob can fly
    INFERNO = 44 # Mob is on fire
    FROZEN = 45 # Mob is frozen
    # PLAYER EFFECTS
    BLESSED = 46 # Player has a higher chance to hit
    CURSED = 47 # Player has a lower chance to hit
    ENLIGHTENED = 48 # Player has a higher chance to dodge
    CONFUSED = 49 # Player has a lower chance to dodge
    PROTECTION = 50 # Player takes half damage
    STRENGTHENED = 51 # Player deals extra damage
    AIDED = 52 # Player has extra health
    HASTED = 53 # Player has extra speed
    STEALTHED = 54 # Player is hidden
    FLIGHT = 55 # Player can fly
    

