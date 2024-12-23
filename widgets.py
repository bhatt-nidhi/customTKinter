import customtkinter as ct
from customtkinter import *
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("Progress bar")
        self.geometry("400x400")
        self._set_appearance_mode("dark")
        self.pb=ct.CTkProgressBar(self)
        self.pb.grid(row=1,column=1,sticky="news")
        self.pb.set(0)  # for decide the starting default pb = 0

        self.but=ct.CTkButton(self,command=self.click,text="click")
        self.but.grid(row=2,column=1,sticky="news",pady=20)
        self.current_progress = 0

    def click(self):
        if self.current_progress < 100:
            self.current_progress += 10
            self.pb.set(self.current_progress / 50) #for how much step to increase
if __name__ == "__main__":
    app = App()
    app.mainloop()

#=========================== check box  ====================================================
import customtkinter as ct
from customtkinter import  *
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x180")
        # self._set_appearance_mode("dark")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure((0, 1), weight=1)

        checkbox1 = ct.CTkCheckBox(self, text="checkbox 1")
        checkbox1.grid(row=0, column=0, padx=(40,0) ,pady=(10, 0), sticky="snew")
        self.checkbox2=ct.CTkCheckBox(self,text="checkbox2")
        self.checkbox2.grid(row=0,column=1,sticky="snew",padx=(0,60),pady=(10, 0))
        self.but=ct.CTkButton(self,text="submit",command=self.button_callback)
        self.but.grid(row=1,padx=(150,0))


    def button_callback(self):
        print("button pressed")

app = App()
app.mainloop()



#==================== radio button =========================================


import customtkinter as ct
from customtkinter import *
class Demo(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("400x350")
        self._set_appearance_mode("light")
        self.title("radio button")
        self.columnconfigure(0,weight=1)
        # self.wm_attributes("-transparentcolor","red")
        self.lab=ct.CTkLabel(self,text="do you like tea?? ")
        self.lab.grid(row=0,column=0,padx=40,pady=30,sticky="news")

        self.radio_var=ct.StringVar(value="other")

        self.rb=ct.CTkRadioButton(self,text="YES",variable=self.radio_var,value="Yes I like",command=self.call_button)
        self.rb.grid(row=1,column=0,padx=(150,0),sticky="news")

        self.rb2 = ct.CTkRadioButton(self, text="NO", variable=self.radio_var,value="No I do not",command=self.call_button)
        self.rb2.grid(row=2, column=0,padx=(150,0),pady=20,sticky="snew")

        self.lab2=ct.CTkLabel(self,text="")
        self.lab2.grid(row=3,column=0,padx=(60,0),pady=40,sticky="news")

    def call_button(self):
        self.lab2.configure(text=self.radio_var.get())
if __name__ == "__main__":
    app = Demo()
    app.mainloop()

# #===================================== segment buttons =============================================
# #
#
import customtkinter as ct
from customtkinter import *
class Segment(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("segment button")
        self.geometry("300x300")
        self.l1=["ABC","DEF","XYZ"]
        self.sb=ct.CTkSegmentedButton(self,values=self.l1,command=self.clicker,corner_radius=5,width=60,height=50)
        self.sb.grid(row=1,column=0,padx=(50,0),pady=30,sticky="nesw")

        # to set default value of the button
        self.sb.set("ABC")

        self.lab=ct.CTkLabel(self,text="")
        self.lab.grid(row=2,column=0,padx=(50,0),pady=50,sticky="nesw")


    def clicker(self,value):
        self.lab.configure(text= f' Hello {self.sb.get()}') # using f string

        # selected_value = self.sb.get()            # to print via variable
        # self.lab.configure(text=selected_value)
if __name__ == '__main__':
    app=Segment()
    app.mainloop()

# # ================= slider =======================================================
#
#
import customtkinter as ct
from customtkinter import *
class Slide(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("segment button")
        self.geometry("300x300")
        self.sld=ct.CTkSlider(self,to=100,from_=0,command=self.slide)
        self.sld.grid(row=1,column=0, padx=(50, 0), pady=30, sticky="nesw")
        self.lab = ct.CTkLabel(self, text="")
        self.lab.grid(row=2, column=0, padx=(50, 0), pady=50, sticky="nesw")

        self.sld.set(0)

    def slide(self,value):
        self.lab.configure(text=f" The progress is : {value}")

if __name__ == '__main__':
    app=Slide()
app.mainloop()
#



#========================== Tab view ======================================
import customtkinter as ct
from customtkinter import *
class Tab(ct.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("600x400")
        self.title("tab view")
        self.tab=ct.CTkTabview(self,
        segmented_button_fg_color="#7b13a6",
        segmented_button_unselected_color="#132ca6",
        )
        self.tab.grid(row=1,column=1,padx=(40,0),pady=(30,0))
        self.tab1=self.tab.add(" Tab 1")
        self.tab2=self.tab.add(" Tab 2")

        self.but1=ct.CTkButton(self,text="click me!!")
        self.but1.grid(row=1,column=1,padx=(40,0),pady=(50,0))

if __name__ == '__main__':
    app=Tab()
    app.mainloop()

#===================================== new window ==========================


import customtkinter as ct
from customtkinter import *

class App(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Main Window")
        self.geometry("400x300")
        self.open_but = ct.CTkButton(self, text="Open New Window", command=self.open_new_window)
        self.open_but.pack(pady=20)
        set_appearance_mode("dark")


    def open_new_window(self):
        new_window = ct.CTkToplevel(self,fg_color="white")
        new_window.title("New  Window")
        new_window.geometry("600x600")
        set_default_color_theme("green")
        # new_window._set_appearance_mode("system")

        label = ct.CTkLabel(new_window, text="Helloo !!",text_color="black")
        label.grid(row=0,column=0,padx=20,pady=10)


        str_var = ct.StringVar(value="on")
        sw=ct.CTkSwitch(new_window,text="switch",variable=str_var,onvalue="on",offvalue="off")
        sw.grid(row=1,column=0,padx=20)


        button = ct.CTkButton(new_window, text="Close Window", command=new_window.destroy)
        button.grid(row=2,column=0,padx=20,pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()

#============================== custom fonts ===============================================

# import customtkinter as ct
# from tkinter import font
#
#
# class App(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Custom Font Example")
#         self.geometry("400x300")
#
#         self.custom_font = ct.CTkFont(family="Helvetica", size=16, weight="bold")
#
#         self.label = ct.CTkLabel(self, text="Hello everyone", font=self.custom_font)
#         self.label.pack(pady=20)
#
#         self.button = ct.CTkButton(self, text="click me",command=self.change)
#         self.button.pack(pady=20)
#     def change(self):
#         self.custom_font.configure(underline=True,size=32)
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()


#==========================================  COMBO BOX ================================================
# import customtkinter as ct
# from customtkinter import *
#
# class Check(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("300x300")
#         self.title("check box")
#         set_appearance_mode("dark")
        # self.lab=ct.CTkLabel(self,text="pick a color")
        # self.lab.grid(row=0,column=0,padx=(30,0),pady=(40,0))
        #
        # self.color=["yellow","red","pink","blue"]
        # self.cb=ct.CTkComboBox(self,values=self.color,fg_color="black")
        # self.cb.grid(row=0,column=0,padx=(40,0),pady=(100,0))
#
# if __name__ == '__main__':
#     app=Check()
#     app.mainloop()


#======================================================== scroll bar =================================================
#
# import customtkinter as ct
# from customtkinter import *
# class Scroll(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("300x300")
#         self.title("scroll bar")
#         self.sc=ct.CTkScrollableFrame(self,label_text="Colors",label_fg_color="gray",label_text_color="white")
#         self.sc.grid(row=0,column=0,padx=40,pady=20)
#         self.value=["red","white","black","red","white","black","red","white","black"]
#         for index,color in enumerate(self.value):
#             ct.CTkButton(self.sc,text=color).pack(pady=10)
# if __name__ == '__main__':
#     app=Scroll()
#     app.mainloop()

#=========================== Widget Animation ==========================================================

# import customtkinter as ct
# from customtkinter import *
#
# class Animation(ct.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.geometry("400x400")
#         self.but=ct.CTkButton(self,text="up")
#         self.but.grid(row=0,column=0,pady=(30,0),padx=(30,0))
#
#         self.but = ct.CTkButton(self, text="down")
#         self.but.grid(row=0, column=1, pady=(30, 0), padx=(30, 0))
#
#         self.t1=ct.CTkTextbox(self,width=100,height=50,fg_color="gray")
#         # self.t1.place(x=700/2,y=450/2,anchor="center")
#         self.t1.grid(row=1,column=0,padx=(70,0),pady=(40,0))
#
#
# if __name__ == '__main__':
#     app=Animation()
#     app.mainloop()

#========================== IMAGES ========================

# import customtkinter as ct
# from customtkinter import  *
# from PIL import Image, ImageTk
# # import  os
#
# class Img(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x400")
#         self.title("images")

#         self.img_path=os.path.join(os.path.dirname(__file__),"../images/map.jpg")
#         self.img = Image.open(self.img_path)
#         self.img1=ct.CTkImage(dark_image=self.img,size=(300,300))
#
#
#         # can also give size this way
#         # self.re_img = self.img.resize((400, 200))
#         # self.img1=ImageTk.PhotoImage(self.re_img) # we can also use this function instead.
#
#
#         self.lab=ct.CTkLabel(self,text="",image=self.img1)
#         self.lab.grid(row=1,column=1)
# if __name__ == '__main__':
#     app=Img()
#     app.mainloop()


#
# import customtkinter as ct
# from customtkinter import *
# from PIL import Image, ImageTk
#
# class Switch(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("300x300")
#
#         self.str_var=ct.StringVar(value="on")
#         self.title("switch button")
#         set_appearance_mode("dark")
#         self.sw=ct.CTkSwitch(self,text="switch",command=self.swicher,variable=self.str_var,onvalue=" it is on",
#                              offvalue="it is off",fg_color="red")
#         self.sw.grid(row=0,column=0,padx=20,pady=20)
#
#
#         self.lab=ct.CTkLabel(self,text="")
#         self.lab.grid(row=1,column=0)
#
#     def swicher(self):
#         self.lab.configure(text=self.sw.get())
#
# if __name__ == '__main__':
#     app=Switch()
#     app.mainloop()