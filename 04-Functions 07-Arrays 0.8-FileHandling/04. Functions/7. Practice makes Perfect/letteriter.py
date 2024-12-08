###
#

def letit(word, let):
    it = 0
    for char in word:
        if char.capitalize() == let.capitalize():
            it += 1
    return it