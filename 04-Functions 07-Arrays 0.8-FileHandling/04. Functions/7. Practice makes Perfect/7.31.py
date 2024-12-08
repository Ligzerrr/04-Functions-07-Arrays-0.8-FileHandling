###
# Recursion for calculating the power of something
def power(x,y):
    if y == 0:
        return 1
    else:
        return x * (x, y - 1)

x = int(input('Choose the base of the power: '))
y = int(input('Choose the exponent of the power: '))
print(f'{x}^{y} = {power(x,y)}')