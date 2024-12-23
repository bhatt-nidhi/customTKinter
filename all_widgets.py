import customtkinter as ct
from customtkinter import *
from PIL import Image, ImageTk

class App(ct.CTk):
    def __init__(self):
        super().__init__()

        #====================== main window =====================
        self.geometry("300x300")
        self.title("window")

        self.but=ct.CTkButton(self,text="click ",command=self.open_new_window)
        self.but.grid(row=0,column=1,padx=80,pady=100)

    def open_new_window(self):
        self.nw=ct.CTkToplevel(self)
        self.nw.geometry("700x600")
        # self.nw.geometry("750x600")
        self.nw.title("New frame")

        #========================= first frame with checkbox =====================
        self.nw.columnconfigure(0,weight=1)
        self.nw.columnconfigure(1,weight=1)

        self.nw.rowconfigure(0,weight=1)
        self.nw.rowconfigure(1,weight=1)
        self.nw.rowconfigure(2,weight=1)
        self.nw.rowconfigure(3,weight=0)


        self.frame1=ct.CTkFrame(self.nw,fg_color="gray",width=300)
        self.frame1.grid(row=0,column=0,padx=(20,0),pady=(10,0),sticky="sewn")
        self.frame1.grid_propagate(False)

        self.frame1.grid_columnconfigure(0, weight=1)
        # self.frame1.grid_rowconfigure((0, 1), weight=0)

        self.checkbox1 = ct.CTkCheckBox(self.frame1, text="checkbox 1")
        self.checkbox1.grid(row=0, column=0, sticky="snew",padx=(10,0),pady=(10,0))

        self.checkbox2 = ct.CTkCheckBox(self.frame1, text="checkbox2")
        self.checkbox2.grid(row=0, column=1, sticky="snew", padx=(0,10),pady=(10,0))

        self.checkbox3 = ct.CTkCheckBox(self.frame1, text="checkbox3")
        self.checkbox3.grid(row=1, column=0, sticky="snew",padx=(10,0),pady=(10,0))

        self.checkbox4 = ct.CTkCheckBox(self.frame1, text="checkbox4")
        self.checkbox4.grid(row=1, column=1, sticky="snew", padx=(0,10),pady=(10,0))

        self.but = ct.CTkButton(self.frame1, text="submit",fg_color="#35334e",hover_color="#53131d") #command=self.button_callback
        self.but.grid(row=2,column=0,columnspan=2,pady=(30,0))

    # def button_callback(self):
    #     print("button pressed")

#======================================  4 frame  with slider ===============================================
        self.frame4=ct.CTkFrame(self.nw,fg_color="#533838",height=200,width=30)
        self.frame4.grid(row=0,column=1,pady=(10,0),sticky="snew",padx=(10,10),rowspan=2)

        self.sld = ct.CTkSlider(self.frame4, to=100, from_=0) #command=self.slide
        self.sld.grid(row=1, column=0, padx=(50, 0), pady=30, sticky="nesw")

    #     self.lab = ct.CTkLabel(self.frame4, text="",text_color="white")
    #     self.lab.grid(row=2, column=0, padx=10, pady=20, sticky="nesw")
    #
    #     self.sld.set(0)
    #
    # def slide(self, value):
    #     self.lab.configure(text=f" The progress is : {value}")

        self.img_path=os.path.join(os.path.dirname(__file__),"../images/map.jpg")
        self.img = Image.open(self.img_path)
        self.img1=ct.CTkImage(dark_image=self.img,size=(240,200))

        self.lab = ct.CTkLabel(self.frame4, text="", image=self.img1)
        self.lab.grid(row=2,column=0,columnspan=2,padx=(20,0),pady=(0,10))


#===============================    frame 2 with radio button =====================================================



        self.frame2=ct.CTkFrame(self.nw,fg_color="gray",width=100)
        self.frame2.grid(row=1,column=0,padx=(20,0),pady=(10,0),sticky="snew")
        self.frame2.grid_propagate(False)

        self.frame2.grid_columnconfigure(0,weight=1)
        self.radio=ct.CTkRadioButton(self.frame2,text="Oprion A")
        self.radio.grid(row=0,column=0,sticky='snew',padx=20,pady=10)

        self.radio = ct.CTkRadioButton(self.frame2, text="Option B")
        self.radio.grid(row=1, column=0, sticky='snew',padx=20,pady=10)

        self.radio = ct.CTkRadioButton(self.frame2, text="Oprion C")
        self.radio.grid(row=0, column=1, sticky='snew', padx=20, pady=10)

        self.radio = ct.CTkRadioButton(self.frame2, text="Option D")
        self.radio.grid(row=1, column=1, sticky='snew', padx=20, pady=10)

        self.submit=ct.CTkButton(self.frame2,text="submit",fg_color="#35334e")
        self.submit.grid(row=2,column=0,columnspan=2,pady=(30,0),padx=(50,0))


#==================================frame3 with Tabview ==========================================================

        self.frame3= ct.CTkFrame(self.nw, fg_color="gray")
        self.frame3.grid(row=2, column=0, padx=(20,0), pady=(10,10),sticky="news")
        self.tab = ct.CTkTabview(self.frame3,
                                 segmented_button_fg_color="#7b13a6",
                                 segmented_button_unselected_color="#132ca6",
                                 width=80,height=120,text_color="white")
        self.tab.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
        self.tab1 = self.tab.add(" Tab 1")
        self.tab2 = self.tab.add(" Tab 2")

        # self.but1 = ct.CTkButton(self.frame3, text="click me!!")
        # self.but1.grid(row=0, column=, padx=(40, 0), pady=(50, 0))

#----------------- second widget combo box ----------------------------

        self.lab = ct.CTkLabel(self.frame3, text="pick a color")
        self.lab.grid(row=0, column=1, padx=(10, 0))

        self.color = ["yellow", "red", "pink", "blue"]
        self.cb = ct.CTkComboBox(self.frame3, values=self.color, fg_color="#533838")
        self.cb.grid(row=0, column=1, padx=(10, 0),rowspan=2)


#----------------------------------  segment button ---------------------------------------

        self.l1 = ["ABC", "DEF", "XYZ"]
        self.sb = ct.CTkSegmentedButton(self.frame3, values=self.l1,  corner_radius=5, width=60,
                                        height=50,command=self.clicker) #
        self.sb.grid(row=1, column=0, padx=(50, 0),sticky="news",pady=10)

        self.sb.set("ABC")


        self.lab = ct.CTkLabel(self.frame3, text="",width=40,height=20)
        self.lab.grid(row=2, column=0, sticky="news")

    def clicker(self, value):
        self.lab.configure(text=f' Hello {self.sb.get()}')  # using f string

#============================ frame 5 with scrollbar ===================================


        self.frame5=ct.CTkFrame(self.nw,fg_color="#533838")
        self.frame5.grid(row=2,column=1,pady=(10,10),sticky="snew",padx=(10,10))

        self.sc = ct.CTkScrollableFrame(self.frame5, label_text="Colors", label_fg_color="gray",
                                        label_text_color="white")

        self.sc.grid(row=0,column=0,padx=40,pady=20)
        self.value=["red","white","black","red","white","black","red","white","black"]
        for index,color in enumerate(self.value):
              ct.CTkButton(self.sc,text=color).pack(pady=10)

#=========================================================================================


        self.but=ct.CTkButton(self.nw,text="close window",command=self.nw.destroy)
        self.but.grid(row=3,column=0,columnspan=2,padx=20)


if __name__ == '__main__':
    app=App()
    app.mainloop()