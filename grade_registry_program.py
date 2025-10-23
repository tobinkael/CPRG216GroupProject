print("Welcome to the Grade Registry Program") # Greets user to program and informs user what the program is

while(True) : # runs until user wishes to exit the program
    userInput = input("Would you like to add a new student? y(yes),n(no)\n").lower()
    if userInput.startswith('y') : 
        name = input("Enter the student's name:\n")
        print("Enter student GPA for each subject. Enter -1 to stop entering GPA.") # Informs user what to do and how to exit loop
        # define variables
        GPA = 0 
        count = 0
        
        while(True) : # loops until user has finished entering values
            numInput = float(input()) # Get's GPA from user
            if numInput == -1 : # if user has finished entering values, exit program
                break
            else :
                GPA += numInput # add input to GPA ()
                count += 1 # counts how many values the user has entered
        if count != 0 :
            GPA/=count
            # add Student and GPA to list
        else :
            # add Student and GPA to list with GPA equal to zero
            print("Dummy print, should add student to list with GPA of zero")
    elif userInput.startswith('n') : # user wishes to exit program
        break
    else : # user has entered something outside of given parameters
        print("Incorrect Input, please enter y(yes)/n(no)")
print("This is the list of students in the system, and their corresponding accumulative GPA")