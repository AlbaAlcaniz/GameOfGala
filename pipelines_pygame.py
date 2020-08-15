import pygame
import numpy as np
from math import pi


def draw_bended_pipe(surface,orientation='WS'):
    pos_x = 315
    pos = [pos_x,pos_x]
    pos += [0,0]
    x_joint = 10
    y_joint = 25
    x_pipe = 50
    y_pipe = 10
    square_width = x_pipe + x_joint*2
    pipe_color = (0,200,0)
    border_color = (0,0,0)
    cardinals = 'NSEW'
    joints = np.array([
        (-y_joint/2,-x_pipe/2,y_joint,-x_joint), #N
        (-y_joint/2,square_width/2,y_joint,-x_joint), #S
        (x_pipe/2,y_joint/2,x_joint,-y_joint), #E
        (-square_width/2,y_joint/2,x_joint,-y_joint), #W
    ])
    joints += np.array(pos)
    joints = joints.astype(int)

    bend = np.array([
        (-60,-5,65,65) #WS
    ])
    bend += np.array(pos)
    bend = bend.astype(int)

    for i in orientation:
        card_index = cardinals.index(i)
        pygame.draw.rect(surface,pipe_color,joints[card_index])
        pygame.draw.rect(surface,border_color,joints[card_index],2)

    pygame.draw.arc(surface,(200,0,0),bend[0],0,pi/2,10)


class MovablePipe():

    def __init__(self,pos,orientation,correct_orientation):
        """Initialize the movable pipes by setting different characteristics of the turtle

        Args:
            position (list): [x,y] list determining the position of the center of the pipe
            orientation (string): orientation of the pipe, which can be ES, EN, WS or WN, where W is west, N is north, etc
            correct_orientation (string): correct orientation of the pipe to complete the pipeline
        """
        x_joint = 10
        y_joint = 25
        x_pipe = 50
        y_pipe = 10
        self.square_width = x_pipe + x_joint*2
        self.pipe_color = (0,200,0)
        self.border_color = (0,0,0)
        self.points_str = np.array([
            [-x_pipe/2-x_joint,-y_joint/2], [-x_pipe/2,-y_joint/2], 
            [-x_pipe/2,-y_pipe/2], [x_pipe/2,-y_pipe/2], [x_pipe/2,-y_joint/2],
            [x_pipe/2+x_joint,-y_joint/2], [x_pipe/2+x_joint,y_joint/2], 
            [x_pipe/2,y_joint/2], [x_pipe/2,y_pipe/2], [-x_pipe/2,y_pipe/2], 
            [-x_pipe/2,y_joint/2], [-x_pipe/2-x_joint,y_joint/2]
        ])
        self.abs_pos = np.array(pos)*self.square_width + self.square_width/2 - 1
        self.orientation = orientation
        self.correct_orientation = correct_orientation

    def draw_pipe(self, surface):
        if self.orientation == 'h':
            hor_points = np.array(self.points_str)
            self.draw_str_pipe(surface, hor_points)
        elif self.orientation == 'v':
            ver_points = np.zeros(self.points_str.shape)
            ver_points[:,0] = self.points_str[:,1]
            ver_points[:,1] = self.points_str[:,0]
            self.draw_str_pipe(surface, ver_points)
        else:
            pass

    def turn_pipe(self):
        """Function that deletes the previous pipe and redraws it according to the new orientation given
        """
        self.clear()
        self.draw_pipe(self,self.orientation)
    
    def draw_str_pipe(self, surface, points):
        points += self.abs_pos
        points = points.astype(int)
        pygame.draw.polygon(surface,self.pipe_color,points)
        pygame.draw.polygon(surface,self.border_color,points,2)
    
class MovableBendedPipe(MovablePipe):
    """Class for all the pipes that are bended and can be moved. It is a child class of the just defined
    MovablePipe class
    """
    cardinal_points = {
        'WN' : 0,
        'EN' : pi/2,
        'ES' : pi,
        'WS' : 3*pi/2,
    }
    points_cardinal = {value:key for (key,value) in cardinal_points.items()}

    def __init__(self,position,orientation,correct_orientation):
        """Initialize the class with the same values as the child class (description of arguments can be found
        there) plus the orientation_angle, which is a number useful to determine the following orientation of the 
        pipe once it is clicked
        """
        super().__init__(position,orientation,correct_orientation)
        self.orientation_angle = self.cardinal_points[self.orientation]
        self.draw_pipe(self,self.orientation)

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
    mov_str_pipes_positions = [
    [5,0],[4,6],[1,2],[2,5],[2,6],[1,4],[0,4]
    ]
    mov_str_pipes_corr_orientations = ['h','h','h','h','h','v','v']
    mov_str_pipes_orientations = ['v','v','v','v','v','h','h']
    # mov_str_pipes_positions = [[1,4],[5,6]]
    # mov_str_pipes_corr_orientations = ['h','h']
    # mov_str_pipes_orientations = ['v','v']

    def __init__(self):
        self.d_str,self.d_str_corr = self.create_pipes_dictionary(self.mov_str_pipes_positions, \
                                                                self.mov_str_pipes_orientations, 
                                                                self.mov_str_pipes_corr_orientations, False)

    def create_pipes_dictionary(self, positions, orientations, correct_orientations, bended):
        i = 0; dic = {}; dic_corr = {}
        for pos in positions:
            pipe_id = str(int(pos[0])) + '_' + str(int(pos[1]))
            # if bended:
            #     dic[pipe_id] = MovableBendedPipe(positions[i],orientations[i],correct_orientations[i])
            # else:
            dic[pipe_id] = MovableStraightPipe(positions[i],orientations[i],correct_orientations[i])
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

        if all(value == True for value in self.d_bend_corr.values()) and \
                all(value == True for value in self.d_str_corr.values()):
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

class Pipe:
    def __init__(self):
        x_joint = 10
        y_joint = 25
        x_pipe = 50
        y_pipe = 10
        self.square_width = x_pipe + x_joint*2
        self.pipe_color = (0,200,0)
        self.border_color = (0,0,0)
        self.points_str = np.array([
            [-x_pipe/2-x_joint,-y_joint/2], [-x_pipe/2,-y_joint/2], 
            [-x_pipe/2,-y_pipe/2], [x_pipe/2,-y_pipe/2], [x_pipe/2,-y_joint/2],
            [x_pipe/2+x_joint,-y_joint/2], [x_pipe/2+x_joint,y_joint/2], 
            [x_pipe/2,y_joint/2], [x_pipe/2,y_pipe/2], [-x_pipe/2,y_pipe/2], 
            [-x_pipe/2,y_joint/2], [-x_pipe/2-x_joint,y_joint/2]
        ])
        self.create_pipes_dictionary()

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
            pipe_id = str(int(pos[0])) + '_' + str(int(pos[1]))
            if bended:
                dic[pipe_id] = MovableBendedPipe(positions[i],orientations[i],correct_orientations[i])
            else:
                dic[pipe_id] = MovableStraightPipe(positions[i],orientations[i],correct_orientations[i])
            if dic[pipe_id].correct_orientation == dic[pipe_id].orientation:
                dic_corr[pipe_id] = True
            else:
                dic_corr[pipe_id] = False
            i += 1
        return dic, dic_corr

class MainScreen():
    def __init__(self, screen_size):
        self.screen = pygame.display.set_mode(screen_size, pygame.RESIZABLE, \
            0, 32)
        self.bg_img = pygame.image.load('figures/6_2_pipelines_background.png')
        self.bg_img2 = pygame.image.load('figures/6_2_pipelines_background2.png')

    def initial_setup(self, pipe_dict):
        pygame.display.update()
        self.screen.blit(self.bg_img, (0,0))
        draw_bended_pipe(self.screen)
        # for pipe in pipe_dict.values():
        #     pipe.draw_pipe(self.screen)

    def new_configuration(self):
        pygame.display.set_mode([640,616],pygame.RESIZABLE,0,32)
        self.text = ''
        self.font = pygame.font.SysFont('calibri',48)
        self.text_color = (0,0,0)
        self.img_text = self.font.render(self.text, True, self.text_color)

        self.rect = self.img_text.get_rect()
        self.rect.topleft = (20, 550)
        self.cursor = pygame.Rect(self.rect.topright, (3, self.rect.height))

    def modify_text(self,event):
        if event.key == pygame.K_BACKSPACE:
            if len(self.text)>0:
                self.text = self.text[:-1]
        else:
            self.text += event.unicode

        self.img_text = self.font.render(self.text, True, self.text_color)
        self.rect.size=self.img_text.get_size()
        self.cursor.topleft = self.rect.topright

    def new_setup(self):
        self.screen.blit(self.bg_img2, (0,0))
        self.screen.blit(self.img_text, self.rect)
        if time.time() % 1 > 0.5:
            pygame.draw.rect(self.screen, self.text_color, self.cursor)
        pygame.display.update()

def main_pipelines():
    screen_width = 490

    pygame.init()
    screen = MainScreen([screen_width,screen_width])
    p = Pipes()

    while True:
        e = pygame.event.wait()
        if e.type == pygame.MOUSEBUTTONDOWN:
            break
        if e.type == pygame.QUIT:
            quit()
        screen.initial_setup(p.d_str)

    # ws.onclick(p.redraw_clicked_pipe)
    # ws.listen()
    # ws.mainloop()

    # game = True
    # while game:
    #     e = pygame.event.wait()
    #     if e.type == pygame.QUIT:
    #         quit()
    #     if e.type == pygame.MOUSEBUTTONDOWN:
    #         deck_cards.identify_card(screen)
    #         screen.initial_setup(card_dict)

    #     if len(card_dict) == 0:
    #         game = False
            
    # screen.new_configuration()

    # running = True
    # while running:
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             running = False
            
    #         if event.type == pygame.KEYDOWN:
    #             screen.modify_text(event)
    #     screen.new_setup()

    #     if screen.text.upper() == 'FERNAN':
    #         running = False
    #         pygame.quit()


main_pipelines()

