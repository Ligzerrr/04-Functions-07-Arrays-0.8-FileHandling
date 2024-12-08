###
# Program that detects if people are leaving or entering
def f(detector):
    count = 0
    for update in detector:
        if update == '+':
            count += 1
        elif update == '-':
            count -= 1
        if count >= 3:
            return True
    return False

str_thing = input("Enter '+' for people entering and '-' for people leaving the room: ")
print(f'{f(str_thing)}')