###
# Program that returns a sentence with spaces removed

def f(sentence):
    nospaces = ""
    for char in sentence:
        if char != " ":
           nospaces += char
    return nospaces

senten = input('Enter a sentence: ')
print(f'Without spaces: \n{f(senten)}')