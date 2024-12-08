###
# Functions to read any data type from the keyboard
#
def input_string(message):
    input_str = input(message)
    return input_str

def input_integer(message):
    input_int = input(message)
    return int(input_int)

def input_real(message):
    input_r = input(message)
    return float(input_r)

def input_boolean(message):
    input_bool = input(message).capitalize()
    if input_bool == 'Y':
        return True
    elif input_bool == 'N':
        return False
   