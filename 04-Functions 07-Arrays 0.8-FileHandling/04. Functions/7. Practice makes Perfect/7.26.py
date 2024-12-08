###
# Program that returns a string with all the characters seperated by dashes :)

def f(text):
    if len(text) == 0:
        return ""
    elif len(text) == 1:
        return text[0]
    sep_text = ""
    for i in range(len(text)):
        sep_text += text[i]  # Add the current character
        if i != len(text) - 1:  # Check if it is not the last character
            sep_text += "-"
    return sep_text

text = input('Enter in a text: ')
print(f'{f(text)}')
