import tkinter.ttk
import customtkinter as ct
from customtkinter import*
import sqlite3

class Form(ct.CTk):
    def __init__(self):
        super().__init__()
        self.title("Login form")
        # self.geometry("640x300")
        # self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")

        #to keep window in center
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = 800
        window_height = 600


        position_top = int((screen_height - window_height) / 2)
        position_left = int((screen_width - window_width) / 2)

        self.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

        self.main_window()


    def main_window(self):
        self.button_frame = ct.CTkFrame(self, fg_color="#050c35")
        self.button_frame.grid(row=1,column=0,padx=10,pady=10,sticky="w")
        # self.button_frame.pack(fill="both",expand="True")
        self.Treeview()


        # self.but1 = ct.CTkButton(self.button_frame, text="READ",command=self.Treeview) # to view the data
        # self.but1.grid(row=1, column=1, padx=10, pady=10, sticky="news")
        self.but2 = ct.CTkButton(self.button_frame, text="INSERT", command=self.login)
        self.but2.grid(row=2,column=1,sticky="e",padx=30,pady=8)

        self.but3 = ct.CTkButton(self.button_frame, text="UPDATE",command=self.update)
        self.but3.grid(row=2,column=2,padx=10,sticky="e",pady=8)

        self.but4 = ct.CTkButton(self.button_frame, text="DELETE",command=lambda :[self.delete(),self.inputbox3()])
        self.but4.grid(row=2,column=3,padx=10,sticky="e",pady=8)

        # self.grid_rowconfigure(1, weight=0)
        self.grid_columnconfigure(0, weight=1)

    def inputbox(self):

        self.dialog_frame = ct.CTkFrame(self.button_frame, fg_color="#33325d", width=300, height=50)
        self.dialog_frame.grid(row=0, column=2, padx=10, pady=10)

        self.dialog_label = ct.CTkLabel(self.dialog_frame, text="record inserted successfully", fg_color="white",
                                        font=("Arial", 12, "bold"))
        self.dialog_label.grid(row=0, column=0, padx=10, pady=20)

        self.after(3000, self.remove_inputbox)


    def inputbox2(self):

        self.dialog_frame = ct.CTkFrame(self.button_frame, fg_color="#33325d", width=300, height=50)
        self.dialog_frame.grid(row=0, column=2, padx=10, pady=10)

        self.dialog_label = ct.CTkLabel(self.dialog_frame, text="record updated successfully", fg_color="white",
                                        font=("Arial", 12, "bold"))
        self.dialog_label.grid(row=0, column=0, padx=10, pady=20)

        self.after(3000, self.remove_inputbox)

    def inputbox3(self):

        self.dialog_frame = ct.CTkFrame(self.button_frame, fg_color="#33325d", width=300, height=50)
        self.dialog_frame.grid(row=0, column=2, padx=10, pady=10)

        self.dialog_label = ct.CTkLabel(self.dialog_frame, text="record deleted successfully", fg_color="white",
                                        font=("Arial", 12, "bold"))
        self.dialog_label.grid(row=0, column=0, padx=10, pady=20)

        self.after(3000, self.remove_inputbox)

    def remove_inputbox(self):
        self.dialog_frame.grid_forget()

    def login(self):

        treeview = ct.CTkToplevel(self, fg_color="black")
        treeview.geometry("390x400")
        treeview.title("login form ")

        #======= to stays top of the front window of treeview.
        treeview.lift()
        treeview.attributes("-topmost", 1)


        self.frame=ct.CTkFrame(treeview,fg_color="#050c35")
        # self.frame.pack(fill="both",expand="True")
        self.frame.grid(row=0,column=0,padx=10,pady=10,sticky="news")
        # #==================== inner frame ===========================
        self.inner_frame=ct.CTkFrame(self.frame,fg_color="#e0e2ee",height=300,width=250)
        self.inner_frame.grid(row=0,column=1,padx=(60,60),pady=50)
        self.inner_frame.grid_propagate(False)

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
                                 command=lambda: [self.Database(),self.main_window(),self.inputbox()])
        self.submit.grid(row=5,column=0,sticky="w",pady=20,padx=(60,0))


    def Database(self):
        # self.withdraw()
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

        print("table created successfully..")
        cur.execute("INSERT INTO detail(username,password,address) VALUES (?,?,?)",(name1,pass1,add1))
        print("data inserted successfully..")
        con.commit()

        cur.execute("SELECT * FROM detail")
        rows = cur.fetchall()

        for row in rows:
            print(row[0],row[1],row[2],row[3])

        self.clear_entries(self.entry, self.entry2,self.entry3)
    def clear_entries(self, entry, entry2,entry3):
        self.entry.delete(0, 'end')
        self.entry2.delete(0, 'end')
        self.entry3.delete(0, 'end')


        #=============== new window ===============================


    def Treeview(self):

        self.tree = tkinter.ttk.Treeview(self.button_frame,height=30)
        self.tree['column'] = ('SR_no','ID', 'USERNAME', 'PASSWORD', 'ADDRESS')

        self.tree.column('#0', width=0)
        self.tree.column('SR_no', anchor='w', width=100)
        self.tree.column('ID', anchor='w', width=350)
        self.tree.column('USERNAME', anchor='w', width=350)
        self.tree.column('PASSWORD', anchor='w', width=350)
        self.tree.column('ADDRESS', anchor='w', width=380)

        self.tree.heading('SR_no', text='SR.NO', anchor='w')
        self.tree.heading('ID', text='ID', anchor='w')
        self.tree.heading('USERNAME', text='Username', anchor='w')
        self.tree.heading('PASSWORD', text='Password', anchor='w')
        self.tree.heading('ADDRESS', text='Address', anchor='w')



        self.sb = tkinter.ttk.Scrollbar(self.button_frame, orient="vertical", command=self.tree.yview)
        self.sb.grid(row=0, column=5, sticky='nsw')

        self.tree.configure(yscrollcommand=self.sb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")

        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM detail")
        rows = cur.fetchall()

        for index,row in enumerate(rows,start=1):
            self.tree.insert('', 'end', values=(index,row[0], row[1], row[2], row[3]))
        # tree.pack(fill="both", expand=True)
        self.tree.grid(row=0,column=1,columnspan=5,padx=10,pady=10,sticky="news")

        count = len(rows)
        self.lab = ct.CTkLabel(self, bg_color="#050c35",text=f"Records: {count}", font=("Arial", 12, "bold"),
                               text_color="white")
        self.lab.grid(row=1,padx=(20,0), column=0,pady=(0,20),sticky="ws")

        self.tree.grid_propagate(False)
        con.close()

    def update(self):

        self.update_form()

        focus = self.tree.focus()
        values = self.tree.item(focus, "values")

        self.idd.insert(0, values[0])
        self.entry.insert(0, values[1])
        self.entry2.insert(0, values[2])
        self.entry3.insert(0, values[3])

    def update_form(self):
        # Create a new window for updating
        self.update_window = ct.CTkToplevel(self)
        self.update_window.geometry("390x400")
        self.update_window.title("Update Form")

        self.frame = ct.CTkFrame(self.update_window, fg_color="#050c35")
        self.frame.pack(fill="both", expand=True)

        self.inner_frame = ct.CTkFrame(self.frame, fg_color="#e0e2ee", height=300, width=300)
        self.inner_frame.pack(padx=(60, 60), pady=50)
        self.inner_frame.grid_propagate(False)

        self.lab = ct.CTkLabel(self.inner_frame, text="Update", font=("Arial", 20))
        self.lab.grid(row=1, column=0, padx=100, pady=10)

        self.id = ct.CTkLabel(self.inner_frame, text="ID", font=("Arial", 12, "bold"))
        self.id.grid(row=2, column=0, padx=(10, 0), pady=10, sticky="w")

        self.idd = ct.CTkEntry(self.inner_frame)
        self.idd.grid(row=2, column=0, sticky="e")

        self.name = ct.CTkLabel(self.inner_frame, text="Username", font=("Arial", 12, "bold"))
        self.name.grid(row=3, column=0, padx=(10, 0), pady=10, sticky="w")

        self.entry = ct.CTkEntry(self.inner_frame)
        self.entry.grid(row=3, column=0, sticky="e")

        self.password = ct.CTkLabel(self.inner_frame, text="Password", font=("Arial", 12, "bold"))
        self.password.grid(row=4, column=0, sticky="w", padx=10, pady=10)

        self.entry2 = ct.CTkEntry(self.inner_frame)
        self.entry2.grid(row=4, column=0, sticky="e")

        self.add = ct.CTkLabel(self.inner_frame, text="Address", font=("Arial", 12, "bold"))
        self.add.grid(row=5, column=0, sticky="w", padx=10, pady=10)

        self.entry3 = ct.CTkEntry(self.inner_frame)
        self.entry3.grid(row=5, column=0, sticky="e")

        self.submit = ct.CTkButton(self.inner_frame, text="Update", font=("Arial", 12, "bold"), fg_color="#33325d",
                                   command=lambda:[self.perform_update(),self.inputbox2()])
        self.submit.grid(row=6, column=0, sticky="w", pady=20, padx=(60, 0))

    def perform_update(self):
        id = self.idd.get()
        name1 = self.entry.get()
        pass1 = self.entry2.get()
        add1 = self.entry3.get()

        # Update the database
        con = sqlite3.connect("data.db")
        cur = con.cursor()

        cur.execute("""
                UPDATE detail SET username = ?, password = ?, address = ?  WHERE id = ?  """,
                    (name1, pass1, add1, id))

        con.commit()
        con.close()


        self.Treeview()

        self.update_window.destroy()
    def delete(self):
        focus = self.tree.focus()
        values = self.tree.item(focus, "values")

        id = values[0]
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute("DELETE FROM detail WHERE id=?", (id,))

        con.commit()
        con.close()
        self.Treeview()


if __name__ == '__main__':
    app=Form()
    app.mainloop()
    # app.Database()