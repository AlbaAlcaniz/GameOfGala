# Import packages
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame
from numpy import array

class Explanation:
    """Explanation of the minigame.
    I read somewhere that the roots should be a class.
    """

    def __init__(self, master):
        """Initialize the explanation.

        Args:
            master (tkinter.Tk): initial window in which the mission is explained
        """
        # Make sure that the window appears on top
        master.attributes('-topmost', True)

        # Export and display the explanation image
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
        
        # Initialize the window
        master.mainloop()

class car(object):
    """Class for the movement of the car
    """
    def __init__(self, start):
        """Initialize the movement of the car by creating the vehicle

        Args:
            start (tuple): Initial position of the car
        """
        # Initial position of the car
        self.pos = start 
        # Direction for x and y
        self.dirnx = 0
        self.dirny = 1
        # The trail are the positions in which the car has been
        # Useful to keep track of the letters collected
        self.trail = [self.pos]

    def move(self):
        """Function that determines the movement of the car
        """
        # Take the car's position
        p = self.pos
        # Each position has an assigned letter which indicates the movements that the car can do
        # These movements are limited by the walls of the labyrinth
        # There is probably a better way to do it, but this is all myself
        matrix = ["hiimjhimmjaiimc","dhjfdfhgfeiijej","hgeohgejdhijeig", "eijfejbfhghghij", "higfhgfeghgagho", \
            "fhigejkijeiiigf","fdhmjegbfhchijf","eigfeiigfkigalg","hiighjhigeijhmj","ejhigeghimjffff","hgfhiijdbdelgff",\
                "kjffbhghohiiigf","ffegkghgfeichio","feijejfbeijhgag","eiceilgeiigeiii"]
        letter_pos = matrix[p[1]][p[0]] #Letter assigned to the position of the car
        
        # When the player interacts with the computer
        for event in pygame.event.get():
            # If she wants to quit, let her quit
            if event.type == pygame.QUIT:
                pygame.quit()

            # Depending on the key pressed and the position of the car inside the labyrinth, the car moves
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and letter_pos in "gilimocj":
                self.dirnx = -1; self.dirny = 0
                self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

            elif keys[pygame.K_RIGHT] and letter_pos in "kalmehi":
                self.dirnx = 1; self.dirny = 0
                self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

            elif keys[pygame.K_UP] and letter_pos in "delfgko":
                self.dirnx = 0; self.dirny = -1
                self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)

            elif keys[pygame.K_DOWN] and letter_pos in "bfhjmko":
                self.dirnx = 0; self.dirny = 1
                self.pos = (self.pos[0] + self.dirnx, self.pos[1] + self.dirny)
            
    def draw_car(self, surface):
        """Draw the car

        Args:
            surface (pygame.Surface): window in which the car will be displayed
        """
        global width, rows
        dis = width // rows #size of a square in the grid
        i = self.pos[0] #row
        j = self.pos[1] #column
        color = (255,0,0) # Red

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
    
    def draw_trail(self, surface):
        """Draw the trail left by the car so that the collection of letters is easier

        Args:
            surface (pygame.Surface): window in which the trail will be displayed
        """
        global width, rows
        # Size of each square in the grid
        dis = width // rows
        # Every movement of the car, add its position to the trail
        if self.pos not in self.trail:
            self.trail.append(self.pos)

        # If the car has moved from the initial position, draw a grey line which represents its movement
        if len(self.trail) > 1:
            a = array(self.trail)*dis+dis/2
            a = a.astype(int)
            for i in range(len(a)-1):
                pygame.draw.line(surface, (175,175,175), a[i], a[i+1], 3)

class letter(object):
    """Class for the letters that are displayed along the labyrinth
    """
    def __init__(self):
        """Initialize the letters
        """
        # Letters left along the labyrinth
        self.message = 'MAIGBIOSTFCGDCALXEU'
        # Relative position of those letters
        self.pos = array([(1.5,2.5),(3.5,5.5),(0.5,8.5),(0.5,13),(5.5,7.5),(5.5,1.5),(6.5,3.5),(8.5,0.5),(13.5,0.5),\
            (14.5,3.5),(10.5,4.5),(9.5,6.5),(8.5,8.5),(9.5,9.5),(14.5,8.5),(13.5,10.5),(10.5,14.5),(6.5,10.5),(7.5,12.5)])
        
        global width, rows
        dis = width // rows #Width of a square of the grid
        # The positions are shifted so that they are absolute with respect to the grid
        self.pos = array(self.pos)*dis
        self.pos = self.pos.astype(int)
        pygame.font.init()
        #Determine the font of the letters
        self.font = pygame.font.SysFont('Comic Sans MS', 30)

    def display_letter(self,surface):
        """Function which displays the letters along the labyrinth

        Args:
            surface (pygame.Surface): window in which the letters will be displayed
        """
        # Loop for plotting all the letters in the window
        i = 0
        for l in self.message:
            text = self.font.render(l, True, (0,255,0), (255,255,255))
            textRect = text.get_rect()
            textRect.center = self.pos[i]
            surface.blit(text, textRect)
            i += 1

def won_game():
    """Function for when the car has reached the end of the labyrinth
    The player needs to submit the message she has found
    """

    #Create the tkinter window
    root = tk.Tk()
    #Make sure that the window appears on top
    root.attributes('-topmost', True)

    def message_box():
        #Make sure that the window appears on top
        root = tk.Tk()
        root.attributes('-topmost', True)
        root.withdraw()
        messagebox.showinfo('Oh oh', 'Mensaje incorrecto. Intentalo otra vez!')
        try:
            root.destroy()
        except:
            pass

    def retrieve_input():
        """Function that gets the string written in the text box if that string is correct
        """
        # Get the message written in the textBox
        # The "1.0" implies that the message is read from the first line, character zero
        # end-1c implies reading until the end of the entry, except for an automatically created last character
        inputValue=textBox.get("1.0","end-1c")
        
        if inputValue.upper() == 'MIEDICA':
            #If the message coincides with the right answer, destroy the root and onto the next minigame!
            root.destroy()
        else:
            # If the message doesn't coincide, warn the player
            message_box()

    # Export image: Congrats!
    img1 = ImageTk.PhotoImage(image = Image.open("figures/1_felicidades.png"))
    panel = tk.Label(root, image = img1)
    panel.pack()
    
    # Create the text space where the message can be written
    textBox=tk.Text(root, height=1, width=20, font=("Helvetica", 32))
    textBox.pack(side = 'left')

    # Create the button for when the message is ready
    img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
    # Define the space for the button
    f = tk.Frame(root, height=50, width=50)
    f.pack_propagate(0)
    f.pack(side = 'right')
    # Create button
    #command=lambda: retrieve_input() >>> just means do this when i press the button
    buttonCommit=tk.Button(f, image = img2, command=lambda: retrieve_input())
    buttonCommit.pack(expand=1)

    root.mainloop()

    pass

def drawLabyrinth(surface):
    """Function which draws the labyrinth

    Args:
        surface (pygame.Surface): window in which the letters will be displayed
    """
    global width, rows
    # How big each square of the grid is
    size_between = width // rows
    
    color_lines = (0,0,0) #Black
    # Define the horizontal lines of the labyrinth
    mat_x = [[0,0,15,0],[1,1,3,1],[0,2,1,2],[6,1,7,1],[10,1,13,1],[14,1,15,1],[4,2,5,2],[7,2,8,2],[9,2,12,2],[13,2,14,2],\
        [1,3,3,3],[5,3,7,3],[8,3,9,3],[10,3,11,3],[12,3,15,3],[0,4,2,4],[4,4,5,4],[9,4,10,4],[11,4,12,4],[13,4,14,4],\
            [1,5,3,5],[5,5,6,5],[7,5,9,5],[10,5,13,5],[2,6,5,6],[7,6,8,6],[9,6,14,6],[1,7,2,7],[5,7,7,7],[10,7,11,7],\
                [12,7,13,7],[0,8,3,8],[4,8,8,8],[10,8,15,8],[1,9,4,9],[7,9,11,9],[0,10,1,10],[3,10,7,10],[8,10,9,10],\
                    [1,11,2,11],[4,11,6,11],[7,11,8,11],[9,11,13,11],[6,12,7,12],[10,12,14,12],[2,13,4,13],[5,13,6,13],\
                        [7,13,8,13],[9,13,12,13],[13,13,14,13],[1,14,3,14],[4,14,5,14],[8,14,10,14],[12,14,15,14],[0,15,15,15]]
    mat_x = array(mat_x) #Make it an array so each number can bemultiplied by size_between
    mat_x = mat_x*size_between

    # Define the vertical lines of the labyrinth
    mat_y = [[0,1,0,15],[1,1,1,2],[1,5,1,7],[1,12,1,14],[2,2,2,3],[2,6,2,7],[2,9,2,13],[3,1,3,2],[3,3,3,5],[3,7,3,8],\
        [3,10,3,12],[3,14,3,15],[4,1,4,6],[4,7,4,9],[4,11,4,14],[5,0,5,2],[5,6,5,7],[5,9,5,10],[5,11,5,12],[6,1,6,6],\
            [6,8,6,9],[6,12,6,14],[7,3,7,5],[7,6,7,7],[7,9,7,12],[7,13,7,15],[8,1,8,4],[8,6,8,8],[8,10,8,11],\
                [8,12,8,14],[9,1,9,3],[9,4,9,9],[9,10,9,13],[10,0,10,1],[10,3,10,4],[10,10,10,11],[11,4,11,5],[11,6,11,7],[11,9,11,10],\
                    [11,13,11,15],[12,2,12,4],[12,7,12,10],[12,12,12,13],[13,1,13,2],[13,4,13,5],[13,9,13,11],[13,13,13,14],\
                        [14,5,14,7],[14,9,14,12],[15,0,15,14]]
    mat_y = array(mat_y) #Make it an array so each number can bemultiplied by size_between
    mat_y = mat_y*size_between

    # Draw the lines of the labyrinth
    for i in range(len(mat_x)):
        pygame.draw.line(surface, color_lines, (mat_x[i][0], mat_x[i][1]), (mat_x[i][2],mat_x[i][3]), 3)
    for i in range(len(mat_y)):
        pygame.draw.line(surface, color_lines, (mat_y[i][0], mat_y[i][1]), (mat_y[i][2],mat_y[i][3]),3)

    pass    

def redrawWindow(surface):
    """On every frame, redraw all the elements of the pygame window

    Args:
        surface (pygame.Surface): window in which the letters will be displayed
    """
    # Make the car and letters global
    global c, l
    color_surface = (255,255,255) #White
    surface.fill(color_surface) #White background
    c.draw_trail(surface) #Draw the trail left by the car
    l.display_letter(surface) #Display the letters
    c.draw_car(surface) #Draw the car
    drawLabyrinth(surface) #Draw the lines of the labyrinth
    pygame.display.update() #Update the window

    pass

def main_labyrinth():
    """Main function which connects all the rest and displays the main directions for the game
    """
    # Make several variables global, such as the car (c) or the letters (l)
    global width, rows, c, l

    # Explain the mission
    root = tk.Tk()
    Explanation(root)
    root.destroy()

    # Rows needs to divide evenly by width
    width = 450; rows = 15
    # Create the pygame window where everything will be displayed
    win = pygame.display.set_mode((width, width))
    #Initialize the car and the letters
    c = car((0,0))
    l = letter()

    flag = True #Variable which is true as long as you don't reach the end of the labyrinth

    clock = pygame.time.Clock() #game's clock

    while flag:
        # The two below commands play with the velocity of the game
        pygame.time.delay(1)
        clock.tick(10)

        #Car moves
        c.move()

        # If you reach the end of the labyrinth, you won
        if c.pos == (14,14):
            won_game()
            return 'miedica'

        # redraw the window onevery frame
        redrawWindow(win)
    pass

# Initialize the game
# main_labyrinth()