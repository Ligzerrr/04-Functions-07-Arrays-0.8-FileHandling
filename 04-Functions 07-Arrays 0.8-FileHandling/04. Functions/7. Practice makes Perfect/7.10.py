###
# Program that returns the number of negative even numbers in the range <x,y>

def range_num(x, y):
    neg_even_num = 0
    for i in range(x, y+1): 
        if i%2 == 0 and i < 0:
            neg_even_num += 1  
    return neg_even_num

x = int(input('Enter the first endpoint: '))
y = int(input('Enter the second endpoint: '))

print(f"There's {range_num(x,y)} negative AND even numbers in the range <{x},{y}>")