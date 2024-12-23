import customtkinter as ct
from customtkinter import *

class Grid(ct.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Grid System")
        self.geometry("600x600")
        self.resizable(False, False)

        # Main Frame
        mainframe = CTkFrame(self, fg_color="gray")
        mainframe.pack(expand=True, fill="both")

        # Configure Rows and Columns
        mainframe.grid_rowconfigure(0, weight=1)  # Header row
        mainframe.grid_rowconfigure(0, weight=0)  # Middle frame row
        mainframe.grid_columnconfigure(0, weight=1)

        # Header Frame
        fr1 = CTkFrame(mainframe, fg_color="#9374a0",height=200)
        fr1.grid(row=0, column=0, sticky="ew")

        lab = CTkLabel(fr1, text="Login Form", text_color="white")
        lab.pack(side="left", fill="x", expand=True)

        # Middle Frame

        midframe = CTkFrame(mainframe, fg_color="#5e5561",height=600)
        midframe.grid(row=1, column=0, pady=1, sticky="nsew")

        midframe.grid_columnconfigure(0, weight=1)
        midframe.grid_columnconfigure(1, weight=8)
        # User Name Label and Entry
        l1 = CTkLabel(midframe, text="User  Name", text_color="white", bg_color="#9374a0", corner_radius=30, width=200)
        l1.grid(row=0, column=0, pady=10, padx=(50, 0), sticky="w")

        t1 = CTkEntry(midframe, bg_color="white")
        t1.grid(row=0, column=1, sticky="ew", pady=10, padx=(0, 10))

        # Password Label and Entry
        l2 = CTkLabel(midframe, text="Password", text_color="white", bg_color="#9374a0", padx=10, corner_radius=40, width=200)
        l2.grid(row=1, column=0, pady=10, padx=(50, 0), sticky="w")

        t2 = CTkEntry(midframe, bg_color="white")
        t2.grid(row=1, column=1, sticky="ew", pady=10, padx=(0, 10))
        # midframe.pack_propagate(False)



        self.mainloop()

if __name__ == "__main__":
     app = Grid()
# Grid()