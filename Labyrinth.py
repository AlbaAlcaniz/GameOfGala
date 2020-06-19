import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
from numpy import array

# Explanation of the game
class Explanation:

    def __init__(self, master):
        master.attributes('-topmost', True)
        # Export image
        img1 = ImageTk.PhotoImage(image = Image.open("figures/1_valencia.png"))
        panel = tk.Label(master, image = img1)
        panel.img1 = img1        
        panel.pack()

        # "Next" button
        img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        # Define the space for the button
        f = tk.Frame(master, height=50, width=50)
        f.pack_propagate(0)
        f.pack(side = "right")
        # Create button
        self.button = tk.Button(f, image = img2, command=f.quit)
        self.button.img2 = img2
        self.button.pack(expand=1)
        
        master.mainloop()

# Class for drawing of the car
class vehicle(object):
    width = 450    
    rows = 15
    def __init__(self, start, dirnx = 1, dirny = 0):
        self.pos = start
        self.dirnx = 1
        self.dirny = 0

    def move(self, dirnx, dirny):
        self.dirnx = dirnx
        self.dirny = dirny
        self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

    def draw_vehicle(self, surface):
        dis = self.width // self.rows
        i = self.pos[0] #row
        j = self.pos[1] #column
        color = (255,0,0)

        # Define useful distances
        x_m = i*dis; y_m = j*dis+dis; x_M = x_m + dis
        a = dis/4; b = int(2*a); c = 3*a; d = a/2
        a = int(a); c = int(c); d = int(d); e = a
        
        # Draw the car        
        pygame.draw.polygon(surface, color, [(x_m,y_m-a), (x_M,y_m-a), (x_M,y_m-b), (x_M-d,y_m-b), (x_M-e,y_m-c), (x_m+e,y_m-c), \
            (x_m+d,y_m-b), (x_m,y_m-b)])

        # Draw the wheels
        centre1 = (int(x_m+8),int(y_m-a))
        centre2 = (int(x_M-8),int(y_m-a))
        radius = 4
        pygame.draw.circle(surface, (25,25,25), centre1, radius)
        pygame.draw.circle(surface, (25,25,25), centre2, radius)

# Class for the movement of the car
class car(object):
    width = 450    
    rows = 15
    def __init__(self, pos):
        self.head = vehicle(pos)
        # Direction for x and y
        self.dirnx = 0
        self.dirny = 1
        self.trail = [pos]

    def move(self):
        # Take the car
        c = self.head
        # Take the position of the car
        p = c.pos
        # Each position has an assigned letter which indicates the movements that the car can do
        matrix = ["hiimjhimmjaiimc","dhjfdfhgfeiijej","hgeohgejdhijeig", "eijfejbfhghghij", "higfhgfeghgagho", \
            "fhigejkijeiiigf","fdhmjegbfhchijf","eigfeiigfkigalg","hiighjhigeijhmj","ejhigeghimjffff","hgfhiijdbdelgff",\
                "kjffbhghohiiigf","ffegkghgfeichio","feijejfbeijhgag","eiceilgeiigeiii"]
        letter_pos = matrix[p[1]][p[0]]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and letter_pos in "gilimocj":
                c.move(-1,0)

            elif keys[pygame.K_RIGHT] and letter_pos in "kalmehi":
                c.move(1,0)

            elif keys[pygame.K_UP] and letter_pos in "delfgko":
                c.move(0,-1)

            elif keys[pygame.K_DOWN] and letter_pos in "bfhjmko":
                c.move(0,1)
            
    def draw_car(self, surface):
        c = self.head
        c.draw_vehicle(surface)
    
    def draw_trail(self, surface):
        dis = self.width // self.rows
        if self.head.pos not in self.trail:
            self.trail.append(self.head.pos)
        if len(self.trail) > 1:
            a = array(self.trail)*dis+dis/2
            a = a.astype(int)
            for i in range(len(a)-1):
                pygame.draw.line(surface, (175,175,175), a[i], a[i+1], 3)

class letter(object):
    def __init__(self):
        self.message = 'MAIGBIOSTFCGDCALXEU'
        self.pos = array([(1.5,2.5),(3.5,5.5),(0.5,8.5),(0.5,13),(5.5,7.5),(5.5,1.5),(6.5,3.5),(8.5,0.5),(13.5,0.5),\
            (14.5,3.5),(10.5,4.5),(9.5,6.5),(8.5,8.5),(9.5,9.5),(14.5,8.5),(13.5,10.5),(10.5,14.5),(6.5,10.5),(7.5,12.5)])
        width = 450
        rows = 15
        dis = width // rows
        self.pos = array(self.pos)*dis
        self.pos = self.pos.astype(int)
        pygame.font.init()
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def display_letter(self,surface):
        i = 0
        for l in self.message:
            text = self.font.render(l, True, (0,255,0), (255,255,255))
            textRect = text.get_rect()
            textRect.center = self.pos[i]
            surface.blit(text, textRect)
            i += 1

# Function when the car has reached to the end
def won_game():
    # Create the main window
    # win = pygame.display.set_mode((500,500))
    # background = pygame.Surface((win.get_size()))
    # background.fill((255, 255, 255))
    # image = pygame.image.load("figures/1_labyrinth.png")

    # image = image.convert()
    # rect = image.get_rect()
    # win.blit(image, rect)

    #Make sure that the window appears on top
    root = tk.Tk()
    root.attributes('-topmost', True)

    # Export image: I need your help
    img1 = ImageTk.PhotoImage(image = Image.open("figures/0_ayuda.png"))
    panel = tk.Label(root, image = img1)
    panel.pack()
    # root.withdraw()

    # for event in pygame.event.get():
    #     keys = pygame.key.get_pressed()
    #     if keys[pygame.K_LEFT]:
    #         print('Gotcha!')
    root.mainloop()
    
    # content = 'You lost. Your score was '
    # MsgBox = messagebox.askquestion (content,'Play again?')
    # if MsgBox == 'yes':
    #     root.destroy()
    #     # walls, rot_apple_on, pois_apple_on = s.reset((10,10))
    #     # return walls, rot_apple_on, pois_apple_on
    # else:
    #     exit()



def drawLabyrinth(width, rows, surface):
    # How big each square is
    size_between = width // rows
    
    color_lines = (0,0,0)
    # Define the horizontal lines of the labyrinth
    mat_x = [[0,0,15,0],[1,1,3,1],[0,2,1,2],[6,1,7,1],[10,1,13,1],[14,1,15,1],[4,2,5,2],[7,2,8,2],[9,2,12,2],[13,2,14,2],\
        [1,3,3,3],[5,3,7,3],[8,3,9,3],[10,3,11,3],[12,3,15,3],[0,4,2,4],[4,4,5,4],[9,4,10,4],[11,4,12,4],[13,4,14,4],\
            [1,5,3,5],[5,5,6,5],[7,5,9,5],[10,5,13,5],[2,6,5,6],[7,6,8,6],[9,6,14,6],[1,7,2,7],[5,7,7,7],[10,7,11,7],\
                [12,7,13,7],[0,8,3,8],[4,8,8,8],[10,8,15,8],[1,9,4,9],[7,9,11,9],[0,10,1,10],[3,10,7,10],[8,10,9,10],\
                    [1,11,2,11],[4,11,6,11],[7,11,8,11],[9,11,13,11],[6,12,7,12],[10,12,14,12],[2,13,4,13],[5,13,6,13],\
                        [7,13,8,13],[9,13,12,13],[13,13,14,13],[1,14,3,14],[4,14,5,14],[8,14,10,14],[12,14,15,14],[0,15,15,15]]
    mat_x = array(mat_x)
    mat_x = mat_x*size_between
    # Define the vertical lines of the labyrinth
    mat_y = [[0,1,0,15],[1,1,1,2],[1,5,1,7],[1,12,1,14],[2,2,2,3],[2,6,2,7],[2,9,2,13],[3,1,3,2],[3,3,3,5],[3,7,3,8],\
        [3,10,3,12],[3,14,3,15],[4,1,4,6],[4,7,4,9],[4,11,4,14],[5,0,5,2],[5,6,5,7],[5,9,5,10],[5,11,5,12],[6,1,6,6],\
            [6,8,6,9],[6,12,6,14],[7,3,7,5],[7,6,7,7],[7,9,7,12],[7,13,7,15],[8,1,8,4],[8,6,8,8],[8,10,8,11],\
                [8,12,8,14],[9,1,9,3],[9,4,9,9],[9,10,9,13],[10,0,10,1],[10,3,10,4],[10,10,10,11],[11,4,11,5],[11,6,11,7],[11,9,11,10],\
                    [11,13,11,15],[12,2,12,4],[12,7,12,10],[12,12,12,13],[13,1,13,2],[13,4,13,5],[13,9,13,11],[13,13,13,14],\
                        [14,5,14,7],[14,9,14,12],[15,0,15,14]]
    mat_y = array(mat_y)
    mat_y = mat_y*size_between
    # Draw the lines of the labyrinth
    for i in range(len(mat_x)):
        pygame.draw.line(surface, color_lines, (mat_x[i][0], mat_x[i][1]), (mat_x[i][2],mat_x[i][3]), 3)
    for i in range(len(mat_y)):
        pygame.draw.line(surface, color_lines, (mat_y[i][0], mat_y[i][1]), (mat_y[i][2],mat_y[i][3]),3)

    pass    

def redrawWindow(surface):
    global rows, width, c, l
    color_surface = (255,255,255)
    surface.fill(color_surface)
    c.draw_trail(surface)
    l.display_letter(surface)
    c.draw_car(surface)
    drawLabyrinth(width, rows, surface)
    pygame.display.update()

    pass

def main():
    global width, rows, c, l
    # root = tk.Tk()
    # Explanation(root)
    # root.destroy()

    # Rows needs to divide evenly by width
    width = 450    
    rows = 15
    win = pygame.display.set_mode((width, width))
    background = pygame.Surface((win.get_size()))
    background.fill((255, 255, 255))
    image = pygame.image.load("figures/1_labyrinth.png")

    image = image.convert()
    rect = image.get_rect()
    win.blit(image, rect)

    c = car((13,14))
    l = letter()

    flag = True

    clock = pygame.time.Clock()

    while flag:
        # The two below commands play with the velocity of the game
        pygame.time.delay(1)
        #Makes sure that the game runs at 10 frame per second
        clock.tick(10)
        #Car moves
        c.move()

        if c.head.pos == (14,14):
            # print('You won!')
            won_game()

        redrawWindow(win)
    pass

main()