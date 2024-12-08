import turtle
import figures
# Set up the screen
window = turtle.Screen()
window.bgcolor("lightgreen")

# Create the turtle

turtle.speed(5)

# Side length
side_length = 100 #normal side + side a for rectangle

# Draw a square
figures.draw_square(side_length)
turtle.penup()
turtle.goto(-300, 300)
turtle.pendown()
figures.draw_triangle(side_length)
turtle.penup()
turtle.goto(300, 300)
turtle.pendown()
figures.draw_rectangle(side_length,50)
# Hide the turtle and finish
turtle.hideturtle()
window.mainloop()