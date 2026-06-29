# Whitney Henry
# 06/29/2026
# P4LAB1 
# This program will use turtle graphics to draw a square and a triangle using loops. 

# Import the turtle graphics library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

# Change background color of the window
win.bgcolor("lightgreen")

# Set turtle options
pen.pencolor("blue")
pen.pensize(3)

# Draw a square using a for loop
for side in range(4):
    pen.forward(100)  
    pen.right(90)     

# Move the turtle to the correct position of square
pen.penup()
pen.pendown()
pen.left(60)  

# Draw the triangle using a while loop
count = 0

while count < 3:
    pen.forward(100)  
    pen.right(120)     
    count += 1

# Wait for user to close window
win.mainloop()  