import tkinter as tk
import pygame
import sys, os
from turtle import RawTurtle, TurtleScreen

import data
from memory import main_memory
from labyrinth import main_labyrinth
from pipelines import main_pipelines
from crossword import main_crossword
from futbolseries import main_futbol, main_series


def resource_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class BasicFrame(tk.Frame):
    """Class inherited from the tkinter frame with common commands for the rest
    of the class used in this file
    """
    def display_image(self, img_path):
        """Display the main image in a panel

        Args:
            img_path (str): path of the image to be displayed
        """
        self.img_panel = tk.PhotoImage(file=img_path)
        self.panel = tk.Label(self,image=self.img_panel)
        self.panel.pack()

    def destroy_frame(self):
        """When necessary, destroy the frame so that the next frame can be
        generated
        """
        self.destroy()
        self.quit()


class InitialFrame(BasicFrame):
    """Frame for the beginning of the game, where the player has the option to
    help on the mission, or reject it. Inherited class from the just defined
    BasicFrame.
    """
    def __init__(self, master, img_path):
        """Initialize the frame by setting the yes and no buttons, and by
        displaying the image where the help is asked for.

        Args:
            master (tkinter.tk): tkinter window where the frames are displayed
            img_path (str): path of the image to be displayed
        """
        tk.Frame.__init__(self, master)
        self.display_image(img_path)
        self.pack()
        self.img_yes = tk.PhotoImage(file=resource_path('figures/0_1_si.png'))
        self.img_no = tk.PhotoImage(file=resource_path('figures/0_1_no.png'))
        self.yes_no_button('left')
        self.yes_no_button('right')

    def yes_no_button(self, button_side):
        """Creates a button which displays the YES or NO options depending on
        the input position.

        Args:
            button_side (string): where the button is placed: 'left' or 'right'
        """
        f = tk.Frame(self, height=50, width=200)
        f.pack(side = button_side)
        if button_side == 'left':
            self.b_yes = tk.Button(f, image=self.img_yes, 
                                    command=self.destroy_frame)
            self.b_yes.pack(expand=1)
        else:
            self.b_no = tk.Button(f, image=self.img_no, command=self.sosa)
            self.b_no.pack(expand=1)

    def sosa(self):
        """Function in case the player doesn't want to help in which the player
        is called boring and the game is closed
        """
        self.b_no.destroy()
        self.b_yes.destroy()

        pygame.mixer.music.load(resource_path('audio/0_monkey.wav'))
        pygame.mixer.music.play()

        self.img_panel = tk.PhotoImage(file=resource_path('figures/0_1_sosa.png'))
        self.panel.configure(image=self.img_panel)


class FigureFrame(BasicFrame):
    """Class inherited from the just defined BasicFrame class. This class
    creates a frame with an image and a "next button". With this structure, the
    story of the game is explained.
    """
    def __init__(self, master, img_path, list_text):
        """Initialize the frame and display on it the image and the next button

        Args:
            master (tkinter.tk): tkinter window where the frames are displayed
            img_path (str): path of the image to be displayed
        """
        tk.Frame.__init__(self, master)
        self.list_text = list_text
        self.text_displayed = 0
        self.pack()
        self.display_text(list_text[self.text_displayed])
        self.display_image(img_path)
        self.next_button()

    def next_text(self):
        if self.text_displayed < (len(self.list_text)-1):
            self.text_displayed += 1
            self.text_label.configure(text=self.list_text[self.text_displayed])
            self.text_label.text = self.list_text[self.text_displayed]
        else:
            self.destroy_frame()

    def display_text(self, text):
        self.text_label = tk.Message(self, text=text, font=('Helvetica', 28), \
            width=800, justify=tk.CENTER)
        self.text_label.pack()

    def next_button(self):
        """Button that, when pressed, destroys the current frame so that the
        next explanation image or game is shown
        """
        f = tk.Frame(self, height=50, width=50)
        f.pack(side='right')
        self.img_next = tk.PhotoImage(file=resource_path('figures/0_0_next.png'))
        self.b_next = tk.Button(f, image=self.img_next, \
            command=self.next_text)
        self.b_next.pack(expand=1)


class MapTransitions(tk.Frame):
    """Inherited class from the tkinter frame where the map and the rocket are
    displayed. This serves so that the player know where she is moving
    everytime and helps with the story-game.
    """
    def __init__(self, master, destination_msg, person_path, 
                rocket_from, rocket_to):
        """Initialize the frame, and display:
        - The image of a person who tells you the next destination
        - The message that this person is saying, telling you the destination
        - A canvas where a turtle environment is created
        - A next button which destroys the frame in order to move forward

        Args:
            master (tkinter.tk): tkinter window where the frames are displayed
            destination_msg (str): message where the next destination is told
            person_path (str): path of the person's fotograph
            rocket_from (str): initial position of the rocket
            rocket_to (str): final position of the rocket
        """
        tk.Frame.__init__(self, master)
        self.pack()

        self.person_talking(person_path)
        tk.Label(self, text=destination_msg, font=('Helvetica', 16)).grid(column=1, row=0)
        w = tk.Canvas(self, width=800, height=560)
        w.grid(row=1, columnspan=2)
        self.next_button()
        r = Rocket(w, rocket_from, rocket_to)

    def person_talking(self, person_path):
        """Display the image of a person who is the one telling the next
        destination

        Args:
            person_path (str): path of the person's fotograph
        """
        self.img_person = tk.PhotoImage(file=person_path)
        tk.Label(self, image=self.img_person).grid(column=0, row=0)

    def next_button(self):
        """Button that, when pressed, destroys the current frame so that the
        next explanation image is shown
        """
        f = tk.Frame(self, height=50, width=50)
        f.grid(row=2, column=1, sticky=tk.E)
        self.img_next = tk.PhotoImage(file=resource_path('figures/0_0_next.png'))
        self.b_next = tk.Button(f, image=self.img_next, command=self.destroy_frame)
        self.b_next.pack(expand=1)

    def destroy_frame(self):
        """When necessary, destroy the frame so that the next frame can be
        generated
        """
        self.destroy()
        self.quit()


class Rocket():
    """Class which contains the turtle environment, with its screen and the
    turtle itself.
    """
    def __init__(self, canvas, rocket_from, rocket_to):
        """Initialize the turtle screen and the turtle object by setting the
        background image and the characteristics of the turtle. Set the initial
        position of the turtle and move it to the next position.

        Args:
            canvas (tkinter.canvas): space where the environment is displayed
            rocket_from (str): initial position of the rocket
            rocket_to (str): final position of the rocket
        """
        self.rocket_to = rocket_to
        self.rocket_from = rocket_from
        self.screen = TurtleScreen(canvas)
        self.screen.bgpic(resource_path('figures/0_0_map_reduced.gif'))
        self.turtle = RawTurtle(self.screen, visible=False)
        self.turtle.speed('slowest')
        self.turtle.pensize(2)
        self.screen.register_shape(resource_path('figures/0_0_rocket.gif'))
        self.turtle.shape(resource_path('figures/0_0_rocket.gif'))
        self.kingdom_places = {
            'castle': (145,-3),
            'photo_village': (-101,-78),
            'train_station': (231,214),
            'labyrinth': (217,-246),
            'balloon': (-299,249),
            'hector': (92,117),
            'sofi': (-152,137)
        }
        rocketSound = pygame.mixer.Sound(resource_path('audio/rocket.wav'))
        rocketSound.play()
        self.set_initial_pos()
        self.move_to()
        rocketSound.stop()

    def set_initial_pos(self):
        """Make the turtle appear in a certain position before the player can
        see it."""
        self.turtle.up()
        self.turtle.goto(self.kingdom_places[self.rocket_from])
        self.turtle.down()
        self.turtle.showturtle()

    def move_to(self):
        """Move the turtle to a certain place"""
        self.turtle.goto(self.kingdom_places[self.rocket_to])


def on_closing():
    """Exit python when the player clicks the cross button on the top right
    window
    """
    sys.exit()


def main_game():
    """Main function for the game created for my cousin. This function relates
    all the classes previously defined and the minigames created.
    """
    root = tk.Tk()
    root.protocol("WM_DELETE_WINDOW",on_closing)
    root.title('The rescue of princess Miguelina')
    pygame.mixer.init()

    app = InitialFrame(root, resource_path('figures/0_1_help.png'))
    app.mainloop()

    root.state('zoomed')
    
    correctSound = pygame.mixer.Sound(resource_path('audio/correct.wav'))

    for img_path in data.image_paths.keys():
        if img_path == 'memory_game':
            main_memory()
        elif img_path == 'futbol_game':
            main_futbol(root)
        elif img_path == 'series_game':
            main_series(root)
        elif img_path == 'labyrinth_game':
            main_labyrinth(root)
        elif img_path == 'pipelines_game':
            main_pipelines()
        elif img_path == 'crossword_game':
            main_crossword(root)
        elif img_path.startswith('move'):
            idx = int(img_path[-1])
            initial_point = data.destinations[idx][0]
            end_point = data.destinations[idx+1][0]
            msg = data.destinations[idx][1]
            who_path = 'figures/0_0_' + data.destinations[idx][2] + '.png'
            m = MapTransitions(root, msg, resource_path(who_path), \
                initial_point, end_point)
            m.mainloop()
        elif img_path.startswith('audio'):
            pygame.mixer.music.load(resource_path(img_path))
            pygame.mixer.music.play(-1)
        else:
            if 'congrats' in img_path:
                correctSound.play()
            img_text = data.image_paths[img_path]
            app = FigureFrame(root, resource_path(img_path), img_text)
            app.mainloop()


main_game()