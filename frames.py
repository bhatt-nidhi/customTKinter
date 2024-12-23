import customtkinter as ct
from customtkinter import *
class App():
    def __init__(self):
        super().__init__()
        root=ct.CTk()
        root.title("Frames")
        root.geometry('800x480')

        mf1=ct.CTkFrame(root,fg_color="dark gray",width=800,height=200)
        mf1.pack(side="top",expand=True,fill="both")
        mf2=ct.CTkFrame(root,fg_color="light gray")
        mf2.pack(side="top",expand=True,fill="both")

        frame1=ct.CTkFrame(mf1,fg_color="#17575d",border_color="white",width=300,height=100)
        but1=ct.CTkButton(frame1,fg_color="blue",text="click")
        but1.pack(side="left",padx=60)
        frame1.pack(side="left",expand=True,fill="both")


        frame2=ct.CTkFrame(mf1,fg_color="#d1d137",border_color="white",width=300,height=100)
        checkbox=CTkCheckBox(frame2,text="ckeck me",fg_color="white",text_color="white",border_color="white")
        checkbox.pack(side="left",padx=60)
        frame2.pack(side="right",expand=True,fill="both")

        frame3=ct.CTkFrame(mf2,fg_color="black",border_color="white",width=300,height=100)
        # text=ct.CTkTextbox(frame3,height=10,fg_color="gray")
        # text.pack(side="left")
        lable=ct.CTkLabel(frame3,text_color="white",text=" This is lable")
        lable.pack(side="left",padx=60)
        frame3.pack(side="left",expand=True,fill="both")


        frame4=ct.CTkFrame(mf2,fg_color="#a411a1",border_color="white",width=300,height=100)
        radio=ct.CTkRadioButton(frame4,fg_color="white",text_color="white",text="check it")
        radio.pack(side="left",padx=60)
        frame4.pack(side="right",expand=True,fill="both")


        root.mainloop()
App()