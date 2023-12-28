import customtkinter 
from PIL import Image


class MessageBox(customtkinter.CTkToplevel):
    def __init__(self,container,message,case):
        super().__init__()
        self.master = container
        self.geometry("230x80")
        self.title(case)
        self.label = customtkinter.CTkLabel(self, text="ToplevelWindow")
        self.message = message
        self.attributes('-topmost', 'true')
        self.case = case
        self.packImage()
        
        # self.mainloop()
    def packImage(self):
        if(self.case == "success"):
            url = "../public/img/success.png"
        elif(self.case == "warning"):
            url = "../public/img/warning.png"
        elif(self.case == "error"):
            url = "../public/img/error.png"
        
        self.img = customtkinter.CTkImage(dark_image=Image.open(url),size=(30,30))
        self.img_bg = customtkinter.CTkLabel(self,image=self.img,text="")
        self.label = customtkinter.CTkLabel(self,text=self.message)
        self.img_bg.grid(row=0,column=1)
        self.label.grid(row=0,column=2)
        