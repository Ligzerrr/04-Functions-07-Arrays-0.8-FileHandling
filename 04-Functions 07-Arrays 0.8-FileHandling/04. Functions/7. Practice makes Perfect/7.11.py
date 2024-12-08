###
# Program that checks if at least 1 of 3 numbers is negative

def f(n1,n2,n3):
    if n1 < 0 or n2 < 0 or n3 < 0:
        return True
    return False

n1 = int(input('Enter your first number: '))
n2 = int(input('Enter your second number: '))
n3 = int(input('Enter your third number: '))

print(f'One of the numbers is negative: {f(n1,n2,n3)}')