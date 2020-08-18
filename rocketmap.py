# https://stackoverflow.com/questions/44634947/how-to-set-a-turtle-to-a-turtle-screen/44639041#44639041
import tkinter as tk
from turtle import RawTurtle, TurtleScreen

class MapTransitions(tk.Frame):
    def __init__(self, master, destination_msg, rocket_from, rocket_to):
        tk.Frame.__init__(self, master, width=567, height=567)
        w = tk.Canvas(self, width=500, height=500)
        w.pack()
        r = Rocket(w, rocket_from, rocket_to)
        r.set_initial_pos(rocket_from)
        r.move_to(rocket_to)
        tk.Label(self, text=next_destination, font=('Helvetica', 16)).pack()
        self.next_button()        

    def next_button(self):
        """Button that shows the next explanation image when pressed
        """
        f = tk.Frame(self, height=50, width=50)
        f.pack(side='right')
        self.img_next = tk.PhotoImage(file='figures/0_0_next.png')
        self.b_next = tk.Button(f, image=self.img_next, command=self.destroy_frame)
        self.b_next.pack(expand=1)

    def destroy_frame(self):
        self.destroy()
        self.quit()

class Rocket():
    def __init__(self, canvas, initial_place, end_place):
        self.screen = TurtleScreen(canvas)
        self.screen.bgpic('figures/0_0_map.gif')
        self.turtle = RawTurtle(self.screen, visible=False)
        self.turtle.speed('slowest')
        self.turtle.pensize(2)
        self.screen.register_shape('figures/0_0_rocket.gif')
        self.turtle.shape('figures/0_0_rocket.gif')
        self.kingdom_places = {
            'castle': (108,34),
            'photo_village': (-75,-25),
            'train_station': (172,187),
            'labyrinth': (163,-200),
            'balloon': (-219,219),
            'hector': (68,121),
            'sofi': (-113,135)
        }
        self.set_initial_pos(initial_place)
        self.move_to(end_place)

    def set_initial_pos(self, place):
        self.turtle.up()
        self.move_to(place)
        self.turtle.down()
        self.turtle.showturtle()

    def move_to(self, place):
        if place in self.kingdom_places:
            self.turtle.goto(self.kingdom_places[place])

def main():
    root = tk.Tk()    
    next_destination = 'Vayamos primero al pueblo de la fotografía'

    m = MapTransitions(root, next_destination, 'castle', 'photo_village')
    tk.mainloop()

main()