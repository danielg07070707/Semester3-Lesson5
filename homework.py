# homework: in class, we drew a canvas with a bunch of carrots, potatos, and a sun.
# TODO: An incomplete version of a house has been added to the canvas. Edit the part where it draws the house, and reposition each piece so that the house is complete.
# website to run turtle is https://play.pyroom.app/playground

import turtle
import random

# ---------- Setup ----------
t = turtle.Turtle()
screen = turtle.Screen()
t.shape("turtle")
t.speed(0) # speed 0 is the fastest
t.pensize(1)
t.pencolor("green")
t.fillcolor("green")
screen.bgcolor("skyblue")
screen.setup(1000, 500) 
t.hideturtle()
#       x (width) is 1000 and y (height) is 500
#       x: -500 to 500        y: -250 to 250

# we are going to draw a beautiful garden today

# ground
t.goto(-500, 50)
t.begin_fill()
for i in range(4):
    t.forward(1000)
    t.right(90)
t.end_fill()


t.goto(0, 0)


# one carrot:
def draw_carrot():
    t.pencolor("black")
    t.fillcolor("orange")
    t.begin_fill()
    t.forward(30)
    t.right(100)
    t.forward(80)
    t.right(160)
    t.forward(80)
    t.end_fill()

    t.pensize(10)
    t.pencolor("lime")
    t.forward(30)
    t.forward(-30)
    t.setheading(0)
    t.forward(30)
    t.left(75)
    t.forward(30)
    t.setheading(0)
    t.pensize(1)

def teleport(x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()


# draw 10 carrots
for i in range(10):
    teleport(random.randint(-500, 500), random.randint(-250, 85))
    draw_carrot()


def draw_potato():
    t.pencolor("ivory")
    t.fillcolor("goldenrod")
    t.begin_fill()
    t.circle(30)
    t.end_fill()

#draw 10 potatos
for i in range(10):
    teleport(random.randint(-500, 500), random.randint(-250, -50))
    draw_potato()

#make the sun appear on the top right corner
teleport(450,150)


# sun
t.pencolor("yellow")
t.fillcolor("yellow")
t.pensize(4)

t.begin_fill()
for i in range(36):
    t.forward(13)
    t.left(10)
    # the lines
    t.right(100)
    t.forward(80)
    t.forward(-80)
    t.left(100)
t.end_fill()


teleport(0,0)
t.pencolor("black")
t.pensize(2)

# house:
def draw_house():
    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
        t.forward(170)
        t.left(90)
        t.forward(130)
        t.left(90)
    t.end_fill()

# window:
def draw_window():
    t.fillcolor("lightblue")
    t.begin_fill()
    for i in range(2):
        t.forward(40)
        t.left(90)
        t.forward(50)
        t.left(90)
    t.end_fill()
    t.forward(20)
    t.setheading(90)
    t.forward(50)
    t.forward(-25)
    t.right(90)
    t.forward(20)
    t.forward(-40)

# roof:
def draw_roof():
    t.fillcolor("brown")
    t.begin_fill()
    t.forward(200)
    t.left(160)
    t.forward(160)
    t.left(40)
    t.forward(160)
    t.left(160)
    t.end_fill()

#A DoOoOoOoOoOoOoOoOoOoOoOoOoOoOoR 1+1=3
def draw_door():
    t.setheading(0)
    t.forward(57)
    t.left(90)
    t.forward(50)
    for i in range(45):
        t.forward(2)
        t.left(4)

    t.forward(52)
    t.left(90)
    t.forward(47)
    t.left(90)
    t.penup()
    t.forward(40)
    t.pendown()
    t.circle(1)


# TODO: edit the coordinates of this part, so that the house is neatly positioned with two windows.
draw_house()
teleport(110, 50)
draw_window()
teleport(40, 131)
draw_roof()
teleport(10,0)
draw_door()



























