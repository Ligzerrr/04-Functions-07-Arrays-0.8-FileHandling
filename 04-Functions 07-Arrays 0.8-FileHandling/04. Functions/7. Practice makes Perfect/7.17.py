###
# Palindrome

def f(palindrome):
    end1 = 0
    end2 = len(palindrome) - 1
    while end1 < end2:
        if (palindrome[end1] != palindrome[end2]):
            return False
        end1+=1
        end2-=1
    return True

stringa = input('Enter a string: ')
print(f'Your string is a palindrome: {f(stringa)}')
            
    