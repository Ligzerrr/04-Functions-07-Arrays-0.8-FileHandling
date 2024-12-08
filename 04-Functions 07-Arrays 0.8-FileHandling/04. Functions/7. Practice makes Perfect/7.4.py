###
# Program that calculates how many times a given letter appeared in a text
#
import letteriter

def main():
    sentence = input('Enter a sentence: ')
    letter = input('Enter a letter to see how many times it appears in your text: ')
    print(f"The letter: '{letter}' appears {letteriter.letit(sentence, letter)} times in: \n{sentence}")
if __name__ == "__main__":
    main()
