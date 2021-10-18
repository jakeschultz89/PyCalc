# description

# imports

# globals


# functions

def print_menu():
    print("-------------------")
    print("Welcome to PyCalc")
    print("-------------------")
    print("[1] Add")
    print("[2] Subtract")
    print("[3] Multiply")
    print("[4] Divide")

    print("-------------------")


# plain instructions
print_menu()

opt = input("Please select an option:")

try:
    num1 = float(input("Please input num 1: "))
    num2 = float(input("Please input num 2: "))
    res = 0

    if(opt == "1"):
        res = num1 + num2

    elif(opt == "2"):
        res = num1 - num2

    elif(opt == "3"):
        res = num1 * num2

    elif(opt == "4"):
        if(num2==0):
            print("Error: Division by zero is not allowed")
        else:
            print(num1/num2)

    print("Result: " + str(res))

except:
    print("Error, unexpected value")