from functions import *
from student import *
print("Welcome to the students record program") # welcome message

new_student = Student(0, "q", "q", 0, 0)
running = True
# loops until user wishes to exit
while running:
    match show_menu():
        case("1"):
            run_add(new_student)
        case("2"):
            run_search(list)
        case("3"):
            run_edit(list)
        case("4"):
            run_remove(list)
        # case("5"):
        #     run_print_list(list)
        # case("6"):
        #     run_save(list)
        case(_):
            print("That is not a valid input. Please input a proper input.")
    # asks if user wants to continue using the program
    while(True) :
        userCont = input("Would you like to continue(y/yes), or exit the program(n/no)?\n")
        # taking in user input as well as error handling
        if userCont.startswith('y') :
            break
        elif userCont.startswith('n') :
            running = False
            break
        else :
            print("That is not a valid input. Please input a proper input.")
        