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
def slider_event(value):
    print(value)
slider = customtkinter.CTkSlider(app, from_=0, to=100, command=slider_event).pack()
# optionmenu.set("Edit")
app.mainloop()
