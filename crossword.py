import tkinter as tk
from tkinter import messagebox

class MainWindow():
    """Main class for constructing the tkinter widgets on a tkinter window 
    on top of the main window with the explanation of the game.
    """
    def __init__(self, master):
        """Create the top level window.

        Args:
            master (tkinter.Tk): window of the general game
        """
        self.top = tk.Toplevel(master)
        self.top.attributes('-topmost', True)
        self.top.attributes('-topmost', False)

    def create_descriptions(self, descriptions, des_font):
        """Create labels with the descriptions of the crossword keys.

        Args:
            descriptions (list): list of strings with the words' definitions
            des_font (int): font size for the description text
        """
        i = 0
        for des in descriptions:
            tk.Label(self.top, text=des, font=('Helvetica', \
                des_font)).grid(row=i, column=0)
            i += 1

    def create_entries(self, let_pos, wid, let_font):
        """Create the entries where the player can write the words and
        implement that after the player has pressed a key, the cursor moves to
        the next entry.

        Args:
            let_pos (list): list of positions for the entries
            wid (int): width of the entries
            let_font (int): font size for the text written on the entries
        """
        self.let_dic = {}
        for pos in let_pos:
            if pos[1] == 5:
                bg_color = '#ccccff'
            else:
                bg_color = '#ffffff'
            self.let_dic[str(pos)] = tk.Entry(self.top, font=('Helvetica', \
                let_font), background = bg_color, width = wid)
            self.let_dic[str(pos)].grid(row=pos[0], column=pos[1])

        entries = [child for child in self.top.winfo_children() if \
            isinstance(child, tk.Entry)]
        for idx, entry in enumerate(entries):
            entry.bind('<Key>', lambda e, idx=idx: self.go_to_entry(e, \
                entries, idx))

    def go_to_entry(self, event, entry_list, this_index):
        """Go to the next or previous entry depending on the key pressed by the
        player. The event.keycode = 8 corresponds to the backspace key

        Args:
            event (tkinter.Event): event: the player has pressed a key
            entry_list (list): list of entries
            this_index (int): index of the position of the entry where the
                player is at
        """
        if event.keycode == 8:
            self.go_to_previous_entry(entry_list, this_index)
        elif event.char == event.keysym:
            self.go_to_next_entry(entry_list, this_index)
        else:
            pass

    def go_to_next_entry(self, entry_list, this_index):
        """Go to the next entry when the player presses a letter key

        Args:
            entry_list (list): list of entries
            this_index (int): index of the position of the entry where the
                player is at
        """
        next_index = (this_index + 1) % len(entry_list)
        entry_list[next_index].focus_set()

    def go_to_previous_entry(self, entry_list, this_index):
        """Go to the previous entry when the player presses a non-letter key,
        such as the backspace

        Args:
            entry_list (list): list of entries
            this_index (int): index of the position of the entry where the
                player is at
        """
        previous_index = (this_index - 1) % len(entry_list)
        entry_list[previous_index].focus_set()
        entry_list[previous_index].delete(0, tk.END)

    def create_next_button(self, img_next):
        """Create a button to check whether the player has correctly filled the
        crossword.

        Args:
            img_next (tkinter.PhotoImage): image displayed in the button
        """
        tk.Button(self.top, height=50, width=50, image=img_next, 
                command=lambda: self.retrieve_input()).grid(row=6, column=10)

    def message_box(self):
        """Generate a warning message in case the message is not correct"""
        root = tk.Toplevel(self.top)
        root.attributes('-topmost', True)
        root.withdraw()
        messagebox.showinfo('Oh oh', 'Mensaje incorrecto. Intentalo otra vez!')
        try:
            root.destroy()
        except:
            pass

    def retrieve_input(self):
        """Read the letters written in the entries on position 5, and compare
        to the correct message. If the written message is correct, the game 
        window is destroyed. Otherwise, a warning message stating that the 
        message is incorrect is shown.
        """
        message = 'NOCHES'
        written_message = ''
        for i in range(0,6):
            let_id = '['+str(i)+', 5]'
            written_message += self.let_dic[let_id].get().upper()

        if message == written_message:
            self.top.destroy()
            self.top.quit()
        else:
            message_box()

def main_crossword(master):
    """Function for the crossword, based on key concepts from balloons. By
    correctly filling the words, the message for the main game is extracted.

    Args:
        master (tkinter.Tk): window of the general game.
    """
    w = MainWindow(master)
    
    descriptions = [
        'Decide la dirección del globo',
        'Ni avión, ni helicóptero, ni zepelín',
        'Donde guardas la fruta y se sube la gente',
        'Vehículo que te rescata por tierra',
        'Calienta el aire para poder volar',
        'Parecen hechas de algodón'
    ]

    let_pos = [
        [0, 2],[0, 3],[0, 4],[0, 5],[0, 6],[0, 7],[1, 1],[1, 2],[1, 3],[1, 4],
        [1, 5],[2, 5],[2, 6],[2, 7],[2, 8],[2, 9],[3, 2],[3, 3],[3, 4],[3, 5],
        [3, 6],[4, 3],[4, 4],[4, 5],[4, 6],[4, 7],[5, 1],[5, 2],[5, 3],[5, 4],
        [5, 5]
    ]

    img_next = tk.PhotoImage(file='figures/0_0_next.png')

    w.create_descriptions(descriptions,16)
    w.create_entries(let_pos, 2, 18)
    w.create_next_button(img_next)    

    w.top.mainloop()