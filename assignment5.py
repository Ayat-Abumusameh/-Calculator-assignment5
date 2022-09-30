print(" Welcome For You In My Calculator >_< ")
print("The Calculator will not stop calculating until you enter instad of an Arithmetic operation anything except the arithmetic operation")
print("Good Luck ^_^")
def calculator():
    while True:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        operation = input("Enter the operation: ")
        if operation=="+":
            print(num1 + num2)
        elif operation=="-":
            print(num1 - num2)
        elif operation=="*":
            print(num1 * num2)
        elif operation=="/":
            print(num1 / num2)
        else:
            print("You have not typed a valid operator")
            loop()
def loop():
    Qs= input("Do you want make another operation? ")
    if Qs=="Yes":
        calculator()
    else:
        print("see you later >_<")
#    restart()
    exit()
#    restart()
#def restart():
#   back=("Do you want come back to the calculator? ")
#if back=="yes":
#     calculator()
calculator()
loop()
#restart()