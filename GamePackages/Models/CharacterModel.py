# CharacterModel.py
from .InventoryModel import Inventory

class playerCharacter:
    def __init__(self, playerNum, name, character_class, strength, dexterity, intelligence, 
                 wisdom, constitution, weapon, armor, defense, attack, hitPoints, maxHitPoints, 
                 magicPoints, maxMagicPoints, level, experience, gold, pWord, currentRoomLocation, ownedRoomRange):
        self.playerNum = playerNum
        self.name = name
        self.character_class = character_class
        self.strength = strength
        self.dexterity = dexterity
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.constitution = constitution
        self.weapon = weapon
        self.armor = armor
        self.defense = defense
        self.attack = attack
        self.hitPoints = hitPoints
        self.maxHitPoints = maxHitPoints
        self.magicPoints = magicPoints
        self.maxMagicPoints = maxMagicPoints
        self.level = level
        self.experience = experience
        self.gold = gold
        self.pWord = pWord
        self.inventory = Inventory()
        self.currentRoomLocation = 0
        self.ownedRoomRange = []
        self.skills = []

    @classmethod
    def from_list(cls, char_list):
        return cls(*char_list)
    
    @staticmethod
    def xp_needed_for_next_level(current_level):
        if current_level <= 50:
            return 150 + 10 * current_level
        else:
            return int(100 * (current_level - 50) ** 2)
    
    def gain_experience(self, amount):
        self.experience += amount
        while self.experience >= playerCharacter.xp_needed_for_next_level(self.level):
            self.level += 1
            self.experience -= playerCharacter.xp_needed_for_next_level(self.level - 1)
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
        self.add_to_inventory(item)

    def equip_weapon(self, weapon):
        self.weapon = weapon
        self.attack = self.strength + weapon.attack
        self.defense = self.dexterity + weapon.defense

    def equip_armor(self, armor):
        self.armor = armor
        self.defense = self.dexterity + armor.defense

    def unequip_weapon(self):
        self.weapon = "None"
        self.attack = self.strength
        self.defense = self.dexterity

    def unequip_armor(self):
        self.armor = "None"
        self.defense = self.dexterity

    def equip_item(self, item):
        if item.item_type == "Weapon":
            self.equip_weapon(item)
        elif item.item_type == "Armor":
            self.equip_armor(item)
        else:
            print("Item type not recognized.")

    def unequip_item(self, item):
        if item.item_type == "Weapon":
            self.unequip_weapon()
        elif item.item_type == "Armor":
            self.unequip_armor()
        else:
            print("Item type not recognized.")

    def use_item(self, item):
        if item.item_type == "Consumable":
            self.hitPoints += item.hp_regen
            self.magicPoints += item.mp_regen
            self.remove_from_inventory(item)
        else:
            print("Item type not recognized.")

    def check_for_item(self, item_name):
        for item in self.inventory.items:
            if item.name == item_name:
                return True
        return False
    
    def attack_enemy(self, enemy):
        if self.attack > enemy.defense:
            damage = self.attack - enemy.defense
            enemy.hitPoints -= damage
            print("You dealt " + str(damage) + " damage to the enemy!")
        else:
            print("You dealt no damage to the enemy!")

    def cast_spell(self, spell):
        if self.magicPoints >= spell.mp_cost:
            self.magicPoints -= spell.mp_cost
            if self.intelligence > spell.magic_defense:
                damage = self.intelligence - spell.magic_defense
                spell.enemy.hitPoints -= damage
                print("You dealt " + str(damage) + " damage to the enemy!")
            else:
                print("You dealt no damage to the enemy!")
        else:
            print("You don't have enough magic points to cast this spell!")

    def rest(self):
        self.hitPoints += self.constitution
        self.magicPoints += self.wisdom
        print("You have rested and recovered some health and magic points!")

    def save_character(self):
        #convert character back to list and append to characters.csv file
        character_list = [self.name, self.character_class, self.strength, self.dexterity, self.intelligence, self.wisdom, self.constitution, self.weapon, self.armor, self.defense, self.attack, self.hitPoints, self.magicPoints, self.level, self.experience, self.gold, self.pWord]
        with open("characters.csv", "a") as file:
            file.write(",".join([str(x) for x in character_list]) + "\n")

    def print_character(self):
        print("Name: " + self.name)
        print("Class: " + self.character_class)
        print("Strength: " + str(self.strength))
        print("Dexterity: " + str(self.dexterity))
        print("Intelligence: " + str(self.intelligence))
        print("Wisdom: " + str(self.wisdom))
        print("Constitution: " + str(self.constitution))
        print("Weapon: " + self.weapon)
        print("Armor: " + self.armor)
        print("Defense: " + str(self.defense))
        print("Attack: " + str(self.attack))
        print("Hit Points: " + str(self.hitPoints))
        print("Magic Points: " + str(self.magicPoints))
        print("Level: " + str(self.level))
        print("Experience: " + str(self.experience))
        print("Gold: " + str(self.gold))
        print("Inventory: ")
        # Print the items in the inventory
        self.inventory.list_items()
        print()

class Mage(playerCharacter):
    def __init__(self, name, strength, dexterity, intelligence, wisdom, 
                 constitution, weapon, armor, defense, attack, hitPoints, 
                 magicPoints, level, experience, gold, pWord):
        super().__init__(name, "Mage", strength, dexterity, intelligence, 
                         wisdom, constitution, weapon, armor, defense, attack, 
                         hitPoints, magicPoints, level, experience, gold, pWord)
        self.skills = [
            {"name": "Fireball", "level": 0},
            {"name": "Frostbolt", "level": 0}
        ]

    def check_skill_upgrade(self):
        # Upgrade skills based on the character's level
        if self.level == 3:
            self._upgrade_skill("Fireball", 1)
        elif self.level == 5:
            self._upgrade_skill("Fireball", 2)
            self._upgrade_skill("Frostbolt", 1)
        elif self.level == 7:
            self._upgrade_skill("Frostbolt", 2)

    def _upgrade_skill(self, skill_name, new_level):
        for skill in self.skills:
            if skill["name"] == skill_name:
                skill["level"] = new_level

    def cast_fireball(self):
        skill_level = self._get_skill_level("Fireball")
        if skill_level == 1:
            print("Fireball Level 1: Dealt 10 damage!")
        elif skill_level == 2:
            print("Fireball Level 2: Dealt 20 damage and has a shorter cooldown!")
        else:
            print("Skill not acquired yet.")

    def cast_frostbolt(self):
        skill_level = self._get_skill_level("Frostbolt")
        if skill_level == 1:
            print("Frostbolt Level 1: Dealt 5 damage and slowed the enemy!")
        elif skill_level == 2:
            print("Frostbolt Level 2: Dealt 10 damage and froze the enemy!")
        else:
            print("Skill not acquired yet.")

    def _get_skill_level(self, skill_name):
        for skill in self.skills:
            if skill["name"] == skill_name:
                return skill["level"]
        return 0
