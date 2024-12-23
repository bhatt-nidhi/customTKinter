from tkinter import Frame

import customtkinter
import customtkinter as ct
from customtkinter import *
root=ct.CTk()
ct.set_default_color_theme("dark-blue")
ct.set_appearance_mode("dark")


# customtkinter.set_widget_scaling(100.00)  # widget dimensions and text size
# customtkinter.set_window_scaling(100.10)  # window geometry dimensions


# root.title("custon tkinter")
# mybutton=ct.CTkButton(root,text="done",border_color="white",border_width=2,text_color="pink",padx=20,command=print("button clicked.."))

# mybutton.pack(pady=20)

import customtkinter as ct

# Create the main window
root = ct.CTk()

# Create buttons with different 'side' values
button1 = ct.CTkButton(root, text="Top", width=200)
button2 = ct.CTkButton(root, text="Bottom", width=200)
button3 = ct.CTkButton(root, text="Left", width=200)
button4 = ct.CTkButton(root, text="Right", width=200)


button1.pack(side="top")
button2.pack(side="bottom")
button3.pack(side="left")
button4.pack(side="right")

root.geometry("500x500")


root.mainloop()


#fames

#
# frame=ct.CTkFrame(root,width=500,height=500,fg_color="blue",border_color="white",border_width=10,corner_radius=20)
# frame.pack()
# root.geometry("600*400")
root.mainloop()


# https://www.plus2net.com/python/tkinter-rowconfigure.php
