from student import *
# When database is mentioned, it refers to the text file that the information
# is being written to. I believe that in a real system that this information
# would be stored inside a database. 
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

def edit_name(lp, i, fn, ln, g, s):
    '''
    Takes in a first name, a last name, gpa, and semester
    '''
    new_student = Student(i, fn, ln, g, s)
    list = []

    f_obj = open("data.txt", "r")
    line = f_obj.readline()

    # searches to see where the id is being used in the program
    while line != "":
        line = line.rstrip()
        lparsed = line.split()
        list.append(lparsed)
        line = f_obj.readline()
    f_obj.close()
    location = list.index(lp)
    list.remove(lp)
    entry = [str(i),fn,ln,str(float(g)),s]
    
    # adds the student back to the temporary list
    list.insert(location, entry)

    f_obj = open("data.txt", "w")

    
    
    
    # prints all the values associated with the key. 
    # This is done to bypass the brackets that come with 
    # printing a dictionary
    for x in range(4):
        values = list[x]
        for y in range(len(list)+1):
            f_obj.write(values[y])
            f_obj.write(" ")
        f_obj.write("\n")
    
    f_obj.close()
    new_entry = list[location]
    print("Student's new info is")
    for z in range(len(list[location])):
        print(new_entry[z], end=" ")
    
def search(userInput):
    '''
    Takes in an object and an int. Searches the 'database' for a match
    '''
    student_exists = False
    
    f_obj = open("data.txt", "r")
    line = f_obj.readline()

    # searches to see if id is being used in the program
    if(userInput == 2):
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
        print(line)
    else:
        print("Student not found")

def save(students):
    pass

def print_list(students):
    pass

def run_search():
    '''
    Takes Student object. Provides the user a chance to 
    change their mind if they selected the wrong option.
    '''
    option = True 
    while option:
        userInput = int(input("\nTo search using the Id enter 1. To search using the first name and last name enter 2. Enter -1 to return to the previous menu\n"))
        # break condition if the user entered the wrong option
        if(userInput == -1) :
            break
        elif(userInput == 1) :
            search(userInput)
        else :
            search(userInput)

def run_edit():
    '''
    Accesses 'database' to see if the id is in the system. Provides the user 
    a chance to change their mind if they selected the wrong option.
    '''
    
    option = True
    while option:
        id = input("\nEnter the id of the student. Enter -1 to return to the previous menu\n")
        # break condition if the user entered the wrong option
        if(int(id) == -1) :
            break
        else :
            # checks to see if the entered id exists within the 'database'. 
            # If not, it will print an error message to the user.

            student_exists = False
            
            f_obj = open("data.txt", "r")
            line = f_obj.readline()

            # searches to see if id is being used in the program
            while line != "":
                line = line.rstrip()
                lparsed = line.split()

                # if the id is being used in the 'database', it will break the loop and print a message to the user
                if(lparsed[0] == id):
                    student_exists = True
                    break
                line = f_obj.readline()

        if(student_exists == True):
            id = int(id)
            fn = input("First name:\n")
            ln = input("Last name:\n")
            g = input("GPA:\n")
            s = input("Semester:\n")
            edit_name(lparsed, id, fn, ln, g, s)
        else:
            print("Student not found")

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
        # informs user of decision
        print("Student Enrolled in the system")

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