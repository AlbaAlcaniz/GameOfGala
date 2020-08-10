# This function creates the circuit of pipelines for the background of the game
# Please don't look at it. This is how I don't want to program
from turtle import Turtle, Screen

#Screen settings
ws = Screen()
screen_width = 490
number_lines = 7
square_width = screen_width/number_lines
ws.screensize(screen_width,screen_width)

# Some distances
x_joint = 10
y_joint = 25
x_pipe = 50
y_pipe = 10
ext_radius = 30
int_radius = ext_radius-y_pipe
square_size = x_pipe+2*x_joint
x_end_pipe = x_joint
radius_end_pipe = (square_size-2*(x_end_pipe+x_joint))/2
if square_size != square_width:
    print('Be careful! Geometry does not match')

def move_turtle(direction):
    """This function moves the turtle to the next square before drawing the new pipe
    Given the direction of movement, the turtle will move there.

    Args:
        direction (string): direction of movement of the turtle. Can be 'begin' or a cardinal point
    """
    if direction == 'begin':
        pipe.goto(-square_width*number_lines/2,square_width*number_lines/2)
    if direction == 'east':
        pipe.forward(square_width)
    if direction == 'west':
        pipe.right(180)
        pipe.forward(square_width)
        pipe.left(180)
    if direction == 'north':
        pipe.left(90)
        pipe.forward(square_width)
        pipe.right(90)
    if direction == 'south':
        pipe.right(90)
        pipe.forward(square_width)
        pipe.left(90)

def draw_pipe(direction):
    """Function that draws the pipe. The pipe can be an extreme (circle), a straight one or a bended one.
    Given the direction of the pipe, it will be drawn.

    Args:
        direction (string): direction of the pipe. It can be 'begin', 'end', 'horizontal', 'vertical', or
            two cardinal points separated by a -. The first cardinal must be west/east and the second north/south.
            Examples: 'east-north', 'west-south'
    """
    def draw_joint():
        """Auxiliar function to save some (small) space
        """
        pipe.forward(x_joint)
        pipe.right(90) 
        pipe.forward(y_joint) 
        pipe.right(90) 
        pipe.forward(x_joint) 
        pipe.right(90)

    def end_circuit_pipe():
        """Draw the extreme pipes, the ones that have circles on it.
        """
        pipe.forward(radius_end_pipe)
        pipe.left(90)        
        pipe.pendown()
        pipe.begin_fill()
        pipe.circle(radius_end_pipe)
        pipe.forward(y_pipe/2)
        pipe.right(90)
        pipe.forward(x_end_pipe)
        pipe.left(90)
        pipe.forward((y_joint-y_pipe)/2)
        pipe.right(90)
        draw_joint()
        pipe.forward(y_joint)
        pipe.forward(-y_pipe-(y_joint-y_pipe)/2)
        pipe.left(90)
        pipe.forward(x_end_pipe)
        pipe.end_fill()
        pipe.penup()
        pipe.right(90)
        pipe.forward(y_pipe/2)
        pipe.left(90)
        pipe.forward(radius_end_pipe)
        pipe.left(180)

    def straight_pipe():
        """Draw a straight pipe, that can be either vertical or horizontal
        """
        pipe.left(180)
        pipe.forward(square_width/2)
        pipe.right(90)
        pipe.forward(y_joint/2)
        pipe.right(90)
        pipe.begin_fill()
        pipe.pendown()
        draw_joint()
        pipe.forward(y_joint) 
        pipe.right(90) 
        pipe.forward(x_joint) 
        pipe.right(90) 
        pipe.forward((y_joint-y_pipe)/2)
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
        pipe.forward((y_joint-y_pipe)/2)
        pipe.right(90) 
        draw_joint()
        pipe.forward((y_joint-y_pipe)/2) 
        pipe.left(90)
        pipe.forward(x_pipe)       
        pipe.end_fill()
        pipe.penup()
        pipe.right(90)
        pipe.forward(y_pipe/2)
        pipe.right(90)
        pipe.forward(x_pipe/2)        

    def bended_pipe():
        """Draw a bended pipe linking two not-opposite cardinal points
        """
        pipe.right(180)
        pipe.forward(square_size/2)
        pipe.pendown()
        pipe.begin_fill()
        pipe.right(90)
        pipe.forward(y_joint/2)
        pipe.right(90)
        draw_joint()
        pipe.forward(y_joint) 
        pipe.right(90) 
        pipe.forward(x_joint) 
        pipe.right(90) 
        pipe.forward((y_joint-y_pipe)/2)
        pipe.right(90) 
        pipe.circle(ext_radius,-90)
        pipe.right(90)
        pipe.forward((y_joint-y_pipe)/2) 
        pipe.right(90) 
        draw_joint()
        pipe.forward(y_joint)
        pipe.right(180)
        pipe.forward((y_joint-y_pipe)/2+y_pipe)
        pipe.right(90) 
        pipe.circle(int_radius,90)
        pipe.right(90)
        pipe.end_fill()
        pipe.penup()
        pipe.forward(y_pipe/2)
        pipe.right(90)
        pipe.forward(ext_radius-y_pipe/2)

    if direction == 'begin':
        end_circuit_pipe()
    if direction == 'end':
        pipe.right(180)
        end_circuit_pipe()
        pipe.left(180)
    if direction == 'west-south':
        bended_pipe()
    if direction == 'west-north':
        pipe.right(90)
        bended_pipe()
        pipe.left(90)
    if direction == 'east-south':
        pipe.left(90)
        bended_pipe()
        pipe.right(90)
    if direction == 'east-north':
        pipe.left(180)
        bended_pipe()
        pipe.right(180)
    if direction == 'horizontal':
        straight_pipe()
    if direction == 'vertical':
        pipe.left(90)
        straight_pipe()
        pipe.right(90)

#Initialize the turtle
pipe = Turtle()
pipe.speed(0.05)
pipe.pensize(2)
pipe.color('black')
pipe.fillcolor('gray')
pipe.penup()

#Draw the circuit
move_turtle('begin')
draw_pipe('begin')
move_turtle('east')
draw_pipe('west-south')
move_turtle('south')
draw_pipe('west-north')
move_turtle('west')
draw_pipe('east-south')
move_turtle('south')
draw_pipe('east-north')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('west-north')
move_turtle('north')
draw_pipe('vertical')
move_turtle('north')
draw_pipe('east-south')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('west-south')
move_turtle('south')
draw_pipe('vertical')
move_turtle('south')
draw_pipe('west-north')
move_turtle('west')
draw_pipe('horizontal')
move_turtle('west')
draw_pipe('horizontal')
move_turtle('west')
draw_pipe('east-north')
move_turtle('north')
draw_pipe('east-south')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('west-south')
move_turtle('south')
draw_pipe('vertical')
move_turtle('south')
draw_pipe('east-north')
move_turtle('east')
draw_pipe('west-south')
move_turtle('south')
draw_pipe('vertical')
move_turtle('south')
draw_pipe('west-north')
move_turtle('west')
draw_pipe('east-north')
move_turtle('north')
draw_pipe('west-south')
move_turtle('west')
draw_pipe('horizontal')
move_turtle('west')
draw_pipe('horizontal')
move_turtle('west')
draw_pipe('east-north')
move_turtle('north')
draw_pipe('east-south')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('west-south')
move_turtle('south')
draw_pipe('vertical')
move_turtle('south')
draw_pipe('west-north')
move_turtle('west')
draw_pipe('horizontal')
move_turtle('west')
draw_pipe('horizontal')
move_turtle('west')
draw_pipe('east-north')
move_turtle('north')
draw_pipe('vertical')
move_turtle('north')
draw_pipe('west-south')
move_turtle('west')
draw_pipe('east-south')
move_turtle('south')
draw_pipe('vertical')
move_turtle('south')
draw_pipe('vertical')
move_turtle('south')
draw_pipe('east-north')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('horizontal')
move_turtle('east')
draw_pipe('end')

ws.exitonclick()