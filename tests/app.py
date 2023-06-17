# import customtkinter
# from PIL import Image
# from touranement_creation import TouranementCreationPage
# #! Probelm with routing some logic is missing
# #! Probelm with routing some logic is missing
# #! Probelm with routing some logic is missing
# #! Probelm with routing some logic is missing
# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Tournament Manager")
#         self.geometry("600x500")
        
#         # Main
#         self.rowconfigure(0,weight=2)
#         self.rowconfigure(1,weight=1)
#         self.columnconfigure(0,weight=1)
        
#         self.img = customtkinter.CTkImage(dark_image=Image.open("./public/img/bg.png"),size=(600,250))
        
#         # Widgets
#         self.imgBg = customtkinter.CTkLabel(self,image=self.img,text="")
#         self.button = customtkinter.CTkButton(self,text="Create a new Account",command=self.start,fg_color="#6C63FF")
        
#         # self.label.grid(row=1,column=0)
#         self.imgBg.grid(row=0,column=0,sticky="ewns",padx=10,pady=10)
#         self.button.grid(row=1,column=0)
        
#         self.mainloop()
        
#     # Methods
#     def start(self):
#         TouranementCreationPage()
    
#     def destroy(self):
#         return self.quit()
    
# App()