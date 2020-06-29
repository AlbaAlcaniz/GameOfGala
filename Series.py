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

def series_function():
    """Minigame where the player needs to complete the numerical series and relate the numbers obtained with the 
    letters of the alphabet.
    """

    #Create the tkinter window
    master2 = tk.Tk()
    #Make sure that the window appears on top
    master2.attributes('-topmost', True)

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
        
        if inputValue.upper() == 'ES_UN':
            #If the message coincides with the right answer, destroy the root and onto the next minigame!
            master2.destroy()
        else:
            # If the message doesn't coincide, warn the player
            message_box()

    # Image with the numerical series
    img1 = ImageTk.PhotoImage(image = Image.open("figures/2_series.png"))
    image = tk.Label(master2, image = img1)
    image.grid(row=0, column=0, columnspan=1, rowspan=5)

    # Font size and width of the entries
    font_ = 32; wid = 3
    # Entries where the player writes the numbers following the series
    tk.Entry(master2, font=("Helvetica", font_), background = "#0000ff", width = wid).grid(row=0, column=1)
    tk.Entry(master2, font=("Helvetica", font_), background = "#ffff00", width = wid).grid(row=1, column=1)
    tk.Entry(master2, font=("Helvetica", font_), background = "#ffffff", width = wid).grid(row=2, column=1)
    tk.Entry(master2, font=("Helvetica", font_), background = "#ff79dc", width = wid).grid(row=3, column=1)
    tk.Entry(master2, font=("Helvetica", font_), background = "#00ffff", width = wid).grid(row=4, column=1)

    # Image with the alphabet as reference to extract the message
    img2 = ImageTk.PhotoImage(image = Image.open("figures/2_abecedario.png"))
    image = tk.Label(master2, image = img2)
    image.grid(row=0, column=2, columnspan=2, rowspan=5)
    
    # Create the text space where the message can be written
    textBox = tk.Text(master2, height=1, width=17, font=("Helvetica", font_))
    textBox.grid(row = 5, column = 2)        

    # Create the button for when the message is ready
    img3 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
    tk.Button(master2, height=50, width=50, image = img3, command=lambda: retrieve_input()).grid(row = 5, column = 3)

    master2.mainloop()

    pass


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
        # img2 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        # tk.Button(master, height=50, width=50, image = img2, command=master.quit).grid(row = 5, column = 1)

        def retrieve_input():
            """Function that gets the string written in the text box if that string is correct
            """
            # Get the message written in the textBox
            # The "1.0" implies that the message is read from the first line, character zero
            # end-1c implies reading until the end of the entry, except for an automatically created last character
            inputValue=textBox.get("1.0","end-1c")
            
            if inputValue.upper() == 'ES_UN':
                #If the message coincides with the right answer, destroy the root and onto the next minigame!
                master.destroy()
            else:
                # If the message doesn't coincide, warn the player
                message_box()

        # Image with the numerical series
        img3 = ImageTk.PhotoImage(image = Image.open("figures/2_abecedario.png"))
        image = tk.Label(master, image = img3)
        image.grid(row=0, column=2, columnspan=2, rowspan=5)
        
        # Create the text space where the message can be written
        textBox = tk.Text(master, height=1, width=20, font=("Helvetica", 32)).grid(row = 5, column = 2)

        # Create the button for when the message is ready
        img4 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
        # Define the space for the button
        # Create button
        #command=lambda: retrieve_input() >>> just means do this when i press the button
        tk.Button(master, height=50, width=50, image = img4, command=lambda: retrieve_input()).grid(row = 5, column = 1)
        
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
    root1 = tk.Tk()
    Explanation(root1, "figures/2_ingenieria.png")
    root1.destroy()

    # Start the series game
    series_function()

    # root2 = tk.Tk()
    # s = Series(root2)
    # s.alphabet(root2)
    # Alphabet(root3)
    # root2.destroy()
    # root3.destroy()

    # Thank you for fulfilling the mission
    root1 = tk.Tk()
    Explanation(root1, "figures/2_gracias.png")
    root1.destroy()

    pass

# Initialize the game
main_series()