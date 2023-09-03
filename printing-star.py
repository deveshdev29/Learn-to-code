# simpler star printing
n=int(input("Enter number of rows of star : "))
for i in range(n):
    print('*' * (i+1))

# tougher star printing
n=int(input("Enter number of rows of star : "))
for i in range(n):
    print(' '*(n-i-1),end='')
    print('*'*(2*i+1),end='')
    print(' '*(n-i-1))