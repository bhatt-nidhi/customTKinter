import tkinter.ttk
import customtkinter as ct
from customtkinter import*
import sqlite3

class Form(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login form")
        self.geometry("390x400")
        self.login()

    def login(self):

        self.frame=ct.CTkFrame(self,fg_color="#050c35")
        self.frame.pack(fill="both",expand="True")

        # #==================== inner frame ===========================
        self.inner_frame=ct.CTkFrame(self.frame,fg_color="#e0e2ee",height=300,width=250)
        self.inner_frame.grid(row=0,column=1,padx=(60,60),pady=50)
        self.inner_frame.grid_propagate(False)
        # self.inner_frame.columnconfigure(1,weight=2)
        #=============================================================

        self.lab=ct.CTkLabel(self.inner_frame,text="Login",font=("Arial",20))
        self.lab.grid(row=1,column=0,padx=100,pady=10)


        self.name=ct.CTkLabel(self.inner_frame,text="Username",font=("Arial",12,"bold"))
        self.name.grid(row=2,column=0,padx=(10,0),pady=10,sticky="w")

        self.entry=ct.CTkEntry(self.inner_frame)
        self.entry.grid(row=2,column=0,sticky="e")

        self.password=ct.CTkLabel(self.inner_frame,text="password",font=("Arial",12,"bold"))
        self.password.grid(row=3,column=0,sticky="w",padx=10,pady=10)

        self.entry2=ct.CTkEntry(self.inner_frame)
        self.entry2.grid(row=3,column=0,sticky="e")

        self.add = ct.CTkLabel(self.inner_frame, text="Address", font=("Arial", 12,"bold"))
        self.add.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        self.entry3 = ct.CTkEntry(self.inner_frame)
        self.entry3.grid(row=4, column=0, sticky="e")

        self.submit=ct.CTkButton(self.inner_frame,text="Login",font=("Arial",12,"bold"),fg_color="#33325d",
                                 command=lambda: [self.Database(), self.new_window()])
        self.submit.grid(row=5,column=0,sticky="w",pady=20,padx=(60,0))


    def Database(self):
        self.withdraw()
        name1=self.entry.get()
        pass1=self.entry2.get()
        add1=self.entry3.get()
        con=sqlite3.connect("data.db")
        print("database id CONNECTED.")
        cur=con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS detail (
                    id INTEGER PRIMARY KEY AUTOINCREMENT ,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL,
                    address TEXT NOT NULL)""")


        print("table creates successfully..")
        cur.execute("INSERT INTO detail(username,password,address) VALUES (?,?,?)",(name1,pass1,add1))
        print("data inserted successfully..")
        con.commit()

        cur.execute("SELECT * FROM detail")
        rows = cur.fetchall()

        for row in rows:
            print(row[0],row[1],row[2],row[3])


        #=============== new window ===============================

    def new_window(self):
        treeview = ct.CTkToplevel(self.frame, fg_color="black")
        treeview.geometry("750x200")
        treeview.title("display the data")

        button_frame = ct.CTkFrame(treeview)
        button_frame.grid(row=0,column=0,padx=10,pady=10,sticky="w")

        but1 = ct.CTkButton(button_frame, text="READ",command=self.Treeview) # to view the data
        but1.grid(row=0, column=1, padx=10, pady=10, sticky="news")


        but2 = ct.CTkButton(button_frame, text="INSERT", command=self.login())
        but2.grid(row=0,column=3,padx=10,pady=10,sticky="news")

        but3 = ct.CTkButton(button_frame, text="UPDATE")
        but3.grid(row=0,column=4,padx=10,pady=10)


        but4 = ct.CTkButton(button_frame, text="DELETE")
        but4.grid(row=0,column=5,padx=10,pady=10)


    def Treeview(self):
        treeview: CTkToplevel = ct.CTkToplevel(self)
        treeview.geometry("390x400")
        treeview.title("display the data")

        tree = tkinter.ttk.Treeview(treeview)
        tree['column'] = ('ID', 'USERNAME', 'PASSWORD', 'ADDRESS')

        tree.column('#0', width=0)
        tree.column('ID', anchor='w', width=50)
        tree.column('USERNAME', anchor='w', width=50)
        tree.column('PASSWORD', anchor='w', width=50)
        tree.column('ADDRESS', anchor='w', width=50)

        tree.heading('ID', text='ID', anchor='w')
        tree.heading('USERNAME', text='Username', anchor='w')
        tree.heading('PASSWORD', text='Password', anchor='w')
        tree.heading('ADDRESS', text='Address', anchor='w')

        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM detail")
        rows = cur.fetchall()

        for row in rows:
            tree.insert('', 'end', values=(row[0], row[1], row[2], row[3]))
        tree.pack(fill="both", expand=True)
        con.close()


if __name__ == '__main__':
    app=Form()
    app.mainloop()
    # app.Database()