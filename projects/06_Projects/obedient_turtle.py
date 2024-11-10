"""
Make an obedient turtle that will obey commands to draw shapes.
"""
import random
import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox, simpledialog, Tk

# TODO)
#   1. Create a turtle.
jayfeather = turtle.Turtle()
lionblaze = turtle.Turtle()
hollyleaf = turtle.Turtle()
brambleclaw = turtle.Turtle()
squirrelflight = turtle.Turtle()
leafpool = turtle.Turtle()
crowfeather = turtle.Turtle()
cinderheart = turtle.Turtle()
half_Moon = turtle.Turtle()


turtles= [jayfeather, lionblaze, hollyleaf, brambleclaw, squirrelflight, leafpool, crowfeather, cinderheart, half_Moon]



#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
for t in turtles:
    x = random.randint(-100, 100)
    y = random.randint(-100, 100)
    t.penup()
    t.goto(x, y)
    t.pendown()
def drawcircle(t):
    t.circle(50)
def drawsquare(t):
    for i in range(4):
        t.forward(50)
        t.left(90)
def drawtriangle(t):
    for i in range(3):
        t.left(120)
        t.forward(50)

shape = simpledialog.askstring(title="", prompt="what shape would you like the robot to draw? circle, triangle, or square?")
if shape == "circle":
    for t in turtles:
        drawcircle(t)

elif shape == "square":
    for t in turtles:
        drawsquare(t)
elif shape == "triangle":
    for t in turtles:
        drawtriangle(t)
else:
    messagebox.showinfo(title="", message ="there was an error in your responce. please exit out and try again. the error could've been either a spelling mistake or it was not in the answer options. so remember to type your answer exactly how the question said it!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
#   3. Ask the user for the for a shape to draw.
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
turtle.exitonclick()
