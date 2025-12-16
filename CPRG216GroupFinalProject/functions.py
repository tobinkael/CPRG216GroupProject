from car import *
def start(list):
    '''
    Takes in a list. Retrives the information from the 
    text file and saves it to the list.
    '''
    f_obj = open("data.txt", "r")
    line = f_obj.readline()

    # reads each line of the text file and saves each line to a new index in a list
    while line != "":
        line = line.rstrip()
        lparsed = line.split()
        list.append(lparsed)
        line = f_obj.readline()
    f_obj.close()

def show_menu():
    '''
    Prints a menu of options for the user to select
    '''
    print("What would you like to do today?")
    print("-Add a car? enter 1")
    print("-Search for car? enter 2")
    print("-Edit car info? enter 3")
    print("-Remove a car? enter 4")
    print("-Print the car list? enter 5")
    print("-Save the data to a file? enter 6")
    print("-Exit? enter 0.")
    option = input() # variable in order to store the users answer
    return option

def add(list):
    running = True
    while running:
        car_exists = False
        print("Enter id of the car, followed by the car's information.")

        id = int(input("id:"))
        n = input("name:")
        m = input("make:")
        b = input("body:")
        y = input("year:")
        v = float(input("value:"))

        # if the id is being used in the list, it will break the loop and print an error message
        for x in range(len(list)):
            value = list[x]
            search_id = str(id)
            str_v = str(v)
            if(search_id == value[0]):
                print("Incorrect Id. Id already exist in the system.")
                car_exists = True
                break
            # if the name, make, body, year, and value are being used in the list, it will break the loop and print an error message
            # The reason this is done is because there are usually multiple cars with the same name, make, body, year, and value in 
            # a store. That is why this is done like this and not by just simply taking in the name of the car.
            elif((n == value[1]) and (m == value[2]) and (b == value[3]) and (y == value[4]) and (str_v == value[5])):
                print("The car is already in the inventory. No action is required..")
                car_exists = True
                break
        # if the id is free, save to the list
        if car_exists == False:
            new_car = Car(id, n, m, b, y, v)
            car_to_add = new_car.__str__()
            temp_list = car_to_add.split()

            list.append(temp_list)
            # informs user of decision
            print("\nCar is added to the inventory\n")
            
            for x in range(len(list)):
                value = list[x]
                search_id = str(id)
                if(search_id == value[0]):
                    for z in range(len(value)):
                        print(value[z], end=" ")
                    car_exists = True
                    break
        # asks user if they want to add another item to the list
        while(True) :
            userCont = input("\nDo you want to add more cars? y(yes)/n(no)\n")
            if userCont.startswith('y'):
                break
            elif userCont.startswith('n'):
                running = False
                break
            # error handling
            else :
                print("That is not a valid input. Please input a proper input.")
    
def search(list):
    while True:
        user_input = input("To search using the Id enter 1. To search using the name of the car enter 2. Enter -1 to return to the previous menu\n")
        match user_input:
            # breaks loop thereby returns the user to the menu screen
            case("-1"):
                break
            case("1"):
                id = int(input("Please Enter the id of the car:\n"))
                # searches through to see if the car exists in the program. 
                # if the car is found it will print out the information.
                for x in range(len(list)):
                    value = list[x]
                    search_id = str(id)
                    car_exists = False
                    if(search_id == value[0]):
                        print("Car found")
                        for z in range(len(value)):
                            print(value[z], end=" ")
                        print("\n")
                        car_exists = True
                        break
                # the car is not found and prints a message to the user
                if(car_exists == False):
                    print("Car not found")
            case("2"):
                n = input("Please Enter the name of the car:\n")
                # searches through to see if the car exists in the program. 
                # if the car is found it will print out the information.
                for x in range(len(list)):
                    value = list[x]
                    search_n = str(n)
                    car_exists = False
                    if(search_n == value[1]):
                        print("Car found")
                        for z in range(len(value)):
                            print(value[z], end=" ")
                        print("\n")
                        car_exists = True
                        break
                # the car is not found and prints a message to the user
                if(car_exists == False):
                    print("Car not found")
            case(_):
                print("That is not a valid input. Please input a proper input.")

def edit(list):
    while True:
        car_exists = False
        id = int(input("\nEnter the id of the car. Enter -1 to return to the previous menu\n"))
        # breaks loop thereby returns the user to the menu screen
        if(id == -1):
            break

        # id entered is real and won't return user to menu screen.
        n = input("name:")
        m = input("make:")
        b = input("body:")
        y = input("year:")
        v = float(input("value:"))

        # if the id is being used in the list, it will update the id with the new information
        for x in range(len(list)):
            value = list[x]
            search_id = str(id)
            if(search_id == value[0]):
                car_exists = True
                new_car = Car(id, n, m, b, y, v)
                car_to_add = new_car.__str__()
                temp_list = car_to_add.split()

                # removing old information
                del list[id-1]  
                # adding new information
                list.insert((id-1),temp_list)
                print("Car's new info is:")

                value = list[id-1]
                search_id = str(id)
                for z in range(len(value)):
                    print(value[z], end=" ")
                break
        # if the car is not in the system
        if(car_exists == False):
            print("\nCar not found")

def remove(list):
    running = True
    while running:
        car_exists = False
        id = int(input("\nEnter id of the car that you want to remove from the inventory.\n"))

        # looks to see if the id is in the system
        search_id = str(id)
        for x in range(len(list)):
            value = list[x]
            if(search_id == value[0]):
                car_exists = True
                break
        # if the id is in the system, remove the car
        if(car_exists == True):
            del list[id-1]  
            print("Car removed")
        # if the id is not in the system, print error message to user
        else:
            print("not found")

        # asks user if they want to remove another item to the list
        while(True) :
            userCont = input("\nDo you want to remove more cars? y(yes)/n(no)\n")
            if userCont.startswith('y'):
                break
            elif userCont.startswith('n'):
                running = False
                break
            # error handling
            else :
                print("That is not a valid input. Please input a proper input.")

def print_list(list):
    '''
    prints out the lists indexes and individual elements
    '''
    print("\n\n")
    for x in range(len(list)):
        values = list[x]
        for y in range(len(values)):
            print(values[y], end=" ")
        print("\n")

def save(list):
    '''
    Takes in a list. Takes the information from the list and
    records it in a text file
    '''
    f_obj = open("data.txt", "w")
        
    # Reads each index of the list
    for x in range(len(list)):
        values = list[x]
        # Reads each elements of the index and writes to file
        for y in range(len(values)):
            f_obj.write(values[y])
            f_obj.write(" ")
        f_obj.write("\n")
    
    print("Data saved to local file successfully!")
