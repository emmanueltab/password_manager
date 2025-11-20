import os
import json

#-------------------------
# CONSTANTS
#-------------------------
PASSWORD_FOLDER = "passwords"

#-------------------------
# HELPERS
#-------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def list_storages():
    try:
        files = next(os.walk(PASSWORD_FOLDER))[2]
        return sorted([f for f in files if f.endswith(".json")])
    except StopIteration:
        return []


def load_storage(file_name):
    filepath = os.path.join(PASSWORD_FOLDER, file_name)
    with open(filepath, 'r') as f:
        return json.load(f)


def save_storage(file_name, data):
    filepath = os.path.join(PASSWORD_FOLDER, file_name)
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)

#-------------------------
# COMMAND FUNCTIONS
#-------------------------
def add(file_name, args):
    """Usage: add key password"""
    if len(args) < 2:
        print("Usage: add key password")
        return
    key, password = args[0], " ".join(args[1:])
    data = load_storage(file_name)
    data[key] = password
    save_storage(file_name, data)
    print(f"{key} added with password.")


def remove(file_name, args):
    """Usage: remove key"""
    if len(args) != 1:
        print("Usage: remove key")
        return
    key = args[0]
    data = load_storage(file_name)
    if key in data:
        data.pop(key)
        save_storage(file_name, data)
        print(f"{key} removed.")
    else:
        print(f"{key} not found.")


def show(file_name, args):
    """Usage: show"""
    data = load_storage(file_name)
    if not data:
        print("No passwords stored.")
    else:
        for k, v in data.items():
            print(f"{k} : {v}")


def get(file_name, args):
    """Usage: get key"""
    if len(args) != 1:
        print("Usage: get key")
        return
    key = args[0]
    data = load_storage(file_name)
    print(data.get(key, f"{key} not found."))


def delete(file_name, args):
    """Usage: delete"""
    filepath = os.path.join(PASSWORD_FOLDER, file_name)
    os.remove(filepath)
    print(f"{file_name} deleted.")


#-------------------------
# STORAGE MENU
#-------------------------
def manage_storage(file_name):
    commands = {
        "add": add,
        "remove": remove,
        "show": show,
        "get": get,
        "delete": delete,
        "help": None  # handled separately
    }

    while True:
        clear_screen()
        print(f"Storage: {file_name}")
        print("Commands: add, remove, get, show, delete, back, help")
        user_input = input("> ").strip()
        if not user_input:
            continue
        parts = user_input.split()
        command, args = parts[0], parts[1:]

        if command == "back":
            break
        elif command == "help":
            print("\nCommand syntax:")
            print("add key password    - Add or update a password")
            print("remove              - Remove a password")
            print("get key             - Show a single password")
            print("show                - Show all passwords")
            print("delete              - Delete the entire storage")
            print("back                - Return to storage menu")
            input("\nPress Enter to continue...")
        elif command in commands:
            commands[command](file_name, args)
            input("\nPress Enter to continue...")
        else:
            print("Invalid command!")
            input("\nPress Enter to continue...")

#-------------------------
# CREATE NEW STORAGE
#-------------------------
def create_storage():
    clear_screen()
    storages = list_storages()
    print("Existing storages:")
    for s in storages:
        print(s)
    print("-------------------")
    print("Enter '<!back>' to return to menu.")

    name = input("Storage name: ").strip()
    if name == "<!back>":
        return
    filepath = os.path.join(PASSWORD_FOLDER, f"{name}.json")
    if os.path.exists(filepath):
        print(f"{name}.json already exists!")
    else:
        with open(filepath, 'w') as f:
            json.dump({}, f)
        print(f"{name}.json created!")
    input("\nPress Enter to continue...")

#-------------------------
# MAIN MENU
#-------------------------
def main():
    os.makedirs(PASSWORD_FOLDER, exist_ok=True)
    while True:
        clear_screen()
        print("Storage Menu:")
        storages = list_storages()
        for s in storages:
            print(s)
        print("-------------------")
        print("Commands: new, quit, or select a storage")

        choice = input("> ").strip()
        if choice == "quit":
            print("Exiting...")
            break
        elif choice == "new":
            create_storage()
        elif choice in storages:
            manage_storage(choice)
        else:
            print("Invalid option!")
            input("\nPress Enter to continue...")

#-------------------------
# PROGRAM ENTRY POINT
#-------------------------
if __name__ == "__main__":
    main()
