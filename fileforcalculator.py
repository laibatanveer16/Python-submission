print("\t\t\t\t\t      BASIC CALCULATOR             \t\t\t\t\t")

print("\nEnter The Numbers:")
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))


def add():
    answer = num1+num2
    print("\n", num1, "+", num2, "=",answer)


def subtract():
    answer = num1-num2
    print("\n", num1, "-", num2, "=", answer)


def multiply():
    answer= num1*num2
    print("\n", num1, "*", num2, "=", answer)


def divide():

    try:
        answer= num1/num2
        print("\n", num1, "/", num2, "=", answer)

    except ZeroDivisionError:
        print("Error: Denominator Cannot Be 0.")


def choices():
    print("\nWhat Operation Do You Want To Perform")
    print('1. Add')
    print('2. Subtract')
    print('3. Multiply')
    print('4. Divide')