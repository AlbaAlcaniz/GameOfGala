# Import packages
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import pygame

class Explanation:
    """Explanation of the minigame.
    """

    def __init__(self, master, figure_root):
        """Initialize the explanation.

        Args:
            master (tkinter.Tk): initial window in which the minigame is explained
            figure_root (string): folder where the image is saved
        """

        # Make sure that the window appears on top
        master.attributes('-topmost', True)

        # Export and display the explanation image
        img1 = ImageTk.PhotoImage(image = Image.open(figure_root))
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

def explanation(master):
    """Explanation of the minigame
    """
    #Make sure that the window appears on top
    master.attributes('-topmost', True)

    # Image with the explanation
    img1 = ImageTk.PhotoImage(image = Image.open("figures/3_futbol.png"))
    image = tk.Label(master, image = img1)
    image.pack()

    # "Next" button
    img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
    # Define the space for the button
    f = tk.Frame(master, height=50, width=50)
    f.pack_propagate(0)
    f.pack(side = "right")
    # Create button
    b = tk.Button(f, image = img2, command=f.quit)
    b.pack(expand=1)

    # Initialize the window
    master.mainloop()

    # return master
    pass

def sumas(master2):
    """Function where the minigame is shown and generated
    """

    #Create the tkinter window
    # master2 = tk.Tk()
    #Make sure that the window appears on top
    master2.attributes('-topmost', True)

    def message_box():
        """Function that generates a warning message in case the message is not correct
        """
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
        
        if inputValue.upper() == 'NOCHES':
            #If the message coincides with the right answer, destroy the root and onto the next minigame!
            master2.destroy()
        else:
            # If the message doesn't coincide, warn the player
            message_box()

    # Image with the numerical series
    img1 = ImageTk.PhotoImage(image = Image.open("figures/4_crucigrama.png"))
    image = tk.Label(master2, image = img1)
    image.grid(row=0, column=0, columnspan=1, rowspan=7)

    # Font size and width of the entries
    font_ = 28; wid = 2
    letter_row = [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,5]
    letter_column = [7,8,9,10,11,3,4,5,6,7,7,8,9,10,11,4,5,6,7,8,5,6,7,8,9,1,2,3,4,5,6,7]
    for i in range(len(letter_row)-1):
        if letter_column[i] == 7:
            tk.Entry(master2, font=("Helvetica", font_), background = "#ccccff", \
            width = wid).grid(row=letter_row[i], column=letter_column[i])
        else:
            tk.Entry(master2, font=("Helvetica", font_), background = "#ffffff", \
            width = wid).grid(row=letter_row[i], column=letter_column[i])

    # Image with the explanation of the relation between letters and numbers
    img2 = ImageTk.PhotoImage(image = Image.open("figures/4_question.png"))
    image = tk.Label(master2, image = img2)
    image.grid(row=6, column=1, columnspan=6, rowspan=1)

    # Create the text space where the message can be written
    textBox = tk.Text(master2, height=1, width=8, font=("Helvetica", font_))
    textBox.grid(row = 6, column = 7, columnspan=4, rowspan=1)

    # Create the button for when the message is ready
    img3 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
    tk.Button(master2, height=43, width=43, image = img3, command=lambda: retrieve_input()).grid(row = 6, column = 11)

    master2.mainloop()
    
    pass

def main_crossword():
    """Main function which connects all the rest and displays the main directions for the minigame
    """
    # Explain the mission
    root1 = tk.Tk()
    Explanation(root1, "figures/4_globos.png")
    root1.destroy()

    #Create the tkinter window
    master = tk.Tk()
    sumas(master)
    
    # End the mission
    root2 = tk.Tk()
    Explanation(root2, "figures/4_avolar.png")
    root2.destroy()

# Initialize the game
# main_crossword()