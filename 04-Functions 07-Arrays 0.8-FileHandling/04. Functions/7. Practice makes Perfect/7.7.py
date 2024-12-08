###
# Program that checks if a binary number is valid

def is_Valid(n):
    # You can use return all(char in '01' for char in n) but I'll use a longer loop
    for char in n:
        if char != '1' and char != '0':
            return False
    return True

bin = input('Enter a binary number: ')
print(f'The number is a binary number: {is_Valid(bin)}')
