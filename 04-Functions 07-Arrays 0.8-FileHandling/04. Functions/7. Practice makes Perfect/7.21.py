###
# Program that returns the difference between the largest and smallest number
#

def f(num1,num2,num3):
    diff = max(num1,num2,num3) - min(num1,num2,num3)
    return diff

n1 = int(input('Enter your first number: '))
n2 = int(input('Enter your second number: '))
n3 = int(input('Enter your third number: '))
print(f'The difference between the biggest and smallest number is: {f(n1,n2,n3)}')    