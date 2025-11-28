def show_menu():
    '''
    Prints a menu of options for the user to select
    '''

    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    option = input() # variable in order to store the users answer
    return option

def add(students, id, name, gpa, semester):
    '''
    Takes in a list, an int, a string, a float, and an int
    '''

    students[id] = [id, name, gpa, semester]
    print("Student added")
    values = students[id]
    
    # prints all the values associated with the key. 
    # This is done to bypass the brackets that come with 
    # printing a dictionary
    for i in range(4):
        print(values[i], end=" ")

def remove(students, id):
    '''
    Takes in a list and an interger id. 
    Removes the key-value pair at the id (key)
    '''

    # checks to see if the entered id was an id that is within the dictionary
    if id in students: 
        students.pop(id)
        print("Student removed.")
    # if the id entered is not a key, print error message to user
    else:
        print("Student not found.",end="")

def edit_name(students, id, new_name):
    '''
    Takes in a list, a key, and the name change
    '''

    # get the indiviudal values within the key 
    # and stores them inside a temporary variable 
    # and temporary list
    values = students[id] 
    gpa = values[2]
    sem = values[3]
    temp ={}
    # Setting the temporary list
    temp[id] = [id, new_name, gpa, sem]
    # Removes old information and updates it 
    students.pop(id)
    students.update(temp)
    # Informs the user that the change was madeS
    print("Student name modified for the student with id", id)
    print("Student's new name is", new_name)

def search(students, id):
    '''
    Takes in a list and a key. Searches for the
    key-value pair.
    '''

    # Checks to see if the entered key 
    # exists within the list
    if id in students:
        print("Student found.")
        values = students[id]

        # This is only range 3 as the testing expected output 
        # doesn't display the semester. Unclear if that is a mistake 
        # or if that is intentional
        for i in range(3): 
            print(values[i], end=" ") # prints the indiviual values to bypass the brackets that come with prints a dictionary on its own
    # Error message for the user
    else:
        print("Student not found.",end="")

def run_search(students):
    '''
    Takes in a list. Provides the user a chance to 
    change their mind if they selected the wrong option.
    '''
    option = True 
    while option:
        id = int(input("\nEnter the id of the student. Enter -1 to return to the previous menu\n"))
        # break condition if the user entered the wrong option
        if(id == -1) :
            break
        else :
            search(students, id)

def run_edit(students):
    '''
    Takes in a list. Provides the user a chance to 
    change their mind if they selected the wrong option.
    '''
    
    option = True
    while option:
        id = int(input("\nEnter the id of the student. Enter -1 to return to the previous menu\n"))
        # break condition if the user entered the wrong option
        if(id == -1) :
            break
        else :
            # checks to see if the entered key exists within the list. 
            # If not, it will print an error message to the user.
            if id in students:
                n = input("Enter the new name of the student\n")
                edit_name(students, id, n)
            else:
                print("Student not found.",end="")

def run_add(students):
    '''
    Takes in a list. Asks the user for different variables 
    and then passes it on to another function
    '''
    option = True
    while option:
        # asking for and storing user input
        print("Enter id of the student, followed by the student's information.")
        i = int(input("id:"))
        n = input("name:")
        g = float(input("gpa:"))
        s = int(input("semester:"))
        add(students, i, n, g, s) # function call

        # asks user if they want to add another item to the list
        while(True) :
            userCont = input("\nDo you want to add another new student? y(yes)/n(no)\n")
            if userCont.startswith('y') :
                break
            elif userCont.startswith('n') :
                option = False
                break
            # error handling
            else :
                print("That is not a valid input. Please input a proper input.")

def run_remove(students):
    '''
    Takes in a list. Provides the user a chance to 
    change their mind if they selected the wrong option
    '''
    option = True
    while option:
        id = int(input("\nEnter id of the student that you want to remove from the students' registry. Enter -1 to return to the previous menu\n"))
        if(id == -1) :
            break
        else :
            remove(students, id) # function call

