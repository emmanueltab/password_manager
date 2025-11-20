import os
import json

#-------------------------
# CONSTANTS
#-------------------------
PASSWORD_FOLDER = "passwords"

#-------------------------
# HELPER FUNCTIONS
#-------------------------
def clear_screen():
    """Clears the terminal screen."""
    os.system('cls' if os.name == 'nt' else 'clear')


def list_storages():
    """Returns a sorted list of JSON files in the password folder."""
    try:
        files = next(os.walk(PASSWORD_FOLDER))[2]
        return sorted([f for f in files if f.endswith(".json")])
    except StopIteration:
        return []

#-------------------------
# CREATE NEW STORAGE
#-------------------------
def create_password_storage():
    """Prompts user to create a new JSON password storage."""
    clear_screen()
    print("Storage Creator\n")
    storages = list_storages()
    
    print("Existing storages:")
    print("-----------------------------------")
    for file in storages:
        print(file)
    print("-----------------------------------")
    print("Enter '<!back>' to return to the storage menu.")
    print("-----------------------------------")

    storage_name = input("Enter a name to create a storage (you don't need to add .json):\n> ")
    if storage_name == "<!back>":
        return None

    filepath = os.path.join(PASSWORD_FOLDER, f"{storage_name}.json")
    if not os.path.exists(filepath):
        with open(filepath, 'w') as f:
            json.dump({}, f)
        print("New .json file has been created!")
    else:
        print(f"{storage_name}.json already exists!")
    input("\nPress Enter to continue...")

#-------------------------
# MANAGE EXISTING STORAGE
#-------------------------
def manage_storage(file_name):
    """Allows user to view, add, remove, or delete passwords in a storage."""
    clear_screen()
    filepath = os.path.join(PASSWORD_FOLDER, file_name)

    #-------------------------
    # HELPER FUNCTION: SHOW OPTIONS
    #-------------------------
    def show_options():
        print("\nStorage Modifier Options:")
        print("delete_st - deletes storage")
        print("return - returns password")
        print("add - adds a new password")
        print("back - goes back to the storage menu")
        print("show - shows all the passwords")
        print("remove - removes a password")
        print("help - clears screen and shows commands")
        print("-----------------------------------")

    #-------------------------
    # COMMAND FUNCTIONS
    #-------------------------
    def cmd_back():
        return "back"

    def cmd_delete_st():
        os.remove(filepath)
        print(f"{file_name} has been deleted.")
        return "back"

    def cmd_help():
        clear_screen()
        show_options()

    def cmd_show():
        with open(filepath, 'r') as f:
            data = json.load(f)
        print(data)

    def cmd_remove():
        with open(filepath, 'r') as f:
            data = json.load(f)
        print("Enter the account key you want to remove. Enter '<-stop->' to stop removing.")
        while True:
            key = input("remove> ").strip()
            if key == "<-stop->":
                break
            if key in data:
                data.pop(key)
                print(f"{key} has been removed.")
            else:
                print(f"{key} is not in {file_name}.")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    def cmd_return():
        with open(filepath, 'r') as f:
            data = json.load(f)
        print("Enter the account key you want to view. Enter '<-stop->' to stop.")
        while True:
            key = input("return> ").strip()
            if key == "<-stop->":
                break
            print(data.get(key, f"There isn't a password associated with {key}"))

    def cmd_add():
        with open(filepath, 'r') as f:
            data = json.load(f)
        print("Adding new passwords. Enter '<-stop->' for either key or password to stop adding.")
        while True:
            key = input("Enter key: ").strip()
            if key == "<-stop->":
                break
            password = input(f"Enter password for {key}: ").strip()
            if password == "<-stop->":
                break
            data[key] = password
            print(f"{key} : {password} has been added.")
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)

    #-------------------------
    # COMMAND DICTIONARY
    #-------------------------
    commands = {
        "back": cmd_back,
        "delete_st": cmd_delete_st,
        "help": cmd_help,
        "show": cmd_show,
        "remove": cmd_remove,
        "return": cmd_return,
        "add": cmd_add
    }

    show_options()
    print(f"\nManaging storage: {file_name}\n")

    #-------------------------
    # MAIN LOOP FOR STORAGE MENU
    #-------------------------
    while True:
        choice = input("> ").strip()
        action = commands.get(choice)
        if action:
            result = action()
            if result == "back":
                break
        else:
            print("That isn't an option.")

#-------------------------
# MAIN MENU FUNCTION
#-------------------------
def main():
    """Main loop of the program: lists storages, allows creation or selection."""
    os.makedirs(PASSWORD_FOLDER, exist_ok=True)

    while True:
        clear_screen()
        storages = list_storages()
        print("Storage Menu\n")
        print("Available storages:")
        print("--------------------------------------------------------")
        for s in storages:
            print(s)
        print("--------------------------------------------------------")
        print("Options: 'new' - create a new storage")
        print("Type 'quit' to exit the program.")
        print("Pick an option from above (include .json when picking files)")

        choice = input("> ").strip()

        if choice.lower() == "quit":
            print("Exiting program...")
            break
        elif choice == "new":
            create_password_storage()
        elif choice in storages:
            manage_storage(choice)
        else:
            print("That isn't an option.")
            input("\nPress Enter to continue...")

#-------------------------
# PROGRAM ENTRY POINT
#-------------------------
if __name__ == "__main__":
    main()
