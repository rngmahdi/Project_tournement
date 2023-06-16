from tkinter import *
from tkinter import ttk
class TournamentList:
    def __init__(self,root):
        self.win = Toplevel(root)
        self.screen_height = self.win.winfo_screenheight
        self.screen_width = self.win.winfo_screenwidth
        self.win.geometry("1000x750")
        self.win.title("Tournament List")
        self.menu = Menu(root)
        self.menu.add_cascade(label="Tournament")
        self.win.config(menu=self.menu)
        # self.tournament_menu = (self.menu,)



root = Tk()
window = TournamentList(root)
root.mainloop()
