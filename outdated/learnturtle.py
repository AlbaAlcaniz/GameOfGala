# Learn how to use the turtle module which deals with mouse interaction
# Learned from https://pbaumgarten.com/python/turtle.md
import random
from turtle import Turtle, Screen, register_shape

# Change the shape of the turtle
# flag.shape("turtle")

def olympic_flag():
    """Olympic Flag project: draw the olympic flag
    """
    # Initialize the turtle
    flag = Turtle()

    radius = 60 #Radius of the flags drawn
    margin = 10 #Distance between horizontal flags

    # Set the speed of the turtle
    flag.speed(10)

    # Set the with of the objects drawn
    flag.pensize(4)

    # In order to move the turtle without drawing, we need the command penup
    flag.penup()
    flag.goto(-radius*2-margin,0)
    flag.pendown()

    # Draw the blue circle of radius 60
    flag.color("blue")
    flag.circle(radius)

    # Yelow circle
    flag.penup(); flag.goto(-radius-margin/2, -radius); flag.pendown()
    flag.color("yellow"); flag.circle(radius)

    # Black circle
    flag.penup(); flag.goto(0,0); flag.pendown()
    flag.color("black"); flag.circle(radius)

    # Green circle
    flag.penup(); flag.goto(radius+margin/2, -radius); flag.pendown()
    flag.color("green"); flag.circle(radius)

    # Green circle
    flag.penup(); flag.goto(radius*2+margin,0); flag.pendown()
    flag.color("red"); flag.circle(radius)

    # Command so that the program does not exist asa it finishes drawing
    ws = Screen()
    ws.exitonclick()

def pizza_project():
    """Fat Tony's pizzeria project: draw a pizza with different fillings
    """
    # Initialize the turtle
    yum = Turtle()

    yum.speed(100) # Set the speed of the turtle
    yum.pensize(4) # Set the with of the objects drawn

    pizza_radius = 300 #External radius of the pizza
    pizza_crust = 20

    # Pizza crust
    yum.penup(); yum.goto(0,-pizza_radius); yum.pendown()
    yum.color('peru'); yum.circle(pizza_radius)
    # Fill the circle
    yum.fillcolor("peru"); yum.begin_fill(); yum.circle(pizza_radius); yum.end_fill()

    # Draw the external crust of the pizza
    yum.penup(); yum.goto(0,-pizza_radius+pizza_crust); yum.pendown()
    yum.fillcolor("navajo white"); yum.begin_fill(); yum.circle(pizza_radius-pizza_crust); yum.end_fill()

    # Tomatoes
    tomatoes_num = 10; tomatoes_radius = 40
    yum.fillcolor('red'); yum.color('red')
    tomato_x = (-50,-187,-37,141,72,224,4,198,57,-180)
    tomato_y = (78,-176,170,132,43,-3,-87,-166,-202,43)
    for i in range(tomatoes_num):
        yum.penup()
        yum.goto(tomato_x[i],tomato_y[i])
        yum.pendown()
        yum.begin_fill()
        yum.circle(tomatoes_radius)
        yum.end_fill()

    # Green pepper
    pepper_num = 25; pepper_width = 10; pepper_length = 30
    yum.fillcolor('green'); yum.color('green')
    for i in range(pepper_num):
        yum.penup()
        yum.goto(random.randint(-200,200),random.randint(-200,200))
        yum.pendown()

        yum.begin_fill()
        yum.right(random.randint(0,360))
        yum.forward(pepper_width) # go right 50 pixels
        yum.right(90) # turn right 90 degrees
        yum.forward(pepper_length) # go down 50 pixels
        yum.right(90) # turn right 90 degrees
        yum.forward(pepper_width) # go left 50 pixels
        yum.right(90) # turn right 90 degrees
        yum.forward(pepper_length) # go up 50 pixels
        yum.right(random.randint(0,360))
        yum.end_fill()

    # Mushroom
    mushroom_num = 25; mushroom_square = 20; mushroom_triangle = 35
    yum.fillcolor('light gray'); yum.color('light gray')
    yum.speed(5)
    for i in range(mushroom_num):
        yum.penup()
        yum.goto(random.randint(-200,200),random.randint(-200,200))
        yum.pendown()

        yum.begin_fill()
        yum.right(random.randint(0,360))
        yum.forward(mushroom_square)
        yum.right(90) 
        yum.forward(mushroom_square) 
        yum.right(90) 
        yum.forward(mushroom_square) 
        yum.right(90)
        yum.forward(mushroom_square+(mushroom_triangle-mushroom_square)/2)
        yum.right(-120)
        yum.forward(mushroom_triangle)
        yum.right(-120)
        yum.forward(mushroom_triangle)
        yum.right(-120)
        yum.forward(mushroom_triangle)        
        yum.end_fill()
   
    # Command so that the program does not exist asa it finishes drawing
    ws = Screen()
    ws.exitonclick()
    
def pipeline():
    """Draw a pipe from the pipelines game I want to do
    """
    # Initialize the turtle
    pipe = Turtle()

    pipe.speed(2) # Set the speed of the turtle
    pipe.pensize(2) # Set the width of the objects drawn
    pipe.color('black'); pipe.fillcolor('gray')

    # pipe.hideturtle()
    x_joint = 20; y_joint = 50
    x_pipe = 100; y_pipe = 20
    ext_radius = 70; int_radius = ext_radius-y_pipe

    def draw_joint():
        """Small function to same some space
        """
        pipe.forward(x_joint)
        pipe.right(90) 
        pipe.forward(y_joint) 
        pipe.right(90) 
        pipe.forward(x_joint) 
        pipe.right(90)

    # Bended pipe
    pipe.begin_fill()
    draw_joint()
    pipe.forward(y_joint) 
    pipe.right(90) 
    pipe.forward(x_joint) 
    pipe.right(90) 
    pipe.forward((y_joint-y_pipe)/2)
    pipe.left(90) 
    pipe.circle(int_radius,90)
    pipe.left(90) 
    pipe.forward((y_joint-y_pipe)/2) 
    pipe.right(90) 
    draw_joint()
    pipe.forward(y_joint)
    pipe.right(180)
    pipe.forward((y_joint-y_pipe)/2+y_pipe)
    pipe.left(90)
    pipe.circle(ext_radius,-90)
    pipe.end_fill()

    def draw_pipe():
        """Small function to save some space
        """
        pipe.left(90) 
        pipe.forward(x_pipe)
        pipe.right(90) 
        pipe.forward(y_pipe) 
        pipe.right(90) 
        pipe.forward(x_pipe) 
        pipe.right(90)
        pipe.forward(y_pipe) 
        pipe.right(90) 
        pipe.forward(x_pipe) 
        pipe.left(90) 

    # Straight pipe
    # pipe.right(90)
    # pipe.begin_fill()
    # draw_joint()
    # pipe.forward(y_joint) 
    # pipe.right(90) 
    # pipe.forward(x_joint) 
    # pipe.right(90) 
    # pipe.forward((y_joint-y_pipe)/2)
    # draw_pipe()
    # pipe.forward((y_joint-y_pipe)/2)
    # pipe.right(90) 
    # draw_joint()
    # pipe.forward((y_joint-y_pipe)/2) 
    # pipe.left(90)
    # pipe.forward(x_pipe)       
    # pipe.end_fill()
   
    # Command so that the program does not exist asa it finishes drawing
    ws = Screen()
    ws.exitonclick()

def water_project():
    """Find the perfect water color for the pipelines background by comparing different blues
    """
    screen_width = 500

    ws = Screen()
    ws.screensize(screen_width,screen_width)
    # ws.bgcolor('cornflowerblue')
    ws.bgpic('figures/0_0_map.gif')

    betty = Turtle()
    betty.speed(10) # Set the speed of the turtle
    betty.pensize(2) # Set the width of the objects drawn
    # betty.color('black')
    register_shape('figures/0_0_rocket.gif')
    betty.shape('figures/0_0_rocket.gif')

    # Bubbles
    num_bubbles = 10; 
    min_radius_bubbles = 10; max_radius_bubbles = 40
    drawing_limit = (screen_width-max_radius_bubbles)/2
    options = ['aquamarine','cyan','deepskyblue', 'skyblue', 'darkturquoise',\
        'darkcyan','steelblue1']
    for fill_color in options:
        betty.fillcolor(fill_color); betty.color(fill_color)
        for _ in range(num_bubbles):
            betty.penup()
            betty.goto(random.uniform(-drawing_limit, drawing_limit),random.uniform(-drawing_limit, drawing_limit))
            betty.pendown()
            betty.begin_fill()
            betty.circle(random.uniform(-min_radius_bubbles, max_radius_bubbles))
            betty.end_fill()

    ws.exitonclick()


#Run the desired project
# olympic_flag()
# pizza_project()
# pipeline()
water_project()