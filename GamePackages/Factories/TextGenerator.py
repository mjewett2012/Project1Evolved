# TextGenerator.py
# NTextGenerator.py is a class that generates random names and descriptions for Rooms, Mobs, and Items.
# It is used by the RoomFactory, MobFactory, and ItemFactory to generate names and descriptions for
# the objects they create.

import random
import os
from Models import RoomModel
from Models import MobModel
from Models import ItemModel

def text_generate(objectClass, theme, rarity=0):
    name = ""
    description = ""

    if objectClass == RoomModel.Room:
        name, description = room_text_generate(theme)
    elif objectClass == MobModel.Mob:
        name, description = mob_text_generate(theme)
    elif objectClass == ItemModel.Item:
        name, description = item_text_generate(theme, rarity)
    elif objectClass == ItemModel.Weapon:
        name, description = weapon_text_generate(theme, rarity)
    elif objectClass == ItemModel.Armor:
        name, description = armor_text_generate(theme, rarity)
    elif objectClass == ItemModel.Consumable:
        name, description = consumable_text_generate(theme, rarity)
    elif objectClass == ItemModel.Container:
        name, description = container_text_generate(theme, rarity)
    elif objectClass == ItemModel.Currency:
        name, description = currency_text_generate(rarity)
    else:
        print("Object class not recognized.")

    return name, description

def room_text_generate(theme):
    name = ""
    description = ""

    prefix = random.choice(["Dark", "Airy", "Bright", "Dank", "Dusty", "Empty", "Flooded", "Gloomy", "Musty", 
                            "Quiet", "Eerie", "Spacious", "Dense", "Suffocating", "Lush", "Verdant", "Sylvan",
                            "Brushwood", "Thicket", "Wooded", "Overgrown", "Wild", "Untamed", "Rugged", "Rustic",
                            "Rural", "Remote", "Secluded", "Desolate", "Barren", "Bleak", "Blighted", "Deserted",
                            "Lonely", "Isolated", "Abandoned", "Forgotten", "Vacant", "Unoccupied", "Uninhabited",
                            "Unpeopled", "Unpopulated", "Unsettled", "Unvisited", "Unfrequented", "Unconquered",
                            "Unclaimed", "Unexplored", "Uncharted", "Unmapped" ])
    
    name += prefix + " "

    if (theme == 1):
        noun = random.choice(["Plains", "Grassland", "Grasslands", "Prairie", "Prairies", "Steppe", "Steppes",
                                "Meadow", "Meadows", "Pasture", "Pastures", "Savanna", "Savannas", "Savannah",
                                "Savannahs", "Veld", "Velds", "Veldt", "Veldts", "Tundra", "Tundras"])
        name += noun
        description = build_room_description(name)
    if (theme == 2):
        noun = random.choice(["Forest", "Wood", "Woods", "Rainforest", "Woodland", "Thicket", "Timberland",
                              "Grove", "Bush", "Backwoods", "Coppice", "Copse"])
        name += noun
        description = build_room_description(name)
    elif (theme == 3):
        noun = random.choice(["Mountain", "Mountains", "Hill", "Hills", "Peak", "Peaks", "Ridge", "Ridges", "Range",
                              "Crest", "Crests", "Summit", "Summits", "Pinnacle", "Pinnacles", "Alp", "Alps",
                              "Alpine", "Alpines", "Alpine Meadow", "Alpine Meadows", "Alpine Pasture",
                              "Alpine Pastures", "Alpine Steppe", "Alpine Steppes", "Alpine Tundra",
                              "Alpine Tundras", "Alpine Desert", "Alpine Deserts", "Alpine Forest",
                              "Alpine Forests", "Alpine Wood", "Alpine Woods", "Alpine Woodland",
                              "Alpine Woodlands", "Alpine Thicket", "Alpine Thickets", "Alpine Brushwood",
                              "Alpine Brushwoods", "Alpine Timberland", "Alpine Timberlands", "Alpine Grove",
                              "Alpine Groves", "Alpine Bush", "Alpine Bushes", "Alpine Backwoods",
                              "Alpine Coppice", "Alpine Coppices", "Alpine Copse"])
        name += noun
        description = build_room_description(name)
    elif (theme == 4):
        noun = random.choice(["Desert", "Deserts", "Badlands", "Badland", "Wasteland", "Wastelands", "Barrens", 
                              "Sands", "Sand", "Dunes", "Dune", "Dust", "Dusts", "Drylands", "Dryland", "Salt Flat",
                                "Salt Flats", "Salt Pan", "Salt Pans", "Salt Marsh", "Salt Marshes", "Salt Desert",
                                "Salt Deserts", "Salt Steppe", "Salt Steppes", "Salt Tundra", "Salt Tundras", "Dust Bowl",
                                "Dust Bowls", "Sand Bowl", "Sand Bowls", "Dune Bowl", "Dune Bowls", "Salt Bowl", 
                                "Sandsea", "Sandseas", "Sand Sea", "Sand Seas", "Dune Sea", "Dune Seas", "Saltsea",
                                "Saltseas", "Salt Sea", "Salt Seas"])
        name += noun
        description = build_room_description(name)
    elif (theme == 5):
        noun = random.choice(["Swamp", "Swamps", "Marsh", "Marshes", "Bog", "Bogs", "Fen", "Fens", "Mire", "Mires",
                                "Wetland", "Wetlands", "Everglade", "Everglades", "Bayou", "Bayous", "Slough", "Sloughs",
                                "Sluice", "Sluices", "Sump", "Sumps", "Wallow", "Wallows", "Quagmire", "Quagmires"])
        name += noun
        description = build_room_description(name)
    elif (theme == 6):
        noun = random.choice(["Ocean", "Oceans", "Sea", "Seas", "Gulf", "Gulfs", "Bay", "Bays", "Sound", "Sounds"])
        name += noun
        description = build_room_description(name)
    elif (theme == 7):
        noun = random.choice(["River", "Rivers", "Stream", "Streams", "Creek", "Creeks", "Brook", "Brooks", "Rivulet",
                              "Rivulets", "Runnel", "Runnels", "Run", "Runs", "Watercourse", "Watercourses", "Waterway",
                              "Waterways", "Waterfall", "Waterfalls"])
        name += noun
        description = build_room_description(name)
    elif (theme == 8):
        noun = random.choice(["Lake", "Lakes", "Pond", "Ponds", "Pool", "Pools", "Lagoon", "Lagoons", "Loch", "Lochs",
                              "Lough", "Loughs", "Mere", "Meres", "Reservoir", "Reservoirs", "Tarn", "Tarns", "Basin",
                                "Basins", "Waterhole", "Waterholes"])
        name += noun
        description = build_room_description(name)
    elif (theme == 9):
        noun = random.choice(["Cave", "Caves", "Cavern", "Caverns", "Grotto", "Grottos", "Grottoes", "Grot", "Grots",
                              "Tunnel", "Tunnels", "Burrow", "Burrows", "Den", "Dens", "Hole", "Holes", "Underground",
                                "Undergrounds", "Underworld", "Underworlds", "Underpass", "Underpasses", "Underway",
                                "Underways", "Undercroft", "Undercrofts", "Underground Chamber", "Underground Chambers",
                                "Underground Room", "Underground Rooms", "Underground Hall", "Underground Halls",
                                "Underground Passage", "Underground Passages", "Underground Corridor", "Underground Corridors",
                                "Underground Gallery", "Underground Galleries", "Underground Vault", "Underground Vaults",
                                "Underground Cavern", "Underground Caverns", "Underground Grotto", "Underground Grottos",
                                "Underground Grottoes", "Underground Grot", "Underground Grots", "Underground Tunnel",
                                "Underground Tunnels", "Underground Burrow", "Underground Burrows", "Underground Den",
                                "Underground Dens", "Underground Hole", "Underground Holes", "Underground Lair",
                                "Underground Lairs", "Underground Nest", "Underground Nests", "Underground Pit",
                                "Underground Pits", "Underground Shelter", "Underground Shelters", "Underground Warren",
                                "Underground Warrens", "Underground Hideout", "Underground Hideouts", "Underground Stronghold"])
        name += noun
        description = build_room_description(name)
    else:
        print("Theme not recognized.")

    return name, description



def build_room_description(name):
    # Sentence structures
    sentence_structures = [
        "This area feels {} with its {} {}.",
        "You're surrounded by a {} aura, characteristic of {} {}.",
        "A {} sense of {} permeates this {}.",
        "The {} essence of {} {} is undeniable.",
        "You immediately notice the {} nature of this {}."
    ]

    # Descriptive words for room types
    room_descriptions = {
        "Plains": ["vast", "endless", "expansive", "rolling", "sweeping"],
        "Forest": ["lush", "dense", "verdant", "wooded", "shadowy"],
        "Mountain": ["jagged", "lofty", "towering", "steep", "soaring"],
        "Desert": ["scorching", "barren", "endless", "sandy", "dusty"],
        "Swamp": ["murky", "mucky", "foggy", "wet", "dank"],
        "Ocean": ["vast", "roaring", "deep", "endless", "sprawling"],
        "River": ["flowing", "meandering", "twisting", "serene", "bubbling"],
        "Lake": ["calm", "placid", "serene", "still", "tranquil"],
        "Cave": ["dark", "mysterious", "echoing", "deep", "chilling"]
        # ... add more room types as needed
    }

    # Random embellishments
    embellishments = [
        "Birds chirp in the distance.",
        "The wind whispers secrets.",
        "You can hear water dripping somewhere.",
        "There's an eerie silence here.",
        "You feel like you're being watched.",
        "The scent of nature is strong here."
    ]

    # Find the matching description for the room type
    for keyword, descriptions in room_descriptions.items():
        if keyword in name:
            chosen_sentence = random.choice(sentence_structures)
            chosen_description = random.choice(descriptions)
            embellishment = random.choice(embellishments)

            # Generate the final description
            description = chosen_sentence.format(chosen_description, keyword, keyword.lower()) + " " + embellishment
            return description
    
    # Default case if no match is found
    return "This place is intriguing, evoking a sense of mystery and wonder."

def mob_text_generate(theme):
    name = ""
    description = ""

    prefix = random.choice(["Dark", "Light", "Bright", "Shadow", "Wild", "Blighted", "Sylvan", "Gloom", "Undead", 
                            "Grey", "Red", "Black", "White", "Brown", "Feral", "Dire", "Giant", "Huge",
                            "Small", "Tiny", "Gigantic", "Enormous", "Colossal", "Massive", "Rabid", "Frenzied",
                            "Crazed", "Mad", "Insane", "Savage", "Vicious", "Fierce", "Ferocious", "Ravenous",
                            "Bloodthirsty", "Bloodlust", "Bloodied", "Bloody", "Crimson", "Scarlet", "Crimson",
                            "Fire", "Flame", "Flaming", "Burning", "Blazing", "Inferno", "Infernal", "Hellish",
                            "Heavenly", "Celestial", "Angelic", "Divine", "Holy", "Unholy", "Demonic", "Diabolic",
                            "Diabolical", "Wicked", "Evil", "Vile", "Corrupt", "Decaying", "Decayed", "Rotting",
                            "Rotten", "Putrid", "Festering", "Festering", "Festering", "Festering", "Festering",
                            "Ice", "Icy", "Frozen", "Frost", "Frosty", "Glacial", "Arctic", "Polar", "Chilling"])   
    name += prefix + " "

    if (theme == 1):
        # Plains creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Groundhog", "Rabbit", "Hare", "Lion", "Tiger", "Cheetah", "zombie", "Skeleton", "Ghoul",
                              "Goblin", "Orc", "Ogre", "Troll", "Giant", "Golem", "Gargoyle", "Minotaur", "Centaur",
                              "Satyr", "Cyclops", "Hydra", "Dragon", "Drake", "Wyvern", "Basilisk", "Cockatrice",
                              "Griffin", "Hippogriff", "Pegasus", "Unicorn", "Peryton", "Manticore", "Chimera",
                              "Sphinx", "Harpy", "Cerberus", "Phoenix", "Banshee", "Wraith", "Spectre", "Ghost",
                              "Poltergeist", "Wight", "Revenant", "Vampire", "Werewolf", "Lycanthrope", "Shapeshifter",
                              "Changeling", "Doppelganger", "Ghast", "Ghoul", "Wendigo", "Yeti", "Sasquatch", "Bigfoot",
                              "Mummy", "salamander", "Lizard", "Snake", "Viper", "Cobra", "Python", "Anaconda", "Boa",
                              "Rattlesnake", "Mamba", "Adder", "Asp", "Crocodile", "Alligator", "Gharial", "Caiman",
                              "Tortoise", "Turtle", "Frog", "Toad", "Newt", "Axolotl"])
        name += noun
        description = build_mob_description(name)
    if (theme == 2):
        # Forest creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Treant", "Ent", "Dryad", "Nymph", "Satyr", "Centaur", "Unicorn", "Pegasus", "Peryton",
                              "Manticore", "Chimera", "Sphinx", "Harpy", "Cerberus", "Phoenix", "Banshee", "Wraith",
                              "Fairy", "Sprite", "Pixie", "Nixie", "Naiad", "Sylph", "Gnome", "Goblin", "Orc", "Ogre",
                              "Troll", "Giant", "Golem", "Gargoyle", "Minotaur", "Cyclops", "Hydra", "Dragon", "Drake"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 3):
        # Mountain creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Mountain Goat", "Mountain Lion", "Mountain Tiger", "Mountain Cheetah", "Mountain Lion",
                              "Mountain Troll", "Fire Giant", "Frost Giant", "Stone Giant", "Hill Giant", "Cloud Giant",
                              "Storm Giant", "Cyclops", "Hydra", "Dragon", "Drake", "Wyvern", "Basilisk", "Cockatrice",
                              "Griffin", "Hippogriff", "Pegasus", "Unicorn", "Peryton", "Manticore", "Chimera",
                              "Sphinx", "Harpy", "Cerberus", "Phoenix", "Banshee", "Wraith", "Spectre", "Ghost"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 4):
        # Desert creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Camel", "Dromedary", "Llama", "Alpaca", "Sandworm", "Sandworm", "Sandworm", "Sandworm",
                              "Cobra", "Viper", "Rattlesnake", "Mamba", "Adder", "Asp", "Scorpion", "Tarantula",
                              "Scorpion", "Tarantula", "Centipede", "Spider", "Snake", "Sand Elemental", "Dust Devil", 
                              "Dust Elemental", "Sand Devil", "Sand Dragon", "Sand Drake"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 5):
        # Swamp creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Frog", "Toad", "Water Snake", "Water Viper", "Water Moccasin", "Water Cobra", "Water Python",
                              "Water Elemental", "Water Devil", "Water Dragon", "Water Drake", "Water Naga", "Water Naga",
                              "Anaconda", "Boa", "Python", "Water Snake", "Water Viper",
                              "Water Moccasin", "Water Cobra", "Water Python", "Water Elemental",
                              "Crocodile", "Alligator", "Gharial", "Caiman", "Tortoise", "Turtle", "Water Elemental"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 6):
        # Ocean creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                                "Sailor", "Pirate", "Captain", "First Mate", "Navigator", "Swashbuckler", "Buccaneer",
                                "Corsair", "Privateer", "Sea Serpent", "Sea Serpent", "Sea Serpent", "Sea Serpent",
                                "Albatross", "Pelican", "Seagull", "Coral", "Jellyfish", "Octopus", "Whale", "Shark", 
                                "Dolphin", "Merfolk"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 7):
        # River creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Frog", "Toad", "Water Snake", "Water Viper", "Water Moccasin", "Water Cobra", "Water Python",
                              "Water Elemental", "Water Devil", "Water Dragon", "Water Drake", "Water Naga", "Water Naga",
                              "Anaconda", "Boa", "Python", "Water Snake", "Water Viper",
                              "Water Moccasin", "Water Cobra", "Water Python", "Water Elemental",
                              "Crocodile", "Alligator", "Gharial", "Caiman", "Tortoise", "Turtle", "Water Elemental"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 8):
        # Lake creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder",
                              "Frog", "Toad", "Water Snake", "Water Viper", "Water Moccasin", "Water Cobra", "Water Python",
                              "Water Elemental", "Water Devil", "Water Dragon", "Water Drake", "Water Naga", "Water Naga",
                              "Anaconda", "Boa", "Python", "Water Snake", "Water Viper",
                              "Water Moccasin", "Water Cobra", "Water Python", "Water Elemental",
                              "Crocodile", "Alligator", "Gharial", "Caiman", "Tortoise", "Turtle", "Water Elemental"])
        name += noun
        description = build_mob_description(name)
    elif (theme == 9):
        # Cave creatures
        noun = random.choice(["Soldier", "Warrior", "Fighter", "Barbarian", "Berserker", "Brawler", "Gladiator",
                              "Bandit", "Brigand", "Thief", "Rogue", "Assassin", "Mercenary", "Hunter", "Ranger",
                              "Archer", "Marksman", "Sniper", "Scout", "Tracker", "Trapper", "Wanderer", "Nomad",
                              "Vagabond", "Vagrant", "Outlaw", "Outcast", "Exile", "Pariah", "Hermit", "Recluse",
                              "Swordsman", "Swordswoman", "Swordfighter", "Swordmaster", "Swordmaiden", "Swordwielder"])
        name += noun
        description = build_mob_description(name)
    else:
        print("Theme not recognized.")

    return name, description

def build_mob_description(name):
    # Step 1: Base Descriptions
    base_descriptions = {
        "Soldier": "A disciplined individual trained in the art of warfare.",
        "Warrior": "Brave combatant, wielding weapons with expertise.",
        "Fighter": "Battle-hardened individual, always ready for conflict.",
        "Barbarian": "Ferocious combatant from untamed lands.",
        "Berserker": "Warrior losing oneself to battle frenzy.",
        "Brawler": "Expert in hand-to-hand combat.",
        "Gladiator": "Entertainer skilled in arena combat.",
        "Bandit": "Robber of the roads, often ambushing travelers.",
        "Brigand": "Bandit operating in groups, terrorizing regions.",
        "Thief": "Stealthy pilferer of valuables.",
        "Rogue": "Sly operative, skilled in theft and deception.",
        "Assassin": "Silent killer for hire.",
        "Mercenary": "Warrior selling combat services.",
        "Hunter": "Expert in tracking and neutralizing wild game.",
        "Ranger": "Guardian of the wilderness, skilled archer.",
        "Archer": "Marksman specializing in the bow.",
        "Marksman": "Expert shooter from a distance.",
        "Sniper": "Stealthy long-distance killer.",
        "Scout": "Observer, gathering information unnoticed.",
        "Tracker": "Expert in following trails and marks.",
        "Trapper": "Hunter using devices to capture prey.",
        "Wanderer": "Endless traveler, exploring new frontiers.",
        "Nomad": "Person with no fixed home, roaming endlessly.",
        "Vagabond": "Drifter, moving without clear purpose.",
        "Vagrant": "Wandering, often homeless individual.",
        "Outlaw": "Criminal evading the law.",
        "Outcast": "One shunned by society or their community.",
        "Exile": "Banished individual, often for political reasons.",
        "Pariah": "Despised or avoided person.",
        "Hermit": "Individual seeking solitude, away from society.",
        "Recluse": "Person avoiding social interactions by choice.",
        "Swordsman": "Master of the blade.",
        "Swordswoman": "Female expert in swordplay.",
        "Swordfighter": "Combatant specializing in the art of the sword.",
        "Swordmaster": "Peak expert in sword techniques.",
        "Swordmaiden": "Fierce female warrior of the blade.",
        "Swordwielder": "One who brandishes a sword with skill.",
        "Groundhog": "Tunneling mammal, predictor of spring's arrival.",
        "Rabbit": "Swift, long-eared herbivore.",
        "Hare": "Larger relative of the rabbit, known for its speed.",
        "Dragon": "Mythical beast, soaring with wings and fiery breath.",
        "Skeleton": "An animated assembly of bones, reanimated by dark forces or magic.",
        "Ghoul": "A malevolent undead creature that feasts on the flesh of the deceased.",
        "Goblin": "A mischievous, small-sized humanoid with a knack for trouble and thievery.",
        "Orc": "A warlike humanoid, often green-skinned, known for its strength and hostility.",
        "Ogre": "A massive, often dim-witted humanoid known for its raw strength and insatiable hunger.",
        "Troll": "A lumbering brute, regenerating wounds quickly, often dwelling under bridges or in dark caves.",
        "Giant": "An enormous being, towering above trees and buildings, with strength proportional to its size.",
        "Golem": "An animated being, crafted from clay or stone, brought to life by rituals or incantations.",
        "Gargoyle": "A stone-carved guardian, often adorning gothic structures, that comes to life to protect its domain.",
        "Minotaur": "A powerful creature with a human's torso and a bull's head, often found in labyrinthine dwellings.",
        "Centaur": "A being with a human upper body and a horse's lower body, skilled in archery and known for its wisdom.",
        "Satyr": "A playful forest spirit with a human upper body and goat-like legs, lover of music and dance.",
        "Cyclops": "A giant humanoid with a singular eye in the center of its forehead, skilled in forging and blacksmithing.",
        "Hydra": "A multi-headed serpent, regrowing two heads for every one severed, a challenge for any hero.",
        "Drake": "A wingless, dragon-esque creature, often guarding treasures or lairs.",
        "Wyvern": "A dragon-like creature with two legs and wings, possessing a venomous bite or tail sting.",
        "Basilisk": "A serpent or dragon with a deadly gaze that can petrify those who look into its eyes.",
        "Cockatrice": "A two-legged dragon with a rooster's head, whose gaze or breath can turn victims to stone.",
        "Griffin": "A majestic creature with the body of a lion and the head and wings of an eagle.",
        "Hippogriff": "A fantastical beast with the body of a horse, wings of an eagle, and the head of a raptor.",
        "Pegasus": "A magnificent winged horse, often white, symbolizing purity and grace.",
        "Unicorn": "A mystical horse with a singular spiraled horn, often representing purity and magic.",
        "Peryton": "A stag-headed bird, casting the shadow of a man, and known for its aggressive nature.",
        "Manticore": "A creature with a lion's body, a human's face, and a scorpion-like tail, often spewing venom or spikes.",
        "Chimera": "A monstrous hybrid with a lion's head, goat's body, and serpent's tail.",
        "Sphinx": "A wise creature with a lion's body and a human head, often posing riddles to travelers.",
        "Harpy": "A creature with a woman's face and a bird's body, luring unsuspecting victims with enchanting songs.",
        "Cerberus": "The three-headed hound guarding the gates of the Underworld, preventing souls from escaping.",
        "Phoenix": "A fiery bird reborn from its ashes, symbolizing renewal and the endless cycle of life.",
        "Banshee": "A wailing spirit, often foretelling death with its mournful cry.",
        "Wraith": "A vengeful spirit, often transparent and chilling to the touch, seeking to drag others into its torment.",
        "Spectre": "A haunting ghost, often tied to the location of its death, filled with sorrow and malice.",
        "Ghost": "The ethereal remnant of a once-living being, lingering between the realms of the living and the dead.",
        "Poltergeist": "A mischievous ghost known for moving objects and creating disturbances.",
        "Wight": "An undead being, reanimated with a dark purpose, often draining the life from the living.",
        "Revenant": "An undead that returns from the grave, driven by a need for revenge or to complete unfinished business.",
        "Vampire": "A nocturnal undead that sustains itself on the blood of the living, often possessing charm and immortality.",
        "Werewolf": "A human cursed to transform into a wolf under the full moon, driven by primal urges.",
        "Lycanthrope": "A generic term for beings able to shift between human and animal forms, including werewolves and others.",
        "Shapeshifter": "A being capable of changing its appearance to mimic other creatures or humans.",
        "Changeling": "A fey creature, often left in place of a human child it has stolen.",
        "Doppelganger": "A deceptive creature able to adopt the appearance and memories of those it encounters.",
        "Ghast": "A stronger, more malevolent form of ghoul, exuding a paralyzing aura of decay and death.",
        "Wendigo": "A cursed creature born from intense hunger, forever seeking human flesh in the icy wastes.",
        "Yeti": "The abominable snowman, a large furry bipedal creature said to inhabit the snowy mountains of the Himalayas.",
        "Sasquatch": "Also known as Bigfoot, a large, elusive ape-like creature reputed to inhabit North American forests.",
        "Mummy": "An undead wrapped in bandages, often associated with ancient curses and tombs.",
        "Lizard": "A cold-blooded reptile, often sunning itself on rocks or scurrying about in search of insects.",
        "Snake": "A legless reptile, known for its slithering movements and, in some species, venomous bite.",
        "Viper": "A group of venomous snakes known for their long fangs and aggressive nature.",
        "Cobra": "A venomous snake, recognized by its hood, and often associated with hypnotic dancing and charm.",
        "Python": "A non-venomous constrictor snake, often found in tropical regions, known for its immense size.",
        "Anaconda": "A massive snake with the power to suffocate even the mightiest of prey in its unyielding coils.",
        "Boa": "A shadowy serpent lurking in the dark, waiting to ensnare the unwary with its muscular embrace.",
        "Rattlesnake": "A sly serpent whose venom strikes as swiftly as its rattle warns.",
        "Mamba": "A deadly dance of venom and speed, this snake's bite is a dance of death.",
        "Adder": "Camouflaged in the brush, its venomous bite can bring down foes much larger than itself.",
        "Asp": "Legend says its bite brought down queens; a small serpent with a deadly secret.",
        "Crocodile": "An ancient guardian of rivers, its armored hide and dagger teeth await the unsuspecting.",
        "Alligator": "A silent predator of the marshes, with eyes that gleam and jaws that snap shut in an instant.",
        "Gharial": "With a snout shaped like an ancient weapon, this reptile lurks in the water's depths.",
        "Caiman": "Dweller of murky waters, this beast's eyes gleam with cunning and hunger.",
        "Tortoise": "Ancient and wise, armored by nature, it moves with the weight of time on its back.",
        "Turtle": "Shielded by shell and at home in the water, this creature carries its fortress wherever it goes.",
        "Frog": "A moonlit singer of the ponds, with eyes that see the magic in the night.",
        "Toad": "Rough of skin but rich in secrets, this creature holds the mysteries of the earth.",
        "Newt": "A water's dance in the form of a creature, ever transforming and ever elusive.",
        "Axolotl": "A wonder of nature, forever young and always smiling, swimming through life's waters.",
        "Lion": "The golden king of the savannah, its roar echoes the power of the sun.",
        "Tiger": "A shadow-striped guardian of the jungle, its gaze is as piercing as its claws.",
        "Cheetah": "Wind incarnate, this feline dashes with a speed that leaves the world blurred in its wake.",
        "Zombie": "A grim reminder of life past, driven by hunger and dark magic, relentless in pursuit.",
        "Treant": "Elder of the forests, its bark and limbs tell stories older than time.",
        "Ent": "Ancient tree-beings, guardians of deep woods, and speakers for the silent trees.",
        "Dryad": "Spirits of the trees, their beauty conceals the wild power of nature.",
        "Nymph": "Bound to the elements, these ethereal beings personify the beauty and mystery of nature.",
        "Fairy": "A flutter of wings and a hint of magic, these tiny beings dance on the edge of reality.",
        "Sprite": "Born from laughter and moonlight, these aerial tricksters light up the night.",
        "Pixie": "Mischief incarnate, their glow leads wanderers astray with their playful pranks.",
        "Nixie": "Watery maidens of ponds and lakes, their songs draw listeners into their watery realms.",
        "Naiad": "Guardians of freshwater, their beauty is as crystal clear as the waters they inhabit.",
        "Sylph": "Whispers of the wind, they dance in the air and sing the songs of the breeze.",
        "Gnome": "Keepers of earth's treasures, these small beings are guardians of secrets beneath the soil.",
        "Mountain Goat": "Masters of treacherous heights, they defy gravity with every nimble step.",
        "Mountain Lion": "Silent shadow of the rugged peaks, its golden eyes watch from high vantages.",
        "Mountain Tiger": "Striped sentinel of snowy altitudes, a chill runs down one's spine under its gaze.",
        "Mountain Cheetah": "Swift ghost of highlands, it races the wind atop the world.",
        "Mountain Troll": "A hulking brute carved from the rock, its roar echoes in hidden valleys.",
        "Fire Giant": "Born of molten fury, their steps ignite the very ground they tread upon.",
        "Frost Giant": "Walking glaciers, they carry the chill of the eternal winter in their veins.",
        "Stone Giant": "Mountains come to life, their strength is unyielding and ancient.",
        "Hill Giant": "Guardians of the rolling landscapes, their might shakes the very earth.",
        "Cloud Giant": "Dwellers of the sky, they weave the mists and command the storms.",
        "Storm Giant": "Raging tempests given form, their wrath is as devastating as a hurricane.",
        "Water Elemental": "The very essence of the river and sea, swirling and ever-changing.",
        "Water Devil": "Whirlpools personified, they drag the unwary into the abyss.",
        "Water Dragon": "Serpentine rulers of lakes and seas, their scales shimmer with the depth's secrets.",
        "Water Drake": "Younger kin to the water dragons, their energy ripples through every wave.",
        "Water Naga": "Majestic water serpents, their allure is as mesmerizing as the deepest ocean.",
        "Camel": "Stalwart traveler of the desert, it carries life in every step.",
        "Dromedary": "One-humped wanderer of the sands, it knows the secrets of mirages.",
        "Llama": "Andean sentinel, its proud stance mirrors the peaks it calls home.",
        "Alpaca": "Soft-footed and gentle-eyed, these creatures carry the warmth of the mountains.",
        "Sandworm": "Titan of the dunes, it burrows and waits for vibrations of the unsuspecting.",
        "Cobra": "Hooded danger, its hiss is a prelude to a venomous dance.",
        "Rattlesnake": "Desert's rattle, its tail's song is a countdown to swift venom.",
        "Scorpion": "Armored and armed with venomous sting, this arachnid is the embodiment of desert peril.",
        "Tarantula": "Hairy sentinel of the sands, its presence is as bold as its venomous bite.",
        "Centipede": "A hundred-footed menace, swift and venomous, a living nightmare.",
        "Spider": "Weaver of silken traps, patience incarnate, waiting for the unwary.",
        "Sand Elemental": "Desert's spirit, shifting and inscrutable as the dunes themselves.",
        "Dust Devil": "Twister of the wastelands, it dances with reckless abandon.",
        "Dust Elemental": "Whirlwind of the barren places, carrying the memories of ancient times.",
        "Sand Devil": "Vortex of scorching grains, blinding and relentless.",
        "Sand Dragon": "Golden guardian of endless dunes, its roar is the hot wind of the desert.",
        "Sand Drake": "Young kin to the sand dragon, its scales reflect the scorching sun.",
        "Sailor": "A person adept at navigating the challenges of the open sea.",
        "Pirate": "A rebellious marauder of the high seas, often seeking treasure and infamy.",
        "Captain": "The authoritative leader of a ship's crew, commanding with experience and respect.",
        "First Mate": "The right-hand of the captain, reliable and key in orchestrating ship operations.",
        "Navigator": "An expert in charting courses, using stars and maps to guide ships safely.",
        "Swashbuckler": "A daring adventurer of the seas, skilled in swordplay and theatrical combat.",
        "Buccaneer": "A freebooter known for audacious raids on coastal settlements and ships.",
        "Corsair": "A privateer of the Mediterranean, skilled in fast hit-and-run tactics.",
        "Privateer": "A sanctioned pirate, given license by their government to raid enemy ships.",
        "Sea Serpent": "A mythical marine creature, long and serpentine, inspiring awe and terror.",
        "Sirens": "Enchantresses of the sea whose haunting melodies lure sailors to their doom.",
        "Mariner": "An experienced seafarer, familiar with the whims and furies of the ocean.",
        "Deckhand": "A hard-working member of the ship's crew, responsible for manual tasks on deck.",
        "Shipwright": "A craftsman skilled in constructing and repairing vessels of all sizes.",
        "Dockmaster": "The overseer of harbor activities, ensuring order among the chaos of arriving and departing ships.",
        "Merfolk": "Beings of the deep, with humanoid upper bodies and fish-like tails, guardians of underwater realms.",
        "Dolphin": "Graceful marine mammals known for their intelligence, playfulness, and affinity with sailors.",
        "Shark": "The fearsome predators of the deep, sleek and powerful, forever on the hunt.",
        "Whale": "Gentle giants of the ocean, their songs echoing in the vast blue depths.",
        "Octopus": "Clever cephalopods with eight tentacles, masters of camouflage and escape.",
        "Jellyfish": "Ethereal drifters with pulsating bells, their tendrils can deliver stinging caresses.",
        "Coral": "Living underwater structures, colorful and varied, forming the backbone of vibrant marine ecosystems.",
        "Seagull": "Ubiquitous coastal birds, known for their piercing cries and thieving antics.",
        "Pelican": "Large water birds adept at fishing, recognizable by their pronounced beaks and throat pouch.",
        "Albatross": "Majestic sea birds with immense wingspans, often seen as omens by superstitious sailors.",
        # ... add more for every noun ...
        # "Albatross", "Pelican", "Seagull", "Coral", "Jellyfish", "Octopus", "Whale", "Shark", "Dolphin", "Merfolk",
    }
    
    # Step 2: Adjectives and Details
    details = {
        "Dark": ["emitting a ghostly glow", "enshrouded in a shadowy embrace", "eyes as deep as a moonless night"],
        "Light": ["radiating a gentle luminescence", "casting a golden halo", "bathing everything in comforting light"],
        "Fire": ["with ember-like whispers encircling", "whose touch ignites fleeting sparks", "scorching earth with each step"],
        "Ice": ["exuding a frosty chill", "trail shimmering with frost", "breathing a mist of winter"],
        "Bright": ["so luminous it's blinding", "casting piercing beams", "with a glow rivaling the sun"],
        "Shadow": ["with an ominously lingering aura", "darkness deepening in its wake", "cloaked in twilight"],
        "Wild": ["with the raw essence of wilderness", "soul untamed as a storm", "whispering tales of the wildlands"],
        "Blighted": ["radiating a sickly green hue", "with an aura of decay", "touch spreading corruption"],
        "Sylvan": ["as calming as a forest's heart", "with the grace of age-old trees", "whispering nature's lullaby"],
        "Gloom": ["weighed down by melancholy", "draped in sorrowful shades", "casting a pall of despair"],
        "Undead": ["sending shivers down one's spine", "aura of forsaken souls", "touch as cold as the grave"],
        "Grey": ["muted like a foggy morning", "blending seamlessly into shadows", "touch as soft as mist"],
        "Red": ["burning with passion's fire", "aura ablaze with desire", "spreading warmth like a blazing ember"],
        "Black": ["with the stillness of the void", "dark as a raven's wing", "echoing the mysteries of the abyss"],
        "White": ["as radiant as fresh snow", "light pure as a dove's feather", "touch with the crispness of a winter morning"],        "Brown": ["whose presence is earthy", "whose aura is earthy", "whose touch is earthy"],
        "Brown": ["resonating the essence of earth", "rich like fertile soil", "touch reminiscent of ancient bark"],
        "Feral": ["wildness echoing primeval forests", "raw and untamed essence", "touch sparking wild instincts"],
        "Dire": ["intimidating as a storm's approach", "aura heavy with foreboding", "touch like thunder's rumble"],
        "Giant": ["towering like ancient monoliths", "shadow stretching across lands", "touch causing the ground to quake"],
        "Huge": ["overwhelming like a mountain's peak", "aura as vast as the horizon", "touch with the weight of a boulder"],
        "Small": ["subtle yet captivating presence", "soft aura like a firefly's glow", "gentle touch like a feather's caress"],
        "Tiny": ["fascinating in its minuteness", "delicate aura like dew on grass", "touch as light as a whisper"],
        "Gigantic": ["dwarfing surroundings like titans of old", "aura filling the expanse", "touch with the force of a tsunami"],
        "Enormous": ["as commanding as an ancient redwood", "shadow engulfing landscapes", "presence like a behemoth's stride"],
        "Colossal": ["rivaling the grandeur of mountains", "casting vastness in its wake", "touch echoing epochs"],
        "Rabid": ["wild-eyed and unpredictable", "aura charged with frantic energy", "touch laced with feverish intent"],
        "Frenzied": ["whirlwind of chaotic vibes", "surrounded by a storm of emotions", "touch sparking a maelstrom"],
        "Crazed": ["eyes alight with madness", "aura swirling with chaos", "touch tinged with hysteria"],
        "Mad": ["disturbingly erratic presence", "aura like a spiraling abyss", "touch sending jolts of unpredictability"],
        "Insane": ["entrancing in its wild unpredictability", "swirling aura of madness", "touch inducing vertigo"],
        "Savage": ["raw and unfiltered wildness", "aura of primal dominance", "touch as sharp as a predator's claw"],
        "Vicious": ["menacingly poised for the attack", "suffused with aggressive intent", "touch that draws blood"],
        "Fierce": ["intense like a tempest's fury", "aura crackling with fierceness", "touch invoking battles of yore"],
        "Ferocious": ["raging like a caged beast", "aura with the ferocity of a storm", "touch sparking primal instincts"],
        "Ravenous": ["hunger palpable in every glance", "aura swirling with insatiable desire", "touch feeding an endless void"],
        "Bloodthirsty": ["with a hunger that's palpable", "aura dripping with anticipation", "touch reminiscent of a predator's bite"],
        "Bloodlust": ["intoxicated by the scent of battle", "aura throbbing with violent desires", "touch sharp as a blade's edge"],
        "Bloodied": ["marked by battles of old", "aura stained with tales of valor", "touch telling stories of fights won and lost"],
        "Bloody": ["like a warrior fresh from battle", "aura echoing cries of war", "touch bearing the weight of countless duels"],
        "Crimson": ["deep and entrancing as a ruby", "aura pulsating with intensity", "touch igniting passions of old"],
        "Scarlet": ["vibrant as the first blush of dawn", "aura burning with fiery resolve", "touch infused with a dancer's grace"],
        "Fire": ["enveloped in lively, dancing flames", "aura warm and inviting", "touch igniting sparks of passion"],
        "Flame": ["alight with untamed energy", "essence flickering with every heartbeat", "touch kindling hidden desires"],
        "Burning": ["radiating an unstoppable force", "aura blazing with determination", "touch leaving a mark of its intensity"],
        "Inferno": ["uncontainable, a force of nature", "aura roaring with wild power", "touch blazing a trail of legends"],
        "Blazing": ["burning bright against the night", "essence a beacon of strength", "touch inspiring warmth and courage"],
        "Scorching": ["hot as a desert's midday sun", "aura sizzling with intensity", "touch reminiscent of a phoenix's embrace"],
        "Fiery": ["fierce and unyielding", "aura crackling with spirit", "touch setting souls aflame"],
        "Infernal": ["as mesmerizing as hellfire", "aura with an otherworldly allure", "touch drawing both fear and fascination"],
        "Hellish": ["darkly entrancing, a forbidden dance", "aura swirling with forbidden knowledge", "touch a mix of pain and pleasure"],
        "Heavenly": ["pure and ethereal", "essence light as a cloud", "touch bestowing blessings"],
        "Celestial": ["transcending worldly confines", "aura shimmering like starlight", "touch gentle as moonbeams"],
        "Angelic": ["with a grace that's otherworldly", "aura singing songs of the divine", "touch imbued with celestial kindness"],
        "Divine": ["radiating a godly aura", "essence pure and transcendent", "touch capable of miracles"],
        "Holy": ["sacred and untainted", "aura aglow with piety", "touch that sanctifies"],
        "Unholy": ["laden with dark secrets", "essence that chills the devout", "touch that defies sacred norms"],
        "Demonic": ["darkly captivating, a siren's call", "aura steeped in chaos", "touch that draws one into the abyss"],
        "Diabolic": ["with malevolence lurking in depths", "aura heavy with schemes", "touch promising both peril and power"],
        "Diabolical": ["sinister and unnervingly astute", "essence dripping with intrigue", "touch paving the path to pandemonium"],
        "Wicked": ["deviously charming", "aura whispering of hidden agendas", "touch with a mischief's promise"],
        "Evil": ["with an unsettling allure", "aura tainted with malevolence", "touch cold and devoid of mercy"],
        "Vile": ["disturbingly captivating", "essence oozing malice", "touch reminiscent of creeping decay"],
        "Corrupt": ["twisted by dark desires", "aura warped with treachery", "touch corrupting pure intentions"],
        "Decaying": ["marked by time's relentless grasp", "aura heavy with a fading glory", "touch brittle, like withered leaves"],
        "Decayed": ["a stark testament to time's passage", "aura echoing memories of grandeur", "touch crumbling, yet oddly poignant"],
        "Rotting": ["evidence of nature's reclaiming", "essence teeming with life's cycle", "touch soft and transformative"],
        "Rotten": ["marked by an era gone by", "aura with a lingering nostalgia", "touch bearing tales of forgotten epochs"],
        "Putrid": ["evoking a grim fascination", "essence challenging one's senses", "touch, a cruel jest of nature"],
        "Festering": ["persistently gnawing at existence", "aura bubbling with latent danger", "touch spreading an insidious malaise"],
        "Ice": ["entrancing as a winter's night", "essence capturing the stillness of glaciers", "touch sealing memories in frost"],
        "Icy": ["sharp and brilliantly cold", "aura reflecting a world in stasis", "touch with the serenity of snowflakes"],
        "Frozen": ["a monument to moments captured", "essence echoing tales of arctic winds", "touch preserving stories in crystalline beauty"],
        "Frost": ["delicate yet undeniably present", "aura shimmering in moonlight's embrace", "touch, a gentle kiss of the cold"],
        "Frosty": ["with a brisk and lively spirit", "essence dancing like morning mist", "touch awakening slumbers with a chill"],
        "Glacial": ["majestic and awe-inspiring", "aura bearing the weight of eons", "touch, a testament to enduring grace"],
        "Arctic": ["wild and untamed", "essence whispering tales of polar adventures", "touch, a stark contrast of danger and beauty"],
        "Polar": ["a unique blend of life's extremes", "aura vibrant against a frozen backdrop", "touch imbued with nature's contrasts"],
        "Chilling": ["evoking an eerie stillness", "essence stirring dormant fears", "touch, a gentle reminder of life's fragility"],
        # ... add more for every prefix ...
    
    
    }
    
    adjectives = {
        "Soldier": ["loyal", "determined", "resolute"],
        "Fighter": ["skilled", "disciplined", "focused"],
        "Warrior": ["brave", "fierce", "valiant"],
        "Barbarian": ["fierce", "savage", "untamed"],
        "Berserker": ["reckless", "unstoppable", "unrelenting"],
        "Brawler": ["agile", "nimble", "quick"],
        "Gladiator": ["skilled", "fearsome", "unyielding"],
        "Bandit": ["sneaky", "devious", "unpredictable"],
        "Brigand": ["sneaky", "devious", "unpredictable"],
        "Thief": ["sneaky", "devious", "unpredictable"],
        "Rogue": ["sneaky", "devious", "unpredictable"],
        "Assassin": ["sneaky", "devious", "unpredictable"],
        "Mercenary": ["sneaky", "devious", "unpredictable"],
        "Hunter": ["skilled", "focused", "determined"],
        "Ranger": ["skilled", "focused", "determined"],
        "Archer": ["skilled", "focused", "determined"],
        "Marksman": ["skilled", "focused", "determined"],
        "Sniper": ["skilled", "focused", "determined"],
        "Scout": ["skilled", "focused", "determined"],
        "Tracker": ["skilled", "focused", "determined"],
        "Trapper": ["skilled", "focused", "determined"],
        "Wanderer": ["adventurous", "free-spirited", "curious"],
        "Nomad": ["adventurous", "free-spirited", "curious"],
        "Vagabond": ["adventurous", "free-spirited", "curious"],
        "Vagrant": ["adventurous", "free-spirited", "curious"],
        "Outlaw": ["sneaky", "devious", "unpredictable"],
        "Outcast": ["sneaky", "devious", "unpredictable"],
        "Exile": ["sneaky", "devious", "unpredictable"],
        "Pariah": ["sneaky", "devious", "unpredictable"],
        "Hermit": ["reclusive", "solitary", "quiet"],
        "Recluse": ["reclusive", "solitary", "quiet"],
        "Swordsman": ["skilled", "disciplined", "focused"],
        "Swordswoman": ["skilled", "disciplined", "focused"],
        "Swordfighter": ["skilled", "disciplined", "focused"],
        "Swordmaster": ["skilled", "disciplined", "focused"],
        "Swordmaiden": ["skilled", "disciplined", "focused"],
        "Swordwielder": ["skilled", "disciplined", "focused"],
        "Groundhog": ["small", "furry", "cute"],
        "Rabbit": ["small", "furry", "cute"],
        "Hare": ["small", "furry", "cute"],
        "Dragon": ["massive", "winged", "fire-breathing"],
        "Skeleton": ["walking", "animated", "undead"],
        "Ghoul": ["rotting", "animated", "undead"],
        "Goblin": ["small", "green", "mischievous"],
        "Orc": ["large", "green", "violent"],
        "Ogre": ["large", "brutish", "violent"],
        "Troll": ["ugly", "large", "violent"],
        "Giant": ["massive", "hungry", "violent"],
        "Golem": ["animated", "stone", "clay"],
        "Gargoyle": ["grotesque", "winged", "violent"],
        "Minotaur": ["large", "bull-headed", "violent"],
        "Centaur": ["large", "horse-bodied", "violent"],
        "Satyr": ["small", "goat-legged", "mischievous"],
        "Cyclops": ["large", "one-eyed", "violent"],
        "Hydra": ["large", "multi-headed", "serpentine"],
        "Drake": ["small", "winged", "dragon-like"],
        "Wyvern": ["large", "winged", "dragon-like"],
        "Basilisk": ["large", "winged", "serpent-like"],
        "Cockatrice": ["large", "winged", "chicken-like"],
        "Griffin": ["large", "winged", "lion-like"],
        "Hippogriff": ["large", "winged", "horse-like"],
        "Pegasus": ["large", "winged", "horse-like"],
        "Unicorn": ["large", "horned", "horse-like"],
        "Peryton": ["large", "winged", "deer-like"],
        "Manticore": ["large", "winged", "lion-like"],
        "Chimera": ["large", "winged", "lion-like"],
        "Sphinx": ["large", "winged", "lion-like"],
        "Harpy": ["large", "winged", "bird-like"],
        "Cerberus": ["large", "three-headed", "dog-like"],
        "Phoenix": ["large", "flaming", "bird-like"],
        "Banshee": ["large", "winged", "ghost-like"],
        "Wraith": ["large", "ghost-like", "violent"],
        "Spectre": ["large", "ghost-like", "violent"],
        "Ghost": ["translucent", "humanoid", "violent"],
        "Poltergeist": ["swirl", "negative", "attitude"],
        "Wight": ["large", "undead", "violent"],
        "Revenant": ["large", "ghost-like", "violent"],
        "Vampire": ["pale", "humanoid", "hungry"],
        "Werewolf": ["large", "wolf-like", "violent"],
        "Lycanthrope": ["large", "wolf-like", "violent"],
        "Shapeshifter": ["human", "nightmare", "violent"],
        "Changeling": ["human", "duplicate", "violent"],
        "Doppelganger": ["human", "duplicate", "violent"],
        "Ghast": ["arms", "muscle", "violent"],
        "Wendigo": ["large", "undead", "violent"],
        "Yeti": ["large", "furry", "violent"],
        "Sasquatch": ["large", "furry", "violent"],
        "Bigfoot": ["large", "furry", "violent"],
        "Mummy": ["large", "undead", "wrapped"],
        "Lizard": ["small", "reptilian", "violent"],
        "Snake": ["small", "slithering", "violent"],
        "Viper": ["small", "venomous", "violent"],
        "Cobra": ["small", "venomous", "violent"],
        "Python": ["large", "constricting", "violent"],
        "Anaconda": ["large", "constricting", "violent"],
        "Boa": ["large", "constricting", "violent"],
        "Rattlesnake": ["small", "venomous", "violent"],
        "Mamba": ["small", "venomous", "violent"],
        "Adder": ["small", "venomous", "violent"],
        "Asp": ["small", "venomous", "violent"],
        "Crocodile": ["large", "scaly", "violent"],
        "Alligator": ["large", "scaly", "violent"],
        "Gharial": ["large", "scaly", "violent"],
        "Caiman": ["large", "scaly", "violent"],
        "Tortoise": ["large", "shelled", "violent"],
        "Turtle": ["small", "shelled", "violent"],
        "Frog": ["small", "amphibious", "violent"],
        "Toad": ["small", "amphibious", "violent"],
        "Newt": ["small", "amphibious", "violent"],
        "Axolotl": ["small", "amphibious", "violent"],
        "Lion": ["large", "feline", "violent"],
        "Tiger": ["large", "feline", "violent"],
        "Cheetah": ["large", "feline", "violent"],
        "zombie": ["rotting", "animated", "undead"],
        "Treant": ["large", "tree-like", "violent"],
        "Ent": ["large", "tree-like", "violent"],
        "Dryad": ["small", "tree-like", "violent"],
        "Nymph": ["small", "tree-like", "violent"],
        "Fairy": ["small", "winged", "violent"],
        "Sprite": ["small", "winged", "violent"],
        "Pixie": ["small", "winged", "violent"],
        "Nixie": ["small", "winged", "violent"],
        "Naiad": ["small", "winged", "violent"],
        "Sylph": ["small", "winged", "violent"],
        "Gnome": ["small", "humanoid", "violent"],
        "Mountain Goat": ["small", "goat-like", "violent"],
        "Mountain Lion": ["large", "feline", "violent"],
        "Mountain Tiger": ["large", "feline", "violent"],
        "Mountain Cheetah": ["large", "feline", "violent"],
        "Mountain Troll": ["large", "brutish", "violent"],
        "Fire Giant": ["massive", "hungry", "violent"],
        "Frost Giant": ["massive", "hungry", "violent"],
        "Stone Giant": ["massive", "hungry", "violent"],
        "Hill Giant": ["massive", "hungry", "violent"],
        "Cloud Giant": ["massive", "hungry", "violent"],
        "Storm Giant": ["massive", "hungry", "violent"],
        "Water Elemental": ["swirling", "mass", "violent"],
        "Water Devil": ["swirling", "mass", "violent"],
        "Water Dragon": ["dragon", "water", "violent"],
        "Water Drake": ["dragon", "water", "violent"],
        "Water Naga": ["large", "snake-like", "violent"],
        "Camel": ["large", "humped", "violent"],
        "Dromedary": ["large", "humped", "violent"],
        "Llama": ["large", "humped", "violent"],
        "Alpaca": ["large", "humped", "violent"],
        "Sandworm": ["large", "burrowing", "violent"],
        "Cobra": ["small", "venomous", "violent"],
        "Rattlesnake": ["small", "venomous", "violent"],
        "Scorpion": ["small", "venomous", "violent"],
        "Tarantula": ["large", "venomous", "violent"],
        "Centipede": ["small", "venomous", "violent"],
        "Spider": ["small", "venomous", "violent"],
        "Sand Elemental": ["swirling", "mass", "violent"],
        "Dust Devil": ["swirling", "mass", "violent"],
        "Dust Elemental": ["swirling", "mass", "violent"],
        "Sand Devil": ["swirling", "mass", "violent"],
        "Sand Dragon": ["dragon", "desert", "violent"],
        "Sand Drake": ["dragon", "desert", "violent"],
        "Sailor": ["skilled", "sailing", "violent"],
        "Pirate": ["skilled", "sailing", "violent"],
        "Captain": ["skilled", "sailing", "violent"],
        "First Mate": ["skilled", "sailing", "violent"],
        "Navigator": ["skilled", "sailing", "violent"],
        "Swashbuckler": ["skilled", "sailing", "violent"],
        "Buccaneer": ["skilled", "sailing", "violent"],
        "Corsair": ["skilled", "sailing", "violent"],
        "Privateer": ["skilled", "sailing", "violent"],
        "Sea Serpent": ["large", "serpentine", "violent"],
        "Albatross": ["Majestic", "wind-swept", "fierce"],
        "Pelican": ["Impressive", "graceful", "determined"],
        "Seagull": ["Bold", "aerial acrobat", "relentless"],
        "Coral": ["Expansive", "maze-like", "unyielding"],
        "Jellyfish": ["Giant", "ethereal drifter", "stinging"],
        "Octopus": ["Massive", "tentacled mastermind", "savage"],
        "Whale": ["Colossal", "oceanic leviathan", "powerful"],
        "Shark": ["Imposing", "predatory missile", "ruthless"],
        "Dolphin": ["Sizable", "aquatic dancer", "playfully fierce"],
        "Merfolk": ["Grand", "scaled enigma", "warrior of the depths"]
        # ... add more for every noun ...
    }
    
    # Step 3: Randomized Structure
    structures = [
        "{base}. This {noun} is {adj} and is {detail}.",
        "{adj} {noun} that {detail}. {base}.",
        "{base}. One can't help but notice its {detail}.",
        "A {adj} {noun}. {base}.",
    ]
    
    # Split the name into prefix and noun
    prefix, noun = name.split(' ', 1)

    base = base_descriptions.get(noun, "A creature of unknown origins.")
    adj = random.choice(adjectives.get(noun, ["enigmatic", "mysterious"]))
    detail = random.choice(details.get(prefix, ["with an unknown aura", "emitting a strange vibe"]))
    
    # Randomly select a structure and format it
    description = random.choice(structures).format(base=base, noun=noun.lower(), adj=adj, detail=detail)
    
    return description

# Test
print(build_mob_description("Dark Dragon"))

import random

def item_text_generate(theme, rarity):
    themes = {
        "PLAINS": [
            ["Feather", "Grass Blade", "Prairie Grass", "Pebble", "Dandelion", "Gopher Hole"],
            ["Meadow Flower", "Buffalo Horn", "Sunflower", "Ant Hill", "Bison Fur", "Prairie Dust"],
            ["Golden Grass", "Buffalo Hoof", "Rainbow Dandelion", "Prairie Gem", "Prairie Fire", "Wind Whisper"],
            ["Starlit Feather", "Moonlit Ant Hill", "Buffalo Spirit", "Eternal Sunflower", "Dancing Grass", "Dreaming Gopher"],
            ["Legend of the Prairie", "Bison King Fur", "Timeless Dandelion", "Eclipsed Sunflower", "Prairie Aurora", "Buffalo Heart"],
            ["Ancient Grass", "Primordial Dandelion", "Bison Ancestor Spirit", "Eon Sunflower", "Gopher Genesis", "Prairie Prodigy"]
        ],
        "FOREST": [
            ["Twig", "Pinecone", "Fern", "Mushroom", "Berry", "Acorn"],
            ["Silvered Pinecone", "Glowing Mushroom", "Forest Lily", "Emerald Fern", "Thorned Berry", "Oaken Acorn"],
            ["Forest Gem", "Starlit Mushroom", "Golden Pinecone", "Twilight Fern", "Moon Berry", "Forest Heart"],
            ["Eternal Fern", "Luminous Mushroom", "Ancient Acorn", "Enchanted Berry", "Majestic Pinecone", "Tree Spirit"],
            ["Forest Whisper", "Legendary Berry", "Guardian Twig", "Timeless Pinecone", "Sacred Mushroom", "Nature's Essence"],
            ["Primordial Twig", "Ageless Acorn", "Eon Fern", "Genesis Berry", "Dawn Pinecone", "Forest Prodigy"]
        ],
        "MOUNTAIN": [
            ["Stone Fragment", "Mountain Grass", "Pebble", "Moss Patch", "Mountain Lichen", "Condor Feather"],
            ["Granite Shard", "Alpine Rose", "Magnetite Ore", "Cave Crystal", "Mountain Monk Scroll", "Rockslide Ruby"],
            ["Everfrost Stone", "Moonlit Moss", "Sunlit Crystal", "Mountain Echo Stone", "Condor's Crest", "Glacier Gem"],
            ["Starlight Stone", "Dreaming Condor", "Mountain Spirit Essence", "Dragon's Breath Stone", "Eternal Echo", "Summit Sigil"],
            ["Legend of the Mountain", "Dragon Heart Shard", "Primordial Moss", "Timeless Crystal", "Celestial Condor Plume", "Eon Stone"],
            ["Ancient Peak", "Genesis Crystal", "Dragon Ancestor Relic", "Mountain Muse Memory", "Condor Prodigy", "Primordial Mountain Melody"]
        ],
        "DESERT": [
            ["Cactus Spine", "Desert Pebble", "Sand Grain", "Scorpion Claw", "Dune Flower", "Lizard Scale"],
            ["Mirage Stone", "Golden Sand", "Desert Rose", "Sunlit Cactus", "Moonlit Lizard", "Desert Dream"],
            ["Desert Star", "Eternal Dune", "Phoenix Feather", "Sands of Time", "Desert Spirit", "Golden Scorpion"],
            ["Desert Whisper", "Cactus Heart", "Dune Mystery", "Phoenix Tear", "Sandstorm Gem", "Lizard King Scale"],
            ["Desert Legend", "Ancient Cactus", "Golden Phoenix", "Timeless Dune", "Eternal Sandstorm", "Primordial Lizard"],
            ["Genesis Sand", "Dawn Scorpion", "Primordial Cactus", "Phoenix Prodigy", "Eon Sandstorm", "Desert Epiphany"]
        ],
        "SWAMP": [
            ["Swamp Mud", "Cattail", "Willow Branch", "Moss", "Frog Egg", "Tadpole"],
            ["Glowing Algae", "Silvered Cattail", "Enchanted Willow", "Swamp Stone", "Moonlit Frog", "Swamp Lily"],
            ["Ancient Moss", "Swamp Spirit", "Golden Tadpole", "Willow Whisper", "Twilight Cattail", "Swamp Gem"],
            ["Swamp Serenade", "Mystic Moss", "Eternal Frog", "Luminous Cattail", "Starlit Swamp", "Willow Heart"],
            ["Legend of the Swamp", "Ageless Frog", "Primordial Willow", "Swamp Aurora", "Eon Moss", "Guardian Cattail"],
            ["Swamp Genesis", "Dawn Tadpole", "Swamp Prodigy", "Primordial Cattail", "Phoenix Lily", "Willow Epiphany"]
        ],
        "OCEAN": [
            ["Seashell", "Seaweed", "Driftwood", "Coral Fragment", "Salt Crystal", "Shark Tooth"],
            ["Starfish", "Moonlit Seaweed", "Ocean Pebble", "Mermaid's Tear", "Tidepool Gem", "Dolphin Fin"],
            ["Siren Song", "Golden Coral", "Ocean Spirit", "Deep Sea Star", "Phoenix Seashell", "Twilight Seaweed"],
            ["Ocean Whisper", "Eternal Tide", "Abyssal Gem", "Coral Crown", "Mermaid's Heart", "Ocean Dream"],
            ["Ocean Legend", "Guardian of the Tides", "Ancient Abyss", "Timeless Seaweed", "Dolphin Dance", "Siren's Heart"],
            ["Ocean Genesis", "Primordial Coral", "Eon Tide", "Dawn Seashell", "Phoenix Seaweed", "Ocean Epiphany"]
        ],
        "RIVER": [
            ["River Stone", "Freshwater Pearl", "Fish Scale", "Cattail", "Pebble", "Reed"],
            ["Golden Pebble", "Moonlit Reed", "River Gem", "Glowing Fish", "Starlit Cattail", "River Lily"],
            ["River Spirit", "Eternal Reed", "Mystic Pebble", "Dancing Fish", "Golden Cattail", "River Whisper"],
            ["River Dream", "Aurora Reed", "Twilight Fish", "Luminous Pebble", "Guardian Cattail", "Phoenix Pearl"],
            ["Legend of the River", "Primordial Fish", "Eon Reed", "Timeless Pebble", "Guardian Pearl", "Majestic Fish"],
            ["River Genesis", "Dawn Cattail", "Phoenix Reed", "Genesis Pebble", "Fish Prodigy", "River Epiphany"]
        ],
        "LAKE": [
            ["Lake Stone", "Water Lily", "Duck Feather", "Freshwater Algae", "Pebble", "Lake Reed"],
            ["Moonlit Lily", "Starlit Algae", "Lake Gem", "Golden Pebble", "Phoenix Feather", "Glowing Reed"],
            ["Lake Spirit", "Aurora Lily", "Twilight Algae", "Dancing Duck", "Eternal Reed", "Lake Whisper"],
            ["Lake Dream", "Majestic Lily", "Luminous Algae", "Guardian Duck", "Starlit Pebble", "Phoenix Reed"],
            ["Legend of the Lake", "Primordial Duck", "Eon Lily", "Timeless Algae", "Guardian Reed", "Lake Aurora"],
            ["Lake Genesis", "Dawn Lily", "Phoenix Algae", "Genesis Duck", "Reed Prodigy", "Lake Epiphany"]
        ],
        "CAVE": [
            ["Stalactite", "Stalagmite", "Cave Moss", "Bat Wing", "Glowing Stone", "Crystal Fragment"],
            ["Moonlit Crystal", "Golden Stalactite", "Twilight Stalagmite", "Glowing Bat", "Cave Gem", "Starlit Moss"],
            ["Cave Spirit", "Eternal Crystal", "Mystic Stone", "Dancing Bat", "Golden Moss", "Cave Whisper"],
            ["Cave Dream", "Aurora Stalactite", "Guardian Stalagmite", "Luminous Bat", "Phoenix Moss", "Majestic Stone"],
            ["Legend of the Cave", "Primordial Bat", "Eon Stalactite", "Timeless Moss", "Guardian Stone", "Cave Aurora"],
            ["Cave Genesis", "Dawn Crystal", "Phoenix Moss", "Genesis Bat", "Stone Prodigy", "Cave Epiphany"]
        ]

    }

    rarity_tiers = {
        0: ["Common", "It's a fairly typical specimen."],
        1: ["Uncommon", "A bit unique, but not hard to come by."],
        2: ["Rare", "It's rare to come across one of these."],
        3: ["Elite", "Crafted by nature's finest artisans."],
        4: ["Legendary", "Only whispered about in ancient tales."],
        5: ["Ancient", "From the dawn of time."],
        6: ["Unique", "One of a kind in existence."]
    }

    # Ensure the theme and rarity are valid
    if theme not in themes:
        return "Invalid theme."

    if rarity not in rarity_tiers:
        return "Invalid rarity."

    item_name = random.choice(themes[theme][rarity])
    rarity_name, rarity_desc = rarity_tiers[rarity]

    return f"{item_name} ({rarity_name}) - {rarity_desc}"

# Example Usage:
print(item_text_generate("PLAINS", 3))

def weapon_text_generate(theme, rarity):
    common_weapons = {
        0: [("Shortsword", "A simple blade."),
            ("Longsword", "A basic long blade."),
            ("Falchion", "A simple curved sword."),
            ("Two-Handed Sword", "A basic massive blade."),
            ("Club", "A basic wooden club."),
            ("Slingshot", "A basic slingshot for small stones."),
            ("Javelin", "A basic throwing spear."),
            ("Dagger", "A basic small blade."),
            ("Bow", "A basic wooden bow."),
            ("Quarterstaff", "A basic wooden staff."),
            ("Axe", "A basic woodcutter's axe."),
            ("Mace", "A basic metal mace."),
            ("Trident", "A basic three-pronged spear."),
            ("Spear", "A basic spear."),
            ("Scimitar", "A basic curved sword."),
            ("Rapier", "A basic thin blade."),
            ("Flail", "A basic spiked ball on a chain."),
            ("Morningstar", "A basic spiked mace."),
            ("Sickle", "A basic curved blade."),
            ("Sai", "A basic three-pronged dagger."),
            ("Katana", "A basic curved blade."),
            ("Nunchaku", "A basic two-sectioned staff."),
            ("Kama", "A basic sickle on a chain."),
            ("Boomerang", "A basic curved throwing blade."),
            ("Saber", "A basic curved sword."),
            ("Crossbow", "A basic wooden crossbow."),],

        1: [("Shortsword+", "A sharpened shortsword."),
            ("Longsword+", "An enhanced long blade."),
            ("Falchion+", "A superior curved sword."),
            ("Two-Handed Sword+", "A reinforced massive blade."),
            ("Club+", "A reinforced wooden club."),
            ("Slingshot+", "An advanced slingshot."),
            ("Javelin+", "A well-crafted throwing spear."),
            ("Dagger+", "A sharpened dagger."),
            ("Bow+", "A reinforced wooden bow."),
            ("Quarterstaff+", "A stronger wooden staff."),
            ("Axe+", "A battle-ready axe."),
            ("Mace+", "A mace with a reinforced head."),
            ("Trident+", "A well-crafted three-pronged spear."),
            ("Spear+", "A sharpened spear."),
            ("Scimitar+", "A sharpened curved sword."),
            ("Rapier+", "A sharpened thin blade."),
            ("Flail+", "A spiked ball on a chain."),
            ("Morningstar+", "A spiked mace."),
            ("Sickle+", "A sharpened curved blade."),
            ("Sai+", "A sharpened three-pronged dagger."),
            ("Katana+", "A sharpened curved blade."),
            ("Nunchaku+", "A reinforced two-sectioned staff."),
            ("Kama+", "A sharpened sickle on a chain."),
            ("Boomerang+", "A sharpened curved throwing blade."),
            ("Saber+", "A sharpened curved sword."),
            ("Crossbow+", "A reinforced wooden crossbow.")],

        2: [("Shortsword++", "A masterfully crafted shortsword."),
            ("Longsword++", "A top-tier long blade."),
            ("Falchion++", "An elite curved sword."),
            ("Two-Handed Sword++", "An elite massive blade."),
            ("Club++", "A top-tier wooden club."),
            ("Slingshot++", "A masterful slingshot."),
            ("Javelin++", "A top-tier throwing spear."),
            ("Dagger++", "An elite small blade."),
            ("Bow++", "A masterfully crafted bow."),
            ("Quarterstaff++", "A top-tier wooden staff."),
            ("Axe++", "An elite woodcutter's axe."),
            ("Mace++", "A masterfully crafted mace."),
            ("Trident++", "A top-tier three-pronged spear."),
            ("Spear++", "An elite spear."),
            ("Scimitar++", "An elite curved sword."),
            ("Rapier++", "An elite thin blade."),
            ("Flail++", "A masterfully crafted spiked ball on a chain."),
            ("Morningstar++", "A masterfully crafted spiked mace."),
            ("Sickle++", "An elite curved blade."),
            ("Sai++", "An elite three-pronged dagger."),
            ("Katana++", "An elite curved blade."),
            ("Nunchaku++", "A masterfully crafted two-sectioned staff."),
            ("Kama++", "An elite sickle on a chain."),
            ("Boomerang++", "An elite curved throwing blade."),
            ("Saber++", "An elite curved sword."),
            ("Crossbow++", "A masterfully crafted crossbow.")],

        3: [("Elite Shortsword", "The pinnacle of shortswords."),
            ("Elite Longsword", "The pinnacle of long blades."),
            ("Elite Falchion", "The pinnacle of curved swords."),
            ("Elite Two-Handed Sword", "The pinnacle of massive blades."),
            ("Elite Club", "The pinnacle of wooden clubs."),
            ("Elite Slingshot", "The pinnacle of slingshots."),
            ("Elite Javelin", "The pinnacle of throwing spears."),
            ("Elite Dagger", "The pinnacle of daggers."),
            ("Elite Bow", "The pinnacle of bows."),
            ("Elite Quarterstaff", "The pinnacle of staffs."),
            ("Elite Axe", "The pinnacle of axes."),
            ("Elite Mace", "The pinnacle of maces."),
            ("Elite Trident", "The pinnacle of three-pronged spears."),
            ("Elite Spear", "The pinnacle of spears."),
            ("Elite Scimitar", "The pinnacle of curved swords."),
            ("Elite Rapier", "The pinnacle of thin blades."),
            ("Elite Flail", "The pinnacle of spiked balls on a chain."),
            ("Elite Morningstar", "The pinnacle of spiked maces."),
            ("Elite Sickle", "The pinnacle of curved blades."),
            ("Elite Sai", "The pinnacle of three-pronged daggers."),
            ("Elite Katana", "The pinnacle of curved blades."),
            ("Elite Nunchaku", "The pinnacle of two-sectioned staffs."),
            ("Elite Kama", "The pinnacle of sickles on a chain."),
            ("Elite Boomerang", "The pinnacle of curved throwing blades."),
            ("Elite Saber", "The pinnacle of curved swords."),
            ("Elite Crossbow", "The pinnacle of crossbows.")],
    }

    themed_weapons = {
        'PLAINS': {
            4: [
                ("Windblade Longsword", "A longsword infused with the essence of the plains' wind."),
                ("Prairie Falchion", "A falchion that sings with the spirit of open grasslands."),
                ("Horizon Cleaver", "A two-handed sword capturing the vastness of the horizon."),
                ("Dusk Dagger", "A dagger reflecting the hues of a plains sunset."),
                ("Meadow Mace", "A mace inspired by the rolling meadows of the plains."),
                ("Sunset Scimitar", "A scimitar capturing the colors of a plains sunset."),
                ("Galewind Glaive", "A glaive infused with the gusts of the plains."),
                ("Breezeblade Axe", "An axe shaped by the gentle winds of the plains."),
                ("Twilight Trident", "A trident echoing the serenity of plains twilight."),
                ("Daybreak Dirk", "A dirk capturing the first light over the plains."),
                ("Sundown Saber", "A saber inspired by the closing of day."),
                ("Dawnstar Dagger", "A dagger that gleams with the first light of dawn.")
            ],
            5: [
                ("Golden Windblade", "A majestic longsword channeling the golden breezes of the plains."),
                ("Silver Prairie Falchion", "A gleaming falchion resonating with the plains."),
                ("Starlit Horizon Cleaver", "A two-handed sword shimmering with starlight."),
                ("Lustrous Dusk Dagger", "A dagger that gleams in the dimming light."),
                ("Radiant Meadow Mace", "A mace glowing with the warmth of the meadow's sun."),
                ("Ecliptic Sunset Scimitar", "A scimitar infused with the essence of a setting sun."),
                ("Tempest Galewind Glaive", "A glaive swirling with stormy energy."),
                ("Harmonic Breezeblade Axe", "An axe that hums with the wind's song."),
                ("Lunar Twilight Trident", "A trident infused with the soft glow of moonlight."),
                ("Sunburst Daybreak Dirk", "A dirk that bursts with the morning's first light."),
                ("Eternal Sundown Saber", "A saber that captures the endless horizon."),
                ("Gleaming Dawnstar Dagger", "A dagger reflecting the endless expanse of the dawn.")
            ],
            6: [
                ("Celestial Windblade", "A longsword touched by the gods of the plains."),
                ("Harvest Prairie Falchion", "A falchion blessed by the harvest season."),
                ("Infinite Horizon Cleaver", "A two-handed sword that feels as vast as the plains."),
                ("Ephemeral Dusk Dagger", "A dagger capturing the fleeting beauty of twilight."),
                ("Pulse of the Meadow Mace", "A mace beating with the life of the plains."),
                ("Solar Flare Scimitar", "A scimitar bursting with solar energy."),
                ("Whirlwind Glaive", "A glaive that causes tempests with every swing."),
                ("Sonic Wind Axe", "An axe that roars with the speed of gales."),
                ("Eclipse Trident", "A trident that can summon lunar shadows."),
                ("First Light Dirk", "A dirk that glows with the promise of a new day."),
                ("Eventide Edge", "A blade that sings the song of the evening."),
                ("Awakening Dawn Dagger", "A dagger infused with the spirit of the waking world.")
            ]
        },
        'FOREST': {
            4: [
                ("Leafblade Longsword", "A longsword with a blade as sharp as forest leaves."),
                ("Vine Whip Falchion", "A falchion intertwined with resilient forest vines."),
                ("Canopy Cleaver", "A two-handed sword with carvings of forest canopies."),
                ("Mossy Mace", "A mace covered in vibrant forest moss."),
                ("Barkblade Dagger", "A dagger with a handle of ancient forest bark."),
                ("Rootwoven Rapier", "A rapier woven with the oldest roots of the forest."),
                ("Greenwood Glaive", "A glaive made from the heartwood of the forest."),
                ("Thorned Thorn", "A thorn that's doubly dangerous to its enemies."),
                ("Foliage Flail", "A flail made of dense forest foliage."),
                ("Sapling Saber", "A saber grown from a forest sapling."),
                ("Timber Trident", "A trident crafted from ancient forest timbers."),
                ("Sprout Sprinkle", "A sprinkle imbued with the energy of forest sprouts.")
            ],
            5: [
                ("Emerald Leafblade", "A longsword glowing with the deep green of forest leaves."),
                ("Crystal Vine Falchion", "A falchion shimmering with the dew of the forest."),
                ("Skyreach Canopy Cleaver", "A two-handed sword as tall as the forest canopy."),
                ("Lichen Luminary Mace", "A mace that glows with the luminescence of forest lichens."),
                ("Ancient Bark Dagger", "A dagger made from the bark of the forest's oldest tree."),
                ("Roots of Yore Rapier", "A rapier that tells tales of the ancient forest."),
                ("Heartwood Halberd", "A halberd made from the very core of the forest."),
                ("Bramble Blade", "A blade entwined with the thickest forest brambles."),
                ("Verdant Veil Flail", "A flail that carries the full vitality of the forest."),
                ("Sylvan Stream Saber", "A saber that flows like the forest's clearest stream."),
                ("Tree's Truth Trident", "A trident that reveals the forest's deepest secrets."),
                ("Seedling Scepter", "A scepter imbued with the potential of a thousand forests.")
            ],
            6: [
                ("Forest's Finale Longsword", "A longsword capturing the eternal spirit of the woods."),
                ("Vital Vine Victory Falchion", "A falchion symbolizing the triumph of nature."),
                ("Canopy Crown Cleaver", "A two-handed sword fit for the guardian of the forest."),
                ("Moss Monarch Mace", "A mace that rules over all forest growth."),
                ("Bark Bastion Dagger", "A dagger that stands as the forest's last line of defense."),
                ("Rapier of Reforestation", "A rapier that brings life back to barren lands."),
                ("Guardian Glaive", "A glaive made by the protectors of the forest."),
                ("Thorn Titan's Touch", "A touch from the greatest defenders of the forest."),
                ("Flail of Fertility", "A flail that ensures the forest's continuous growth."),
                ("Saber of the Sylvan Shade", "A saber that shelters all creatures of the forest."),
                ("Trident of Tree's Testament", "A trident that carries the forest's ancient wisdom."),
                ("Scepter of Sprouting Spring", "A scepter heralding the rejuvenation of the woods.")
            ]
        },
        'MOUNTAIN': {
            4: [
                ("Stoneblade Longsword", "A longsword carved from the hardest mountain rock."),
                ("Peak Point Falchion", "A falchion inspired by the towering mountain peaks."),
                ("Crag Cleaver", "A two-handed sword with a blade as rugged as mountain terrain."),
                ("Boulder Breaker Mace", "A mace with the weight of a mountain behind every swing."),
                ("Pinnacle Pike", "A pike that embodies the spirit of the highest summits."),
                ("Ridge Rapier", "A rapier as sharp as the mountain ridges."),
                ("Elevation Edge Dagger", "A dagger imbued with the energy of rising altitudes."),
                ("Plateau Poleaxe", "An axe inspired by the vast mountain plateaus."),
                ("Summit Scythe", "A scythe that slices with the cold of the mountain tops."),
                ("Altitude Axe", "An axe that channels the thin air of high elevations."),
                ("Terrace Trident", "A trident that strikes with the stability of mountain terraces."),
                ("Gorge Glaive", "A glaive that whirls with the fury of mountain gorges.")
            ],
            5: [
                ("Granite Guard Longsword", "A longsword offering the protection of solid granite."),
                ("Pristine Peak Falchion", "A falchion that glows with the purity of untouched summits."),
                ("Cavern Cleaver", "A two-handed sword that echoes with the depths of mountain caverns."),
                ("Magma Mace", "A mace that burns with the heat of mountain magma."),
                ("Snow-capped Saber", "A saber that chills foes with the cold of snowy peaks."),
                ("Echo Edge Dagger", "A dagger that resonates with the sound of mountain valleys."),
                ("Avalanche Axe", "An axe that descends with the force of a mountain avalanche."),
                ("Slope Scimitar", "A scimitar that cuts with the sharpness of steep slopes."),
                ("Vista Blade", "A blade that offers views of distant horizons."),
                ("Ravine Rapier", "A rapier that delves deep like mountain ravines."),
                ("Height Halberd", "A halberd that reaches for the highest skies."),
                ("Pinnacle Polearm", "A polearm infused with the spirit of the highest peaks.")
            ],
            6: [
                ("Monolith Maul", "A maul that stands unyielding like a mountain monolith."),
                ("Everest Edge Longsword", "A longsword that challenges the might of the tallest mountains."),
                ("Fissure Falchion", "A falchion that splits foes like mountain fissures."),
                ("Crystalline Cleaver", "A two-handed sword that shines with the clarity of mountain crystals."),
                ("Orogeny Oscillator", "A weapon that resonates with the creation of mountains."),
                ("Pinnacle Pike Prime", "A pike that stands as the best among mountain weapons."),
                ("Zenith Zephyr Blade", "A blade that carries the breezes of the highest altitudes."),
                ("Topmost Trident", "A trident that touches the sky's zenith."),
                ("Peak's Pinnacle Poleaxe", "An axe that captures the very essence of a mountain's peak."),
                ("Sheer Summit Saber", "A saber that reflects the sheerness of mountain cliffs."),
                ("Lofty Lance", "A lance that thrusts with the aspirations of reaching the highest summits."),
                ("Heavenly Height Halberd", "A halberd that aims to breach the heavens.")
            ]
        },
                'DESERT': {
            4: [
                ("Duneblade Longsword", "A longsword inspired by the shifting desert dunes."),
                ("Oasis Falchion", "A falchion that promises the relief of a desert oasis."),
                ("Sandslice Scimitar", "A scimitar as swift as a desert sandstorm."),
                ("Sunburn Saber", "A saber that blazes with the heat of the desert sun."),
                ("Mirage Mace", "A mace that confuses foes like a desert mirage."),
                ("Quicksand Dagger", "A dagger that ensnares foes like desert quicksand."),
                ("Pyramid Pike", "A pike that stands firm like the ancient desert pyramids."),
                ("Sandstorm Scythe", "A scythe that whirls with the fury of desert storms."),
                ("Cactus Cutlass", "A cutlass with thorns like a desert cactus."),
                ("Pharaoh's Falchion", "A falchion that once belonged to desert royalty."),
                ("Desolation Dagger", "A dagger that embodies the vastness of the desert."),
                ("Droughtblade Dagger", "A dagger that drains foes of their strength.")
            ],
            5: [
                ("Golden Sand Longsword", "A longsword that glistens like golden desert sands."),
                ("Searing Sun Saber", "A saber that burns with the intensity of the desert sun."),
                ("Dervish's Dance Dagger", "A dagger that moves as swiftly as a desert dervish."),
                ("Camel's Calm Cutlass", "A cutlass that offers the endurance of a desert camel."),
                ("Sandcastle Scimitar", "A scimitar that carries the weight of desert fortresses."),
                ("Desert Dreamblade", "A blade that whispers tales of desert dreams."),
                ("Parched Pike", "A pike that speaks of the desert's thirst."),
                ("Tomb's Touch Trident", "A trident that resonates with the secrets of ancient tombs."),
                ("Sandswirl Scythe", "A scythe that dances with the rhythm of desert winds."),
                ("Riddle of Ra Rapier", "A rapier imbued with the mysteries of the desert sun god."),
                ("Nomad's Nightblade", "A blade that hides in the shadows of desert nights."),
                ("Sandstorm Sickle", "A sickle that whirls with the speed of desert sandstorms.")
            ],
            6: [
                ("Desert's Destiny Longsword", "A longsword that carries the fate of the desert."),
                ("Sun God's Saber", "A saber that shines with the brilliance of the desert sun god."),
                ("Sandsea Scimitar", "A scimitar that flows with the vastness of desert landscapes."),
                ("Oasis Oracle Blade", "A blade that foretells the future amidst the desert's uncertainty."),
                ("Pharaoh's Final Pike", "A pike that holds the power of the last desert king."),
                ("Golden Guardian Glaive", "A glaive that protects the treasures of the desert."),
                ("Sphinx's Secret Scythe", "A scythe that guards the riddles of the desert sphinx."),
                ("Mummy's Mystery Mace", "A mace wrapped in the enigma of desert tombs."),
                ("Dune's Dream Dagger", "A dagger that dreams of endless desert landscapes."),
                ("Cleopatra's Cutlass", "A cutlass that once belonged to the desert's greatest queen."),
                ("Ramses' Rapier", "A rapier that resonates with the power of a legendary pharaoh."),
                ("Pyramid Prime Pike", "A pike that stands as the pinnacle of desert craftsmanship.")
            ]},
        'SWAMP': {
            4: [("Swamp Cleaver", "A longsword that thrives in the swamp."),
                ("Mudclub", "A club born from the swamp's depths."),
                ("Toadsticker", "A dagger perfect for the swamp's silence."),
                ("Bog Bow", "A bow crafted from swamp materials."),
                ("Marsh Mace", "A mace infused with swamp essence."),
                ("Silt Slingshot", "A slingshot using swamp silt as ammunition."),
                ("Reed Javelin", "A javelin made of stiff swamp reeds."),
                ("Mossy Axe", "An axe covered in swamp moss."),
                ("Swampguard Sword", "A sword that's a sentinel of the swamp."),
                ("Mire Mallet", "A club that's as sticky as the swamp's mire."),
                ("Bog Dagger", "A dagger with a handle of swamp bone."),
                ("Quicksand Quarterstaff", "A staff that pulls enemies in like quicksand.")],
            
            5: [("Swamp King's Cleaver", "A sword passed down through swamp royalty."),
                ("Toad Titan Club", "A club that commands the respect of the swamp."),
                ("Boglord Bow", "A bow that's said to rule over the swamp."),
                ("Marsh Master Mace", "A mace that's a testament to swamp craftsmanship."),
                ("Silt Supreme Slingshot", "A slingshot that embodies the swamp's spirit."),
                ("Reed Ruler Javelin", "A javelin that's the pinnacle of swamp weaponry."),
                ("Moss Monarch Axe", "An axe that's the heart of the swamp."),
                ("Swamp Sovereign Sword", "A sword that's a symbol of swamp leadership."),
                ("Mire Majesty Mallet", "A club that's the embodiment of the swamp."),
                ("Bog Baron Dagger", "A dagger that's the jewel of the swamp."),
                ("Quicksand Queen Quarterstaff", "A staff that's the essence of swamp power."),
                ("Toadstool Titan Two-Handed Sword", "A massive blade with the spirit of the swamp.")],

            6: [("Legend of the Swamp Cleaver", "A mythical sword whispered in swamp tales."),
                ("Mud Monolith Club", "A club that's a living swamp legend."),
                ("Boglore Bow", "A bow that carries the history of the swamp."),
                ("Marsh Myth Mace", "A mace that's a swamp legend brought to life."),
                ("Silt Saga Slingshot", "A slingshot that's the stuff of swamp legends."),
                ("Reed Relic Javelin", "A javelin that's a relic from ancient swamp times."),
                ("Moss Memory Axe", "An axe that embodies the swamp's ancient memories."),
                ("Swampland Story Sword", "A sword that's a tale of the swamp in metal."),
                ("Mire Mystery Mallet", "A club that's a riddle of the swamp."),
                ("Bogtale Dagger", "A dagger that's a story from old swamp days."),
                ("Quicksand Quest Quarterstaff", "A staff that's a journey through the swamp."),
                ("Toadstool Testament Two-Handed Sword", "A blade that's the swamp's old testament.")],
            },
        'OCEAN': {
            4: [("Tideblade", "A longsword that moves with the rhythm of the tides."),
                ("Coral Crusher", "A club made of dense coral from the seabed."),
                ("Wave Whisperer", "A dagger that carries the secrets of the sea."),
                ("Deepsea Bow", "A bow crafted from driftwood and ocean treasures."),
                ("Siren's Mace", "A mace that echoes the songs of the sirens."),
                ("Saltstone Slingshot", "A slingshot using dense saltstone pellets."),
                ("Abyssal Javelin", "A javelin inspired by the deep ocean creatures."),
                ("Sharktooth Axe", "An axe with a blade as sharp as a shark's tooth."),
                ("Poseidon's Guard", "A sword that protects the mysteries of the ocean."),
                ("Seashell Smasher", "A club made from bound seashells."),
                ("Mermaid Dagger", "A dagger with an intricate mermaid-shaped handle."),
                ("Current Caller Quarterstaff", "A staff that controls the ocean's currents.")],
            
            5: [("Leviathan Longsword", "A sword inspired by the mightiest ocean creatures."),
                ("Coral Crown Club", "A club that is the pride of the coral reefs."),
                ("Wave Walker Bow", "A bow that rides the ocean's waves."),
                ("Siren Sovereign Mace", "A mace that commands the respect of the sirens."),
                ("Triton's Treasure Two-Handed Sword", "A blade that holds the power of ocean deities."),
                ("Deepsea Dominator Dagger", "A dagger that reigns over the ocean's depths."),
                ("Current Captain Quarterstaff", "A staff that navigates the ocean's currents."),
                ("Poseidon's Power Axe", "An axe infused with the might of the ocean god."),
                ("Shark Sovereign Slingshot", "A slingshot that strikes fear into ocean predators."),
                ("Abyssal Authority Javelin", "A javelin that governs the deep ocean."),
                ("Tide Titan Falchion", "A curved blade that wields the power of the tides."),
                ("Saltstone Supreme Sword", "A sword crystallized from the ocean's essence.")],

            6: [("Ocean Oracle Longsword", "A mythical blade prophesied in oceanic legends."),
                ("Deepsea Deity Dagger", "A dagger that carries the blessings of ocean spirits."),
                ("Leviathan Legacy Bow", "A bow that is a relic from ancient oceanic battles."),
                ("Siren Saga Slingshot", "A slingshot that tells tales of the siren's song."),
                ("Coral Chronicle Club", "A club that carries the history of the coral reefs."),
                ("Wave Wisdom Quarterstaff", "A staff that imparts the knowledge of the waves."),
                ("Poseidon's Prophecy Axe", "An axe that's been foretold in ancient oceanic scriptures."),
                ("Shark Scripture Slingshot", "A slingshot inscribed with the shark's lore."),
                ("Abyssal Archive Javelin", "A javelin that holds the archives of the deep ocean."),
                ("Triton's Testament Two-Handed Sword", "A blade that is the ocean god's testament."),
                ("Mermaid Memory Mace", "A mace that embodies the memories of oceanic mermaids."),
                ("Tide Tale Falchion", "A curved blade that tells the tales of the tides.")],
            },
        'RIVER': {
            4: [("Riverrun Rapier", "A blade that flows like the river's current."),
                ("Catfish Club", "A club inspired by the river's feline fish."),
                ("Delta Dagger", "A dagger that splits its path like a river's delta."),
                ("Streamshot Slingshot", "A slingshot echoing the murmur of gentle streams."),
                ("Waterway Bow", "A bow crafted with wood from riverbanks."),
                ("Torrent Two-Handed Sword", "A blade as fierce as a raging river."),
                ("Current Caller Javelin", "A javelin that channels the river's momentum."),
                ("Fluvial Falchion", "A curved blade that mirrors a winding river."),
                ("River Reed Quarterstaff", "A staff made from the tallest river reeds."),
                ("Basin Blade", "A sword echoing the depths of river basins."),
                ("Rapids Rapier", "A blade as swift as river rapids."),
                ("Bankguard Bow", "A bow that's a sentinel of the riverbank.")],

            5: [("River Ruler's Rapier", "A sword wielded by legendary river guardians."),
                ("Current King's Club", "A club channeling the force of dominant currents."),
                ("Delta Duke Dagger", "A dagger with the intricacies of a river's end."),
                ("Stream Sovereign Slingshot", "A slingshot preferred by river royals."),
                ("Waterway Wizard's Bow", "A bow enchanted by river sages."),
                ("Torrent Titan's Two-Handed Sword", "A blade that summons the river's wrath."),
                ("Basin Baron Blade", "A sword holding authority over river realms."),
                ("Rapids Ruler Rapier", "A blade as swift and sharp as the fiercest rapids."),
                ("River Reed Regent Quarterstaff", "A staff bearing the mark of river leaders."),
                ("Fluvial Prince Falchion", "A blade that dances like a playful river."),
                ("Bankguard Baron Bow", "A bow that shields the treasures of the river."),
                ("Current Captain Javelin", "A javelin thrown with the river's blessing.")],

            6: [("Riverlore Rapier", "A mythical blade inscribed with river tales."),
                ("Stream Saga Slingshot", "A slingshot echoing ancient river ballads."),
                ("Delta Dream Dagger", "A dagger dreamt of in river myths."),
                ("Basin Ballad Bow", "A bow that sings tales of river origins."),
                ("Torrent Testament Two-Handed Sword", "A blade bearing the river's oldest tales."),
                ("Fluvial Fable Falchion", "A curved blade recounting river adventures."),
                ("River Reed Relic Quarterstaff", "A staff preserved from river's ancient rituals."),
                ("Rapids Rapier Remnant", "A blade recalling the valor of river warriors."),
                ("Waterway Whispering Javelin", "A javelin that whispers river secrets."),
                ("Current Chronicle Club", "A club that narrates river histories."),
                ("Bankguard Book of Bow", "A bow inscribed with riverbank tales."),
                ("Rivertide Tale Teller Two-Handed Sword", "A blade echoing the river's time-told tales.")],
        },
        'LAKE': {
            4: [("Lakeside Longsword", "A blade inspired by calm lakeside evenings."),
                ("Lilypad Lasher", "A club made of dense lily pads bound together."),
                ("Loch's Dagger", "A dagger reflecting the lake's depth and mystery."),
                ("Stillwater Slingshot", "A slingshot as serene as a placid lake."),
                ("Pond Prince Bow", "A bow embraced by the lake's gentle spirits."),
                ("Lake Luster Javelin", "A javelin shining with the lake's brilliance."),
                ("Basilisk Blade", "A sword with a hilt shaped like a lake beast."),
                ("Lakeshore Lance", "A spear that guards the boundaries of the lake."),
                ("Mirrorwater Mace", "A mace as clear and reflective as lake waters."),
                ("Freshwater Falchion", "A curved blade kissed by freshwater dew."),
                ("Lakebed Two-Handed Sword", "A blade grounded in the heart of the lake."),
                ("Reed Warden Quarterstaff", "A staff woven with the blessings of lake reeds.")],

            5: [("Lakelord Longsword", "A blade bearing the lake's ancient insignia."),
                ("Lilypad Luminary Lasher", "A club of leaders who understood lake's rhythm."),
                ("Loch Legend Dagger", "A dagger passed down through lake-guardian lineages."),
                ("Placid Protector Slingshot", "A slingshot used by the lake's revered watchers."),
                ("Pond Paladin Bow", "A bow that honors the protectors of sacred lakes."),
                ("Lustrous Lagoon Javelin", "A javelin that gleams with enchanted lake waters."),
                ("Beastbane Blade", "A sword said to have felled a lake monster."),
                ("Lakeside Luminary Lance", "A spear that's seen countless lake sunrises."),
                ("Mirror Master Mace", "A mace, its head like a perfectly still lake."),
                ("Freshflare Falchion", "A blade radiant with the essence of pure lake water."),
                ("Lakedeep Defender Two-Handed Sword", "A sword carrying the weight of the lake's depths."),
                ("Reed Royal Quarterstaff", "A staff bearing the emblem of the lake king.")],

            6: [("Lake's Legacy Longsword", "A blade echoing tales from the lake's origin."),
                ("Eternal Lilypad Lasher", "A club embodying the unending cycle of lake life."),
                ("Loch's Lore Dagger", "A dagger with inscriptions of lake myths."),
                ("Serene Sentinel Slingshot", "A slingshot channeling the lake's eternal calm."),
                ("Pond Paragon Bow", "A bow reflecting the pinnacle of lake craftsmanship."),
                ("Lustrous Luminance Javelin", "A javelin glowing with the heart of the lake."),
                ("Beast's Blessing Blade", "A sword believed to be a gift from a lake deity."),
                ("Lakeshore Legend Lance", "A spear etched with the lake's ancient map."),
                ("Mirror Mystique Mace", "A mace capturing the mysticism of the lake."),
                ("Freshfate Falchion", "A falchion foretold in the prophecies of the lake."),
                ("Lakedeep Lorekeeper Two-Handed Sword", "A blade preserving the lake's oldest tales."),
                ("Reed Ruler's Staff", "A staff that once commanded the lake's spirits.")],
            },

        'CAVE': {
            4: [("Cavern Cleaver", "A blade forged in the heart of dark caves."),
                ("Stalactite Stick", "A club made from dense cave formations."),
                ("Troglo-dagger", "A dagger favored by ancient cave dwellers."),
                ("Echoing Ebon Bow", "A bow that reverberates with the cave's secrets."),
                ("Darkdepths Two-Handed Sword", "A blade as deep and mysterious as the caves."),
                ("Batsight Slingshot", "A slingshot guided by the instincts of cave bats."),
                ("Grotto Guardian Javelin", "A javelin sworn to protect cave treasures."),
                ("Chasm Chopper", "An axe that echoes the vastness of cave chambers."),
                ("Shadowspire Spear", "A spear born from the cave's eternal darkness."),
                ("Limestone Lance", "A spear sharp as the edges of cave walls."),
                ("Crystal Cavern Club", "A club gleaming with embedded cave crystals."),
                ("Subterranean Saber", "A blade that delves deep into cave legends.")],

            5: [("Cave Conqueror Cleaver", "A blade that's seen and conquered cave's heart."),
                ("Stalactite Sovereign Stick", "A club held by cave kings of old."),
                ("Troglo-tribute Dagger", "A dagger dedicated to cave saviors."),
                ("Ebon Elder Bow", "A bow touched by the ancient magic of the caves."),
                ("Darkdepths Dominator Two-Handed Sword", "A blade echoing the authority of cave lords."),
                ("Batlord Slingshot", "A slingshot inspired by the master of cave bats."),
                ("Grotto Guru Javelin", "A javelin reflecting wisdom from deep within the caves."),
                ("Chasm Chief Chopper", "An axe symbolizing the rule over cave chasms."),
                ("Shadowsire Spear", "A spear drenched in the cave's oldest shadows."),
                ("Limestone Luminary Lance", "A spear renowned in the epics of cave dwellers."),
                ("Crystal Commander Club", "A club representing the hierarchy of cave miners."),
                ("Subterrene Saber", "A blade that whispers cave tales of old.")],

            6: [("Cavern Chronicle Cleaver", "A blade inscribed with the cave's entire history."),
                ("Stalactite Saga Stick", "A club bearing the tales of countless cave epochs."),
                ("Troglo-treasure Dagger", "A dagger that's more legend than weapon."),
                ("Echoing Epoch Bow", "A bow that has witnessed cave ages pass by."),
                ("Darkdepths Destiny Two-Handed Sword", "A blade foretold in cave prophecies."),
                ("Batsight Blessing Slingshot", "A slingshot created from bat whispers."),
                ("Grotto Gem Javelin", "A javelin, its tip a rare cave gemstone."),
                ("Chasm Crown Chopper", "An axe symbolizing the zenith of cave achievements."),
                ("Shadowscript Spear", "A spear where each scratch tells a cave story."),
                ("Limestone Legacy Lance", "A spear passed through generations of cave leaders."),
                ("Crystal Codex Club", "A club inscribed with the rituals of cave spirits."),
                ("Subterranean Scripture Saber", "A blade echoing with cave hymns of yore.")],
            },
        }

    if rarity in common_weapons:
        weapon, description = random.choice(common_weapons[rarity])
    elif theme in themed_weapons and rarity in themed_weapons[theme]:
        weapon, description = random.choice(themed_weapons[theme][rarity])
    else:
        return None, None

    return weapon, description

def armor_text_generate(theme, rarity):
    common_armors = { 
        0: [("Leather Armor", "A simple leather armor."),
            ("Forester's Leather", "A patterned leather armor."),
            ("Studded Leather", "A leather armor with metal studs."),
            ("Padded Armor", "A simple cloth armor."),
            ("Monk's Robes", "A simple monk's robes."),
            ("Magician Robes", "A simple magician's robes."),
            ("Banded Mail", "A simple banded mail."),
            ("Chain shirt", "A simple chain shirt."),
            ("Chainmail Armor", "A simple chainmail armor."),
            ("Scale Mail", "A simple scale mail."),
            ("Splint Mail", "A simple splint mail."),
            ("Half Plate", "A simple half plate."),
            ("Platemail Armor", "A simple platemail armor.")],

        1: [("Leather Armor+", "A reinforced leather armor."),
            ("Forester's Leather+", "A reinforced patterned leather armor."),
            ("Studded Leather+", "A reinforced leather armor with metal studs."),
            ("Padded Armor+", "A reinforced cloth armor."),
            ("Monk's Robes+", "A reinforced monk's robes."),
            ("Magician Robes+", "A reinforced magician's robes."),
            ("Banded Mail+", "A reinforced banded mail."),
            ("Chain shirt+", "A reinforced chain shirt."),
            ("Chainmail Armor+", "A reinforced chainmail armor."),
            ("Scale Mail+", "A reinforced scale mail."),
            ("Splint Mail+", "A reinforced splint mail."),
            ("Half Plate+", "A reinforced half plate."),
            ("Platemail Armor+", "A reinforced platemail armor.")],

        2: [("Leather Armor++", "A masterfully crafted leather armor."),
            ("Forester's Leather++", "A masterfully crafted patterned leather armor."),
            ("Studded Leather++", "A masterfully crafted leather armor with metal studs."),
            ("Padded Armor++", "A masterfully crafted cloth armor."),
            ("Monk's Robes++", "A masterfully crafted monk's robes."),
            ("Magician Robes++", "A masterfully crafted magician's robes."),
            ("Banded Mail++", "A masterfully crafted banded mail."),
            ("Chain shirt++", "A masterfully crafted chain shirt."),
            ("Chainmail Armor++", "A masterfully crafted chainmail armor."),
            ("Scale Mail++", "A masterfully crafted scale mail."),
            ("Splint Mail++", "A masterfully crafted splint mail."),
            ("Half Plate++", "A masterfully crafted half plate."),
            ("Platemail Armor++", "A masterfully crafted platemail armor.")],

        3: [("Elite Leather Armor", "The pinnacle of leather armor."),
            ("Elite Forester's Leather", "The pinnacle of patterned leather armor."),
            ("Elite Studded Leather", "The pinnacle of leather armor with metal studs."),
            ("Elite Padded Armor", "The pinnacle of cloth armor."),
            ("Elite Monk's Robes", "The pinnacle of monk's robes."),
            ("Elite Magician Robes", "The pinnacle of magician's robes."),
            ("Elite Banded Mail", "The pinnacle of banded mail."),
            ("Elite Chain shirt", "The pinnacle of chain shirt."),
            ("Elite Chainmail Armor", "The pinnacle of chainmail armor."),
            ("Elite Scale Mail", "The pinnacle of scale mail."),
            ("Elite Splint Mail", "The pinnacle of splint mail."),
            ("Elite Half Plate", "The pinnacle of half plate."),
            ("Elite Platemail Armor", "The pinnacle of platemail armor.")],
    }

    themed_armors = {
    "PLAINS": {
        4: [("Sunlit Cuirass", "A chestplate gleaming with the brilliance of a thousand suns."),
            ("Prairie Defender", "Armor with an essence of the vast plains."),
            ("Wind Whisperer Robe", "A robe that seems to echo the gentle winds of the plains."),
            ("Dandelion Mail", "Chainmail adorned with patterns resembling dandelions."),
            ("Steppe Guardian", "Armor pieces that vibrate with the energy of the vast steps."),
            ("Golden Grass Mail", "Golden mail that seems made of intertwined grass strands."),
            ("Prairie Plate", "Plate armor engraved with patterns from the plains."),
            ("Sunrise Cuirass", "Armor that captures the first light of the dawn."),
            ("Grassland Guardian", "The chosen armor for those who defend the vast grasslands."),
            ("Breeze Draped Robe", "This robe has a gentle and calming touch."),
            ("Horizon Mail", "A chainmail capturing the vastness of the horizon."),
            ("Prairie Lord's Armor", "A legendary armor set reserved for the ruler of the plains.")],

        5: [("Bison Guardian Plate", "Armor inspired by the mighty bison of the plains."),
            ("Eon Sun Robe", "A robe that glimmers, reflecting the eternal sun."),
            ("Legend Wrapped Suit", "An armor whispered in tales told by the ancient wind."),
            ("Grass King's Plate", "A plate that resembles the vast sea of grass."),
            ("Twilight Plate", "Armor imbued with the last rays of the setting sun."),
            ("Buffalo's Revenge", "A heavy plate armor, tribute to the wild buffalo."),
            ("Harvest Mail", "A chainmail with golden hues, representing the harvest season."),
            ("Echoing Wind Suit", "Armor that resonates with the whispers of the wind."),
            ("Dusk Draped Robe", "A robe that captures the tranquility of the evening."),
            ("Prairie Spirit Suit", "Armor believed to be blessed by the spirits of the plains."),
            ("Meadow's Embrace", "Armor that gives the warmth of lying down in a meadow."),
            ("Sunset Guardian Armor", "Armor that seems to merge with the hues of the setting sun.")],

        6: [("Primordial Plains Protector", "Ancient armor told in legends, echoing the birth of plains."),
            ("Golden Grass Shield", "A shield that appears to be woven from the eternal grass."),
            ("Dawn Creator Plate", "A plate that brings forth the dawn's first light."),
            ("Sun God's Mail", "A mail believed to be worn by the god of the sun."),
            ("Infinite Horizon Plate", "Armor that seems to extend into infinity, like the horizon."),
            ("Ageless Dandelion Suit", "A suit inspired by the timeless beauty of dandelions."),
            ("Everlasting Day Robe", "A robe that captures the essence of an endless day."),
            ("First Wind's Embrace", "Armor that carries the touch of the first wind."),
            ("Prairie's Pulse", "Armor that beats with the very heart of the vast plains."),
            ("Solar Radiance Plate", "A plate that emanates the brilliance of the sun."),
            ("Twilight's Last Stand", "Armor that stands defiant, capturing the last light."),
            ("Eternal Plains Guardian", "The legendary armor of the eternal protector of the plains.")]
    },
    "FOREST": {
        4: [("Greenwood Mail", "A chainmail with a hue reminiscent of deep forests."),
            ("Forest Walker Robes", "Robes that seem to blend seamlessly with the forest."),
            ("Bark Plated Armor", "Armor that has the texture and strength of tree bark."),
            ("Mossy Cuirass", "A cuirass that is covered in a layer of soft moss."),
            ("Canopy Defender", "Armor that embodies the spirit of the forest canopy."),
            ("Leaf Cloak", "A cloak made from woven leaves, granting natural camouflage."),
            ("Ancient Tree Plate", "Armor carved from the wood of ancient trees."),
            ("Fernweave Suit", "A suit that has patterns of ferns all over it."),
            ("Grove Guardian Armor", "A set of armor blessed by the spirits of the grove."),
            ("Root Wrapped Robe", "A robe that has roots intricately wrapped around it."),
            ("Timber Mail", "Chainmail with wooden links, harmonizing armor with nature."),
            ("Forest Lord's Armor", "Legendary armor said to be worn by the ruler of the forest.")],

        5: [("Elven Plate", "A plate crafted by elves, blending magic and nature."),
            ("Dew Draped Robes", "Robes that shimmer with the morning dew of the forest."),
            ("Branchbound Mail", "A chainmail intertwined with resilient branches."),
            ("Moonlit Leaf Suit", "Armor that glows faintly under moonlight."),
            ("Mystic Tree Armor", "Armor infused with the magic of ancient trees."),
            ("Silvan Protector Plate", "Armor that has seen many battles under the forest canopy."),
            ("Nature's Embrace", "Armor that nurtures like Mother Nature."),
            ("Grove Whisper Robe", "A robe that whispers secrets of the enchanted grove."),
            ("Forest Spirit Suit", "A suit believed to be worn by forest spirits."),
            ("Thicket Guardian Mail", "Chainmail tough as the dense thicket."),
            ("Entwood Armor", "Armor crafted from the wood of the mighty Ents."),
            ("Sun Dappled Plate", "Plate armor that captures the sun's dance in the forest.")],

        6: [("Ageless Canopy Defender", "Legendary armor representing the timeless forest canopy."),
            ("Mystic Moon Plate", "Plate armor reflecting the mystic moon’s gleam in the forest."),
            ("Silvan Emperor's Suit", "The exquisite armor of the Emperor of the Sylvan realm."),
            ("Treeheart Robes", "Robes pulsating with the very heart of ancient trees."),
            ("Enchanted Forest Plate", "Armor echoing with enchantments from the forest's core."),
            ("Nature’s Final Stand", "Armor that is nature's response to dire threats."),
            ("Primordial Grove Mail", "Ancient chainmail echoing tales of the primordial grove."),
            ("Ent King’s Armor", "Armor that embodies the power and majesty of the King of Ents."),
            ("Mystic Glade Robes", "Robes reflecting the serenity and magic of mystic glades."),
            ("Forest Genesis Suit", "The suit that harks back to the dawn of the first forest."),
            ("Moonshadow Plate", "Plate armor that moves stealthily like shadows under moonlight."),
            ("Evergreen Guardian", "The armor of the guardian who never lets the forest wither.")]
    },

    "MOUNTAIN": {
        4: [("Rockplate Armor", "Armor that mirrors the ruggedness of mountains."),
            ("Mountain Soul Cuirass", "A cuirass infused with the spirit of the mountains."),
            ("Stonebind Mail", "A chainmail that is as resilient as mountain stone."),
            ("Peak Climber Robes", "Robes that grant agility to traverse mountain peaks."),
            ("Cliffside Defender", "Armor inspired by the sheer cliffs of mountains."),
            ("Granite Suit", "Armor crafted with the toughness of granite."),
            ("Highland Plate", "A plate that embodies the grandeur of highlands."),
            ("Crag Lord's Armor", "Armor that resonates with the might of the crag lord."),
            ("Echoing Canyon Mail", "Chainmail that captures the essence of echoing canyons."),
            ("Summit Seeker Suit", "A suit designed for those who seek mountain summits."),
            ("Avalanche Plate", "Armor with the force and power of an avalanche."),
            ("Ridge Walker Robes", "Robes designed for those who walk the mountain ridges.")],

        5: [("Eagle Flight Suit", "Armor granting the wearer the majesty of mountain eagles."),
            ("Stoneheart Plate", "Plate armor infused with the very heart of mountain stone."),
            ("Mountain Spirit Robes", "Robes that carry blessings from mountain spirits."),
            ("Crag Protector Mail", "Chainmail designed to protect against mountain threats."),
            ("Ancient Peak Armor", "Armor that has witnessed the birth of ancient peaks."),
            ("Ravine Runner Suit", "A suit tailored for those who navigate deep ravines."),
            ("Skytouch Plate", "Armor for those who aspire to touch the mountain sky."),
            ("Frostpeak Guardian", "Armor designed for guarding the snowy mountain peaks."),
            ("Summit's Embrace", "Armor that hugs the wearer like the mountain's peak."),
            ("Stonewind Robes", "Robes that resonate with the winds that sweep across stone."),
            ("Everhigh Plate", "Plate armor reflecting the eternal majesty of high peaks."),
            ("Mountain King's Armor", "The legendary armor of the king of the mountains.")],

        6: [("Primordial Peak Plate", "Plate armor that speaks of the first mountain peak."),
            ("Sky Emperor's Robes", "Robes worn by the emperor who ruled the mountain skies."),
            ("Ridge Ruler Suit", "Suit that grants dominion over all mountain ridges."),
            ("Heartstone Armor", "Armor pulsating with the very heart of the mountain."),
            ("Eagle's Aerie Plate", "Plate armor inspired by the high nests of mountain eagles."),
            ("Canyon Creator Mail", "Chainmail echoing the creation of mountain canyons."),
            ("Mystic Mountain Robes", "Robes reflecting mysteries locked deep within mountains."),
            ("Everpeak Defender", "Armor that stands tall like the eternal mountain peaks."),
            ("Stone Emperor’s Suit", "The magnificent suit of the emperor of all stones."),
            ("Cliff Guardian Armor", "Armor that has the resilience of sheer mountain cliffs."),
            ("Mountain's Pulse", "Armor that beats with the very pulse of the mountain."),
            ("Timeless Peak Plate", "Plate armor that stands as timeless as mountain peaks.")]
    },

    "DESERT": {
        4: [("Sandweaver Robes", "Robes that blend seamlessly with desert sands."),
            ("Dune Defender", "Armor designed to protect against desert challenges."),
            ("Sunscorch Plate", "Armor that mirrors the intensity of the desert sun."),
            ("Oasis Seeker Suit", "A suit designed for those seeking desert oases."),
            ("Sandstorm Mail", "A chainmail designed to withstand desert sandstorms."),
            ("Cactus Plate", "A plate made resilient by adopting the qualities of a cactus."),
            ("Desert Mirage Robes", "Robes that play tricks on the eyes, like desert mirages."),
            ("Sandsnake Suit", "A suit that allows swift and silent movement like a desert snake."),
            ("Sunset Cuirass", "A cuirass that captures the colors of the desert sunset."),
            ("Camel Rider Armor", "Armor tailored for the brave riders of desert camels."),
            ("Heatwave Mail", "Chainmail that reflects the intense heat of desert waves."),
            ("Desert Nomad Robes", "Robes tailored for those who wander the vast deserts.")],

        5: [("Pharaoh's Plate", "A plate that speaks of the might and majesty of desert pharaohs."),
            ("Sand Emperor's Robes", "Robes worn by the emperor who ruled the vast sands."),
            ("Dune Walker Suit", "A suit tailored for those who traverse vast sand dunes."),
            ("Desert Spirit Mail", "Chainmail that carries the blessings of desert spirits."),
            ("Mirage Creator Armor", "Armor that creates illusions like the desert mirage."),
            ("Oasis Guardian Plate", "Plate armor that protects the life-giving desert oases."),
            ("Sandsea Sailor Suit", "A suit designed for those sailing the vast sea of sand."),
            ("Desert Wind Robes", "Robes that resonate with the gentle winds of the desert."),
            ("Suncurse Armor", "Armor that carries the curse of the relentless desert sun."),
            ("Moonlit Dune Mail", "Chainmail that gleams under the desert moonlight."),
            ("Desert Rose Robes", "Robes inspired by the beauty and resilience of the desert rose."),
            ("Golden Sand Plate", "Plate armor that gleams like the golden sands of the desert.")],

        6: [("Timeless Desert Defender", "Armor that stands as eternal as the timeless desert."),
            ("Sun God’s Plate", "Plate armor believed to be worn by the god of the sun."),
            ("Sands of Eternity Robes", "Robes that echo tales from the sands of eternity."),
            ("Desert Phoenix Armor", "Armor that embodies the rebirth and fire of the desert phoenix."),
            ("Dune Emperor's Suit", "The magnificent suit of the emperor of all dunes."),
            ("Desert's Heart Plate", "Plate armor pulsating with the very heart of the desert."),
            ("Mirage Master Mail", "Chainmail designed by the master of desert illusions."),
            ("Sandsea King’s Robes", "Robes reflecting the majesty of the king of the sandsea."),
            ("Oasis Dreamer Suit", "Suit worn by those who dream of lush desert oases."),
            ("Desert Storm Guardian", "Armor designed to protect against the fiercest desert storms."),
            ("Golden Dune Defender", "Armor that shimmers like the golden dunes under the sun."),
            ("Eternal Desert Plate", "Plate armor that resonates with the eternity of the desert.")]
    },
    "SWAMP": {
        4: [("Bog Guardian Plate", "Armor crafted to defend the murky depths of the swamp."),
            ("Mirewalker Robes", "Robes tailored for those who traverse mucky terrain."),
            ("Marshmist Armor", "Armor that embodies the ethereal mist of marshlands."),
            ("Reedweave Suit", "A suit woven from the resilient reeds of the swamp."),
            ("Mudshield Mail", "Chainmail designed to repel the swamp's thick mud."),
            ("Swamp Serpent Scale", "Armor bearing the durable scales of swamp serpents."),
            ("Fen Protector Plate", "Armor reflecting the silent watch of the fens."),
            ("Boglore Robes", "Robes that carry the ancient tales of swamp spirits."),
            ("Marshlight Mail", "A chainmail that gleams faintly in the swamp's gloom."),
            ("Wetland Wanderer Suit", "Armor designed for the nomads of the wetlands."),
            ("Bog Shadow Armor", "Armor granting the ability to blend with swamp shadows."),
            ("Mossclad Plate", "Plate armor covered in a protective layer of swamp moss.")],

        5: [("Swampland Sorcerer Robes", "Robes imbued with the arcane energies of the swamp."),
            ("Mudmantle Armor", "Armor that provides excellent camouflage in the swamp."),
            ("Bogstrider Boots", "Boots that allow swift movement across swampy terrains."),
            ("Miremage Plate", "A plate armor designed for spellcasters in the swamps."),
            ("Serpentscale Armor", "Armor made from the scales of swamp-dwelling serpents."),
            ("Bogshade Robes", "Robes that allow the wearer to blend into swampy shadows."),
            ("Marshwater Mantle", "A protective mantle that shields against swamp water."),
            ("Reedrunner Ringmail", "Ringmail perfect for quick maneuvers in the swamp."),
            ("Bogbound Brigandine", "A brigandine that's resilient to the swamp's dampness."),
            ("Mudmark Mail", "A chainmail marked by the distinctive mud of the swamp."),
            ("Wetleaf Warplate", "A plate designed for swamp skirmishes."),
            ("Fenlight Frocks", "Robes that gleam under the faint light of the swamp.")],

        6: [("Swampdrake Scaleplate", "Armor crafted from the scales of a legendary swamp drake."),
            ("Bogbeast Boneguard", "A guard made from the bones of ancient swamp beasts."),
            ("Miremystic Robes", "Robes radiating the arcane aura of the swamp."),
            ("Fenfire Façade", "Armor that glows with the mysterious fires of the fen."),
            ("Swampshadow Shroud", "A shroud that envelops the wearer in swampy shadows."),
            ("Marshmaster Mail", "A chainmail that's worn by the masters of the swamp."),
            ("Bogbinder Brigandine", "A brigandine that binds the power of the bog."),
            ("Swamplurk Silks", "Silks that are soft to touch but tough against swamp hazards."),
            ("Mudmaul Mantle", "A mantle that provides powerful protection in the mires."),
            ("Swampspell Sequins", "Robes adorned with sequins that shimmer with magic."),
            ("Bogboss Breastplate", "A breastplate worn by the leaders in the swamp."),
            ("Miremarsh Mail", "Chainmail that merges the essence of mires and marshes.")],
    },
    "OCEAN": {
        4: [("Waveguard Plate", "A shimmering plate infused with the spirit of the ocean."),
            ("Seawalker Robes", "Robes that harness the calmness of the vast sea."),
            ("Abyssal Armor", "Armor forged from materials of the ocean's depths."),
            ("Coral Crafted Suit", "A suit crafted from robust ocean corals."),
            ("Tidetouched Mail", "Chainmail that ebbs and flows like the ocean's tides."),
            ("Siren's Scale", "Armor that resonates with the haunting melodies of sirens."),
            ("Barnacle Barrier", "Armor that's as tough as age-old ocean barnacles."),
            ("Oceanlord Robes", "Robes that command the respect of all sea beings."),
            ("Deep Dive Mail", "Chainmail designed for oceanic expeditions."),
            ("Marine Mirage Suit", "Armor that blends seamlessly with the ocean."),
            ("Saltsealed Plate", "Armor sealed with the ageless salt of the seas."),
            ("Kelpclad Armor", "Armor intertwined with the toughness of ocean kelp.")],

        5: [("Krakenhide Armor", "Armor crafted from the hide of a formidable kraken."),
            ("Seabreeze Silks", "Silks that flow gracefully, echoing the ocean's grace."),
            ("Nautical Knight Plate", "Plate armor favored by the knights of the ocean."),
            ("Pearlpride Robes", "Robes adorned with pearls from the ocean's depths."),
            ("Tsunami Tasset", "Armor that carries the overwhelming force of tsunamis."),
            ("Merfolk Mail", "A shimmering mail worn by the guardians of merfolk."),
            ("Coral Crown Guard", "A guard that's as elegant as a coral crown."),
            ("Whalebone Ward", "Armor reinforced with the mighty bones of whales."),
            ("Seastorm Scale", "Armor that embodies the fury of oceanic storms."),
            ("Depthdancer Drapes", "Robes that move fluidly, akin to an oceanic dance."),
            ("Mariner's Mantle", "A protective mantle worn by seasoned ocean explorers."),
            ("Wave Whisperer Wares", "Armor that whispers tales of the vast ocean.")],

        6: [("Ocean Emperor Plate", "A plate that stands testament to the ocean's majesty."),
            ("Abyssal Aegis Armor", "Armor that provides an aegis against oceanic abysses."),
            ("Seagod Silks", "Silks that are blessed by the deities of the ocean."),
            ("Triton's Triumph", "Armor that captures the grandeur of oceanic tritons."),
            ("Maelstrom Mail", "A mail that swirls with the energies of oceanic maelstroms."),
            ("Sirenqueen Scale", "A magnificent armor dedicated to the queen of sirens."),
            ("Deeplord Drapes", "Robes that rule over the mysterious oceanic depths."),
            ("Coral King Cuirass", "A cuirass that's as regal as the king of corals."),
            ("Seadevil Suit", "Armor that embodies the mischief of oceanic devils."),
            ("Ocean Oracle Outfit", "Robes that predict the whims and fancies of the sea."),
            ("Tidal Titan Tunic", "A tunic that harnesses the strength of oceanic tides."),
            ("Wave Witch Ward", "Armor favored by the enigmatic witches of the ocean.")],
    },
    "RIVER": {
        4: [("Rivertide Robes", "Robes that capture the gentle flow of rivers."),
            ("Stream Seeker Suit", "Armor tailor-made for river exploration."),
            ("Banksman's Barrier", "A protective gear favored by river banksmen."),
            ("Currentclad Chain", "Chain armor that sways like river currents."),
            ("River Reed Robe", "A robe woven from the finest river reeds."),
            ("Rill Raider's Rig", "Gear worn by those who traverse rivulets and rills."),
            ("Brookblessed Breastplate", "Breastplate bathed in the purity of brooks."),
            ("Rapid Runner Raiment", "Raiment designed for river rapid adventurers."),
            ("Fluvial Flow-fold", "A protective gear mimicking river fluidity."),
            ("Riverstone Reinforced", "Armor fortified with smooth river stones."),
            ("Delta Draped Drape", "Armor inspired by the intricate river deltas."),
            ("Meadow's Margin Mail", "Chain mail resembling the meadows by rivers.")],

        5: [("River Guardian Guard", "A guard worn by protectors of sacred rivers."),
            ("Streamlord Silks", "Silks that command the respect of all freshwater beings."),
            ("Banksman's Bulwark", "An improved defensive gear for river banksmen."),
            ("Cascadeclad Chain+", "An upgraded chain armor infused with cascading energies."),
            ("River Deity Drapery", "A robe blessed by the deities of the river."),
            ("Rill King's Rigging", "Gear that signifies authority over rills."),
            ("Brookblessed Barrier++", "A reinforced breastplate with brook blessings."),
            ("Rapid Dominator Dress", "A dress for those who dominate river rapids."),
            ("Fluvial Phantom Fold", "Gear that gives the wearer a river ghostly presence."),
            ("Riverstone Rig++", "An enhanced armor with embedded river gemstones."),
            ("Delta Dream Drapery", "Armor echoing the dreams of river deltas."),
            ("Meadow's Majesty Mail", "A majestic mail dedicated to river meadows.")],

        6: [("River Emperor Ensemble", "An ensemble dedicated to the river's majesty."),
            ("Streamlord Supreme Silks", "The ultimate silks dedicated to streamlords."),
            ("Banksman's Bastion", "The ultimate protective gear for river banksmen."),
            ("Cascade King's Chain", "Chain armor that's the envy of all cascades."),
            ("River Royalty Robe", "A robe that only river royalty can adorn."),
            ("Rill Ruler's Rigging+", "The pinnacle of gear for rill rulers."),
            ("Brook's Best Breastplate", "A breastplate that's the best of all brooks."),
            ("Rapid Masterpiece Mail", "A mail that's a masterpiece in rapid traversal."),
            ("Fluvial God's Fold", "Gear that's touched by the hands of river gods."),
            ("Riverstone Relic Rig", "A relic armor from the ancient riverstone times."),
            ("Delta Divine Drapery", "Armor that echoes the divine touch of deltas."),
            ("Meadow's Miracle Mail", "A mail that's nothing short of a river meadow miracle.")],
    },

    "LAKE": {
        4: [("Lakeshore Laminar", "Armor that embodies the calmness of lakes."),
            ("Lake Leaf Leather", "Leather armor made from lakebed leaves."),
            ("Pondplate Armor", "Armor inspired by the stillness of ponds within lakes."),
            ("Lakewater Loom", "Robes woven from the threads of lake spirits."),
            ("Lakeside Ledger", "Armor crafted by the guardians of the lakeside."),
            ("Lake Legend Layer", "Layered armor echoing the legends of the lake."),
            ("Lake Luminary Leather", "Leather armor that gleams under the lake's light."),
            ("Water Warden Wardrobe", "Wardrobe worn by the wardens of freshwater."),
            ("Deep Lake Drapes", "Drapes inspired by the deep mysteries of lakes."),
            ("Lakeshadow Suit", "A suit that captures the shadows of the lake."),
            ("Lakelight Livery", "Livery that glows with the gentle lights of the lake."),
            ("Lakebreeze Linen", "Linen robes touched by the breezes of the lake.")],

        5: [("Lake Guardian Gear", "Gear worn by the sacred protectors of lakes."),
            ("Lakelord's Ledger", "A ledger armor that demands authority over lakes."),
            ("Pondplate Protector", "An upgraded armor inspired by pristine ponds."),
            ("Lake Essence Ensemble", "Ensemble resonating with the essence of the lake."),
            ("Lakeside Luminary", "Armor inspired by the luminaries of the lakeside."),
            ("Lake Legend Layer+", "A superior layered armor of lake legends."),
            ("Deep Lake Defender", "A protective gear dedicated to the lake's depths."),
            ("Water Warden Wardrobe+", "An improved wardrobe of lake wardens."),
            ("Lakebottom Barrier", "Armor inspired by the hard bottom of lakes."),
            ("Lakeshadow Stealth Suit", "A suit that harnesses the lake's shadows."),
            ("Lakelight Luminary", "Livery that outshines all lights of the lake."),
            ("Lakebreeze Bliss", "Robes that embody the blissful breezes of the lake.")],

        6: [("Lake Emperor Armor", "Armor dedicated to the unmatched emperor of lakes."),
            ("Lakelord's Legend", "The pinnacle of armor dedicated to the lakelord."),
            ("Pondplate Paragon", "The ultimate armor inspired by ancient ponds."),
            ("Lake Essence Elysium", "The Elysium ensemble of lake essence."),
            ("Lakeside Lordship", "Armor echoing the lordship over all lakesides."),
            ("Lake Legend's Legacy", "Armor that's a legacy of lake legends."),
            ("Deep Lake Dominator", "The dominator's gear for the depths of lakes."),
            ("Water Warden's Wonder", "A wondrous wardrobe of top lake wardens."),
            ("Lakebottom Bastion", "A bastion armor inspired by the lake's base."),
            ("Lakeshadow Supreme", "The supreme suit harnessing lake shadows."),
            ("Lakelight Luminance", "The most luminous livery of the lake."),
            ("Lakebreeze Blessing", "Robes that are the ultimate blessing of lake breezes.")],
    },
    "CAVE": {
        4: [("Caveshadow Coat", "Armor that embraces the serenity of caves."),
            ("Cavernclad Chain", "Chain armor that mimics the patterns of caverns."),
            ("Stalactite Suit", "Armor inspired by the stalactites of caves."),
            ("Stalagmite Mail", "Mail armor echoing the might of stalagmites."),
            ("Cavecloth Cloak", "A cloak woven from the fabric of cave spirits."),
            ("Underrock Uniform", "Uniform inspired by the sturdy base of caves."),
            ("Cave Core Corset", "A corset that touches the very core of cave essence."),
            ("Grotto Guard", "Armor worn by the guardians of ancient grottos."),
            ("Echoing Egress Ensemble", "Ensemble inspired by the echoing cave exits."),
            ("Tunnel Titan Tunic", "Tunic that captures the strength of cave tunnels."),
            ("Cave Crown Cloak", "A cloak that's fit for the king of all caves."),
            ("Subterranean Suit", "A suit inspired by the mysteries of the subterranean.")],

        5: [("Cave Guardian Gear", "Gear that's the envy of all cave guardians."),
            ("Cavern King's Chain", "The chain armor of the undisputed cavern king."),
            ("Stalactite Sentinel Suit", "Armor dedicated to the sentinels of stalactites."),
            ("Stalagmite Master Mail", "A master's mail armor of stalagmite might."),
            ("Cavecloth Cloak+", "An enhanced cloak touched by cave spirits."),
            ("Underrock Ultra Uniform", "An upgraded uniform of the cave's underrock."),
            ("Cave Core Corset+", "A superior corset of cave core energy."),
            ("Grotto Guardian Gear", "Gear dedicated to the ultimate grotto guardian."),
            ("Echoing Egress Elite", "An elite ensemble of echoing cave egress."),
            ("Tunnel Titan Tunic+", "An enhanced tunic of tunnel titan strength."),
            ("Cave Crown Coronation Cloak", "A cloak dedicated to cave crown coronations."),
            ("Subterranean Supreme Suit", "The supreme suit of the subterranean.")],

        6: [("Cave Emperor Ensemble", "The ensemble dedicated to the cave emperor."),
            ("Cavernclad Crown", "The crown armor of all caverns."),
            ("Stalactite Sovereign Suit", "The sovereign's suit of stalactites."),
            ("Stalagmite Majesty Mail", "The majestic mail of stalagmite strength."),
            ("Cavecloth Coronation Cloak", "The coronation cloak of cavecloth spirit."),
            ("Underrock Ultimate Uniform", "The ultimate uniform of the cave's underrock."),
            ("Cave Core King's Corset", "The king's corset of cave core energy."),
            ("Grotto God's Guard", "The guard gear of the god of grottos."),
            ("Echoing Egress Emperor", "The emperor's ensemble of echoing egress."),
            ("Tunnel Titan's Top Tunic", "The top tunic of tunnel titan strength."),
            ("Cave Crowned Cloak", "The ultimate cloak of the cave crown."),
            ("Subterranean Sovereign Suit", "The sovereign suit of the subterranean.")],
    }
    }

    if rarity in common_armors:
        armor, description = random.choice(common_armors[rarity])
    elif theme in themed_armors and rarity in themed_armors[theme]:
        armor, description = random.choice(themed_armors[theme][rarity])
    else:
        return None, None

    return armor, description

def consumable_text_generate(theme, rarity):
    common_consumables = {
            0: [
                ("Minor Healing Potion", "Restores a small amount of health."),
                ("Basic Mana Elixir", "Restores a small amount of mana."),
                ("Stale Bread", "Barely nutritious, but it's food."),
                ("Weak Stamina Drink", "Slightly boosts stamina."),
                ("Rusty Key", "Might open an old lock."),
                ("Tattered Map", "Could lead to nowhere or somewhere."),
                ("Crumbled Note", "A note with some faded writings."),
                ("Diluted Poison", "Weakens the enemy slightly."),
                ("Fruit Peel", "Slippery when stepped on."),
                ("Empty Flask", "Can be used to store liquids."),
                ("Muddy Water", "Not safe for drinking."),
                ("Worn Scroll", "A scroll with barely readable magic."),
            ],
            1: [
                ("Healing Potion", "Restores health."),
                ("Mana Elixir", "Restores mana."),
                ("Fresh Bread", "Nutritious and fresh."),
                ("Stamina Drink", "Boosts stamina."),
                ("Iron Key", "Opens locked doors."),
                ("Map", "Marks a specific location."),
                ("Note", "Information from a stranger."),
                ("Poison", "Weakens the enemy."),
                ("Banana Peel", "Trick enemies with this."),
                ("Flask", "Used to store various liquids."),
                ("Clean Water", "Safe for drinking."),
                ("Scroll", "A scroll with magic incantations."),
            ],
            2: [
                ("Major Healing Potion", "Restores a large amount of health."),
                ("Epic Mana Elixir", "Restores a large amount of mana."),
                ("Roast Chicken", "Delicious and filling."),
                ("Mighty Stamina Drink", "Greatly boosts stamina."),
                ("Golden Key", "A key for a special lock."),
                ("Detailed Map", "Marks multiple points of interest."),
                ("Signed Note", "An important message."),
                ("Deadly Poison", "Dangerous to enemies."),
                ("Spiked Trap", "Harms enemies who step on it."),
                ("Crystal Flask", "A beautifully designed flask."),
                ("Spring Water", "Refreshes and revitalizes."),
                ("Magic Scroll", "A scroll with powerful magic."),
            ],
            3: [
                ("Ultra Healing Potion", "Fully restores health."),
                ("Mystic Mana Elixir", "Fully restores mana."),
                ("Feast Platter", "A feast for the brave!"),
                ("Ultimate Stamina Drink", "Maximizes stamina."),
                ("Enchanted Key", "Opens any lock."),
                ("Mystic Map", "Reveals hidden locations."),
                ("Sealed Note", "Contains secretive information."),
                ("Lethal Poison", "Instantly fatal to enemies."),
                ("Bear Trap", "Catches bigger threats."),
                ("Gilded Flask", "For the finest of liquids."),
                ("Elixir", "Grants minor buffs."),
                ("Ancient Scroll", "Holds forbidden magic."),
            ],
        },
           
    themed_consumables = {
        "PLAINS": {
            4: [
                ("Prairie Soup", "A hearty soup made from prairie ingredients."),
                ("Windrunner Potion", "Run as fast as the prairie winds."),
                ("Golden Grain", "Grains that restore vitality."),
                ("Sunset Brew", "A calming drink that mirrors the plains' colors."),
                ("Bison Broth", "A nutritious broth made from bison."),
                ("Prairie Nectar", "Sweet liquid extracted from wildflowers.")
            ],
            5: [
                ("Dewdrop Elixir", "Captures the first light of dawn."),
                ("Prairie Fire Drink", "Spicy drink to keep you warm at night."),
                ("Golden Grass Juice", "Revitalizes and gives energy."),
                ("Horizon's Blessing", "Glimpse distant places with a sip."),
                ("Gopher's Escape Potion", "Disappear from sight momentarily."),
                ("Boundless Sky Brew", "Feel limitless under the open sky.")
            ],
            6: [
                ("Starfall Potion", "Imbued with a fragment of a shooting star."),
                ("Moonshadow Tea", "Reveals hidden truths in the night."),
                ("Sunrise Salve", "Heals wounds at the break of day."),
                ("Endless Plain Elixir", "The vastness of the plains in a drink."),
                ("Buffalo Spirit Brew", "Gain the strength of a mighty buffalo."),
                ("Prairie King's Tribute", "A drink worthy of plains royalty.")
            ]
        },
        "FOREST": {
            4: [
                ("Forest Herb Mix", "A mix of herbs found only in the forest."),
                ("Bark Shield Potion", "Provides a shield made of tree bark."),
                ("Mystic Mushroom", "Restores mana and gives a forest's blessing."),
                ("Potion of Photosynthesis", "Regenerate health in sunlight."),
                ("Vine Whip Potion", "Allows user to summon vine whips."),
                ("Woodland Camouflage", "Blend in with the forest surroundings."),
                ("Tree Sap Elixir", "Increases resistance to physical attacks."),
                ("Fruit of Vitality", "Instantly restores a portion of health."),
                ("Nectar of Agility", "Increases speed for a short duration."),
                ("Forest Mist Potion", "Become invisible in forest environments."),
                ("Sylvan Sprout", "Plant it to grow something mysterious."),
                ("Elixir of Forest Spirits", "Feel more connected to the forest."),
            ],
            5: [
                ("Ancient Oak Elixir", "Temporarily gain the strength of an old oak."),
                ("Mystic Fern Potion", "A potion made from rare forest ferns."),
                ("Heart of the Forest", "Restores all health and mana."),
                ("Elven Bread", "Lasts for ages and is incredibly nutritious."),
                ("Potion of Deep Woods", "Navigate the forest without getting lost."),
                ("Moonlit Dew", "Dew from forest plants, shines in moonlight."),
                ("Forest God's Nectar", "Boosts all stats when consumed."),
                ("Nature's Blessing", "Temporarily immune to all forest-based ailments."),
                ("Root of Endurance", "Boosts stamina recovery for an extended period."),
                ("Forest Phantom Elixir", "Become one with the forest shadows."),
                ("Tree Whisper Potion", "Communicate with the forest trees."),
                ("Enchanted Moss", "Eat to regain mana over time."),
            ],
            6: [
                ("Forest God's Brew", "Said to contain the blessings of the forest god."),
                ("Elixir of Eternal Spring", "Experience the vitality of an evergreen forest."),
                ("Luminous Fungus", "Emit a calming glow in the dark."),
                ("Nature's Essence", "Capture the very essence of the forest."),
                ("Enchanted Forest Fruit", "A fruit said to grant visions."),
                ("Woodland God's Blessing", "The highest blessing from the forest."),
                ("Greenwood Elixir", "Turn into a tree temporarily."),
                ("Moonshadow Potion", "Navigate the forest safely at night."),
                ("Ancient Forest Spirit Brew", "Attract forest spirits for protection."),
                ("Forest Dream Potion", "Experience dreams of ancient forests."),
                ("Nature's Heartbeat", "Sync with the heartbeat of the forest."),
                ("Guardian's Respite", "A potion preferred by forest guardians."),
            ],
        },
        "MOUNTAINS": {
            4: [
                ("Mountain Herb Mix", "A blend of mountain herbs known for their potency."),
                ("Granite Shield Potion", "Provides a shield as sturdy as mountain rock."),
                ("Alpine Mushroom", "A rare mushroom that grows at high altitudes."),
                ("Potion of Rockskin", "Turn your skin as hard as stone temporarily."),
                ("Cliffside Brew", "Increases grip, ideal for climbing."),
                ("Eagle's Sight Elixir", "Sharpens eyesight to spot distant objects."),
                ("Stalwart Stamina Potion", "Stamina drains slower at high altitudes."),
                ("Mountain Goat's Grace", "Navigate treacherous terrains with ease."),
                ("Potion of Thin Air", "Breathe easier in high altitudes."),
                ("Snowmelt Elixir", "Keeps you warm in freezing temperatures."),
                ("Echo Drink", "Hear and create echoes for communication."),
                ("Rockslide Potion", "Summon small rockslides."),
            ],
            5: [
                ("Ancient Summit Elixir", "Feel the energy of the highest peaks."),
                ("Frozen Heart Ice Brew", "Stay cool even in intense heat."),
                ("Potion of Mountain's Blessing", "The mountains protect you from harm."),
                ("Yak Milk Cheese", "Rich and nutritious cheese from mountain yaks."),
                ("Crag Lord's Protection", "The mountain itself guards you."),
                ("Alpine Dew", "Collected from high altitude, restores mana."),
                ("Mountain Guardian's Favor", "Attract benevolent mountain spirits."),
                ("Elixir of the Peaks", "Experience visions of ancient summits."),
                ("Golden Eagle's Blessing", "Soar the skies in spirit."),
                ("Tectonic Tonic", "Feel the movements of the earth."),
                ("Summit Star Drink", "Align with the constellations seen from summits."),
                ("Moonlit Mountain Brew", "A brew that shines under the mountain's moonlight."),
            ],
            6: [
                ("Mountain God's Brew", "Said to contain the power of the mountain god."),
                ("Elixir of Endless Peaks", "Experience the vastness of a never-ending range."),
                ("Diamond Dust", "Sprinkle for protection and allure."),
                ("Essence of the Range", "Capture the essence of the entire mountain range."),
                ("Pinnacle Fruit", "A fruit said to grant immense energy."),
                ("Mountain Spirit's Favor", "The highest honor from the mountain."),
                ("Frozen Fire Brew", "Feel warmth in cold, and coolness in heat."),
                ("Starlit Summit Potion", "Navigate the mountains under the starlight."),
                ("Ancient Avalanche Ale", "Summon the power and momentum of an avalanche."),
                ("Mountain Dream Drink", "Dream of the highest summits and deepest valleys."),
                ("Potion of the Mountain's Heart", "Sync with the heart of the mountain."),
                ("Guardian's Mountain Mixture", "A brew preferred by mountain guardians."),
            ],
        },
                "DESERT": {
            4: [
                ("Desert Bloom Tea", "Refreshing tea from desert flowers."),
                ("Mirage Elixir", "Causes hallucinations of water."),
                ("Sandstorm Shield", "Protects from harsh desert winds."),
                ("Cactus Juice", "Hydrating drink from desert plants."),
                ("Camel's Brew", "Stay hydrated for an extended period."),
                ("Golden Sand Potion", "Turns one's skin rough and grainy.")
            ],
            5: [
                ("Searing Sun Salve", "Protection from the intense desert heat."),
                ("Oasis Elixir", "An immediate source of refreshment."),
                ("Pharaoh's Brew", "A drink rumored to be of ancient kings."),
                ("Dune Walker's Delight", "Navigate sand dunes with ease."),
                ("Moonlit Desert Drink", "See clearly under a desert night."),
                ("Scorpion Sting Antidote", "Neutralizes venomous bites.")
            ],
            6: [
                ("Sandswirl Potion", "Create a protective vortex of sand."),
                ("Ancient Pyramid Brew", "Drink from the forgotten eras."),
                ("Desert Mirage Concoction", "View a paradise amidst the barren."),
                ("Golden Oasis Elixir", "Discover the rarest of desert springs."),
                ("Desert Spirit's Boon", "Attract benevolent desert entities."),
                ("Sandstone Strength Salve", "Gain the resilience of rock.")
            ]
        },
                "SWAMP": {
            4: [
                ("Moss Tea", "A murky tea with a strangely refreshing taste."),
                ("Frog's Breath Potion", "Boosts one's agility."),
                ("Mudslide Elixir", "Gives skin a slick coating."),
                ("Swamp Herb Broth", "A hearty broth with medicinal properties."),
                ("Will-o'-Wisp Drink", "Slightly luminescent, helps in the dark."),
                ("Lily Pad Soup", "Soothing soup with a fragrant aroma.")
            ],
            5: [
                ("Bogman's Brew", "A mysterious brew with hidden properties."),
                ("Serpent's Salve", "Neutralizes poisons."),
                ("Gator Guard Potion", "Toughens skin momentarily."),
                ("Reed Reedjuice", "Sipped to clear the lungs."),
                ("Marsh Moss Munch", "Chewed for its energy-giving properties."),
                ("Swamplight Elixir", "A glowing drink that lights your way.")
            ],
            6: [
                ("Bayou Blessing", "Invokes the spirits of the swamp."),
                ("Cursed Croak Concoction", "Grants a voice that terrifies enemies."),
                ("Deep Bog Brew", "Said to be brewed from the heart of the swamp."),
                ("Mystic Marsh Mist", "Breathing it transports one briefly to another realm."),
                ("Elder Reed Extract", "Offers visions of ancient times."),
                ("Primordial Potion", "Reveals the ancient secrets of the swamp.")
            ]
        },

        "OCEAN": {
            4: [
                ("Saltwater Tonic", "A refreshing drink with a briny tang."),
                ("Coral Tea", "Infused with minerals from the deep."),
                ("Tidal Elixir", "Harness the power of ocean currents."),
                ("Seashell Soup", "A rich, seafood-based soup."),
                ("Deep Sea Draught", "Brings glimpses of the ocean's depths."),
                ("Merfolk Mead", "A drink rumored to be favored by mermaids.")
            ],
            5: [
                ("Wave Whisper Wine", "Hear the secrets of the waves."),
                ("Siren's Song Serum", "Offers a melodious voice."),
                ("Abyssal Alchemy", "Taste the mysteries of the ocean deep."),
                ("Triton's Tribute", "A drink as mighty as the ocean's rulers."),
                ("Pearl Potion", "Shimmering drink that revitalizes."),
                ("Lunar Tide Tincture", "Synchronize with the pull of the moon.")
            ],
            6: [
                ("Kraken's Kiss", "Dark, inky potion with immense power."),
                ("Neptune's Nectar", "The might of the ocean in a drink."),
                ("Sapphire Sea Salve", "Heal with the essence of pristine waters."),
                ("Endless Ocean Elixir", "Feel the vastness of the great blue."),
                ("Tempestuous Tonic", "Unleash the storms within."),
                ("Celestial Sea Cider", "Align with the constellations above.")
            ]
        },

        "RIVER": {
            4: [
                ("River Reed Rinse", "Cleanses and refreshes."),
                ("Current Cordial", "Feel the river's flow within you."),
                ("Stonebed Soup", "Earthy and filling."),
                ("Fishfin Flask", "Increases one's agility in water."),
                ("Riverside Rose Tea", "Delicate tea with floral notes."),
                ("Stream Spirit Sip", "Commune with the spirits of the river.")
            ],
            5: [
                ("Whirlpool Whiskey", "A swirling drink with a kick."),
                ("Banks' Blessing Brew", "The protection of the riverbank in a bottle."),
                ("Cascade Concoction", "Harness the power of waterfalls."),
                ("Rapid Rye", "Speeds up reflexes and reactions."),
                ("Lunar Lake Lager", "Soothing drink under the moonlight."),
                ("Delta Draught", "Taste the meeting of river and ocean.")
            ],
            6: [
                ("Aqueous Ambrosia", "Divine drink of the purest waters."),
                ("Riverlord Rum", "A potent drink of river rulers of old."),
                ("Eddy Essence", "Embrace the spiral dance of the river."),
                ("Silverscale Syrup", "Infused with the glint of rare fish."),
                ("Waterway Wine", "A journey of the river in every sip."),
                ("Mystic Mouthful", "Reveal the hidden depths of the river.")
            ]
        },

        "LAKE": {
            4: [
                ("Lakeside Lemonade", "Refreshing drink with a hint of citrus."),
                ("Depth Diver Draught", "Peer into the lake's depths."),
                ("Reedroot Relish", "Savory and energizing."),
                ("Freshwater Flask", "Pure and invigorating."),
                ("Moonlit Marshmallow Mead", "Sweet and calming."),
                ("Lilypad Latte", "A creamy drink with a hint of green.")
            ],
            5: [
                ("Lake Luminance Liqueur", "Glowing drink of the deep."),
                ("Silt Salve", "Nourishes and revitalizes."),
                ("Beachberry Brew", "A tangy concoction from lakeside berries."),
                ("Loch Libation", "Experience the mysteries of hidden lakes."),
                ("Ripple Rum", "Feel the gentle waves within."),
                ("Sunset Sip", "Taste the colors of the lake at dusk.")
            ],
            6: [
                ("Serene Springs Spirit", "Drawn from the source of hidden springs."),
                ("Lake Lore Liquor", "Hear tales of ancient lakes."),
                ("Nectar of the Naiad", "Blessed by the spirits of the lake."),
                ("Deep Delve Drink", "Journey to the very bottom."),
                ("Starry Surface Syrup", "See the stars mirrored in the lake."),
                ("Ancient Aquifer Ale", "Taste the history of ancient waters.")
            ]
        },

        "CAVE": {
            4: [
                ("Stalactite Sip", "Mineral-rich and rejuvenating."),
                ("Batwing Broth", "Dark and slightly bitter."),
                ("Crystal Clear Concoction", "Purified from cave springs."),
                ("Echo Elixir", "Hear distant sounds clearly."),
                ("Mushroom Mingle", "A blend of various cave fungi."),
                ("Cavernous Cocoa", "Warm and comforting in the dark.")
            ],
            5: [
                ("Spelunker's Spirit", "Brave the depths with courage."),
                ("Glowworm Grog", "Light up your way in the darkest tunnels."),
                ("Deep Dark Draught", "Embrace the essence of the abyss."),
                ("Tunnel Tincture", "Navigate mazes with ease."),
                ("Rockslide Rye", "Steady yourself against cave dangers."),
                ("Luminous Lager", "A brew that glows in the dark.")
            ],
            6: [
                ("Chasmal Chalice", "Drink from the deepest chambers."),
                ("Subterranean Salve", "Heal wounds in the cave's embrace."),
                ("Goblin's Goblet", "A drink of mischievous creatures."),
                ("Dripstone Delight", "Savor the slow passage of time."),
                ("Ancient Abyss Ale", "Taste the oldest caverns."),
                ("Underworld Uplift", "Rise with the power of hidden realms.")
            ]
        }
    }  

    if rarity in common_consumables:
        consumable, description = random.choice(common_consumables[rarity])
    elif theme in themed_consumables and rarity in themed_consumables[theme]:
        consumable, description = random.choice(themed_consumables[theme][rarity])
    else:
        return None, None

    return consumable, description

# Example usage:
print(consumable_text_generate("MOUNTAINS", 4))

def container_text_generate(theme, rarity):
    common_containers = {
    # Common containers for all themes with rarities 0-3
        0: [
            ("Plain Box", "A basic box."),
            ("Simple Pouch", "Just a plain pouch."),
            ("Ordinary Sack", "It holds stuff."),
            ("Regular Basket", "Woven from common materials."),
            ("Standard Vase", "Holds flowers or liquids.")
        ],
        1: [
            ("Sturdy Box", "Reinforced corners make this stronger."),
            ("Leather Pouch", "Fine leather, with a smooth feel."),
            ("Reinforced Sack", "Stronger fabric and better stitching."),
            ("Crafted Basket", "Handmade with care."),
            ("Decorative Vase", "A few artistic touches adorn this vase.")
        ],
        2: [
            ("Steel Box", "Almost unbreakable."),
            ("Suede Pouch", "Soft and plush."),
            ("Lockable Sack", "For added security."),
            ("Artisan Basket", "A master craft."),
            ("Porcelain Vase", "Delicate and beautiful.")
        ],
        3: [
            ("Masterwork Box", "The finest of its kind."),
            ("Silk Pouch", "Luxurious and soft."),
            ("Safekeeping Sack", "With multiple locks."),
            ("Exquisite Basket", "A true work of art."),
            ("Crystal Vase", "Transparent and shimmering.")
        ]
    }

        # Theme-specific containers for rarity levels 4-6
    theme_containers = {
        "PLAINS": {
            4: [
                ("Prairie Box", "Inspired by the grasslands."),
                ("Golden Grass Pouch", "Glitters like the morning dew."),
                ("Meadow Sack", "Spacious and comforting."),
                ("Harvest Basket", "Reminiscent of fall in the plains."),
                ("Sunset Vase", "Radiant hues of a plains sunset.")
            ],
            5: [
                ("Ancient Prairie Chest", "Once buried, now uncovered."),
                ("Grassland Relic Pouch", "An artifact of the open plains."),
                ("Endless Meadow Sack", "Seems to hold more than possible."),
                ("Dusk Harvest Basket", "Capturing the fleeting moment before night."),
                ("Horizon Vase", "The horizon of the plains captured in form.")
            ],
            6: [
                ("Unique Prairie Keeper", "One of a kind, truly special."),
                ("Golden Horizon Pouch", "A rare sight, capturing the beauty of the plains."),
                ("Sacred Meadow Sack", "Tales say it was crafted by the gods."),
                ("Plains Master Basket", "Holds the essence of the plains."),
                ("Sunrise Vase", "The first light of the plains, solidified.")
            ]
        },
        "FOREST": {
            4: [
                ("Timber Box", "Crafted from the oldest tree."),
                ("Emerald Leaf Pouch", "Glows with a mysterious light."),
                ("Deep Forest Sack", "Smells of moss and ancient bark."),
                ("Nature Basket", "Feels alive to the touch."),
                ("Moonlit Vase", "Captures the quiet of the forest at night.")
            ],
            5: [
                ("Ancient Tree Chest", "Said to have been here before mankind."),
                ("Forest Spirit Pouch", "Rumored to house a forest sprite."),
                ("Enchanted Moss Sack", "Whispers when opened."),
                ("Woodland Essence Basket", "Holds the heart of the forest."),
                ("Forest Dew Vase", "Holds the morning dew from the first forest.")
            ],
            6: [
                ("Unique Timber Vault", "Carved from a mythical tree."),
                ("Guardian Leaf Pouch", "Protected by the spirits of the woods."),
                ("Sacred Grove Sack", "Crafted in a forest clearing under a full moon."),
                ("Nature's Heart Basket", "The very essence of the forest."),
                ("Eternal Tree Vase", "From a tree that never withers.")
            ]
        },
                "MOUNTAIN": {
            4: [
                ("Rocky Chest", "Crafted from the mountain's core."),
                ("Peak Pouch", "Embodies the pinnacle of heights."),
                ("Stone-guard Sack", "Rugged and steadfast."),
                ("Altitude Basket", "Feels light and airy."),
                ("Summit Vase", "A representation of the mountain's peak.")
            ],
            5: [
                ("Mountain Heart Chest", "Contains the essence of all highlands."),
                ("Elevated Pouch", "Holds the serenity of mountain air."),
                ("Plateau Sack", "Steady and unyielding."),
                ("Echo Basket", "The whispers of the mountain."),
                ("Pinnacle Vase", "The highest quality from the highest peaks.")
            ],
            6: [
                ("Unique Rocky Vault", "The mountain's biggest secret."),
                ("Heaven's Pouch", "Feels like holding a piece of the sky."),
                ("Eternal Stone Sack", "From the beginning of time."),
                ("Snowcap Basket", "Holds the cold of the highest snows."),
                ("Everpeak Vase", "A tribute to the unscalable.")
            ]
        },
        "DESERT": {
            4: [
                ("Sands Chest", "Embraces the vastness of the desert."),
                ("Mirage Pouch", "Shimmers like a desert illusion."),
                ("Dune Sack", "Feels warm and shifting."),
                ("Oasis Basket", "A relief in the barren."),
                ("Sunscar Vase", "Burns with the intensity of the desert sun.")
            ],
            5: [
                ("Golden Sands Chest", "Gleams under the sun."),
                ("Desolation Pouch", "The barren beauty of the desert."),
                ("Scorching Sack", "Emits the heat of the midday sun."),
                ("Nomad's Basket", "Crafted by wanderers."),
                ("Sunset Mirage Vase", "The cooling desert dusk.")
            ],
            6: [
                ("Unique Desert Vault", "One of the desert's many mysteries."),
                ("Pharaoh's Pouch", "Crafted in ancient times."),
                ("Eternal Dune Sack", "Said to have existed since time immemorial."),
                ("Sandstorm Basket", "Holds the rage of the desert."),
                ("Twilight Desert Vase", "The transition of the desert day.")
            ]
        },
        "SWAMP": {
            4: [
                ("Marsh Chest", "Holds the mysteries of the swamp."),
                ("Bog Pouch", "Feels wet and mysterious."),
                ("Mire Sack", "Damp to the touch."),
                ("Reed Basket", "Crafted from the swamp's vegetation."),
                ("Darkwater Vase", "Holds the murkiness of the swamp depths.")
            ],
            5: [
                ("Eternal Marsh Chest", "An artifact of the ageless swamp."),
                ("Sorcerer's Pouch", "Rumored to be of magical origin."),
                ("Will-o'-the-wisp Sack", "Emits a faint glow."),
                ("Lagoon Basket", "Holds the serenity of still swamp waters."),
                ("Mystic Vase", "Intricate patterns of the swamp at night.")
            ],
            6: [
                ("Unique Swamp Vault", "Said to hold the swamp's biggest secrets."),
                ("Guardian's Pouch", "Protected by the spirits of the marsh."),
                ("Sacred Bog Sack", "Holds the stories of the past."),
                ("Everglow Basket", "Glow that never fades."),
                ("Dusk Marsh Vase", "The beauty of the swamp at twilight.")
            ]
        },
        "OCEAN": {
            4: [
                ("Abyss Chest", "Deep and mysterious."),
                ("Tidal Pouch", "Rises and falls like the ocean waves."),
                ("Current Sack", "Feels like a rush of water."),
                ("Coral Basket", "Crafted with intricate designs."),
                ("Seabreeze Vase", "Brings the scent of the sea.")
            ],
            5: [
                ("Deepsea Chest", "Crafted from the ocean's depths."),
                ("Siren's Pouch", "Holds an enchanting allure."),
                ("Whirlpool Sack", "Intense and mesmerizing."),
                ("Shipwreck Basket", "From treasures lost to the sea."),
                ("Horizon Vase", "Where the sea meets the sky.")
            ],
            6: [
                ("Unique Ocean Vault", "The ocean's biggest secret."),
                ("Poseidon's Pouch", "Blessed by the god of the sea."),
                ("Eternal Wave Sack", "Crashes with the might of the ocean."),
                ("Treasure Island Basket", "Maps to the greatest treasures."),
                ("Dawn Ocean Vase", "The calm of the morning sea.")
            ]
        },
        "RIVER": {
            4: [
                ("Flowing Chest", "Smooth and unending."),
                ("Stream Pouch", "Represents the smaller tributaries."),
                ("Rapid Sack", "The rush of the river."),
                ("Riverstone Basket", "Polished over time."),
                ("Riverbend Vase", "Replicates the curves of a river.")
            ],
            5: [
                ("Ancient River Chest", "Tales of the old flow within."),
                ("River Spirit Pouch", "Feels animated and alive."),
                ("Cascade Sack", "Majestic waterfalls in a container."),
                ("Delta Basket", "Where the river meets its end."),
                ("Moonlit River Vase", "Serenity of the river at night.")
            ],
            6: [
                ("Unique River Vault", "One with the river's secrets."),
                ("Rain's Gift Pouch", "Origin of every river."),
                ("Eternal Flow Sack", "River that never dries."),
                ("Confluence Basket", "The meeting of two great forces."),
                ("Sunrise River Vase", "The river's awakening.")
            ]
        },
        "LAKE": {
            4: [
                ("Stagnant Chest", "Holds the lake's stillness."),
                ("Clearwater Pouch", "Pure and untainted."),
                ("Lakeside Sack", "The peace of a lake's edge."),
                ("Reflection Basket", "Mirrors everything perfectly."),
                ("Freshwater Vase", "Crisp and invigorating.")
            ],
            5: [
                ("Deep Lake Chest", "From the darkest depths."),
                ("Mystical Lake Pouch", "Enchantments of old."),
                ("Serenity Sack", "The calm of a lake's surface."),
                ("Island Basket", "Hidden treasures within the lake."),
                ("Twilight Lake Vase", "The lake under the setting sun.")
            ],
            6: [
                ("Unique Lake Vault", "Holds the lake's greatest tales."),
                ("Guardian Lake Pouch", "Protected by ancient spirits."),
                ("Ageless Water Sack", "Water from the first lake."),
                ("Ethereal Basket", "Transcends the physical."),
                ("Starlit Lake Vase", "Lake under a sky full of stars.")
            ]
        },
        "CAVE": {
            4: [
                ("Echoing Chest", "Resonates with cave sounds."),
                ("Stalactite Pouch", "Jagged and unique."),
                ("Darkdepth Sack", "Embraces the cave's darkness."),
                ("Mineral Basket", "Shimmers with embedded gems."),
                ("Underground Vase", "Crafted from cave walls.")
            ],
            5: [
                ("Ancient Cavern Chest", "Tales of the hidden beneath."),
                ("Subterranean Pouch", "Feels cool and mysterious."),
                ("Dripstone Sack", "Replicates the formations of caves."),
                ("Gemstone Basket", "Holds the cave's treasures."),
                ("Cave Pool Vase", "Captures the still underground waters.")
            ],
            6: [
                ("Unique Cave Vault", "Holds the cave's biggest mysteries."),
                ("Labyrinth Pouch", "Lost within its complex designs."),
                ("Eternal Darkness Sack", "Absorbs all light."),
                ("Crystal Basket", "Radiates with inner luminescence."),
                ("Cavern Whisper Vase", "Holds the cave's silent tales.")
            ]
        }
    }

    # Return the correct item based on rarity and theme
    if rarity in common_containers:
        container, description = random.choice(common_containers[rarity])
    elif theme in theme_containers and rarity in theme_containers[theme]:
        container, description = random.choice(theme_containers[theme][rarity])
    else:
        return None, None

    return container, description

# Test the function
name, desc = container_text_generate("CAVE", 6)
print(f"Name: {name}\nDescription: {desc}")

def currency_text_generate(rarity):
    # Currencies for each rarity
    currencies = {
        0: [
            ("Copper Coin", "A basic currency for common transactions."),
            ("Bronze Token", "Frequently used in local trade."),
            ("Leather Scrip", "A simple note used for barter.")
        ],
        1: [
            ("Silver Coin", "A currency of moderate value."),
            ("Iron Seal", "Used in guilds for standard transactions."),
            ("Parchment Voucher", "A promise of trade among merchants.")
        ],
        2: [
            ("Gold Coin", "A high-value currency."),
            ("Steel Medallion", "Favored by knights and nobles."),
            ("Ink Certificate", "A written promise of significant value.")
        ],
        3: [
            ("Platinum Piece", "Among the most valuable coins."),
            ("Emerald Badge", "Used for large transactions among elites."),
            ("Golden Ticket", "Admittance to exclusive events or services.")
        ],
        4: [
            ("Mystic Pearl", "A rare and legendary form of currency."),
            ("Diamond Insignia", "Used for monumental transactions."),
            ("Arcane Script", "A note imbued with magical essence.")
        ],
        5: [
            ("Dragon Coin", "Crafted from genuine dragon scales."),
            ("Star Sapphire Token", "Holds the power of the cosmos."),
            ("Elder Scroll", "A written vow from ancient powers.")
        ],
        6: [
            ("Cosmic Coin", "Rumored to be from another dimension."),
            ("Phoenix Medallion", "Renews its own value with time."),
            ("Eternal Promise", "An unbreakable bond across lifetimes.")
        ]
    }

    # Return the correct currency based on rarity
    currency = random.choice(currencies[rarity])  

    return currency

# Test the function
name, desc = currency_text_generate(4)
print(f"Name: {name}\nDescription: {desc}")