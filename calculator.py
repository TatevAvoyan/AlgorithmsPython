def add_numbers():
    number1 = input("Enter first Number: ")
    number2 = input("Enter second Number: ")

    print(float(number1) + float(number2))

def subtract_numbers():
    number1 = input("Enter first Number: ")
    number2 = input("Enter second Number: ")

    print(float(number1) - float(number2))

def display_menu():
    print("---> Choose the operation <---")
    print("1. Add Numbers")
    print("2. Subtract Numbers")

    operation = input()

    if operation == "1":
        return add_numbers()
    elif operation == "2":
        return subtract_numbers()
    else:
        print("Wrong operation entered. Pls try again: ")
        display_menu()

display_menu()