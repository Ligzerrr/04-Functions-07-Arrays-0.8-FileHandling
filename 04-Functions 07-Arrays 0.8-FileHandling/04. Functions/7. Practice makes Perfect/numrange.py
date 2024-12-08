###
#

def range_num(num, x, y):
    for i in range(x, y+1): # Mozna zrobic return x <= num <= y whatever 
        if num == i:
            return True
    return False
        
