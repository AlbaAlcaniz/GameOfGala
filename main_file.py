import tkinter as tk
from PIL import ImageTk, Image

#Import the minigames
from labyrinth import main_labyrinth
from series import main_series
from futbol import main_futbol
from crossword import main_crossword
# from pipelines import main_pipelines


class StartGame(tk.Frame):
    """Inherited class from the Frame class from tkinter.
    This class starts the game by asking the player for help on a mission.
    If the player wants to help, the mission is explained.
    Otherwise, the game will call the player boring and it will be closed.
    """

    def __init__(self, master):
        """Initialize the class by setting the attributes of the tkinter window
        together with the buttons and the image

        Args:
            master (tkinter.Tk): window where the buttons and image are 
                displayed
        """
        tk.Frame.__init__(self, master)
        self.master.geometry("+300+100")
        self.master.attributes('-topmost', True)
        self.help_image()
        self.pack()
        self.img_yes = tk.PhotoImage(file='figures/0_si.png')
        self.img_no = tk.PhotoImage(file='figures/0_no.png')
        self.yes_no_button('left')
        self.yes_no_button('right')
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def help_image(self):
        """Create and display the panel where the help image is shown
        """
        self.img_panel = tk.PhotoImage(file='figures/0_ayuda.png')
        self.panel = tk.Label(image=self.img_panel)
        self.panel.pack()

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
                                    command=self.callback)
            self.b_yes.pack(expand=1)
        else:
            self.b_no = tk.Button(f, image=self.img_no, command=self.sosa)
            self.b_no.pack(expand=1)

    def callback(self):
        """Function in case the player wants to help which destroys the root 
        widget so that the next figures are displayed
        """
        self.master.destroy()

    def sosa(self):
        """Function in case the player doesn't want to help in which the player
        is called boring and the game is closed
        """
        self.b_no.destroy()
        self.b_yes.destroy()

        self.img_panel = tk.PhotoImage(file='figures/0_sosa.png')
        self.panel.configure(image=self.img_panel)

        self.destroy()

    def on_closing(self):
        """Exit python when the player clicks the cross button on the top right
        window
        """
        exit()


class ExplainMission(tk.Frame):
    """Class inherited from the Frame class of the tkinter module.
    This class explains the mission by showing several images
    """

    image_paths = [
        'figures/0_alcanicil.png',
        'figures/0_letsgo.png'
    ]

    def __init__(self, master=None):
        """Initialize the class by setting the attributes of the tkinter window
        together with the button and the images

        Args:
            master (tkinter.Tk): window where the images and button are 
                displayed
        """
        tk.Frame.__init__(self, master)
        self.master.geometry("+300+100")
        self.master.attributes('-topmost', True)
        self.explanation_image()
        self.pack(side = 'right')
        self.next_button()
        self.counter = 0
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)

    def explanation_image(self):
        """Create and display the panel where the image is shown
        """
        self.img_panel = tk.PhotoImage(file='figures/0_miguelina.png')
        self.panel = tk.Label(image=self.img_panel)
        self.panel.pack()

    def next_button(self):
        """Button that shows the next explanation image when pressed
        """
        f = tk.Frame(self, height=50, width=50)
        f.pack(side='left')
        self.img_next = tk.PhotoImage(file='figures/0_next.png')
        self.b_next = tk.Button(f,image=self.img_next,command=self.next_image)
        self.b_next.pack(expand=1)

    def next_image(self):
        """Command for when the next_button is pressed where the following
        image of the series is updated and displayed
        """
        if self.counter == 2:
            self.master.destroy()
        else:
            if self.counter == 1:
                self.img_next = tk.PhotoImage(file='figures/0_letsgobutton.png')
                self.b_next.configure(image=self.img_next)
                self.b_next.image = self.img_next
            self.img_panel = tk.PhotoImage(file=self.image_paths[self.counter])
            self.panel.configure(image=self.img_panel)
            self.panel.image = self.img_panel
            self.counter += 1

    def on_closing(self):
        """Exit python when the player clicks the cross button on the top right
        window
        """
        exit()


def main():
    """Main function where the mission is explained and links all the minigames
    """
    root = tk.Tk()
    app = StartGame(master=root)
    app.mainloop()

    root = tk.Tk()
    app = ExplainMission(master=root)
    app.mainloop()

    # Minigames
    main_futbol() #ducho
    main_series() #es un
    main_labyrinth() #miedica

    # main_pipelines() #medias
    main_crossword() #noches

main()