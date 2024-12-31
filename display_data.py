import sqlite3
def Database(self):
    # self.withdraw()
    name1 = self.entry.get()
    pass1 = self.entry2.get()
    add1 = self.entry3.get()
    con = sqlite3.connect("data.db")
    print("database id CONNECTED.")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS detail (
                   id INTEGER PRIMARY KEY AUTOINCREMENT ,
                   username TEXT NOT NULL,
                   password TEXT NOT NULL,
                   address TEXT NOT NULL)""")

    print("table created successfully..")
    cur.execute("INSERT INTO detail(username,password,address) VALUES (?,?,?)", (name1, pass1, add1))
    print("data inserted successfully..")
    con.commit()

    cur.execute("SELECT * FROM detail")
    rows = cur.fetchall()

    for row in rows:
        print(row[0], row[1], row[2], row[3])

    self.clear_entries(self.entry, self.entry2, self.entry3)


def clear_entries(self, entry, entry2, entry3):
    self.entry.delete(0, 'end')
    self.entry2.delete(0, 'end')
    self.entry3.delete(0, 'end')

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