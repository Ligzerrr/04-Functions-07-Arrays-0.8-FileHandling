###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

letter_read = input('Input a letter: ')
print(f'You input {letter_read}.')

number = int("20303")
print(f'Number representing the string "20303": {number}')

str_bin = bin(304)
print(f'The binary string representing decimal number 304 is: {str_bin}')

str_hex = hex(304)
print(f'The hexadecimal string representing the decimal number 304 is: {str_hex}')

int_uni = ord('€')
print(f'The ascii code representing € sign is: {int_uni}')

int_abs = abs(-17)
print(f'The absolute value of -17 is: {int_abs}')