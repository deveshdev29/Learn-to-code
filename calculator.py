def main():
    x = int(input("What's your first number: "))
    y = int(input("What's your second number: "))
    print("1 --- Additon")
    print("2 --- Subtraction")
    print("3 --- Multiplication")
    print("4 --- Division")
    print("5 --- Power")

    choice = int(input("What you wanna do?? "))

    if choice == 1:
        print(addition(x,y))
    elif choice == 2:
        print(subtraction(x,y))
    elif choice == 3:
        print(multiplication(x,y))
    elif choice == 4:
        print(division(x,y))
    elif choice == 5:
        print(power(x,y))
    else:
        print("Opps! Looks like you entered a wrong choice ")
    

def addition(x,y):
    return x + y


def subtraction(x,y):
    return x - y


def multiplication(x,y):
    return x * y


def division(x,y):
    return x / y


def power(x,y):
    return x ** y


if __name__ == "__main__":
    main()