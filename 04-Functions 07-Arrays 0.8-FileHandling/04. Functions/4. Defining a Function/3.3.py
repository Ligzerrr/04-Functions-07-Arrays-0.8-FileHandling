###
# Calculates the area of a triangle based on the lengths
# of the triangle's sides
#
import math

def triangle_area(a,b,c):
    sp = (a + b + c) / 2
    area = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    return area

a = int(input('Enter the first side of the triangle: '))
b = int(input('Enter the first side of the triangle: '))
c = int(input('Enter the first side of the triangle: '))
print(f'The area of ​​a triangle with sides {a}, {b} and {c} is {triangle_area(a,b,c)}')
