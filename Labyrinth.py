import pygame
import tkinter as tk
from tkinter import PhotoImage
from numpy import array
from futbolseries import MainTopLevel
import sys, os
from ctypes import windll


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Car:
    """Class for the car which moves along the labyrinth
    """
    def __init__(self, initial_pos, square_side):
        """Define the initial position and useful distances

        Args:
            initial_pos (tuple): Initial position of the car
            square_side(int): size of the square side from the labyrinth
        """
        self.pos = initial_pos
        self.dirnx = 0
        self.dirny = 1
        self.trail = [self.pos]
        self.car_color = (255,0,0)
        self.wheels_color = (25,25,25)
        self.radius = 4
        self.dis = square_side
        self.a = self.dis//4
        self.b = self.dis//2
        self.c = self.dis*3//4
        self.d = self.dis//8
        self.matrix = [
            'hiimjhimmjaiimc', 'dhjfdfhgfeiijej', 'hgeohgejdhijeig',
            'eijfejbfhghghij', 'higfhgfeghgagho', 'fhigejkchliiigf',
            'fdhmjegbfhchijf', 'eigfeiigfkigalg', 'hiighjhigeijhmj',
            'ejhigeghimjffff', 'hgfhiijdbdelgff', 'kjffbhghohiiigf',
            'ffegkghgfeichio','feijejfbeijhgag','eiceilgeiigeiii'
            ]

    def move(self, event):
        """Move the car considering the key clicked and the labyrinth walls.
        Each position has an assigned letter which indicates the movements that
        the car can do. These movements are limited by the walls of the 
        labyrinth.
        """
        letter_pos = self.matrix[self.pos[1]][self.pos[0]]

        if event.key == pygame.K_LEFT and letter_pos in 'gilimocj':
            self.dirnx = -1; self.dirny = 0
            self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        elif event.key == pygame.K_RIGHT and letter_pos in 'kalmehi':
            self.dirnx = 1; self.dirny = 0
            self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        elif event.key == pygame.K_UP and letter_pos in 'delfgko':
            self.dirnx = 0; self.dirny = -1
            self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        elif event.key == pygame.K_DOWN and letter_pos in 'bfhjmko':
            self.dirnx = 0; self.dirny = 1
            self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
        else:
            pass
            
    def draw_car(self, surface):
        """Draw the car as a polygon with two grey circles as wheels

        Args:
            surface (pygame.Surface): window where the car will be displayed
        """        
        i = self.pos[0]
        j = self.pos[1]
        x_m = i*self.dis
        y_m = self.dis*(j+1)
        x_M = x_m + self.dis
        centre1 = (x_m+8,y_m-self.a)
        centre2 = (x_M-8,y_m-self.a)
        
        pygame.draw.polygon(surface, self.car_color, [
            (x_m,y_m-self.a), (x_M,y_m-self.a), (x_M,y_m-self.b), \
            (x_M-self.d,y_m-self.b), (x_M-self.a,y_m-self.c), \
            (x_m+self.a,y_m-self.c), (x_m+self.d,y_m-self.b), (x_m,y_m-self.b)
            ])        
        pygame.draw.circle(surface, self.wheels_color, centre1, self.radius)
        pygame.draw.circle(surface, self.wheels_color, centre2, self.radius)
    
    def draw_trail(self, surface):
        """Draw the trail left by the car so that the collection of letters is 
        easier. For every movement of the car, its position is added to the 
        trail. A grey line is drawn connecting all the positions in which the
        car has been.

        Args:
            surface (pygame.Surface): window where the trail is displayed
        """        
        self.trail.append(self.pos)

        if len(self.trail) > 1:
            aux = self.dis*(array(self.trail) + 1/2)
            aux = aux.astype(int)
            for i in range(len(aux)-1):
                pygame.draw.line(surface, (175,175,175), aux[i], aux[i+1], 3)


class Window:
    """Class that contains all the properties and related functions to the game
    window.
    """
    def __init__(self, width, square_side):
        """Initialize the window by generating it and defining colors and
        useful parameters of the objects drawn.
        The first lines are attributes so that the pygame window is always on
        top.

        Args:
            width (int): width of the game window
            square_side (int): width of the squares of the labyrinth
        """
        self.win = pygame.display.set_mode((width, width))
        SetWindowPos = windll.user32.SetWindowPos
        SetWindowPos(pygame.display.get_wm_info()['window'], -1, 100, 100, 0, \
            0, 0x0001)
        self.color_background = (255,255,255)
        self.color_lines = (0,0,0)
        self.color_arrows = (0,0,255)
        self.color_letters = (0,255,0)
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)
        self.message = 'MAIGBDOSTFCGICALXEU'
        self.letters_pos = array([
            (1.5,3.5),(3.5,5.5),(3.5,8.5),(0.5,13),(5.5,7.5),(6.5,10.5),
            (6.5,3.5),(8.5,0.5),(13.5,0.5),(14.5,3.5),(9.5,3.5),(9.5,6.5),
            (8.5,8.5),(13.5,6.5),(14.5,8.5),(13.5,10.5),(10.5,14.5),(2.5,13.5),
            (7.5,12.5)
            ])*square_side
        self.letters_pos = self.letters_pos.astype(int)
        self.mat_x = [
            [0,0,15,0],[1,1,3,1],[0,2,1,2],[6,1,7,1],[10,1,13,1],[14,1,15,1],
            [4,2,5,2],[7,2,8,2],[9,2,12,2],[13,2,14,2],[1,3,3,3],[5,3,7,3],
            [8,3,9,3],[10,3,11,3],[12,3,15,3],[0,4,2,4],[4,4,5,4],[9,4,10,4],
            [11,4,12,4],[13,4,14,4],[1,5,3,5],[5,5,6,5],[7,5,9,5],[10,5,13,5],
            [2,6,5,6],[7,6,8,6],[9,6,14,6],[1,7,2,7],[5,7,7,7],[10,7,11,7],
            [12,7,13,7],[0,8,3,8],[4,8,8,8],[10,8,15,8],[1,9,4,9],[7,9,11,9],
            [0,10,1,10],[3,10,7,10],[8,10,9,10],[1,11,2,11],[4,11,6,11],
            [7,11,8,11],[9,11,13,11],[6,12,7,12],[10,12,14,12],[2,13,4,13],
            [5,13,6,13],[7,13,8,13],[9,13,12,13],[13,13,14,13],[1,14,3,14],
            [4,14,5,14],[8,14,10,14],[12,14,15,14],[0,15,15,15]
        ]
        self.mat_x = array(self.mat_x)*square_side
        self.mat_y = [
            [0,1,0,15],[1,1,1,2],[1,5,1,7],[1,12,1,14],[2,2,2,3],[2,6,2,7],
            [2,9,2,13],[3,1,3,2],[3,3,3,5],[3,7,3,8],[3,10,3,12],[3,14,3,15],
            [4,1,4,6],[4,7,4,9],[4,11,4,14],[5,0,5,2],[5,6,5,7],[5,9,5,10],
            [5,11,5,12],[6,1,6,6],[6,8,6,9],[6,12,6,14],[7,3,7,5],[7,6,7,7],
            [7,9,7,12],[7,13,7,15],[8,1,8,4],[8,5,8,8],[8,10,8,11],[8,12,8,14],
            [9,1,9,3],[9,4,9,5],[9,6,9,9],[9,10,9,13],[10,0,10,1],[10,3,10,4],
            [10,10,10,11],[11,4,11,5],[11,6,11,7],[11,9,11,10],[11,13,11,15],
            [12,2,12,4],[12,7,12,10],[12,12,12,13],[13,1,13,2],[13,4,13,5],
            [13,9,13,11],[13,13,13,14],[14,5,14,7],[14,9,14,12],[15,0,15,14]
        ]
        self.mat_y = array(self.mat_y)*square_side
        self.border_pos = array([15,0,1,14])*square_side
        self.arrow1 = tuple(array([[0.15,0.5],[0.75,0.5],[0.5,0.25],\
            [0.5,0.75],[0.75,0.5]])*square_side)
        self.arrow2 = tuple(array([[14.15,14.5],[14.75,14.5],[14.5,14.25],\
            [14.5,14.75],[14.75,14.5]])*square_side)

    def display_letters(self):
        """Display the letters along the labyrinth.
        """
        i = 0
        for l in self.message:
            text = self.font.render(l, True, self.color_letters, \
                self.color_background)
            textRect = text.get_rect()
            textRect.center = self.letters_pos[i]
            self.win.blit(text, textRect)
            i += 1

    def draw_labyrinth(self):
        """Draw the lines of the labyrinth by defining the initial and 
        final points in a series of arrays. One array includes all the vertical
        lines while the second one includes all horizontal ones.
        """
        for i in range(len(self.mat_x)):
            pygame.draw.line(self.win, self.color_lines, \
                (self.mat_x[i][0], self.mat_x[i][1]), \
                (self.mat_x[i][2],self.mat_x[i][3]), 3)
        for i in range(len(self.mat_y)):
            pygame.draw.line(self.win, self.color_lines, \
                (self.mat_y[i][0], self.mat_y[i][1]), \
                (self.mat_y[i][2],self.mat_y[i][3]), 3)
    
    def draw_arrows(self):
        """Draw the initial and final arrows indicating the entrances to the
        labyrinth.
        """
        pygame.draw.polygon(self.win, self.color_arrows, self.arrow1)
        pygame.draw.polygon(self.win, self.color_arrows, self.arrow1,2)
        pygame.draw.polygon(self.win, self.color_arrows, self.arrow2)
        pygame.draw.polygon(self.win, self.color_arrows, self.arrow2,2)

    def redraw_window(self, car):
        """Redraw the elements of the pygame window every frame.

        Args:
            car (labyrinth.Car): car object
        """        
        self.win.fill(self.color_background)
        car.draw_trail(self.win)
        self.display_letters()
        self.draw_arrows()
        car.draw_car(self.win)
        self.draw_labyrinth()
        pygame.display.update()


def won_game(master, win):
    """When the game is won, a tkinter window appears asking for the words
    found on the way.

    Args:
        master (tkinter.Tk): window of the general game.
    """
    top_labyrinth = MainTopLevel(master,'MIEDICA', pygame_win=True)
    img = PhotoImage(file=resource_path('figures/4_2_question.png'))
    img_next = PhotoImage(file=resource_path('figures/0_0_next.png'))

    top_labyrinth.display_image(img,[0,0,2,1])
    top_labyrinth.create_text_box([1,0,1,1], 28)
    top_labyrinth.create_next_button(img_next,[1,1])

    top_labyrinth.top.mainloop()


def main_labyrinth(master):
    """Main function for the labyrinth game. You have a car and need to take it
    to the end of the labyrinth, indicated by the arrows.
    """
    width = 450; rows = 15
    square_side = width//rows

    pygame.init()
    pygame.display.set_caption('Get the grandpas out of the labyrinth!')

    win = Window(width, square_side)
    car = Car((0,0),square_side)

    running = True
    win.redraw_window(car)
    while running:
        events = pygame.event.get()
        for e in events:
            if e.type == pygame.QUIT:
                quit()
            if e.type == pygame.KEYDOWN:
                car.move(e)
                win.redraw_window(car)

        if car.pos == (14,14):
            won_game(master, win)
            running = False
            pygame.display.quit()