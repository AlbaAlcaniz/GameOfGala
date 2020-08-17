# https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041

from random import randint
from turtle import Turtle, Screen, register_shape

health = 50
damage = 10
fight = randint(10, 20)
step = 0

def up():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(90)
    turtle.forward(10)

def down():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(-90)
    turtle.forward(10)

def left():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(180)
    turtle.forward(10)

def right():
    global step

    if step == fight:
        combat()
    step += 1
    turtle.seth(0)
    turtle.forward(10)

def combat():
    enemy = Turtle()
    enemy.up()
    eHealth = randint(20, 100)
    eDamage = randint(10, 20)

screen = Screen()
screen.screensize(500,500)
screen.bgpic('figures/0_0_map.png')
# screen.setup(500, 350)  # visible portion of screen area
turtle = Turtle()
# turtle.up()
turtle = Turtle()
turtle.speed(10) # Set the speed of the turtle
turtle.pensize(2) # Set the width of the objects drawn
register_shape('figures/0_0_rocket.gif')
turtle.shape('figures/0_0_rocket.gif')

screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

screen.mainloop()