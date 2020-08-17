
##################
# a = []
# for i in range(2,8):
#     a.append([0,i])
# for i in range(1,6):
#     a.append([1,i])
# for i in range(5,10):
#     a.append([2,i])
# for i in range(2,7):
#     a.append([3,i])
# for i in range(3,8):
#     a.append([4,i])
# for i in range(1,5):
#     a.append([5,i])
# print(a)
##################
# from tkinter import *

# class Application(Frame):
#     def say_hi(self):
#         print("hi there, everyone!")

#     def createWidgets(self):
#         self.QUIT = Button(self)
#         self.QUIT["text"] = "QUIT"
#         self.QUIT["fg"]   = "red"
#         self.QUIT["command"] =  self.quit

#         self.QUIT.pack({"side": "left"})

#         self.hi_there = Button(self)
#         self.hi_there["text"] = "Hello",
#         self.hi_there["command"] = self.say_hi

#         self.hi_there.pack({"side": "left"})

#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.pack()
#         self.createWidgets()

# root = Tk()
# app = Application(master=root)
# app.mainloop()
# root.destroy()

##################
# from math import pi
# cardinal_points = {
#     "WN" : 0,
#     "EN" : pi/2,
#     "ES" : pi,
#     "WS" : 3*pi/2,
# }
# points_cardinal = {value:key for (key,value) in cardinal_points.items()}
# # points_cardinal = {cardinal_points[x]: x for x in cardinal_points}
# print(points_cardinal)
#################

# from tkinter import *

# master = Tk()

# e = Entry(master)
# e.pack()

# e.focus_set()

# def callback():
#     print(e.get())

# b = Button(master, text="get", width=10, command=callback)
# b.pack()

# mainloop()

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