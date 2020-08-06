from turtle import Turtle, Screen
from pipelines_aux import draw_pipe_aux
from math import floor, pi

class MovablePipe(Turtle):
    """Class which determines all the common characteristics of the pipes that can be moved (such as color,
    speed, etc). It is a child class of the Turtle class from the turtle module
    """
    def __init__(self,position,orientation,correct_orientation):
        """Initialize the movable pipes by setting different characteristics of the turtle

        Args:
            position (list): [x,y] list determining the position of the center of the pipe
            orientation (string): orientation of the pipe, which can be ES, EN, WS or WN, where W is west, N is north, etc
            correct_orientation (string): correct orientation of the pipe to complete the pipeline
        """
        super().__init__()
        self.ht()
        self.color('black')
        self.fillcolor('green')
        self.position = position
        self.speed(0)
        self.pensize(2)
        self.penup()
        self.goto(self.position)
        self.orientation = orientation
        self.correct_orientation = correct_orientation
        draw_pipe_aux(self,self.orientation)

    def turn_pipe(self):
        """Function that deletes the previous pipe and redraws it according to the new orientation given
        """
        self.clear()
        draw_pipe_aux(self,self.orientation)
    
class MovableBendedPipe(MovablePipe):
    """Class for all the pipes that are bended and can be moved. It is a child class of the just defined
    MovablePipe class
    """
    cardinal_points = {
        "WN" : 0,
        "EN" : pi/2,
        "ES" : pi,
        "WS" : 3*pi/2,
    }
    points_cardinal = {value:key for (key,value) in cardinal_points.items()}
    def __init__(self,position,orientation,correct_orientation):
        """Initialize the class with the same values as the child class (description of arguments can be found
        there) plus the orientation_angle, which is a number useful to determine the following orientation of the 
        pipe once it is clicked
        """
        super().__init__(position,orientation,correct_orientation)
        self.orientation_angle = self.cardinal_points[self.orientation]
        draw_pipe_aux(self,self.orientation)

    def change_orientation(self):
        """Change the orientation of the pipe and turn it after it has been clicked
        """
        self.orientation_angle += pi/2
        self.orientation_angle = self.orientation_angle - 2*pi*floor(self.orientation_angle/(2*pi))
        self.orientation = self.points_cardinal[self.orientation_angle]
        self.turn_pipe()

class MovableStraightPipe(MovablePipe):
    """Class for all the pipes that are straight and can be moved. It is a child class of the just defined
    MovablePipe class
    """
    def change_orientation(self):
        """Change the orientation of the pipe and turn it accordingly
        """
        if self.orientation == 'v':
            self.orientation = 'h'
        else:
            self.orientation = 'v'
        self.turn_pipe()

class Pipes:
    """Class which initializes the movable pipes and is the linkage between the previous classes and the user
    interaction
    """
    ########### GOOD ONES
    mov_bend_pipes_positions = [
        [-210,70],[-140,140],[-70,70],[210,70],[0,70],[140,140],[210,-140],[140,-70],[-70,-70],[70,0],
        [70,-140],[-140,0],[210,0],[-70,0]
        ]
    mov_bend_pipes_corr_orientations = ['EN', 'WN', 'WN', 'WN', 'EN', 'WS', 'WN', 'WS', 'EN', 'WS', 'WN', 'WS', 'WS', 'ES']
    mov_bend_pipes_orientations = ['WN','WS','ES','WS','WN','WN','WS','WS','ES','EN','WS','EN','WN','WN']
    ########### TEMPORARY ONES
    # mov_bend_pipes_positions = [[-210,70],[-140,140]]
    # mov_bend_pipes_corr_orientations = ['EN','WN']
    # mov_bend_pipes_orientations = ['WN','WS']

    ########### GOOD ONES
    mov_str_pipes_positions = [
        [-140,70],[140,210],[70,-210],[-70,-140],[-70,-210],[-140,-70],[-210,-70]
        ]
    mov_str_pipes_corr_orientations = ['h', 'h', 'h', 'h', 'h', 'v', 'v']
    mov_str_pipes_orientations = ['v','v','v','v','v','h','h']
    ########### TEMPORARY ONES
    # mov_str_pipes_positions = [[-140,70],[140,210]]
    # mov_str_pipes_corr_orientations = ['h', 'h']
    # mov_str_pipes_orientations = ['v','v']

    def __init__(self):
        """Initialize the class by creating the dictionaries which include the MovablePipe objects
        """
        self.d_bend, self.d_bend_corr = self.create_pipes_dictionary(self.mov_bend_pipes_positions, \
            self.mov_bend_pipes_orientations, self.mov_bend_pipes_corr_orientations, True)
        self.d_str, self.d_str_corr = self.create_pipes_dictionary(self.mov_str_pipes_positions, \
            self.mov_str_pipes_orientations, self.mov_str_pipes_corr_orientations, False)

    def create_pipes_dictionary(self,positions, orientations, correct_orientations, bended):
        """Create the dictionaries where the MovablePipe objects are stored and identified

        Args:
            positions (list): List with the position of all the pipes that can be moved
            orientations (list): List with the orientation of all the pipes that can be moved
            correct_orientations (list): List with the correct orientation of all the pipes that can be moved
            bended (bool): Variable which let us know if we are dealing with bended or straight pipes

        Returns:
            dic(dictionary): dictionary which stores and identifies all the pipe objects
            dic_corr(dictionary): dictionary which determines if all the pipe objects have the correct orientation
        """
        i = 0; dic = {}; dic_corr = {}
        for pos in positions:
            pipe_id = str(int(pos[0]))+'_'+str(int(pos[1]))
            if bended:
                dic[pipe_id] = MovableBendedPipe(positions[i],orientations[i], correct_orientations[i])
            else:
                dic[pipe_id] = MovableStraightPipe(positions[i],orientations[i], correct_orientations[i])
            if dic[pipe_id].correct_orientation == dic[pipe_id].orientation:
                dic_corr[pipe_id] = True
            else:
                dic_corr[pipe_id] = False
            i += 1
        return dic, dic_corr

    def redraw_clicked_pipe(self,x_pos,y_pos):
        """Once the player clicks somewhere on the screen, this function determines if the clicked position
        corresponds to one of the pipes that can be bended. Moreover, every time the screen is clicked, this function checks if all
        the movable pipes are in the correct position, in which case the game is quitted.

        Args:
            x_pos (float): x coordinate of the position clicked
            y_pos (float): y coordinate of the position clicked
        """
        global square_width, ws
        x_pipe = floor(x_pos/square_width+0.5)*square_width
        y_pipe = floor(y_pos/square_width+0.5)*square_width
        self.is_pipe_movable(x_pipe,y_pipe,self.mov_bend_pipes_positions,self.d_bend,self.d_bend_corr)
        self.is_pipe_movable(x_pipe,y_pipe,self.mov_str_pipes_positions,self.d_str,self.d_str_corr)

        if all(value == True for value in self.d_bend_corr.values()) and all(value == True for value in self.d_str_corr.values()):
            ws.bye()
    
    def is_pipe_movable(self,x_pipe,y_pipe,positions,dic,dic_corr):
        """Function that checks if the given coordinates correspond to one of the coordinates of the pipes.
        In affirmative case, the orientation of the pipe is changed and it is redrawn. It also checks if the
        new orientation is the correct one.

        Args:
            x_pipe (float): x coordinate of the position clicked centered around its square
            y_pipe (float): y coordinate of the position clicked centered around its square
            positions (list): List with the position of all the pipes that can be moved
            dic (dictionary): dictionary which stores and identifies all the pipe objects
            dic_corr(dictionary): dictionary which determines if all the pipe objects have the correct orientation
        """
        if [x_pipe,y_pipe] in positions:
            pipe_id = str(int(x_pipe))+'_'+str(int(y_pipe))
            m = dic[pipe_id]
            m.change_orientation()
            if m.orientation == m.correct_orientation:
                dic_corr[pipe_id] = True

def main_pipelines():
    """Main function for the pipelines game, where a pipeline circuit needs to be completed by changing the
    orientation of the green pipes.
    """
    global square_width, ws
    screen_width = 490
    number_lines = 7
    square_width = screen_width/number_lines

    ws = Screen()
    ws.screensize(screen_width,screen_width)
    ws.bgpic('figures/5_pipelines_background.PNG')
    
    p = Pipes()
    ws.onclick(p.redraw_clicked_pipe)
    ws.listen()
    ws.mainloop()

main_pipelines()