def main():
    n = get_number()
    meow(n)

def get_number():
    while True:
        number = int(input("What's n?? "))
        if number > 0:
            return number
        
def meow(n):
    for _ in range(n):
        print("meow")

main()