from tkinter import * 
from tkinter import ttk
import customtkinter

root = Tk()
root.title("Tournament manegements")
root.state("zoomed")
root.geometry("800x700")

########################################################################

def tournament_list():
      window = TournamentList(root)
      # root.quit()


button = customtkinter.CTkButton(root, text="Create new tournament",
                                 font=("Bahnschrift Light Condensed",40,"bold"),
                                 command=tournament_list)
button.configure(fg_color="#37CEFE",width=400,height=80)
button.pack(pady=20,padx=20)
button.place(anchor = CENTER, relx = .5, rely = .55)

root.mainloop()