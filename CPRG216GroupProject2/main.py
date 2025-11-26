from functions import *
list = dict()
print("Welcome to the students record program")
while True:
    match show_menu():
        case("1"):
            print("Reached 1")
        case("2"):
            print("Reached 2")
        case("3"):
            print("Reached 3")
        case("4"):
            print("Reached 4")
        case(_):
            print("That is not a valid input. Please input a proper input.")