from functions import *
print("Welcome to the students record program") # welcome message

list = {} # intialize list
running = True
# loops until user wishes to exit
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
    # asks if user wants to continue using the program
    while(True) :
        userCont = input("Would you like to continue, or exit the program (y/yes)(n/no)?\n")
        # taking in user input as well as error handling
        if userCont.startswith('y') :
            break
        elif userCont.startswith('n') :
            running = False
            break
        else :
            print("That is not a valid input. Please input a proper input.")
        