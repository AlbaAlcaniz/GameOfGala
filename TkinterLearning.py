import tkinter as tk

from memory import main_memory
from futbol import main_futbol

class BasicFrame(tk.Frame):
    def display_image(self, img_path):
        self.img_panel = tk.PhotoImage(file=img_path)
        self.panel = tk.Label(self,image=self.img_panel)
        self.panel.pack()

    def destroy_frame(self):
        self.destroy()
        self.quit()


class InitialFrame(BasicFrame):
    def __init__(self, master, img_path):
        tk.Frame.__init__(self, master)
        self.display_image(img_path)
        self.pack()
        self.img_yes = tk.PhotoImage(file='figures/0_si.png')
        self.img_no = tk.PhotoImage(file='figures/0_no.png')
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

        self.img_panel = tk.PhotoImage(file='figures/0_sosa.png')
        self.panel.configure(image=self.img_panel)


class BasicFrame(BasicFrame):
    """Class inherited from the Frame class of the tkinter module.
    This class explains the mission by showing several images
    """

    def __init__(self, master,img_path):
        tk.Frame.__init__(self, master)
        self.display_image(img_path)
        # self.pack(side = 'right')
        self.next_button()
        self.pack()
        self.counter = 0

    def next_button(self):
        """Button that shows the next explanation image when pressed
        """
        f = tk.Frame(self, height=50, width=50)
        f.pack(side='left')
        self.img_next = tk.PhotoImage(file='figures/0_next.png')
        self.b_next = tk.Button(f,image=self.img_next,command=self.destroy_frame)
        self.b_next.pack(expand=1)


def on_closing():
    """Exit python when the player clicks the cross button on the top right
    window
    """
    exit()

root = tk.Tk()
root.geometry("+300+100")
root.protocol("WM_DELETE_WINDOW",on_closing)

app = InitialFrame(root,'figures/0_ayuda.png')
app.mainloop()

image_paths = [
    'figures/0_miguelina.png',
    'figures/0_alcanicil.png',
    'figures/0_letsgo.png',
    'figures/6_explanation.png',
    'memory_game',
    'figures/6_congrats.png',
    'figures/3_futbol.png',
    'futbol_game',
    'figures/3_conseguido.png'
]
for img_path in image_paths:
    if img_path == 'memory_game':
        main_memory()
    elif img_path == 'futbol_game':
        main_futbol()
    else:
        app = BasicFrame(root, img_path)
        app.mainloop()


