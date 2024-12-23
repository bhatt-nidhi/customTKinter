from operator import index

import customtkinter as ct
from customtkinter import *
class App(ct.CTk):
    def __init__(self):
        super().__init__()
        root=ct.CTk()
        root.title("Grid System")
        # ct.set_appearance_mode("system")
        root.geometry("400x400")
        ct.set_appearance_mode("dark")
#
#         # mainframe = CTkFrame(self, fg_color="gray")
#         # mainframe.pack(expand=True, fill="both")
#
#         #============== INNER FRAME ===================
#         inner=CTkFrame(self,fg_color="#9374a0",height=60,width=800)
#         inner.grid(row=0,column=0,sticky="snew")
#         # inner.grid_columnconfigure(1,weight=1)
#         # mainframe.rowconfigure(0,weight=1)
#
#         lab=CTkLabel(inner,text="Login Form ",text_color="white")
#         lab.pack(side="left",fill="x",expand=True)
#         # lab.grid(row=0,column=1,sticky="snew")
#         # inner.pack_propagate(False)
#         # inner.grid_rowconfigure(0,weight=1)
#         # inner.grid_columnconfigure(0,weight=1)
# #========================================= middle frame ==========================
#
#
#         midframe = CTkFrame(self, fg_color="#5e5561",height=400,width=700)
#         midframe.grid(row=1, column=0, pady=1, sticky="nsew")
#
#
#         # l1 = CTkLabel(midframe, text="User Name", text_color="white", bg_color="#9374a0", corner_radius=30,width=200)
#         # l1.grid(row=0, column=0, pady=10, padx=(50, 0), sticky="w")
#         # t1 = CTkEntry(midframe, bg_color="white")
#         # t1.grid(row=0, column=1, sticky="snew", pady=10, padx=(0, 10))
#         # midframe.pack_propagate(True)
#         midframe.columnconfigure(0,weight=1)
#         midframe.rowconfigure(1,weight=1)

#======================================================================================
        root.columnconfigure(0,weight=1)
        root.rowconfigure(0,weight=1)
        root.rowconfigure(1,weight=10)
        root.rowconfigure(2,weight=1)



        frametop=ct.CTkFrame(root,fg_color="#9374a0")
        framemiddle=ct.CTkFrame(root,fg_color="#5e5561")
        framelast=ct.CTkFrame(root,fg_color="#9374a0")


            #grid
        frametop.grid(row=0,column=0,sticky="wesn")
        framemiddle.grid(row=1,column=0,sticky="wesn")
        framelast.grid(row=2,column=0,sticky="wesn")

        #label
        l1=ct.CTkLabel(frametop,text="Login Form",font=('Roboto',13))
        l1.grid(row=0,column=0,padx=10)
        frametop.columnconfigure(0,weight=2)
        frametop.rowconfigure(0,weight=2)

        l2= ct.CTkLabel(framemiddle, text="  User Name ",font=('Roboto',15))
        l2.grid(row=0, column=0, padx=10, pady=(30,0))

        t1 = CTkEntry(framemiddle, bg_color="white")
        t1.grid(row=0, column=1, sticky="snew", pady=(30,0), padx=(10, 10))
        framemiddle.columnconfigure(1,weight=2)

        l2 = ct.CTkLabel(framemiddle, text=" Password ", font=('Roboto', 15))
        l2.grid(row=1, column=0, padx=10, pady=(55,0))
        t2 = CTkEntry(framemiddle, bg_color="white")
        t2.grid(row=1, column=1, sticky="snew", pady=(55,0), padx=(10, 10))
        framemiddle.columnconfigure(1, weight=2)

        lab=ct.CTkLabel(framemiddle,text="Forget password?")
        lab.grid(row=2,column=1,sticky="snew")

        lab = ct.CTkLabel(framemiddle, text="or sign with")
        lab.grid(row=3, column=0, sticky="snew",columnspan=2,pady=(20,0))

        lab = ct.CTkButton(framemiddle, text="Sign in with google",fg_color="#9374a0",hover_color="#5e5561")
        lab.grid(row=4, column=0, sticky="snew", pady=(20, 0),columnspan=2)
        # lab.place(anchor="center")

        # framelast.pack_propagate(False)
        l3 = ct.CTkButton(framelast, text="Log in",fg_color="#5e5561")
        l3.grid(row=0, column=1,sticky="snew",padx=(120,0),pady=(12,0))

        root.mainloop()


if __name__ == "__main__":
    app = App()