###
# 
#
def sum(n):
    if n == 1:
        return 1
    total = n + sum(n - 1)
    return total

number = int(input('Enter a number for the range from 1 - n: '))
print(f'The sum of natural numbers in the range 1 - {number} is: {sum(number)}')