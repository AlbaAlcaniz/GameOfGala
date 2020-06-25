from tkinter import *

master = Tk()

e = Entry(master)
e.pack()

e.focus_set()

def callback():
    print(e.get())

b = Button(master, text="get", width=10, command=callback)
b.pack()

mainloop()

#####################


# import tkinter as tk
# from PIL import ImageTk, Image

# master=tk.Tk()
# font_ = 32; wid = 3

# # Image with the numerical series
# img1 = ImageTk.PhotoImage(image = Image.open("figures/2_series.png"))
# image = tk.Label(master, image = img1)
# image.grid(row=0, column=0, columnspan=1, rowspan=5)

# # Entries where the player writes the numbers following the series
# tk.Entry(master, font=("Helvetica", font_), background = "#0000ff", width = wid).grid(row=0, column=1)
# tk.Entry(master, font=("Helvetica", font_), background = "#ffff00", width = wid).grid(row=1, column=1)
# tk.Entry(master, font=("Helvetica", font_), background = "#ffffff", width = wid).grid(row=2, column=1)
# tk.Entry(master, font=("Helvetica", font_), background = "#ff79dc", width = wid).grid(row=3, column=1)
# tk.Entry(master, font=("Helvetica", font_), background = "#00ffff", width = wid).grid(row=4, column=1)

# # Image with the alphabet, so that the player can relate each number with the letter
# img2 = ImageTk.PhotoImage(image = Image.open("figures/2_abecedario.png"))
# image2 = tk.Label(master, image = img2)
# image2.grid(row=5, column=0, columnspan=1, rowspan=5)

# # Create the text space where the message can be written
# tk.Text(master, height=1, width=20, font=("Helvetica", font_)).grid(row=11, column=0)

# # # Create the button for when the message is ready
# # img3 = ImageTk.PhotoImage(Image.open("figures/0_next.png"))
# # # Define the space for the button
# # f = tk.Frame(root, height=50, width=50)
# # f.pack_propagate(0)
# # f.pack(side = 'right')
# # # Create button
# # #command=lambda: retrieve_input() >>> just means do this when i press the button
# # buttonCommit=tk.Button(f, image = img2, command=lambda: retrieve_input())
# # buttonCommit.pack(expand=1)

# master.mainloop()