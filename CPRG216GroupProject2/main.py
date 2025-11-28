from functions import *
print("Welcome to the students record program")

list = {}
running = True
while running:
    match show_menu():
        case("1"):
            run_search(list)
        case("2"):
            run_edit(list)
        case("3"):
            run_add(list)
        case("4"):
            run_remove(list)
        case(_):
            print("That is not a valid input. Please input a proper input.")
    while(True) :
        userCont = input("Would you like to continue, or exit the program (y/yes)(n/no)?\n")
        if userCont.startswith('y') :
            break
        elif userCont.startswith('n') :
            running = False
            break
        else :
            print("That is not a valid input. Please input a proper input.")
        