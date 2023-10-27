import sys
import random

def exit_program():
    print("The world still needs you.  Come back!")
    sys.exit()

def dice_roller(low, high):
    roll = random.randint(low, high)
    return roll

def stat_calculator(myClass, strength, dexterity, intelligence, wisdom, constitution, formatted=False):
    if myClass == "Warrior":
        defense = round(10 + dexterity/10)
        attack = round(10 + strength/10)
        hitPoints = round(10 + constitution/10)
        magicPoints = round(10 + intelligence/10)
    elif myClass == "Rogue":
        defense = round(10 + dexterity/10)
        attack = round(10 + strength/10)
        hitPoints = round(10 + constitution/10)
        magicPoints = round(10 + intelligence/10)
    elif myClass == "Priest":
        defense = round(10 + dexterity/10)
        attack = round(10 + strength/10)
        hitPoints = round(10 + constitution/12)
        magicPoints = round(10 + wisdom/7)
    elif myClass == "Wielder":
        defense = round(10 + dexterity/12)
        attack = round(10 + strength/12)
        hitPoints = round(10 + constitution/10)
        magicPoints = round(10 + intelligence/6)

    if formatted:
        return f"Defense: {defense}\nAttack: {attack}\nHit Points: {hitPoints}\nMagic Points: {magicPoints}"
    else:
        return defense, attack, hitPoints, magicPoints

def ordinal_suffix_of(i):
    # Returns the ordinal suffix of a number
    # Example: 1st, 2nd, 3rd, 4th, etc.
    level = int(i)
    j = level % 10
    k = level % 100
    if (j == 1 and k != 11):
        return str(i) + "st"
    if (j == 2 and k != 12):
        return str(i) + "nd"
    if (j == 3 and k != 13):
        return str(i) + "rd"
    return str(i) + "th"