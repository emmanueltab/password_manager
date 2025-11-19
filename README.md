
# Password Manager (Python + JSON)

This is a simple command-line password manager written in Python.
It stores passwords in separate JSON files (called “storages”) inside a `passwords` folder.
You can create new password storages, add passwords, remove them, view them, and delete entire storages.

This project focuses on basic file handling, JSON manipulation, and interactive CLI menus.

---

## Features

* Create new password storage files (`.json`)
* Add new password entries
* Remove existing password entries
* View all stored passwords within a storage
* Retrieve a specific password by key
* Delete an entire storage file
* Simple text-based interface
* JSON-based persistent storage

---

## How It Works

Each password storage is a `.json` file stored inside the `passwords/` directory.
The structure of each storage is a dictionary:

```
{
    "account_name": "password123",
    "email": "mypassword",
    "github": "abc123"
}
```

The program allows creating and modifying these storages using a menu-driven interface.

---

## Requirements

* Python 3.x
* A folder named `passwords` in the same directory as the script

Example structure:

```
project/
│── passwords/
│     └── example.json
│── password_manager.py
```

---

## Running the Program

1. Create a folder named `passwords` in the same directory as the script.
2. Run:

```
python3 password_manager.py
```

3. Use the on-screen prompts to:

   * Create new storage files
   * Add or remove passwords
   * List contents
   * Retrieve passwords
   * Delete storages

---

## Commands Overview

Inside a storage:

* `add` — Add a new password entry
* `remove` — Remove an existing key
* `return` — Show the password for a given key
* `show` — Display all passwords
* `delete_st` — Delete the storage file
* `help` — Clear the screen and show commands
* `back` — Return to the main menu

---

## Notes

* If a key already exists, adding it again will overwrite the previous password.
* Entering special values like `<-stop->` or `<!back>` cancels certain operations.
* This tool does not encrypt passwords; it is strictly for educational and personal practice.

---

## Future Improvements

* Password encryption
* A GUI interface
* Environment variable support
* Password strength checker
* Search functionality
