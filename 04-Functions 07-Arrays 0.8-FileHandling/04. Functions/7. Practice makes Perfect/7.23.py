###
# Program that checks if password is valid
#
def f(password):
    if len(password) < 6:
        return False
    for j in range(len(password)):
        for i in range(j + 1, len(password)):  
            if password[j] == password[i]:  
                return False  
    return True 

password = input('Enter in your password: ')
print(f'Your password is valid: {f(password)}')


