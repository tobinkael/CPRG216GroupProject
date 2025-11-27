def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    option = input()
    return option

def add(students, id, name, gpa, semester):
    students[id] = [id, name, gpa, semester]
    print("Student added")
    values = students[id]
    for i in range(4):
        print(values[i], end=" ")

def remove(students, id):
    pass

def edit_name(students, id, new_name):
    pass

def search(students, id):
    if id in students:
        print("Student found.")
        values = students[id]
        for i in range(3):
            print(values[i], end=" ")
    else:
        print("Student not found.",end="")
        
def run_search(students):
    option = True
    while option:
        id = int(input("\nEnter the id of the student. Enter -1 to return to the previous menu\n"))
        if(id == -1) :
            break
        else :
            search(students, id)

def run_edit(students):
    pass

def run_add(students):
    option = True
    while option:
        print("Enter id of the student, followed by the student's information.")
        i = int(input("id:"))
        n = input("name:")
        g = float(input("gpa:"))
        s = int(input("semester:"))
        add(students, i, n, g, s)

        while(True) :
            userCont = input("\nDo you want to add another new student? y(yes)/n(no)\n")
            if userCont.startswith('y') :
                break
            elif userCont.startswith('n') :
                option = False
                break
            else :
                print("That is not a valid input. Please input a proper input.")

def run_remove(students):
    pass

