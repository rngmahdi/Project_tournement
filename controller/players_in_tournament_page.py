import customtkinter

class PlayerInTournament(customtkinter.CTk):
    def __init__(self, container):
        super().__init__()
        self.main = container
        self.frame = customtkinter.CTkToplevel(self.main)