import tkinter as tk
from turtle import RawTurtle, TurtleScreen

from memory import main_memory
from futbol_series import main_futbol, main_series
from labyrinth import main_labyrinth
from pipelines import main_pipelines
from crossword import main_crossword

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
        self.img_yes = tk.PhotoImage(file='figures/0_1_si.png')
        self.img_no = tk.PhotoImage(file='figures/0_1_no.png')
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

        self.img_panel = tk.PhotoImage(file='figures/0_1_sosa.png')
        self.panel.configure(image=self.img_panel)


class FigureFrame(BasicFrame):
    """Class inherited from the just defined BasicFrame class. This class
    creates a frame with an image and a "next button". With this structure, the
    story of the game is explained.
    """
    def __init__(self, master, img_path):
        """Initialize the frame and display on it the image and the next button

        Args:
            master (tkinter.tk): tkinter window where the frames are displayed
            img_path (str): path of the image to be displayed
        """
        tk.Frame.__init__(self, master)
        self.display_image(img_path)
        self.next_button()
        self.pack()
        self.counter = 0

    def next_button(self):
        """Button that, when pressed, destroys the current frame so that the
        next explanation image or game is shown
        """
        f = tk.Frame(self, height=50, width=50)
        f.pack(side='left')
        self.img_next = tk.PhotoImage(file='figures/0_0_next.png')
        self.b_next = tk.Button(f,image=self.img_next,command=self.destroy_frame)
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
        tk.Frame.__init__(self, master, width=567, height=567)
        self.pack()

        self.person_talking(person_path)
        tk.Label(self, text=destination_msg, font=('Helvetica', 16)).grid(column=1, row=0)
        w = tk.Canvas(self, width=567, height=467)
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
        f.grid(row=2, column=0, sticky=tk.W)
        self.img_next = tk.PhotoImage(file='figures/0_0_next.png')
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
        self.screen = TurtleScreen(canvas)
        self.screen.bgpic('figures/0_0_map_reduced.gif')
        self.turtle = RawTurtle(self.screen, visible=False)
        self.turtle.speed('slowest')
        self.turtle.pensize(2)
        self.screen.register_shape('figures/0_0_rocket.gif')
        self.turtle.shape('figures/0_0_rocket.gif')
        self.kingdom_places = {
            'castle': (122,-1),
            'photo_village': (-84,-67),
            'train_station': (193,177),
            'labyrinth': (175,-204),
            'balloon': (-249,205),
            'hector': (78,95),
            'sofi': (-128,112)
        }
        self.set_initial_pos(rocket_from)
        self.move_to(rocket_to)

    def set_initial_pos(self, place):
        """Make the turtle appear in a certain position before the player can
        see it.

        Args:
            place (str): place where the turtle will be located
        """
        self.turtle.up()
        self.move_to(place)
        self.turtle.down()
        self.turtle.showturtle()

    def move_to(self, place):
        """Move the turtle to a certain place

        Args:
            place (str): place where the turtle will move to
        """
        if place in self.kingdom_places:
            self.turtle.goto(self.kingdom_places[place])


def on_closing():
    """Exit python when the player clicks the cross button on the top right
    window
    """
    exit()


def main():
    """Main function for the game created for my cousin. This function relates
    all the classes previously defined and the minigames created.
    """
    root = tk.Tk()
    root.geometry("+300+100")
    root.protocol("WM_DELETE_WINDOW",on_closing)

    app = InitialFrame(root,'figures/0_1_help.png')
    app.mainloop()

    image_paths = [
        'figures/0_2_miguelina.png',
        'figures/0_3_alcanicil.png',
        'figures/0_4_letsgo.png',
        'move0',
        'figures/1_1_explanation.png',
        'memory_game',
        'figures/1_3_congrats.png',
        'move1',
        'figures/2_1_explanation.png',
        'futbol_game',
        'figures/2_3_congrats.png',
        'move2',
        'figures/3_1_explanation.png',
        'series_game',
        'figures/3_3_congrats.png',
        'move3',
        'figures/4_1_explanation.png',
        'labyrinth_game',
        'figures/4_3_congrats.png',
        'move4',
        'figures/5_1_wakeupprincess.png',
        'figures/5_2_failed.png',
        'figures/5_3_blai.png',
        'move5',
        'figures/6_1_explanation.png',
        'pipelines_game',
        'figures/6_3_congrats.png',
        'move6',
        'figures/7_1_explanation.png',
        'crossword_game',
        'figures/7_3_congrats.png',
        'move7',
        'figures/8_1_wakeupprincess.png',
        'figures/8_2_success.png'
    ]

    destinations = [
        ['castle', 'Vayamos primero al pueblo de la fotografía', 'fernando'],
        ['photo_village', 'Siguiente parada: casa del tío', 'antonio'],
        ['hector', '¡Rápido! A la estación de tren', 'paco'],
        ['train_station', 'Nos adentramos en el laberinto...', 'fernando'],
        ['labyrinth', '¡Lo tenemos! De vuelta al castillo', 'paco'],
        ['castle', 'Pongamos rumbo a casa de los papas', 'antonio'],
        ['sofi', '¡Ahora toca volar en globo!', 'fernando'],
        ['balloon', '¡Último viaje! Hacia el castillo', 'paco'],
        ['castle','aux']
    ]

    for img_path in image_paths:
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
            initial_point = destinations[idx][0]
            end_point = destinations[idx+1][0]
            msg = destinations[idx][1]
            who_path = 'figures/0_0_' + destinations[idx][2] + '.png'
            m = MapTransitions(root, msg, who_path,initial_point, end_point)
            m.mainloop()
        else:
            app = FigureFrame(root, img_path)
            app.mainloop()


main()