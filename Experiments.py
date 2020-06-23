# from tkinter import *
import tkinter as tk
root=tk.Tk()
def retrieve_input():
    inputValue=textBox.get("1.0","end-1c")
    print(inputValue)
    if inputValue == 'Fernando':
        print('Congrats!')
        exit()

    # return inputValue

textBox=tk.Text(root, height=2, width=10)
textBox.pack()
buttonCommit=tk.Button(root, height=1, width=10, text="Commit", 
                    command=lambda: retrieve_input())
#command=lambda: retrieve_input() >>> just means do this when i press the button
buttonCommit.pack()

root.mainloop()