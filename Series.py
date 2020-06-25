# Import packages
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame

class Explanation:
    """Explanation of the minigame.
    """

    def __init__(self, master):
        """Initialize the explanation.

        Args:
            master (tkinter.Tk): initial window in which the minigame is explained
        """
        # Make sure that the window appears on top
        master.attributes('-topmost', True)

        # Export and display the explanation image
        img1 = ImageTk.PhotoImage(image = Image.open("figures/2_ingenieria.png"))
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

class Series:
    """Minigame where the player needs to complete the numerical series and relate the numbers obtained with the 
    letters of the alphabet.
    """

    def __init__(self, master):
        """Initialize the minigame.

        Args:
            master (tkinter.Tk): window where the minigame runs
        """
        # Make sure that the window appears on top
        master.attributes('-topmost', True)

        font_ = 32; wid = 3

        # Image with the numerical series
        img1 = ImageTk.PhotoImage(image = Image.open("figures/2_series.png"))
        image = tk.Label(master, image = img1)
        image.grid(row=0, column=0, columnspan=1, rowspan=5)

        # Entries where the player writes the numbers following the series
        tk.Entry(master, font=("Helvetica", font_), background = "#0000ff", width = wid).grid(row=0, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#ffff00", width = wid).grid(row=1, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#ffffff", width = wid).grid(row=2, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#ff79dc", width = wid).grid(row=3, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#00ffff", width = wid).grid(row=4, column=1)

        # Create the button for when the numbers are ready
        img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        tk.Button(master, height=50, width=50, image = img2, command=master.quit).grid(row = 5, column = 1)
        
        # Initialize the window
        master.mainloop()

    def alphabet(self,master):

        font_ = 32; wid = 3

        # Image with the numerical series
        img1 = ImageTk.PhotoImage(image = Image.open("figures/2_series.png"))
        image = tk.Label(master, image = img1)
        image.grid(row=0, column=0, columnspan=1, rowspan=5)

        # Entries where the player writes the numbers following the series
        tk.Entry(master, font=("Helvetica", font_), background = "#0000ff", width = wid).grid(row=0, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#ffff00", width = wid).grid(row=1, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#ffffff", width = wid).grid(row=2, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#ff79dc", width = wid).grid(row=3, column=1)
        tk.Entry(master, font=("Helvetica", font_), background = "#00ffff", width = wid).grid(row=4, column=1)

        # Image with the numerical series
        img3 = ImageTk.PhotoImage(image = Image.open("figures/2_abecedario.png"))
        image = tk.Label(master, image = img3)
        image.grid(row=0, column=2, columnspan=1, rowspan=5)

        # Create the button for when the numbers are ready
        img4 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        tk.Button(master, height=50, width=50, image = img4, command=master.quit).grid(row = 5, column = 2)

        master.mainloop()


class Alphabet:
    """Minigame where the player needs to complete the numerical series and relate the numbers obtained with the 
    letters of the alphabet.
    """

    def __init__(self, master):
        """Initialize the minigame.

        Args:
            master (tkinter.Tk): window where the minigame runs
        """
        # Make sure that the window appears on top
        master.attributes('-topmost', True)


        # Image with the numerical series
        img1 = ImageTk.PhotoImage(image = Image.open("figures/2_abecedario.png"))
        image = tk.Label(master, image = img1)
        image.grid(row=0, column=0, columnspan=1, rowspan=5)

        # # Create the text space where the message can be written
        # tk.Text(master, height=1, width=20, font=("Helvetica", 30)).grid(row=5, column=0)

        # # Create the button for when the message is ready
        # img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        # tk.Button(master, height=50, width=50, image = img2, command=master.quit).grid(row = 5, column = 1)
        
        # Initialize the window
        master.mainloop()      

def main_series():
    """Main function which connects all the rest and displays the main directions for the game
    """
    # Explain the mission
    # root1 = tk.Tk()
    # Explanation(root1)
    # root1.destroy()

    # Start the series game
    root2 = tk.Tk()
    s = Series(root2)
    s.alphabet(root2)
    # Alphabet(root3)

    # root2.destroy()
    # root3.destroy()



    pass

# Initialize the game
main_series()