def main():
    x = get_int("What's x?? ")
    print(f"x is {x}")

 
def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("What you entered is not an integer")
        else:
            return x

main() 