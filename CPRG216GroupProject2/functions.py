def show_menu():
    print("What would you like to do today?")
    print("-Find a student? enter 1")
    print("-edit a student's info using student ID? enter 2")
    print("-Add a new student? enter 3")
    print("-Remove a student? enter 4")
    option = input()
    return option

def add(students, id, name, gpa, semester):
    pass
    print("Student added")
    print(students.get(id))

def remove(students, id):
    pass

def edit_name(students, id, new_name):
    pass

def search(students, id):
    pass

def run_search(students):
    pass

def run_edit(students):
    pass

def run_add(students):
    print("Enter id of the student, followed by the student's information.")
    i = input("id:")
    n = input("name:")
    gpa = input("gpa:")
    s = input("semester:")
    add(i, n, gpa, s)

def run_remove(students):
    pass

