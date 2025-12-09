from student import *

def show_menu():
    '''
    Prints a menu of options for the user to select
    '''

    print("What would you like to do today?")
    print("-Add a student? enter 1")
    print("-Search for student 2")
    print("-Edit student info? enter 3")
    print("-Remove a student? enter 4")
    print("-Print the student list? enter 5")
    print("-Save the data to a file? enter 6")
    option = input() # variable in order to store the users answer
    return option

def add(student):
    '''
    Takes in an object records data to data.txt
    '''
    student_exists = False

    f_obj = open("data.txt", "r")
    line = f_obj.readline()

    # new student to enter
    nlist = student.__str__()
    nparsed = nlist.split()

    # searches to see if id is being used in the program
    while line != "":
        line = line.rstrip()
        lparsed = line.split()

        # if the id is being used in the 'database', it will break the loop and print an error message
        if(lparsed[0] == nparsed[0]):
            print("Incorrect Id. Id already exist in the system.")
            student_exists = True
            break
        line = f_obj.readline()
    f_obj.close()
    # if the id is free, write to the file
    if student_exists == False :
        f_obj = open("data.txt", "a")
        
        f_obj.write(student.__str__())
        f_obj.close()
    # informs user of decision
    print("Student Enrolled in the system")
    # values = students[id]
    
    # prints all the values associated with the key. 
    # This is done to bypass the brackets that come with 
    # printing a dictionary
    # for i in range(4):
    #     print(values[i], end=" ")

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
    Takes in an object and an int. Searches the 'database' for a match
    '''
    student_exists = False
    
    f_obj = open("data.txt", "r")
    line = f_obj.readline()

    # searches to see if id is being used in the program
    if(id == 2):
        fn = input("Please Enter the first name of the student:\n")
        ln = input("Please Enter the last name of the student:\n")

        while line != "":
            line = line.rstrip()
            lparsed = line.split()

            # if the name is being used in the 'database', it will break the loop and print a message to the user
            if((lparsed[1] == fn) and (lparsed[2] == ln)):
                student_exists = True
                break
            line = f_obj.readline()
    else:
        i = input("Please Enter the id of the student:\n")
        while line != "":
            line = line.rstrip()
            lparsed = line.split()

            # if the id is being used in the 'database', it will break the loop and print a message to the user
            if(lparsed[0] == i):
                student_exists = True
                break
            line = f_obj.readline()
    if(student_exists == True):
        print("Student found")
    else:
        print("Student not found")








    # # Checks to see if the entered key 
    # # exists within the list
    # if id in students:
    #     print("Student found.")
    #     values = students[id]

    #     # This is only range 3 as the testing expected output 
    #     # doesn't display the semester. Unclear if that is a mistake 
    #     # or if that is intentional
    #     for i in range(3): 
    #         print(values[i], end=" ") # prints the indiviual values to bypass the brackets that come with prints a dictionary on its own
    # # Error message for the user
    # else:
    #     print("Student not found.",end="")

def run_search(students):
    '''
    Takes Student object. Provides the user a chance to 
    change their mind if they selected the wrong option.
    '''
    option = True 
    while option:
        id = int(input("\nTo search using the Id enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu\n"))
        # break condition if the user entered the wrong option
        if(id == -1) :
            break
        elif(id == 1) :
            search(students, id)
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

def run_add(student):
    '''
    Takes in an object. Asks the user for different variables 
    and then passes it on to another function
    '''
    option = True
    while option:
        # asking for and storing user input
        print("Enter id of the student, followed by the student's information.")
        i = int(input("Id:"))
        fn = str(input("First name:"))
        ln = str(input("Last name:"))
        g = float(input("GPA:"))
        s = int(input("Semester:"))
        new_student = Student(i, fn, ln, g, s)
        add(new_student) # function call

        # asks user if they want to add another item to the list
        while(True) :
            userCont = input("\nDo you want to add more students? y(yes)/n(no)\n")
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

def run_save(students):
    pass

def run_print_list(students):
    pass