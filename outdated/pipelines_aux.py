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

def draw_pipe_aux(pipe, direction):
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

    def straight_pipe():
        """Draw a straight pipe, that can be either vertical or horizontal
        """
        pipe.left(180)
        pipe.forward(square_size/2)
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

    if direction == 'WS':
        bended_pipe()
    if direction == 'WN':
        pipe.right(90)
        bended_pipe()
        pipe.left(90)
    if direction == 'ES':
        pipe.left(90)
        bended_pipe()
        pipe.right(90)
    if direction == 'EN':
        pipe.left(180)
        bended_pipe()
        pipe.right(180)
    if direction == 'h':
        straight_pipe()
    if direction == 'v':
        pipe.left(90)
        straight_pipe()
        pipe.right(90)