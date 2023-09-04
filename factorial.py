# using for loop
fac=int(input('Enter a number : '))
product=1
for i in range(fac):
    product=product*(i+1)
print(product)

# using function
def factorial(n):
    product=1
    for i in range(n):
        product=product*(i+1)
    return product
    
print(factorial(5))

# using Recursion
def factorial_recursion(n):
    if n==1 or n==0:
        return 1
    return n*factorial_recursion(n-1)

print(factorial_recursion(5))