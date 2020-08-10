#Copied from https://www.youtube.com/watch?v=vzzEP_YI424
# https://www.youtube.com/watch?v=rWaSo2usU4A&list=PLB_ibvUSN7mzUffhiay5g5GUHyJRO4DYr&index=16
#Commented by myself
# I have realized that this game would be too difficult for my cousin, and it doesn't explain mouse interaction
# which is what I wanted to learn. Therefore for now I won't continue with it

# Minute 11.42
from tkinter import *
from tkinter.ttk import Entry,Button,OptionMenu
from PIL import Image, ImageTk
import random
import tkinter.filedialog
import os

class Tiles():
    def __init__(self,grid):
        self.tiles = []
        self.grid = grid
        self.gap = None

    def add(self,tile):
        self.tiles.append(tile)

    def getTile(self,*pos):
        for tile in self.tiles:
            if tile.pos == pos:
                return tile
    
    def getTileAroundGap(self):
        gRow,gCol = self.gap.pos 
        return self.getTile(gRow,gCol-1),self.getTile(gRow-1,gCol),self.getTile(gRow+1,gCol),self.getTile(gRow,gCol+1)

    def changeGap(self,tile):
        gPos = self.gap.pos 
        self.gap.pos = tile.pos 
        tile.pos = gPos

    def slide(self,key):
        left,top,down,right = self.getTileAroundGap()
        if key == 'Up':
            self.changeGap(down)
        if key == 'Down':
            self.changeGap(top)
        if key == 'Left':
            self.changeGap(right)
        if key == 'Right':
            self.changeGap(left)
        self.show()


    def shuffle(self):
        random.shuffle(self.tiles)
        i = 0
        for row in range(self.grid):
            for col in range(self.grid):
                self.tiles[i].pos = (row,col)
                i += 1

    def show(self):
        for tile in self.tiles:
            if self.gap != tile:
                tile.show()

    def setGap(self,index):
        self.gap = self.tiles[index]

class Tile(Label):
    def __init__(self,parent,image,pos):
        Label.__init__(self,parent,image = image)

        self.image = image
        self.pos = pos
        self.curPos = pos
    
    def show(self):
        self.grid(row = self.pos[0], column = self.pos[1])

class Board(Frame):
    MAX_BOARD_SIZE = 500
    def __init__(self,parent,image,grid,*args,**kwargs):
        Frame.__init__(self,parent,*args,**kwargs)

        self.parent = parent
        self.grid = grid
        self.image = self.openImage(image)
        self.tileSize = self.image.size[0]/self.grid
        self.tiles = self.createTiles()
        self.tiles.shuffle()
        self.tiles.show()
        self.bindKeys()
    
    def openImage(self,image):
        image = Image.open(image)
        if min(image.size) > self.MAX_BOARD_SIZE:
            image = image.resize((self.MAX_BOARD_SIZE,self.MAX_BOARD_SIZE),Image.ANTIALIAS)
        if image.size[0] != image.size[1]:
            image = image.crop((0,0,image.size[0],image.size[0]))

        return image

    def bindKeys(self):
        self.bind_all("<Key-Up>",self.slide)
        self.bind_all("<Key-Down>",self.slide)
        self.bind_all("<Key-Right>",self.slide)
        self.bind_all("<Key-Left>",self.slide)
    
    def slide(self,event):
        self.tiles.slide(event.keysym)


    def createTiles(self):
        tiles = Tiles(self.grid)
        for row in range(self.grid):
            for col in range(self.grid):
                x0 = col*self.tileSize
                y0 = row*self.tileSize
                x1 = x0+self.tileSize
                y1 = y0+self.tileSize
                tileImage = ImageTk.PhotoImage(image = self.image.crop((x0,y0,x1,y1)))
                tile = Tile(self,tileImage,(row,col))
                tiles.add(tile)
        tiles.setGap(-1)
        return tiles


class Main():
    def __init__(self,parent):
        self.parent = parent

        self.image = StringVar()
        self.grid = IntVar()

        self.createWidgets()

    def createWidgets(self):
        self.mainFrame = Frame(self.parent)
        Label(self.mainFrame,text = 'Sliding Puzzle',font = ('',50)).pack(padx = 10, pady = 10)
        frame = Frame(self.mainFrame)
        Label(frame,text = "Image").grid(sticky = W)
        Entry(frame,textvariable = self.image,width = 50).grid(row = 0, column = 1,padx = 10, pady = 10)
        Button(frame,text = 'Browse',command = self.browse).grid(row = 0, column = 2, pady = 10,padx = 10)
        Label(frame,text = "Grid").grid(sticky = W)
        OptionMenu(frame,self.grid,*[3,4,5,6,7,8,9,10]).grid(row = 0, column = 1,padx = 10, pady = 10,sticky = W)
        frame.pack(padx = 10, pady = 10)
        Button(self.mainFrame,text = 'Start',command = self.start).pack(padx = 10,pady = 10)
        self.mainFrame.pack()
        self.board = Frame(self.parent)
        self.winFrame = Frame(self.parent)

    def start(self):
        image = self.image.get()
        grid = self.grid.get()
        if os.path.exists(image):
            self.board = Board(self.parent,image,grid)
            self.mainFrame.pack_forget()
            self.board.pack()

    def browse(self):
        self.image.set(tkinter.filedialog.askopenfilename(title = "Select Image",filetype = (("png File","*.png"),("jpg File","*.jpg"))))
        

if __name__=="__main__":
    root = Tk()
    Main(root)
    root.mainloop()
