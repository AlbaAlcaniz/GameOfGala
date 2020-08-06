from turtle import Turtle, Screen
from pipelines_aux import draw_pipe_aux
from math import ceil, floor, pi, cos, sin
import tkinter

screen_width = 490
number_lines = 7
square_width = screen_width/number_lines

ws = Screen()
ws.screensize(screen_width,screen_width)
ws.bgpic('figures/5_pipelines_background.PNG')
    
class MovableBendedPipe(Turtle):
    cardinal_points = {
        "WN" : 0,
        "EN" : pi/2,
        "ES" : pi,
        "WS" : 3*pi/2,
    }
    # points_cardinal = {cardinal_points[x]: x for x in cardinal_points}
    def __init__(self,position,orientation,correct_orientation):
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
        self.cardinal2number()
        draw_pipe_aux(self,self.orientation)

    def turn_pipe(self):
        self.orientation_angle += pi/2
        self.number2cardinal()
        self.clear()
        draw_pipe_aux(self,self.orientation)

    def cardinal2number(self):
        self.orientation_angle = self.cardinal_points[self.orientation]

    def number2cardinal(self):
        self.orientation_angle = self.orientation_angle - 2*pi*floor(self.orientation_angle/(2*pi))
        for orient, orient_angle in self.cardinal_points.items():
            if self.orientation_angle == orient_angle:
                self.orientation = orient

class MovableStraightPipe(Turtle):
    def __init__(self,position,orientation,correct_orientation):
        super().__init__()
        self.ht()
        self.color('black')
        self.fillcolor('green')
        self.position = position
        self.speed(0.01)
        self.pensize(2)
        self.penup()
        self.goto(self.position)
        self.orientation = orientation
        self.correct_orientation = correct_orientation
        draw_pipe_aux(self,self.orientation)

    def turn_pipe(self):
        if self.orientation == 'v':
            self.orientation = 'h'
        else:
            self.orientation = 'v'
        self.clear()
        draw_pipe_aux(self,self.orientation)

def move_turtle(pipe_turtle,x_square, y_square):
    x_pos = (x_square-1/2)*square_width - screen_width/2
    y_pos = screen_width/2 - (y_square-1/2)*square_width
    pipe_turtle.goto(x_pos,y_pos)

########### GOOD ONES
# mov_bend_pipes_positions = [
#     [-210,70],[-140,140],[-70,70],[210,70],[0,70],[140,140],[210,-140],[140,-70],[-70,-70],[70,0],
#     [70,-140],[-140,0],[210,0],[-70,0]
#     ]
# mov_bend_pipes_corr_orientations = ['EN', 'WN', 'WN', 'WN', 'EN', 'WS', 'WN', 'WS', 'EN', 'WS', 'WN', 'WS', 'WS', 'ES']
# mov_bend_pipes_orientations = ['WN','WS','ES','WS','WN','WN','WS','WS','ES','EN','WS','EN','WN','WN']
########### TEMPORARY ONES
mov_bend_pipes_positions = [[-210,70],[-140,140]]
mov_bend_pipes_corr_orientations = ['EN','WN']
mov_bend_pipes_orientations = ['WN','WS']

i = 0; mov_bend_pipes_id = []
for pos in mov_bend_pipes_positions:
    mov_bend_pipes_id.append(str(int(pos[0]))+'_'+str(int(pos[1])))

i = 0; d_bend = {}; d_bend_corr = {}
for pipe_id in mov_bend_pipes_id:
    d_bend[pipe_id] = MovableBendedPipe(mov_bend_pipes_positions[i],mov_bend_pipes_orientations[i],\
        mov_bend_pipes_corr_orientations[i])
    if d_bend[pipe_id].correct_orientation == d_bend[pipe_id].orientation:
        d_bend_corr[pipe_id] = True
    else:
        d_bend_corr[pipe_id] = False
    i += 1

########### GOOD ONES
# mov_str_pipes_positions = [
#     [-140,70],[140,210],[70,-210],[-70,-140],[-70,-210],[-140,-70],[-210,-70]
#     ]
# mov_str_pipes_corr_orientations = ['h', 'h', 'h', 'h', 'h', 'v', 'v']
# mov_str_pipes_orientations = ['v','v','v','v','v','h','h']
########### TEMPORARY ONES
mov_str_pipes_positions = [[-140,70],[140,210]]
mov_str_pipes_corr_orientations = ['h', 'h']
mov_str_pipes_orientations = ['v','v']

i = 0; mov_str_pipes_id = []
for pos in mov_str_pipes_positions:
    mov_str_pipes_id.append(str(int(pos[0]))+'_'+str(int(pos[1])))

i = 0; d_str = {}; d_str_corr = {}
for pipe_id in mov_str_pipes_id:
    d_str[pipe_id] = MovableStraightPipe(mov_str_pipes_positions[i],mov_str_pipes_orientations[i],\
        mov_str_pipes_corr_orientations[i])
    if d_str[pipe_id].correct_orientation == d_str[pipe_id].orientation:
        d_str_corr[pipe_id] = True
    else:
        d_str_corr[pipe_id] = False
    i += 1

def redraw_clicked_pipe(x_pos,y_pos):
    x_pipe = floor(x_pos/square_width+0.5)*square_width
    y_pipe = floor(y_pos/square_width+0.5)*square_width
    if [x_pipe,y_pipe] in mov_bend_pipes_positions:
        pipe_id = str(int(x_pipe))+'_'+str(int(y_pipe))
        m = d_bend[pipe_id]
        m.turn_pipe()
        if m.orientation == m.correct_orientation:
            d_bend_corr[pipe_id] = True

    if [x_pipe,y_pipe] in mov_str_pipes_positions:
        pipe_id = str(int(x_pipe))+'_'+str(int(y_pipe))
        m = d_str[pipe_id]
        m.turn_pipe()
        if m.orientation == m.correct_orientation:
            d_str_corr[pipe_id] = True

    if all(value == True for value in d_bend_corr.values()) and all(value == True for value in d_str_corr.values()):
        ws.bye()

ws.onclick(redraw_clicked_pipe)
ws.listen()
ws.mainloop()