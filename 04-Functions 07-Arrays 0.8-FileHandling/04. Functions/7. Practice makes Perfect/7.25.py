###
# Program that returns the sum of the numbers in a <x,y> range that are divisible by 2 and 3 and not by 4
#

def f(x,y):
    total = 0
    for i in range(x, y+1):
        if i%2 == 0 and i%3 == 0 and i%4 !=0:
            total += i
    return total

x = int(input('Enter the lower bound of the range: '))
y = int(input('Enter the higher bound of the range: '))
print(f'The sum of numbers in the range <{x},{y}> that are divisible by 2 and 3 and not by 4 is: {f(x,y)}')
