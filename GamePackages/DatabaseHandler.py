import sqlite3

class DatabaseHandler:
    def __init__(self, db_name="GameData.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_tables()

    def _initialize_tables(self):
        """Initialize all tables in the database."""

        # Mobs Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS mobs (
                mobNum INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                strength INTEGER,
                dexterity INTEGER,
                intelligence INTEGER,
                wisdom INTEGER,
                constitution INTEGER,
                weapon TEXT,
                armor TEXT,
                defense INTEGER,
                hitPoints INTEGER,
                maxHitPoints INTEGER,
                magicPoints INTEGER,
                maxMagicPoints INTEGER,
                level INTEGER,
                experience INTEGER,
                gold INTEGER,
                worldTheme TEXT,
                currentRoomLocation INTEGER,
                inventory TEXT,
                skills TEXT
            )
        """)

        # Characters Table
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS characters (
                charNum INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                class TEXT NOT NULL,
                strength INTEGER NOT NULL,
                dexterity INTEGER NOT NULL,
                intelligence INTEGER NOT NULL,
                wisdom INTEGER NOT NULL,
                constitution INTEGER NOT NULL,
                weapon VARCHAR(20),
                armor VARCHAR(20),
                defense INTEGER,
                attack INTEGER,
                hitPoints INTEGER NOT NULL,
                maxHitPoints INTEGER NOT NULL,
                magicPoints INTEGER NOT NULL,
                maxMagicPoints INTEGER NOT NULL,
                level INTEGER NOT NULL,
                experience INTEGER,
                gold INTEGER,
                pword VARCHAR(50) NOT NULL,
                inventory TEXT,
                currentRoomLocation INTEGER,
                ownedRoomRange TEXT,
                skills TEXT
            )
        """)

        # Items Tables
        item_tables = [
            # DefaultWeapons
            """
            CREATE TABLE IF NOT EXISTS DefaultWeapons (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                damage INTEGER, durability INTEGER, attackType TEXT
            )
            """,
            # DefaultArmor
            """
            CREATE TABLE IF NOT EXISTS DefaultArmor (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                defense INTEGER, durability INTEGER
            )
            """,
            # DefaultConsumables
            """
            CREATE TABLE IF NOT EXISTS DefaultConsumables (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                effect TEXT
            )
            """,
            # DefaultContainers
            """
            CREATE TABLE IF NOT EXISTS DefaultContainers (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                capacity INTEGER, locked INTEGER, keyNumber INTEGER
            )
            """,
            # DefaultKeys
            """
            CREATE TABLE IF NOT EXISTS DefaultKeys (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                keyNumber INTEGER
            )
            """,
            # DefaultQuestItems
            """
            CREATE TABLE IF NOT EXISTS DefaultQuestItems (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                quest TEXT
            )
            """,
            # DefaultCurrency
            """
            CREATE TABLE IF NOT EXISTS DefaultCurrency (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                currencyType TEXT
            )
            """,
            # ActiveWeapons
            """
            CREATE TABLE IF NOT EXISTS ActiveWeapons (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                damage INTEGER, currentDurability INTEGER, attackType TEXT
            )
            """,
            # ActiveArmor
            """
            CREATE TABLE IF NOT EXISTS ActiveArmor (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                defense INTEGER, currentDurability INTEGER
            )
            """,
            # ActiveConsumables
            """
            CREATE TABLE IF NOT EXISTS ActiveConsumables (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                effect TEXT, usesLeft INTEGER
            )
            """,
            # ActiveContainers
            """
            CREATE TABLE IF NOT EXISTS ActiveContainers (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                itemsContained TEXT, locked INTEGER, keyNumber INTEGER
            )
            """,
            # ActiveKeys
            """
            CREATE TABLE IF NOT EXISTS ActiveKeys (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                keyNumber INTEGER
            )
            """,
            # ActiveQuestItems
            """
            CREATE TABLE IF NOT EXISTS ActiveQuestItems (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                quest TEXT
            )
            """,
            # ActiveCurrency
            """
            CREATE TABLE IF NOT EXISTS ActiveCurrency (
                iNumber INTEGER PRIMARY KEY,
                name TEXT, description TEXT, price INTEGER, worldTheme TEXT,
                currencyType TEXT
            )
            """,
            # Rooms
            """
            CREATE TABLE IF NOT EXISTS rooms (
                roomNum INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                location TEXT NOT NULL,
                theme TEXT NOT NULL,
                mobs TEXT DEFAULT '',
                inventory TEXT DEFAULT ''
            )
            """,
            """
                CREATE TABLE IF NOT EXISTS room_exits (
                id INTEGER PRIMARY KEY,
                source_room INTEGER,
                destination_room INTEGER,
                direction TEXT,
                FOREIGN KEY(source_room) REFERENCES rooms(roomNum),
                FOREIGN KEY(destination_room) REFERENCES rooms(roomNum)
            )
            """
        ]

        for table in item_tables:
            self.cursor.execute(table)

        self.conn.commit()

    def insert_into_table(self, table_name, data):
        placeholders = ', '.join('?' for _ in data)
        columns = ', '.join(data.keys())
        values = tuple(data.values())
        query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.conn.commit()

    def insert_character(self, character_data):
        columns = ', '.join(character_data.keys())
        placeholders = ', '.join(f":{key}" for key in character_data.keys())
        query = f"""
        INSERT INTO characters ({columns})
        VALUES ({placeholders})
        """
        self.cursor.execute(query, character_data)
        self.conn.commit()

    def fetch_all_characters(self):
        self.cursor.execute("SELECT * FROM characters")
        return self.cursor.fetchall()

    def delete_character_by_name(self, character_name):
        query = "DELETE FROM characters WHERE name = ?"
        self.cursor.execute(query, (character_name,))
        self.conn.commit()

    def fetch_character_by_name(self, name):
        self.cursor.execute("SELECT * FROM characters WHERE name=?", (name,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None

    def update_character(self, character_name, column_name, new_value):
        query = f"UPDATE characters SET {column_name} = ? WHERE name = ?"
        self.cursor.execute(query, (new_value, character_name))
        self.conn.commit()

    def fetch_all_rooms(self):
        self.cursor.execute("SELECT * FROM rooms")
        return self.cursor.fetchall()
    
    def fetch_room_by_number(self, room_number):
        self.cursor.execute("SELECT * FROM rooms WHERE roomNum=?", (room_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_room_by_id(self, room_id):
        self.cursor.execute("SELECT * FROM rooms WHERE roomNum=?", (room_id,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_mobs(self):
        self.cursor.execute("SELECT * FROM mobs")
        return self.cursor.fetchall()
    
    def fetch_mob_by_number(self, mob_number):
        self.cursor.execute("SELECT * FROM mobs WHERE mobNum=?", (mob_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_items(self):
        self.cursor.execute("SELECT * FROM items")
        return self.cursor.fetchall()
    
    def fetch_item_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM items WHERE itemNum=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_default_weapons(self):
        self.cursor.execute("SELECT * FROM DefaultWeapons")
        return self.cursor.fetchall()
    
    def fetch_default_weapon_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultWeapons WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_default_armor(self):
        self.cursor.execute("SELECT * FROM DefaultArmor")
        return self.cursor.fetchall()
    
    def fetch_default_armor_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultArmor WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_default_consumables(self):
        self.cursor.execute("SELECT * FROM DefaultConsumables")
        return self.cursor.fetchall()
    
    def fetch_default_consumable_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultConsumables WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_default_containers(self):
        self.cursor.execute("SELECT * FROM DefaultContainers")
        return self.cursor.fetchall()
    
    def fetch_default_container_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultContainers WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_default_keys(self):
        self.cursor.execute("SELECT * FROM DefaultKeys")
        return self.cursor.fetchall()
    
    def fetch_default_key_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultKeys WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        return None
    
    def fetch_all_default_quest_items(self):
        self.cursor.execute("SELECT * FROM DefaultQuestItems")
        return self.cursor.fetchall()
    
    def fetch_default_quest_item_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultQuestItems WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_default_currency(self):
        self.cursor.execute("SELECT * FROM DefaultCurrency")
        return self.cursor.fetchall()
    
    def fetch_default_currency_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM DefaultCurrency WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_weapons(self):
        self.cursor.execute("SELECT * FROM ActiveWeapons")
        return self.cursor.fetchall()
    
    def fetch_active_weapon_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveWeapons WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_armor(self):
        self.cursor.execute("SELECT * FROM ActiveArmor")
        return self.cursor.fetchall()
    
    def fetch_active_armor_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveArmor WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_consumables(self):
        self.cursor.execute("SELECT * FROM ActiveConsumables")
        return self.cursor.fetchall()
    
    def fetch_active_consumable_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveConsumables WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_containers(self):
        self.cursor.execute("SELECT * FROM ActiveContainers")
        return self.cursor.fetchall()
    
    def fetch_active_container_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveContainers WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_keys(self):
        self.cursor.execute("SELECT * FROM ActiveKeys")
        return self.cursor.fetchall()
    
    def fetch_active_key_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveKeys WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_quest_items(self):
        self.cursor.execute("SELECT * FROM ActiveQuestItems")
        return self.cursor.fetchall()
    
    def fetch_active_quest_item_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveQuestItems WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_active_currency(self):
        self.cursor.execute("SELECT * FROM ActiveCurrency")
        return self.cursor.fetchall()
    
    def fetch_active_currency_by_number(self, item_number):
        self.cursor.execute("SELECT * FROM ActiveCurrency WHERE iNumber=?", (item_number,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            return dict(zip(columns, row))
        
    def fetch_all_default_items(self):
        self.cursor.execute("SELECT * FROM DefaultWeapons")
        self.cursor.execute("SELECT * FROM DefaultArmor")
        self.cursor.execute("SELECT * FROM DefaultConsumables")
        self.cursor.execute("SELECT * FROM DefaultContainers")
        self.cursor.execute("SELECT * FROM DefaultKeys")
        self.cursor.execute("SELECT * FROM DefaultQuestItems")
        self.cursor.execute("SELECT * FROM DefaultCurrency")
        return self.cursor.fetchall()
    
    def fetch_all_active_items(self):
        self.cursor.execute("SELECT * FROM ActiveWeapons")
        self.cursor.execute("SELECT * FROM ActiveArmor")
        self.cursor.execute("SELECT * FROM ActiveConsumables")
        self.cursor.execute("SELECT * FROM ActiveContainers")
        self.cursor.execute("SELECT * FROM ActiveKeys")
        self.cursor.execute("SELECT * FROM ActiveQuestItems")
        self.cursor.execute("SELECT * FROM ActiveCurrency")
        return self.cursor.fetchall()
    
    def fetch_all_default_items_by_theme(self, theme):
        self.cursor.execute("SELECT * FROM DefaultWeapons WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM DefaultArmor WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM DefaultConsumables WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM DefaultContainers WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM DefaultKeys WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM DefaultQuestItems WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM DefaultCurrency WHERE worldTheme=?", (theme,))
        return self.cursor.fetchall()
    
    def fetch_all_active_items_by_theme(self, theme):
        self.cursor.execute("SELECT * FROM ActiveWeapons WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM ActiveArmor WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM ActiveConsumables WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM ActiveContainers WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM ActiveKeys WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM ActiveQuestItems WHERE worldTheme=?", (theme,))
        self.cursor.execute("SELECT * FROM ActiveCurrency WHERE worldTheme=?", (theme,))
        return self.cursor.fetchall()
    
    def fetch_all_default_items_by_type(self, itemType):
        self.cursor.execute("SELECT * FROM DefaultWeapons WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM DefaultArmor WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM DefaultConsumables WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM DefaultContainers WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM DefaultKeys WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM DefaultQuestItems WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM DefaultCurrency WHERE itemType=?", (itemType,))
        return self.cursor.fetchall()
    
    def fetch_all_active_items_by_type(self, itemType):
        self.cursor.execute("SELECT * FROM ActiveWeapons WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM ActiveArmor WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM ActiveConsumables WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM ActiveContainers WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM ActiveKeys WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM ActiveQuestItems WHERE itemType=?", (itemType,))
        self.cursor.execute("SELECT * FROM ActiveCurrency WHERE itemType=?", (itemType,))
        return self.cursor.fetchall()
    
    def fetch_all_default_items_by_theme_and_type(self, theme, itemType):
        self.cursor.execute("SELECT * FROM DefaultWeapons WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM DefaultArmor WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM DefaultConsumables WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM DefaultContainers WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM DefaultKeys WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM DefaultQuestItems WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM DefaultCurrency WHERE worldTheme=? AND itemType=?", (theme, itemType))
        return self.cursor.fetchall()
    
    def fetch_all_active_items_by_theme_and_type(self, theme, itemType):
        self.cursor.execute("SELECT * FROM ActiveWeapons WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM ActiveArmor WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM ActiveConsumables WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM ActiveContainers WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM ActiveKeys WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM ActiveQuestItems WHERE worldTheme=? AND itemType=?", (theme, itemType))
        self.cursor.execute("SELECT * FROM ActiveCurrency WHERE worldTheme=? AND itemType=?", (theme, itemType))
        return self.cursor.fetchall()
    
    def fetch_all_default_items_by_name(self, name):
        self.cursor.execute("SELECT * FROM DefaultWeapons WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM DefaultArmor WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM DefaultConsumables WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM DefaultContainers WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM DefaultKeys WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM DefaultQuestItems WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM DefaultCurrency WHERE name=?", (name,))
        return self.cursor.fetchall()
    
    def fetch_all_active_items_by_name(self, name):
        self.cursor.execute("SELECT * FROM ActiveWeapons WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM ActiveArmor WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM ActiveConsumables WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM ActiveContainers WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM ActiveKeys WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM ActiveQuestItems WHERE name=?", (name,))
        self.cursor.execute("SELECT * FROM ActiveCurrency WHERE name=?", (name,))
        return self.cursor.fetchall()
    
    def save_room(self, room):
        data = {
            "name": room.name,
            "description": room.description,
            "location": f"{room.x},{room.y}",
            "mobs": ",".join(map(str, room.mobs)),
            "inventory": ",".join(map(str, room.inventory))
        }
        self.insert_into_table("rooms", data)
    
    def fetch_room_by_location(self, location):
        self.cursor.execute("SELECT * FROM rooms WHERE location=?", (location,))
        row = self.cursor.fetchone()
        if row:
            columns = [desc[0] for desc in self.cursor.description]
            room_data = dict(zip(columns, row))
            
            # Convert comma-separated strings back to lists
            room_data["mobs"] = list(map(int, room_data["mobs"].split(","))) if room_data["mobs"] else []
            room_data["inventory"] = list(map(int, room_data["inventory"].split(","))) if room_data["inventory"] else []
            
            # Fetch exits for the room
            room_data["exits"] = self.get_exits_for_room(room_data["roomNum"])
            
            return room_data
        return None
        
    def close(self):
        self.conn.close()

if __name__ == "__main__":
    db = DatabaseHandler()
    db.insert_into_table("characters", {
        "name": "Fireangel",
        "pword": "Password123!",
        "strength": 30,
        "dexterity": 30,
        "intelligence": 30,
        "wisdom": 30,
        "constitution": 30,
        "weapon": "",
        "armor": "",
        "defense": 10,
        "hitPoints": 100,
        "maxHitPoints": 100,
        "magicPoints": 50,
        "maxMagicPoints": 50,
        "level": 1,
        "experience": 0,
        "gold": 10,
        "inventory": "[]",
        "currentRoomLocation": 1,
        "ownedRoomRange": "", # Placeholder
        "skills": "[]"
    })
    db.close()
