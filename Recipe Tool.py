## Recipe App
from os.path import exists

### This is a Python tool that can create, edit, and delete recipe files.

## Functions and variables.

def display_menu():
    print("---RECIPE TOOL---")

    main_menu = {
        1:"Write New Recipe",
        2:"Delete Existing Recipe",
        3:"Update Existing Recipe",
        4:"Exit"
    }

    for i in main_menu:
        print(f'{i} : {main_menu[i]}')

    option = int(input("Input the number of your options. > "))
    if option == 1:
        write_recipe()
    else:
        print("Please provide a valid option.")
        display_menu()

def write_recipe():
    print("---NEW RECIPE---")
    print("You will be writing a new recipe.")
    new_filename = input("What is the title of your recipe? > ")
    new_filename = new_filename + ".txt"

    if exists(new_filename):
        print("This file already exists.")
        print("Please provide a new filename.")
        write_recipe()

    new_file = open(new_filename,"a+",newline="\n")
    new_file.write(f'<-----{new_filename.replace(".txt","").upper()}----->')
    new_file.write("\n")

    print("---WRITE RECIPES---")
    to_write = "" 
    print("Provide the text you want to write.")
    print("To end writing, type 'END'.")
    while to_write != "END":
        to_write = input("> ")
        new_file.write(to_write)
        new_file.write("\n")
        if to_write == "END":
            print("---Closing Text---")

## Displaying the main menu.

display_menu()