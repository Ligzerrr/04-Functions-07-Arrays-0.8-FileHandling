###
# Program that returns the sum of even or odd digits in a number
#

def f(number, even):
    summ = 0
    if even:
        for char in number:
            if int(char)%2 == 0:
                summ += int(char)
    else:
        for char in number:
            if int(char)%2 != 0:
                summ += int(char)    
    return summ
            
number = input('Enter a number: ')
is_even = input('Calculate the sum of even (Y) or odd (N) numbers? ').lower() == 'y'
if is_even:
    print(f'The sum of even digits in your number is: {f(number,is_even)}')
else:
    print(f'The sum of odd digits in your number is {f(number,is_even)}')