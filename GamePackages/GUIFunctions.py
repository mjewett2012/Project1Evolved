# Filename: GUIFunctions.py
import re
import tkinter as tk
from tkinter import scrolledtext
import tkinter.messagebox
from .DatabaseHandler import DatabaseHandler
from .Utility import dice_roller, stat_calculator, ordinal_suffix_of
from .GameLogic import main_game_loop

class ScrollingText(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.txt = tk.Text(self, wrap="word")
        self.txt.pack(side="left", fill="both", expand=True)

        scrollb = tk.Scrollbar(self, command=self.txt.yview)
        scrollb.pack(side="right", fill="y")
        self.txt["yscrollcommand"] = scrollb.set

class CharacterData(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        
        self.txt = tk.Text(self, wrap="word")
        self.txt.grid(row=0, column=0, sticky="nsew", columnspan=2)

        scrollb = tk.Scrollbar(self, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky="ns")
        self.txt["yscrollcommand"] = scrollb.set

        self.new_char_button = tk.Button(self, text="New Character", command=self.new_character_popup)
        self.load_char_button = tk.Button(self, text="Load Character", command=self.load_character_popup)
        
        self.new_char_button.grid(row=1, column=0, pady=10, sticky="ew")
        self.load_char_button.grid(row=2, column=0, pady=10, sticky="ew")
        
        # Configure the grid to expand the text widget and scrollbar
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Initially, buttons are visible
        self.character_loaded = False
        self.update_button_visibility()

    def new_character_popup(self):
        self.character_selection_frame = CharacterCreationFrame(self)

    def load_character_popup(self):
        self.character_selection_frame = CharacterSelectionFrame(self, self)
        self.character_selection_frame.grid(row=3, column=0, columnspan=2, sticky="nsew")  # Adjust the row and column as needed
        self.character_selection_frame.character_listbox.bind("<Double-Button-1>", self.character_selected)  # Bind the double click event
        
    def update_button_visibility(self):
        if self.character_loaded:
            self.new_char_button.grid_remove()
            self.load_char_button.grid_remove()
        else:
            self.new_char_button.grid()
            self.load_char_button.grid()


    def character_selected(self, event=None):
        db_handler = DatabaseHandler()

        selected_character_name = self.character_selection_frame.character_listbox.get(tk.ACTIVE)
        character_data = db_handler.fetch_character_by_name(selected_character_name)
        db_handler.close()

        if character_data:
            self.display_selected_character_stats(character_data)
            main_game_loop(character_data)
        else:
            display_text_in_gui("Character not found.", target="char")

    def display_character_stats(self, event=None):
        db_handler = DatabaseHandler()
        selected_character_name = self.character_listbox.get(tk.ACTIVE)
        character_data = db_handler.fetch_character_by_name(selected_character_name)
        # Assuming character_data is a dictionary, format it as a string and display it
        character_info = "\n".join([f"{key}: {value}" for key, value in character_data.items()])
        self.master.txt.delete("1.0", tk.END)  # Clear the current text
        self.master.txt.insert(tk.END, character_info)  # Insert the character's details

    def display_selected_character_stats(self, event=None):
        self.after(100, self.process_selection)  # Delay processing by 100 milliseconds

    def process_selection(self):
        db_handler = DatabaseHandler()
        cur_selection = self.character_selection_frame.character_listbox.curselection()
        if not cur_selection:
            return

        # Get the selected character name
        selected_character_name = self.character_selection_frame.character_listbox.get(cur_selection[0])
        print(f"Selected character: {selected_character_name}")

        # Access db_handler from character_selection_frame
        character_data = self.character_selection_frame.db_handler.fetch_character_by_name(selected_character_name)

        # If characterdata is already displayed, clear it and display the selected character's data
        # Use clear_text() and display_text_in_gui() functions
        clear_text(target="char")

        character_data = db_handler.fetch_character_by_name(selected_character_name)

        # Assuming character_data is a dictionary, format it as a string and display it
        if character_data:
        # List of attributes to display
            attributes_to_display = [
                "name", "class", "strength", "dexterity", "intelligence", 
                "wisdom", "constitution", "weapon", "armor", "defense", 
                "attack", "hitPoints", "maxHitPoints", "magicPoints", 
                "maxMagicPoints", "level", "experience", "gold"
            ]

            # Extract and format the data
            character_info = f"{character_data['name']} the {ordinal_suffix_of(character_data['level'])} Level {character_data['class']}\n\n"
            character_info += f"Strength: {character_data['strength']}\n"
            character_info += f"Dexterity: {character_data['dexterity']}\n"
            character_info += f"Intelligence: {character_data['intelligence']}\n"
            character_info += f"Wisdom: {character_data['wisdom']}\n"
            character_info += f"Constitution: {character_data['constitution']}\n"
            character_info += f"Weapon: {character_data['weapon']}\n"
            character_info += f"Armor: {character_data['armor']}\n"
            character_info += f"Defense: {character_data['defense']}\n"
            character_info += f"Attack: {character_data['attack']}\n"
            character_info += f"Hit Points: {character_data['hitPoints']}/{character_data['maxHitPoints']}\n"
            character_info += f"Magic Points: {character_data['magicPoints']}/{character_data['maxMagicPoints']}\n\n"
            character_info += f"Experience: {character_data['experience']}\n"
            character_info += f"Gold: {character_data['gold']}\n"

            # Display the data in the character data frame
            display_text_in_gui(character_info, target="char")

class CharacterCreationFrame(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Character Creation")
        self.geometry("600x400")
        center_on_parent(self)
        # Center this frame on the parent window
        self.update_idletasks()
        x = parent.winfo_rootx() + (parent.winfo_width() // 2) - (self.winfo_width() // 2)
        y = parent.winfo_rooty() + (parent.winfo_height() // 2) - (self.winfo_height() // 2)
        self.geometry("+{}+{}".format(x, y))

        # Make it non-resizable
        self.resizable(False, False)
        self.movable = False

        # Name input
        self.name_label = tk.Label(self, text="Name:")
        self.name_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.name_entry = tk.Entry(self)
        self.name_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        # Password input
        self.password_label = tk.Label(self, text="Password:")
        self.password_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Password confirmation input
        self.confirm_password_label = tk.Label(self, text="Confirm Password:")
        self.confirm_password_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        self.confirm_password_entry = tk.Entry(self, show="*")
        self.confirm_password_entry.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        # Class selection dropdown
        self.class_label = tk.Label(self, text="Class:")
        self.class_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        self.class_var = tk.StringVar(self)
        self.class_var.set("Warrior")  # default value
        self.class_dropdown = tk.OptionMenu(self, self.class_var, "Warrior", "Rogue", "Priest", "Wielder")
        self.class_dropdown.grid(row=4, column=1, padx=10, pady=10, sticky="w")

        # Submit button
        self.submit_button = tk.Button(self, text="Create", command=self.create_character, state=tk.DISABLED)
        self.submit_button.grid(row=5, column=0, columnspan=2, pady=20)

        # StatRollerFrame on the right side
        self.stat_roller = StatRollerFrame(self, class_var=self.class_var)
        self.stat_roller.grid(row=0, column=2, rowspan=6, padx=10, pady=10, sticky="nsew")

        # Configure the grid to distribute the rows evenly
        for i in range(6):  # We have 6 rows in total
            self.grid_rowconfigure(i, weight=1)

        # Configure the grid to expand the StatRollerFrame
        self.grid_columnconfigure(2, weight=1)

    def create_character(self):
        # 1. Gather Data
        character_name = self.name_entry.get()
        character_password = self.password_entry.get()
        character_class = self.class_var.get()
        character_stats = self.stat_roller.get_stats()  # Assuming you have a get_stats method in StatRollerFrame
        derived_stats = stat_calculator(character_class, character_stats["Strength"], character_stats["Dexterity"], character_stats["Intelligence"], character_stats["Wisdom"], character_stats["Constitution"])
        # 2. Validation
        # Check if the character name already exists
        db = DatabaseHandler()
        existing_character = db.fetch_character_by_name(character_name)
        if existing_character:
            tk.messagebox.showerror("Error", "Character name already exists!")
            return

        # Check if password and confirm password match
        if character_password != self.confirm_password_entry.get():
            tk.messagebox.showerror("Error", "Passwords do not match!")
            return

        # Check if the password is valid using validate_password method
        if not self.validate_password():
            return

        # calculate derived stats

        # 3. Insertion
        character_data = {
            "name": character_name,
            "class": character_class,
            "strength": character_stats["Strength"],
            "dexterity": character_stats["Dexterity"],
            "intelligence": character_stats["Intelligence"],
            "wisdom": character_stats["Wisdom"],
            "constitution": character_stats["Constitution"],
            # Add other default values or gather them from the GUI
            "weapon": "DefaultWeapon",  # Placeholder
            "armor": "DefaultArmor",   # Placeholder
            "defense": derived_stats[0],
            "attack": derived_stats[1],
            "hitPoints": derived_stats[2],
            "maxHitPoints": derived_stats[2],  
            "magicPoints": derived_stats[3],
            "maxMagicPoints": derived_stats[3],
            "level": 1,
            "experience": 0,
            "gold": 10,
            "inventory": "{}",         # Placeholder
            "currentRoomLocation": "1",
            "ownedRoomRange": "{}",        # Placeholder
            "skills": "{}",             # Placeholder
            "pword": character_password
        }
        db.insert_character(character_data)
        db.close()

        # After character creation
        tk.messagebox.showinfo("Success", "Character created successfully!")
        self.master.character_selection_frame.refresh_character_list()  # Refresh the list of characters
        self.destroy()  # Close the character creation window

    def enable_submit(self):
        self.submit_button.config(state=tk.NORMAL)

    def disable_event(self):
        pass  # Disabling the close button

    def validate_password(self):
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        # Check if passwords match
        if password != confirm_password:
            tk.messagebox.showerror("Error", "Passwords do not match!")
            return False

        # Regex pattern for validation
        pattern = r"^(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#])[A-Za-z\d@$!%*?&#]{8,}$"
        if not re.match(pattern, password):
            tk.messagebox.showerror("Error", "Password must have at least 8 characters, one uppercase letter, one number, and one special symbol!")
            return False

        return True

class StatRollerFrame(tk.Frame):
    def __init__(self, parent, class_var=None, *args, **kwargs):
        super().__init__(parent, padx=10, pady=20, *args, **kwargs, borderwidth=2, relief=tk.SUNKEN)
        
        # Define class variable
        self.myClass = class_var
        
        # Create widgets
        self.label = tk.Label(self, text="Roll your stats!", anchor="center", justify=tk.CENTER)
        self.label.grid(row=0, column=0, columnspan=2, pady=10, sticky="nsew")  # Spanning 2 columns for centering

        self.roll_button = tk.Button(self, text="Roll Stats", command=lambda: self.roll_stats(self.myClass.get()))
        self.roll_button.grid(row=1, column=0, pady=10, sticky="ew")

        self.confirm_button = tk.Button(self, text="Confirm", command=self.confirm_stats)
        self.confirm_button.grid(row=1, column=1, pady=10, sticky="ew")

        # Configure the grid to expand the label and buttons
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

    def roll_stats(self, myClass):
        # This method will handle the stat rolling
        # ... existing code ...

       # This method will handle the stat rolling
        if myClass == "Warrior":
            self.strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
            self.dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6)
            self.intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 3
            self.wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 3
            self.conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 5
        elif myClass == "Rogue":
            self.strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 1
            self.dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
            self.intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
            self.wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 3
            self.conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 1
        elif myClass == "Priest":
            self.strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6)
            self.dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) 
            self.intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
            self.wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
            self.conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6)
        elif myClass == "Wielder":
            self.strRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
            self.dexRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
            self.intRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 5
            self.wisRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) + 3
            self.conRoll = dice_roller(1, 6) + dice_roller(1, 6) + dice_roller(1, 6) - 1
        else:
            # This should never happen, but just in case
            raise ValueError("Invalid class: {}".format(self.myClass.get()))

        self.label.config(text=f"Your stats are:\n\nStrength: {self.strRoll}\nDexterity: {self.dexRoll}\nIntelligence: {self.intRoll}\nWisdom: {self.wisRoll}\nConstitution: {self.conRoll}\n" + 
                      f"\nStats derived from above:\n\n{stat_calculator(self.myClass.get(), self.strRoll, self.dexRoll, self.intRoll, self.wisRoll, self.conRoll, True)}")

    def confirm_stats(self):
        # This method will handle the confirmation of the stats
        response = tk.messagebox.askyesno("Confirm Stats", "Are you happy with these stats?")
        self.master.lift()  # Bring the CharacterCreationFrame to the front
        if response:
            self.master.enable_submit()  # Enable the "Create" button in the CharacterCreationFrame
            self.roll_button.config(state=tk.DISABLED)  # Disable the "Roll Stats" button
            self.confirm_button.config(state=tk.DISABLED)  # Disable the "Confirm" button
        else:
            # Let the user roll the stats again
            self.roll_stats(self.myClass.get())

    def get_stats(self):
        return {
            "Strength": self.strRoll,
            "Dexterity": self.dexRoll,
            "Intelligence": self.intRoll,
            "Wisdom": self.wisRoll,
            "Constitution": self.conRoll
        }

# Soon to be quit, settings, etc.
class CommandButtons(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.button1 = tk.Button(self, text="Enter1")
        self.button2 = tk.Button(self, text="Enter2")
        self.button3 = tk.Button(self, text="Enter3")

        self.button1.grid(row=0, column=0)
        self.button2.grid(row=0, column=1)
        self.button3.grid(row=0, column=2)

class CharacterSelectionFrame(tk.Frame):
    def __init__(self, parent, character_data, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.characterdata = character_data
        self.db_handler = DatabaseHandler()  # Initialize the database handler
        self.character_listbox = tk.Listbox(self)  # Create a listbox to display characters
        self.character_listbox.pack(fill=tk.BOTH, expand=True)
        self.display_characters()  # Display characters when the frame is initialized
        self.character_listbox.bind("<<ListboxSelect>>", self.on_character_selected)  # Bind the selection event to on_character_selected method

    def display_characters(self):
        characters = self.db_handler.fetch_all_characters()  # Fetch all characters from the database
        for character in characters:
            self.character_listbox.insert(tk.END, character[1])  # Insert the character name into the listbox

    def refresh_character_list(self):
        self.character_listbox.delete(0, tk.END)  # Clear the current list
        self.display_characters()  # Display the updated list of characters

    def on_character_selected(self, event=None):
        selected_character_name = self.character_listbox.get(tk.ACTIVE)
        character_data = self.db_handler.fetch_character_by_name(selected_character_name)
        self.characterdata.display_selected_character_stats(character_data)

# This is the main GUI window
root = tk.Tk()
root.title("Ancient Citadel")
root.geometry("1024x768")
root.state('zoomed')

# Create a horizontal PanedWindow
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL)
paned_window.pack(fill=tk.BOTH, expand=1)

# This is the main GUI frame
main_text_frame = ScrollingText(paned_window)
paned_window.add(main_text_frame, stretch="always")

vertical_frame = tk.Frame(paned_window)
paned_window.add(vertical_frame, width=256, stretch="never")

character_data_frame = CharacterData(vertical_frame)
character_data_frame.pack(fill="both", expand=True)

command_buttons_frame = CommandButtons(vertical_frame)
command_buttons_frame.pack(fill="x", pady=5)

def init_gui():
    root.mainloop()

def display_text_in_gui(text, target="main", format_type="normal"):
    if target == "main":
        main_text_frame.txt.insert("end", text)
    else:
        character_data_frame.txt.insert("end", text)

def clear_text(target="main"):
    if target == "main":
        main_text_frame.txt.delete("1.0", "end")
    else:
        character_data_frame.txt.delete("1.0", "end")

def display_character_data(character):
    if character == None:
        display_text_in_gui("No character found. Create a new character.", target="char")
    else:
        display_text_in_gui(str(character), target="char")  # Assuming the character has a __str__ method

# display the title graphics from title.txt
def display_title_graphics():
    FILENAME = "title.txt"
    try:
        with open(FILENAME, "r") as title:
            for line in title:
                display_text_in_gui(line, target="main")
    except FileNotFoundError:
        display_text_in_gui("Error: 'title.txt' not found!", target="main")

def center_on_parent(self):
    x = self.master.winfo_rootx() + (self.master.winfo_width() // 2) - (self.winfo_width() // 2)
    y = self.master.winfo_rooty() + (self.master.winfo_height() // 2) - (self.winfo_height() // 2)
    self.geometry("+{}+{}".format(x, y))

if __name__ == "__main__":
    display_title_graphics()
    init_gui()
