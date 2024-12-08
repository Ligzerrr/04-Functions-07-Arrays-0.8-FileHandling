###
#

import turtle
def draw_square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)

def draw_triangle(length):
    for i in range(3):
        turtle.forward(length)
        turtle.left(120)

def draw_rectangle(length_a, length_b):
    for i in range(2):
        turtle.left(90)
        turtle.forward(length_b)
        turtle.left(90)
        turtle.forward(length_a)

        