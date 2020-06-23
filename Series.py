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
        """Initialize the explanation.

        Args:
            master (tkinter.Tk): window where the minigame runs
        """
        # Make sure that the window appears on top
        master.attributes('-topmost', True)

        # Display the numerical series of numbers
        series = "15 15 10 10  5 \n24 22 20 18 16 \n15 12 9 6 3 \n70 60 50 40 30 \n11 22 33 22 11"
        w = tk.Message(master, text=series, font=("Helvetica", 32),width = 350)
        w.pack(side = 'left')

        # Create the text space where the message can be written
        
        # textBox=tk.Text(master, height=1, width=20, font=("Helvetica", 32))
        # textBox.insert("1.0","15 15 10 10 5")
        # textBox.pack(side = 'left')

        # # Export and display the explanation image
        # img1 = ImageTk.PhotoImage(image = Image.open("figures/2_ingenieria.png"))
        # panel = tk.Label(master, image = img1)
        # panel.img1 = img1        
        # panel.pack()

        # # "Next" button
        # img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        # # Define the space for the button
        # f = tk.Frame(master, height=50, width=50)
        # f.pack_propagate(0)
        # f.pack(side = "right")
        # # Create button
        # self.button = tk.Button(f, image = img2, command=f.quit)
        # self.button.img2 = img2
        # self.button.pack(expand=1)
        
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
    Series(root2)
    root2.destroy()



    pass

# Initialize the game
main_series()