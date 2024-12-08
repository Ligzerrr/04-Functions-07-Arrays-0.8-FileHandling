###
# Program that returns the acronym for the name of the book
def f(name):
    acronym = ""
    # Split the name into words by spaces
    words = name.split()
    for word in words:
        acronym += word[0]  # Take the first letter of each word
    return acronym

name = input('Enter the name of your book: ')
print(f'The acronym of your book is {f(name)}')
