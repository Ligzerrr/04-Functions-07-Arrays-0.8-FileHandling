###
# Program that returns the sum of repeated digits in a number
#

def f(number):
    numer = 0
    sum = 0
    while True:
        if numer >9:
            return sum
        for char in number:
            liczba = int(char)
            if numer == liczba:
                sum += numer
        numer+=1

number = input('Please enter a number: ')
print(f'The sum of repeated digits in the number is: {f(number)}')




