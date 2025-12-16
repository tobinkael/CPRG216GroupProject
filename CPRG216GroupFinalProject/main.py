from functions import *
from car import *
list = []
start(list)
print("Welcome to the cars inventory system") # welcome message

# loops until user wishes to exit
while True:
    match show_menu():
        case("1"):
            add(list)
        case("2"):
            search(list)
        case("3"):
            edit(list)
        case("4"):
            remove(list)
        case("5"):
            print_list(list)
        case("6"):
            save(list)
        case("0"):
            break
        case(_):
            print("That is not a valid input. Please input a proper input.")