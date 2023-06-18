import customtkinter
app = customtkinter.CTk()
app.geometry("400x300")

# def segmented_button_callback(value):
#     print("segmented button clicked:", value)


# segemented_button = customtkinter.CTkSegmentedButton(app, values=["Value 1", "Value 2", "Value 3"],
#                                                      command=segmented_button_callback)
# segemented_button.pack()

# def switch_event():
#     print("switch toggled, current value:", switch_var.get())

# switch_var = customtkinter.StringVar(value="on")
# switch = customtkinter.CTkSwitch(app, text="CTkSwitch", command=switch_event,
#                                  variable=switch_var, onvalue="on", offvalue="off").pack()
def optionmenu_callback(choice):
    print("optionmenu dropdown clicked:", choice)

optionmenu = customtkinter.CTkOptionMenu(app, values=["option 1", "option 2"],
                                         command=optionmenu_callback)
optionmenu.pack()
# optionmenu.set("Edit")
app.mainloop()
