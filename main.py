import os
import json

onlyfiles = next(os.walk("passwords"))[2] # list of all the txt files in passwords
sorted(onlyfiles)



def create_passwordsTXT(mainnn):
    onlyfiles = next(os.walk("passwords"))[2] # list of all the txt files in passwords
    sorted(onlyfiles)
    print("the storages:\n-----------------------------------")
    for file in onlyfiles:
        print(file)
    print("-----------------------------------\nentering a taken name wont do anything\nenter '<!back>' to return to main\n-----------------------------------")
    ask_for_name = input("enter a name to create a storage(you dont have to enter .json):\n> ")
  # if there are no txt files for the passwords thne it will do this
    if ask_for_name == "<!back>":
        os.system('cls')
        mainnn()
    else:

        pw = {}
        pw2 = json.dumps(pw)
        with open(f"passwords\{ask_for_name}.json", 'w') as writer: # creates json file
            writer.write(pw2)
            print("new .json file has been created!")
            writer.close()
        



def does_stuff_to_files(chosen_file, mainn): # storage menu
    os.system('cls')
    optionss = ("delete_st", "return", "add", "back", "show", "remove", "help")
    print("the options(pick one):\ndelete_st - deletes storage\nreturn - returns password\nadd - adds a new password\nback - goes back to the main thing\nshow - shows all the passwords\nremove - removes password\nhelp - clears screen and prints commands")
    print(f"-----------------------------------\nwhat would you like to do with {chosen_file}?")
    


    while True:
        operations = input("> ")
        if operations not in optionss:
            print('that aint an option')
        

            
        elif operations == "back":  # returns to main
            os.system('cls')     # DOES NOT REQUIRE py_dictionary
            mainn()

        elif operations == "delete_st":      # deletes the file the user selected and returns to main
            os.remove(f"passwords/{chosen_file}")  # DOES NOT REQUIRE py_dictionary
            os.system('cls')        
            mainn()

        elif operations == "help":
            os.system("cls")   # prints help commands
            print("the options(pick one):\ndelete_st - deletes storage\nreturn - returns password\nadd - adds a new password\nback - goes back to the main thing\nshow - shows all the passwords\nremove - removes password\nhelp - clears the screen and prints commands")
            print("-------------------------------------------------")
        
        

        elif operations == "show":
            with open(f"passwords/{chosen_file}", "r") as f:
                py_dictionary = json.load(f)  # python dictionary
                f.close()
            print(py_dictionary)
            
            
        
        elif operations == "remove":
            with open(f"passwords/{chosen_file}", "r") as f:
                py_dictionary = json.load(f)  # python dictionary
                f.close()
            print("enter the account : password that you want to remove.enter <-stop-> to get out: ")
            while True:
                remove_which = input("> ")
                if remove_which == "<-stop->":
                    break

                elif remove_which not in py_dictionary:
                    print(f"{remove_which} is not in {chosen_file}")
                else:
                  py_dictionary.pop(remove_which)
                  print(f"{remove_which} has been removed from {chosen_file}\n-------------------------")

                  dumper = json.dumps(py_dictionary, indent=1)
                  with open(f"passwords/{chosen_file}", "w") as x:
                        x.write(dumper)
                        
                        f.close()
            

        elif operations == "return":
            with open(f"passwords/{chosen_file}", "r") as f:
                py_dictionary = json.load(f)  # python dictionary
                f.close()
            print("which password do you want? (enter <-stop-> to go back)")
            while True:
                which_one = input("> ")
                if which_one == "<-stop->":
                    break

                elif which_one in py_dictionary:
                    print(py_dictionary.get(which_one))
                else:
                    print(f"there isnt a password associated with {which_one}")


            
        
        elif operations == 'add':
            with open(f"passwords/{chosen_file}", "r") as f:
                py_dictionary = json.load(f)  # python dictionary
                f.close()
            

            os.system('cls')
            print("if you enter a taken key then the new password will replace the old one.\n enter <-stop-> for either key or password and youll return to storage menu")
            print("---------------------------------------------------------------------------------------------------------------------------------------------------")
            while True:
                keyy = input('enter key: ')
                password = input(f"enter password for {keyy}: ")

                if keyy == "<-stop->" or password == "<-stop->":
                    dumper = json.dumps(py_dictionary, indent=1)
                    with open(f"passwords/{chosen_file}", "w") as x:
                        x.write(dumper)
                        
                        f.close()
                    os.system("cls")
                    mainn()
                else:
                    py_dictionary[keyy] = password
                    

                    print(f"{keyy} : {password} has been added to {chosen_file}\n---------------------------")


                
                    
def pick_create_txt(): # main
    onlyfiles = next(os.walk("passwords"))[2] # list of all the files in passwords
    sorted(onlyfiles)
    first_options = ["new"] + onlyfiles


    

    print("options with the .json extention is available storage\n--------------------------------------------------------\nnew - creates a new storage")
    for storage in onlyfiles:
        print(storage)
    print("--------------------------------------------------------\npick an option from above^(include .json when picking files)")
    while True:
        picker = input("> ") 
        if picker not in first_options:
            print("that isnt an option.")

        elif picker in onlyfiles:
            return does_stuff_to_files(picker, pick_create_txt)
            

        elif picker == "new":
            os.system('cls')
            create_passwordsTXT(pick_create_txt)
            os.system('cls')
            print('that has been added to the storage folder')
            pick_create_txt()
            



pick_create_txt()


    

