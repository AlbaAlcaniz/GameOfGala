# Import the packages
import pygame
import tkinter as tk
from PIL import ImageTk, Image

#Import the minigames
from Labyrinth import main_labyrinth
from Series import main_series
from futbol import main_futbol
from crossword import main_crossword

def start_game():
    """Function for the beginning of the game, where I ask the player for help
    """
    # Create the root widget
    root = tk.Tk()
    # Make sure that the window appears on top
    root.attributes('-topmost', True)

    # Export and display image: I need your help
    img1 = ImageTk.PhotoImage(image = Image.open("figures/0_ayuda.png"))
    panel = tk.Label(root, image = img1)
    panel.pack()

    def callback():
        """Function in case the player wants to help which destroys the root widget
        """
        root.destroy()

    def sosa():
        """Function in case the player doesn't want to help
        """
        # Destroy the previous root
        root.destroy()
        # Create a new root widget
        root2 = tk.Tk()
        root2.attributes('-topmost', True)

        # Export image: Sosa! (meaning dull)
        img4 = ImageTk.PhotoImage(image = Image.open("figures/0_sosa.jpg"))
        panel = tk.Label(root2, image = img4)
        panel.pack()

        # Run the main loop for the root
        root2.mainloop()
        exit()

    # Button for helping
    # Export image: "Yes" option
    img2 = ImageTk.PhotoImage(Image.open("figures/0_si.png"))
    # Define the space for the button
    f = tk.Frame(root, height=50, width=200)
    f.pack_propagate(0)
    f.pack(side = "left")
    # Create button
    b = tk.Button(f, image = img2, command=callback)
    b.pack(expand=1)

    # Button for not helping
    # Export image: "No" option
    img3 = ImageTk.PhotoImage(Image.open("figures/0_no.png"))
    # Define the space for the button
    g = tk.Frame(root, height=50, width=200)
    g.pack_propagate(0)
    g.pack(side = "right")
    # Create button
    c = tk.Button(g, image = img3, command=sosa)
    c.pack(expand=1)

    # Run the main loop for the root
    root.mainloop()

def main_mission(image_root,button_root,button_size,button_side):
    """Function in which the mission is explained once accepted the help

    Args:
        image_root (string): directory in which the image to be displayed is kept
        button_root (string): directory in which the image to be displayed is kept
        button_size (tuple): (length,width) of the button
        button_side (string): position of the button
    """
    # Create the root widget
    root = tk.Tk()
    root.attributes('-topmost', True)

    def callback():
        """Destroy the root widget once pressed the button
        """
        root.destroy()

    # Export and display image
    img1 = ImageTk.PhotoImage(image = Image.open(image_root))
    panel = tk.Label(root, image = img1)
    panel.pack()

    # "Next" button
    img2 = ImageTk.PhotoImage(Image.open(button_root))
    # Define the space for the button
    f = tk.Frame(root, height=button_size[1], width=button_size[0])
    f.pack_propagate(0)
    f.pack(side = button_side)
    # Create button
    b = tk.Button(f, image = img2, command=callback)
    b.pack(expand=1)

    root.mainloop()

def main():
    """Main function for the game which connects all minigames
    """
    # Explanation of the main mission
    start_game()
    main_mission("figures/0_miguelina.png","figures/0_next.png",(50,50),'right')
    main_mission("figures/0_alcanicil.png","figures/0_next.png",(50,50),'right')
    main_mission("figures/0_letsgo.png","figures/0_letsgobutton.png",(567,122),'bottom')

    # Minigames
    main_futbol()
    main_series() #es un
    main_labyrinth() #miedica

    main_crossword() #noches
    

main()