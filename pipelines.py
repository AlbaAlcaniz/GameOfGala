from turtle import Turtle, Screen

ws = Screen()

ws.bgpic('figures/5_pipelines_background.PNG')
screen_width = 490
number_lines = 7
square_width = screen_width/number_lines

pipe = Turtle()
pipe.speed(10)
pipe.pensize(2)
pipe.color('green')
pipe.fillcolor('green')
# pipe.penup()

def move_turtle(pipe_turtle,x_square, y_square):
    x_pos = (x_square-1/2)*square_width - screen_width/2
    y_pos = (y_square-1/2)*square_width + screen_width/2
    pipe_turtle.goto(x_pos,y_pos)

move_turtle(pipe,1,1)
# move_turtle(pipe,7,7)
# move_turtle(pipe,1,7)

class Pipeline:
    def __init__(self,turtle_speed = 2):
        self.turtle_speed = turtle_speed
        self.pipe = Turtle()
        self.pipe.speed(self.turtle_speed)
        self.pipe.pensize(2)
        self.pipe.color('black')
        self.pipe.fillcolor('gray')
        self.pipe.penup()

class DrawPipe(Pipeline):
    x_joint = 10
    y_joint = 25
    x_pipe = 50
    y_pipe = 10
    ext_radius = 35
    int_radius = ext_radius-y_pipe
    square_size = x_pipe+2*x_joint

    if square_size != square_width:
        print('BE CAREFUUUUUUUUUUL')

    def end_circuit_pipe(self):
        x_end_pipe = self.x_joint
        radius_end_pipe = self.square_size-2*(x_end_pipe+self.x_joint)
        self.pipe.circle(radius_end_pipe)
        self.pipe.forward(self.y_joint) 
        self.pipe.right(90) 
        self.pipe.forward(self.x_joint) 
        self.pipe.right(90)

class MoveTurtle(Pipeline):
    def move_to_center(self):
        self.pipe.goto(-square_width*3,square_width*3)

    def move_west(self):
        self.pipe.forward(square_width)

    def move_east(self):
        self.pipe.right(180)
        self.pipe.forward(square_width)

    def move_north(self):
        self.pipe.left(90)
        self.pipe.forward(square_width)

    def move_south(self):
        self.pipe.right(90)
        self.pipe.forward(square_width)


# def pipeline():
#     def draw_joint():
#         pipe.forward(x_joint)
#         pipe.right(90) 
#         pipe.forward(y_joint) 
#         pipe.right(90) 
#         pipe.forward(x_joint) 
#         pipe.right(90)

#     # Vertical/horizontal (uncomment next line) pipe
#     pipe.begin_fill()
#     draw_joint()
#     pipe.forward(y_joint) 
#     pipe.right(90) 
#     pipe.forward(x_joint) 
#     pipe.right(90) 
#     pipe.forward((y_joint-y_pipe)/2)
#     pipe.left(90) 
#     pipe.circle(int_radius,90)
#     pipe.left(90) 
#     pipe.forward((y_joint-y_pipe)/2) 
#     pipe.right(90) 
#     draw_joint()
#     pipe.forward(y_joint)
#     pipe.right(180)
#     pipe.forward((y_joint-y_pipe)/2+y_pipe)
#     pipe.left(90)
#     pipe.circle(ext_radius,-90)
#     pipe.end_fill()

#     def draw_pipe():
#         pipe.left(90) 
#         pipe.forward(x_pipe)
#         pipe.right(90) 
#         pipe.forward(y_pipe) 
#         pipe.right(90) 
#         pipe.forward(x_pipe) 
#         pipe.right(90)
#         pipe.forward(y_pipe) 
#         pipe.right(90) 
#         pipe.forward(x_pipe) 
#         pipe.left(90) 

    # Vertical/horizontal (uncomment next line) pipe
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
    # ws = Screen()


ws.exitonclick()