# # import customtkinter as ct
# # from customtkinter import *
# # class App():
# #
# #          root=ct.CTk()
# #          root.title("Frames")
# #          root.geometry('800x480')
# #
# #          mf1=ct.CTkFrame(root,fg_color="dark gray")
# #          mf1.pack(side="top",expand=True,fill="both")
# #          mf2=ct.CTkFrame(root,fg_color="light gray")
# #          mf2.pack(side="top",expand=True,fill="both")
# #
# #          frame1=ct.CTkFrame(mf1,fg_color="#17575d",border_color="white")
# #          but1=ct.CTkButton(frame1,fg_color="blue",text="click")
# #          but1.pack(side="left",padx=60)
# #          frame1.pack(side="left",expand=True,fill="both")
# #          frame2=ct.CTkFrame(mf1,fg_color="#d1d137",border_color="white")
# #          checkbox = CTkCheckBox(frame2, text="ckeck me", fg_color="white", text_color="white", border_color="white")
# #          checkbox.pack(side="left",padx=60)
# #          frame2.pack(side="right",expand=True,fill="both")
# #
# #          frame3=ct.CTkFrame(mf2,fg_color="black",border_color="white")
# #          # text=ct.CTkTextbox(frame3,height=10,fg_color="gray")
# #          # text.pack(side="left")
# #          # lable=ct.CTkLabel(frame3,text_color="white",text=" This is lable")
# #         # lable.pack(side="left",padx=60)
# #          frame3.pack(side="left",expand=True,fill="both")
# #
# #
# #          frame4=ct.CTkFrame(mf2,fg_color="#a411a1",border_color="white")
# #          # radio=ct.CTkRadioButton(frame4,fg_color="white",text_color="white",text="check it")
# #          # radio.pack(side="left",padx=60)
# #          frame4.pack(side="right",expand=True,fill="both")
# #
# #          root.mainloop()
# # App()
# #
# #
# #  # import customtkinter as ct
# # # from customtkinter import *
# # #
# # #
# # # class App():
# # #     def __init__(self):
# # #         super().__init__()
# # #
# # #         # Create the main root window
# # #         self.root = ct.CTk()
# # #         self.root.title("Frames")
# # #         self.root.geometry('800x480')
# # #
# # #         # Create the first main frame (mf1) with fixed size
# # #         mf1 = ct.CTkFrame(self.root, fg_color="dark gray", width=800, height=200)
# # #         mf1.pack(side="top", fill="both")
# # #
# # #         # Create the second main frame (mf2) with fixed size
# # #         mf2 = ct.CTkFrame(self.root, fg_color="light gray", width=800, height=280)
# # #         mf2.pack(side="top", fill="both")
# # #
# # #         # Create a subframe inside mf1 (frame1) with fixed size
# # #         frame1 = ct.CTkFrame(mf1, fg_color="#17575d", border_color="white", width=300, height=100)
# # #         but1 = ct.CTkButton(frame1, fg_color="blue", text="Click")
# # #         but1.pack(side="left", padx=60)
# # #         frame1.pack(side="left", expand=False)  # Prevent expansion, keep fixed size
# # #
# # #         # Create another subframe inside mf1 (frame2) with fixed size
# # #         frame2 = ct.CTkFrame(mf1, fg_color="#d1d137", border_color="white", width=300, height=100)
# # #         checkbox = CTkCheckBox(frame2, text="Check me", fg_color="white", text_color="white", border_color="white")
# # #         checkbox.pack(side="left", padx=60)
# # #         frame2.pack(side="right", expand=False)  # Prevent expansion, keep fixed size
# # #
# # #         # Create a subframe inside mf2 (frame3) with fixed size
# # #         frame3 = ct.CTkFrame(mf2, fg_color="black", border_color="white", width=300, height=100)
# # #         label = ct.CTkLabel(frame3, text_color="white", text="This is label")
# # #         label.pack(side="left", padx=60)
# # #         frame3.pack(side="left", expand=False)  # Prevent expansion, keep fixed size
# # #
# # #         # Create another subframe inside mf2 (frame4) with fixed size
# # #         frame4 = ct.CTkFrame(mf2, fg_color="#a411a1", border_color="white", width=300, height=100)
# # #         radio = ct.CTkRadioButton(frame4, fg_color="white", text_color="white", text="Check it")
# # #         radio.pack(side="left", padx=60)
# # #         frame4.pack(side="right", expand=False)  # Prevent expansion, keep fixed size
# # #
# # #         # Run the main event loop
# # #         self.root.mainloop()
# # #
# # #
# # # # Run the application
# # # if __name__ == "__main__":
# # #     app = App()
# #
# # #
# # # import customtkinter as ct
# # #
# # # class MyScrollableCheckboxFrame(ct.CTkScrollableFrame):
# # #     def __init__(self, master, title, values):
# # #         super().__init__(master, label_text=title)  # Initialize the CTkScrollableFrame
# # #         self.grid_columnconfigure(0, weight=1)  # Configure the grid column to expand
# # #         self.values = values  # List of checkbox values
# # #         self.checkboxes = []  # List to store the checkboxes
# # #
# # #         # Loop through the provided values to create checkboxes
# # #         for i, value in enumerate(self.values):
# # #             checkbox = ct.CTkCheckBox(self, text=value)
# # #             checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")  # Place the checkbox in grid
# # #             self.checkboxes.append(checkbox)  # Add to the list of checkboxes
# # #
# # #     def get(self):
# # #         """Returns a list of values of the checked checkboxes."""
# # #         checked_checkboxes = []
# # #         for checkbox in self.checkboxes:
# # #             if checkbox.get() == 1:  # Check if the checkbox is checked
# # #                 checked_checkboxes.append(checkbox.cget("text"))  # Append the text of checked checkbox
# # #         return checked_checkboxes  # Return the list of checked values
# # #
# # # # Sample usage of the MyScrollableCheckboxFrame class in an application
# # # if __name__ == "__main__":
# # #     root = ct.CTk()  # Create the root window
# # #     root.title("Scrollable Checkbox Example")
# # #
# # #     # Define some sample checkbox values
# # #     checkbox_values = ["Option 1", "Option 2", "Option 3", "Option 4", "Option 5"]
# # #
# # #     # Create an instance of the scrollable frame with checkboxes
# # #     scrollable_frame = MyScrollableCheckboxFrame(root, title="Select Options", values=checkbox_values)
# # #     scrollable_frame.pack(padx=20, pady=20, fill="both", expand=True)  # Pack the scrollable frame
# # #
# # #     # A button to print the selected values
# # #     def show_selected():
# # #         selected_values = scrollable_frame.get()
# # #         print("Selected values:", selected_values)
# # #
# # #     button = ct.CTkButton(root, text="Show Selected", command=show_selected)
# # #     button.pack(pady=10)
# # #
# # #     root.mainloop()
#
# #
# # import customtkinter as ctk
# #
# # # Set the appearance mode and default color scheme
# # ctk.set_appearance_mode("light")
# # ctk.set_default_color_theme("blue")
# #
# # # Initialize the main window
# # root = ctk.CTk()
# #
# # # Set the size of the main window
# # root.geometry("400x400")
# #
# # # Create the main gray frame
# # main_frame = ctk.CTkFrame(root, width=300, height=300, corner_radius=10, fg_color="gray")
# # main_frame.grid(row=0, column=0, padx=50, pady=50, sticky="nsew")
# #
# # # Create the inner blue frame
# # inner_frame = ctk.CTkFrame(main_frame, width=250, height=100, corner_radius=10, fg_color="blue")
# # inner_frame.grid(row=0, column=0, padx=25, pady=25, sticky="nsew")
# #
# # # Create the button inside the inner blue frame
# # button = ctk.CTkButton(inner_frame, text="Click Me", width=150, height=40)
# # button.grid(row=0, column=0, padx=20, pady=20)
#
# # Start the main loop to run the application
# # root.mainloop()
# #
# # import customtkinter as ct
# # # from tkinter import mainloop
# # #
# # #
# # # class Grid(ct.CTk):
# # #     def __init__(self):
# # #         super().__init__()
# # #         self.title("Grid System")
# # #         self.geometry("800x800")
# # #
# # #         ###### Main Gray Frame #######
# # #         mainframe = ct.CTkFrame(self, fg_color="gray", width=200, height=200)
# # #         mainframe.pack(expand=True, fill="both")
# # #
# # #         ########### Grid Configuration ##########################
# # #         # Configuring rows and columns for the mainframe
# # #         mainframe.grid_rowconfigure(0, weight=1)  # First row for blue frame, takes 1 part of the space
# # #         mainframe.grid_rowconfigure(1, weight=3)  # Second row (more space for content below)
# # #         mainframe.grid_columnconfigure(0, weight=1)  # One column, span the entire width
# # #
# # #         ########### Blue Frame on Top (Expanding Horizontlaly) ###########
# # #         fr1 = ct.CTkFrame(mainframe, fg_color="blue", height=100)  # Height fixed at 100px
# # #         fr1.grid(row=0, column=0, sticky="ew", padx=10, pady=10)  # Stretch across horizontally with sticky="ew"
# # #
# # #         ########### Button inside Blue Frame ###########
# # #         button = ct.CTkButton(fr1, text="Click Me")
# # #         button.grid(row=0, column=0,padx=20, pady=20)  # Center button inside the blue frame
# #
# #         ########### Expanding Blue Frame Vertically ###########
# #         # We will use weight configuration to allow the blue frame to expand vertically if needed
# #         # mainframe.grid_rowconfigure(0, weight=2)  # Increase weight for top row (blue frame)
# #
# #         # self.mainloop()
# #
# #
# # # Run the application
# # # Grid()
# #
# #
# # #
# # # import customtkinter as ct
# # # from tkinter import mainloop
# # # from customtkinter import *
# # # class Grid(ct.CTk):
# # #     def __init__(self, *args, **kwargs):
# # #         super().__init__(*args, **kwargs)
# # #         self.title("Grid System")
# # #         self.geometry("800x480")
# # #
# # #         mainframe = ct.CTkFrame(self)
# # #         ###### Main frame #######
# # #         mainframe = CTkFrame(self, fg_color="gray", width=200, height=200)
# # #         mainframe.pack(expand=True, fill="both")
# # #
# # #         ########### Inner frames ##########################
# # #         self.grid_rowconfigure(0, weight=1)
# # #         self.grid_rowconfigure(1, weight=3)
# # #         mainframe.grid_columnconfigure(0, weight=1)
# # #
# # #         # Top Frame
# # #         fr1 = CTkFrame(mainframe, fg_color="#9374a0", height=30, width=800)
# # #         fr1.grid(row=0, column=0, sticky="ew")
# # #
# # #         lab = CTkLabel(fr1, text="This is a Label", text_color="white")
# # #         lab.grid(row=0, column=0, padx=350)
# # #
# # #         ########################################### Middle frame ###############################################
# # #
# # #         midframe = CTkFrame(mainframe, width=800, height=300, fg_color="#5e5561")
# # #         midframe.grid(row=1, column=0, pady=1)
# # #         midframe.grid_columnconfigure(0, weight=1)
# # #         midframe.grid_columnconfigure(1, weight=2)  # Ensure that the input space is also resizable.
# # #
# # #         l1 = CTkLabel(midframe, text="User Name", text_color="white", bg_color="transparent")
# # #         l1.grid(row=0, column=0, pady=10, padx=10, sticky="w")
# # #
# # #         # Entry widget for User Name input
# # #         user_entry = CTkEntry(midframe, width=200)
# # #         user_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")
# # #
# # #         self.mainloop()
# # #
# # # Grid()
# #
# # import customtkinter as ct
# # from tkinter import mainloop
# # from customtkinter import *
# #
# # class Grid(ct.CTk):
# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.title("Grid System")
# #         self.geometry("800x480")  # Window size
# #
# #         mainframe = ct.CTkFrame(self)
# #         ###### Main frame #######
# #         mainframe = CTkFrame(self, fg_color="gray", width=200, height=200)
# #         mainframe.pack(expand=True, fill="both")
# #
# #         ########### Inner frames ##########################
# #         self.grid_rowconfigure(0, weight=1)
# #         self.grid_rowconfigure(1, weight=3)
# #         mainframe.grid_columnconfigure(0, weight=1)
# #
# #         # Top Frame
# #         fr1 = CTkFrame(mainframe, fg_color="#9374a0", height=30, width=800)
# #         fr1.grid(row=0, column=0, sticky="ew")
# #
# #         lab = CTkLabel(fr1, text="This is a Label", text_color="white")
# #         lab.grid(row=0, column=0, padx=350)
# #
# #         ########################################### Middle frame ###############################################
# #
# #         # Now midframe will expand and fill the space
# #         midframe = CTkFrame(mainframe, width=800, height=300, fg_color="#5e5561")
# #         midframe.grid(row=1, column=0, pady=1, sticky="nsew")  # Sticky to expand in all directions
# #
# #         # Configuring grid inside midframe
# #         midframe.grid_columnconfigure(0, weight=1)
# #         midframe.grid_columnconfigure(1, weight=2)  # Ensuring input field takes up more space
# #
# #         l1 = CTkLabel(midframe, text="User Name", text_color="white", bg_color="transparent")
# #         l1.grid(row=0, column=0, pady=10, padx=10, sticky="w")  # Align label to the left
# #
# #
# #         # Entry widget for User Name input
# #         user_entry = CTkEntry(midframe, width=200)
# #         user_entry.grid(row=0, column=1, pady=10, padx=10, sticky="ew")  # Entry widget expands horizontally
# #
# #         self.mainloop()
# # Grid()
#
#
#
#
#
# # import customtkinter as ctk
# #
# # # Create the main window
# # root = ctk.CTk()
# #
# # # Set the window size
# # root.geometry("600x400")
# #
# # # Create two responsive frames inside the main window
# # frame_1 = ctk.CTkFrame(master=root)
# # frame_1.grid(row=0, column=0, sticky="nsew")  # sticky to all directions (North, South, East, West)
# #
# # frame_2 = ctk.CTkFrame(master=root)
# # frame_2.grid(row=1, column=0, sticky="nsew")
# #
# # # Add widgets inside the frames
# # label_1 = ctk.CTkLabel(master=frame_1, text="This is Frame 1")
# # label_1.pack(padx=20, pady=20)
# #
# # label_2 = ctk.CTkLabel(master=frame_2, text="This is Frame 2")
# # label_2.pack(padx=20, pady=20)
# #
# # # Set grid weight for responsive resizing
# # root.grid_rowconfigure(0, weight=1)  # Frame 1 expands
# # root.grid_rowconfigure(1, weight=1)  # Frame 2 expands
# # root.grid_columnconfigure(0, weight=1)  # Single column expands
# #
# # # Start the main loop
# # root.mainloop()
#
# #
# #
# # import customtkinter as ct
# # from customtkinter import *
# #
# # class App(ct.CTk):
# #     def __init__(self):
# #         super().__init__()
# #         self.title("Grid System")
# #         self.geometry("800x600")
# #         ct.set_appearance_mode("dark")
# #
# #         # Inner Frame
# #         inner = CTkFrame(self, fg_color="#9374a0", height=60, width=800)
# #         inner.grid(row=0, column=0, sticky="snew")
# #         inner.pack_propagate(False)  # Prevent inner frame from resizing
# #
# #         lab = CTkLabel(inner, text="Login Form", text_color="white")
# #         lab.pack(side="left", fill="x", expand=True)
# #
# #         # Middle Frame
# #         midframe = CTkFrame(self, fg_color="#5e5561", height=400, width=700)
# #         midframe.grid(row=1, column=0, pady=1, sticky="nsew")
# #           # Prevent middle frame from resizing
# #
# #         l1 = CTkLabel(midframe, text="User  Name", text_color="white", bg_color="#9374a0", corner_radius=30, width=200)
# #         l1.grid(row=0, column=0, pady=10, padx=(50, 0), sticky="w")
# #
# #         t1 = CTkEntry(midframe, bg_color="white")
# #         t1.grid(row=0, column=1, sticky="snew", pady=10, padx=(0, 10))
# #         midframe.pack_propagate(False)
# #         midframe.columnconfigure(0, weight=1)
# #
# #         self.mainloop()
# #
# # if __name__ == "__main__":
# #     app = App()
#
#
# # from tkinter import mainloop
# # import customtkinter as ct
# # from customtkinter import *
# #
# #
# # class Grid(ct.CTk):
# #     def __init__(self, *args, **kwargs):
# #         super().__init__(*args, **kwargs)
# #         self.title("Grid System")
# #         self.geometry("600x600")
# #         self.resizable(False, False)
# #
# #         # Main Frame
# #         mainframe = CTkFrame(self, fg_color="gray")
# #         mainframe.pack(expand=True, fill="both")
# #
# #         # Configure Rows and Columns
# #         mainframe.grid_rowconfigure(0, weight=1)  # Header row
# #         mainframe.grid_rowconfigure(0, weight=0)  # Middle frame row
# #         mainframe.grid_columnconfigure(0, weight=1)
# #
# #         # Header Frame
# #         fr1 = CTkFrame(mainframe, fg_color="#9374a0", height=200)
# #         fr1.grid(row=0, column=0, sticky="ew")
# #
# #         lab = CTkLabel(fr1, text="Login Form", text_color="white")
# #         lab.pack(side="left", fill="x", expand=True)
# #
# #         # Middle Frame
# #
# #         midframe = CTkFrame(mainframe, fg_color="#5e5561", height=600)
# #         midframe.grid(row=1, column=0, pady=1, sticky="nsew")
# #
# #         midframe.grid_columnconfigure(0, weight=1)
# #         midframe.grid_columnconfigure(1, weight=8)
# #         # User Name Label and Entry
# #         l1 = CTkLabel(midframe, text="User  Name", text_color="white", bg_color="#9374a0", corner_radius=30, width=200)
# #         l1.grid(row=0, column=0, pady=10, padx=(50, 0), sticky="w")
# #
# #         t1 = CTkEntry(midframe, bg_color="white")
# #         t1.grid(row=0, column=1, sticky="ew", pady=10, padx=(0, 10))
# #
# #         # Password Label and Entry
# #         l2 = CTkLabel(midframe, text="Password", text_color="white", bg_color="#9374a0", padx=10, corner_radius=40,
# #                       width=200)
# #         l2.grid(row=1, column=0, pady=10, padx=(50, 0), sticky="w")
# #
# #         t2 = CTkEntry(midframe, bg_color="white")
# #         t2.grid(row=1, column=1, sticky="ew", pady=10, padx=(0, 10))
# #         # midframe.pack_propagate(False)
# #
# #         self.mainloop()
# #
# #
# # if __name__ == "__main__":
# #     app = Grid()
# # Grid()
#
# from operator import index
#
# # import customtkinter as ct
# # from customtkinter import *
# # class App(ct.CTk):
# #     def __init__(self):
# #         super().__init__()
# #         root=ct.CTk()
# #         root.title("Grid System")
# #         # ct.set_appearance_mode("system")
# #         root.geometry("400x400")
# #         ct.set_appearance_mode("dark")
# #
# #         root.columnconfigure(0,weight=1)
# #         root.rowconfigure(0,weight=1)
# #         root.rowconfigure(1,weight=10)
# #         root.rowconfigure(2,weight=1)
# #
# #
# #
# #         frametop=ct.CTkFrame(root,fg_color="#9374a0")
# #         framemiddle=ct.CTkFrame(root,fg_color="#5e5561")
# #         framelast=ct.CTkFrame(root,fg_color="yellow")
# #
# #
# #             #grid
# #         frametop.grid(row=0,column=0,sticky="wesn")
# #         framemiddle.grid(row=1,column=0,sticky="wesn")
# #         framelast.grid(row=2,column=0,sticky="wesn")
# #
# #         #label
# #         l1=ct.CTkLabel(frametop,text="Login Form",font=('Roboto',13))
# #         l1.grid(row=0,column=0,padx=10)
# #         frametop.columnconfigure(0,weight=2)
# #         frametop.rowconfigure(0,weight=2)
# #
# #
# #         l2= ct.CTkLabel(framemiddle, text="User Name ",font=('Roboto',15))
# #         l2.grid(row=3, column=0, padx=10, pady=2)
# #
# #         t1 = CTkEntry(framemiddle, bg_color="white")
# #         t1.grid(row=3, column=1, sticky="snew", pady=2, padx=(10, 10))
# #         framemiddle.columnconfigure(1,weight=2)
# #
# #         l2 = ct.CTkLabel(framemiddle, text=" Password ", font=('Roboto', 15))
# #         l2.grid(row=6, column=0, padx=10, pady=2)
# #         t2 = CTkEntry(framemiddle, bg_color="white")
# #         t2.grid(row=6, column=1, sticky="snew", pady=2, padx=(10, 10))
# #         framemiddle.columnconfigure(1, weight=2)
# #
# #
# #         l3 = ct.CTkLabel(framelast, text="Login Form")
# #         l3.grid(row=0, column=0, padx=10, pady=2)
# #
# #         root.mainloop()
# #
# #
# # if __name__ == "__main__":
# #     app = App()
#
# import customtkinter as ct
# from customtkinter import *
#
#
# class App(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         root = ct.CTk()
#         root.title("Grid System")
#         root.geometry("400x400")
#         ct.set_appearance_mode("dark")
#
#         root.columnconfigure(0, weight=1)
#         root.rowconfigure(0, weight=1)
#         root.rowconfigure(1, weight=10)
#         root.rowconfigure(2, weight=1)
#
#         frametop = ct.CTkFrame(root, fg_color="#9374a0")
#         framemiddle = ct.CTkFrame(root, fg_color="#5e5561")
#         framelast = ct.CTkFrame(root, fg_color="yellow")
#
#         # Grid layout
#         frametop.grid(row=0, column=0, sticky="wesn")
#         framemiddle.grid(row=1, column=0, sticky="wesn")
#         framelast.grid(row=2, column=0, sticky="wesn")
#
#         # Label
#         l1 = ct.CTkLabel(frametop, text="Login Form", font=('Roboto', 13))
#         l1.grid(row=0, column=0, padx=10)
#         frametop.columnconfigure(0, weight=2)
#         frametop.rowconfigure(0, weight=2)
#
#         l2 = ct.CTkLabel(framemiddle, text="User Name", font=('Roboto', 15))
#         l2.grid(row=0, column=0, padx=10, pady=2)  # Place "Username" label in row 0
#
#         t1 = CTkEntry(framemiddle, bg_color="white")
#         t1.grid(row=1, column=0, columnspan=2, sticky="snew", pady=2, padx=(10, 10))  # Place "Username" entry in row 1
#
#         # Add an empty row for spacing between the username and password fields
#         framemiddle.rowconfigure(2, weight=1)  # Empty row with weight for spacing
#
#         l3 = ct.CTkLabel(framemiddle, text="Password", font=('Roboto', 15))
#         l3.grid(row=3, column=0, padx=10, pady=2)  # Place "Password" label in row 3
#
#         t2 = CTkEntry(framemiddle, bg_color="white")
#         t2.grid(row=4, column=0, columnspan=2, sticky="snew", pady=2, padx=(10, 10))  # Place "Password" entry in row 4
#
#         framemiddle.columnconfigure(0, weight=2)
#
#         l4 = ct.CTkLabel(framelast, text="Login Form")
#         l4.grid(row=0, column=0, padx=10, pady=2)
#
#         root.mainloop()
#
#
# if __name__ == "__main__":
#     app = App()

#
# class App(ct.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Progress bar")
#         self.geometry("400x400")
#         self._set_appearance_mode("dark")
#
#         # Create the progress bar and set it to 0 initially
#         self.pb = ct.CTkProgressBar(self)
#         self.pb.grid(row=1, column=1, sticky="news")
#         self.pb.set(0)  # Initialize progress bar at 0
#
#         # Create a button that triggers the click method
#         self.but = ct.CTkButton(self, command=self.click, text="Click")
#         self.but.grid(row=2, column=1, sticky="news", pady=20)
#
#     def click(self):
#         # Increment the progress bar by 10 each time the button is clicked
#         self.pb.step(10)
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



# import customtkinter as ct
# from customtkinter import *
# # import customtkinter as ct
# # from customtkinter import *
#
# class App(ct.CTk):
#     def __init__(self):
#         super().__init__()
#
#         self.title("Progress bar")
#         self.geometry("400x400")
#         self._set_appearance_mode("dark")
#
#         # Create the progress bar and set it to 0 initially
#         self.pb = ct.CTkProgressBar(self)
#         self.pb.grid(row=1, column=1, sticky="news")
#         self.pb.set(0)  # Initialize progress bar at 0
#
#         # Create a button that triggers the click method
#         self.but = ct.CTkButton(self, command=self.click, text="Click")
#         self.but.grid(row=2, column=1, sticky="news", pady=20)
#
#     def click(self):
#         # Increment the progress bar by 10 each time the button is clicked
#         current_value = self.pb.get()
#         if current_value < 1.0:  # Check if the progress bar is less than 100%
#             self.pb.step(0.1)  # Increment by 10% (0.1 in a scale of 0 to 1)
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()







# import customtkinter as ct
#
#
# class SliderApp(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Slider Example")
#         self.geometry("300x200")
#
#         # Create a label to display the slider value
#         self.label = ct.CTkLabel(self, text="Slider Value: 0")
#         self.label.pack(pady=20)
#
#         # Create a slider with a range from 0 to 100
#         self.slider = ct.CTkSlider(self, from_=0, to=100, command=self.update_label)
#         self.slider.pack(pady=20)
#
#     def update_label(self, value):
#         self.label.config(text=f"Slider Value: {value:.2f}")
#
#
# if __name__ == "__main__":
#     app = SliderApp()
#     app.mainloop()

#
# import customtkinter as ct
# from customtkinter import set_appearance_mode
#
#
# class App(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Main Window")
#         self.geometry("400x300")
#         self.open_but = ct.CTkButton(self, text="Open New Window", command=self.open_new_window)
#         self.open_but.pack(pady=20)
#         set_appearance_mode("dark")  # Set the main window to dark mode
#
#
#     def open_new_window(self):
#         # Create new top-level window
#         new_window = ct.CTkToplevel(self)
#         new_window.title("New Window")
#         new_window.geometry("300x300")
#         new_window._set_appearance_mode("dark")  # Set the new window to dark mode
#
#         label = ct.CTkLabel(new_window, text="This is a new top-level window!")
#         label.pack(pady=20)
#
#         button = ct.CTkButton(new_window, text="Close Window", command=new_window.destroy)
#         button.pack(pady=10)
#
#
# if __name__ == "__main__":
#     app = App()
#     app.mainloop()



# import customtkinter as ct
# from customtkinter import *
#
#
# class Scroll(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("300x300")
#         self.title("Scroll bar")
#
#         # Create a scrollable frame
#         self.sc = ct.CTkScrollableFrame(self)
#         self.sc.grid(row=0, column=0, padx=40, pady=20)
#
#         # Define button values
#         self.value = ["red", "white", "black", "red", "white", "black", "red", "white", "black"]
#
#         # Create buttons with the values list
#         for index, color in enumerate(self.value):
#             # Create a button with text as the color from the list
#             ct.CTkButton(self.sc, text=color, command=lambda color=color: self.button_click(color)).pack(pady=10)
#
#     def button_click(self, color):
#         # Print the color value of the clicked button
#         print(f"Button clicked with value: {color}")
#
#
# if __name__ == '__main__':
#     app = Scroll()
#     app.mainloop()

# import customtkinter as ct
# from PIL import Image, ImageTk
# import os
#
#
# class Img(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x400")
#         self.title("Images")
#
#         # Correct path to the image
#         self.img_path = os.path.join(os.path.dirname(__file__), "../images/logo.png")
#
#         # Open the image
#         self.img = Image.open(self.img_path)
#
#         # Resize the image to the desired size (400x200)
#         self.re_img = self.img.resize((400, 200))
#
#         # Convert resized image to CTkImage format
#         self.ct_img = ct.CTkImage(light_image=self.re_img)
#
#         # Create a label to display the image
#         self.lab = ct.CTkLabel(self, text="", image=self.ct_img)
#         self.lab.grid(row=1, column=1)
#
#
# if __name__ == '__main__':
#     app = Img()
#     app.mainloop()


# import customtkinter as ct
# from PIL import Image, ImageTk
# import os
#
#
# class Img(ct.CTk):
#     def __init__(self):
#         super().__init__()
#         self.geometry("400x400")
#         self.title("Images")
#
#         # Correct path to the image
#         self.img_path = os.path.join(os.path.dirname(__file__), "../images/logo.png")
#
#         # Open the image
#         self.img = Image.open(self.img_path)
#
#         # Resize the image to the desired size (400x200)
#         self.re_img = self.img.resize((400, 200))
#
#         # Convert the resized image to a Tk-compatible format using ImageTk.PhotoImage
#         self.tk_img = ImageTk.PhotoImage(self.re_img)
#
#         # Create a label to display the image
#         self.lab = ct.CTkLabel(self, text="", image=self.tk_img)
#         self.lab.grid(row=1, column=1)
#
#         # Keep a reference to the image object to prevent it from being garbage collected
#         self.lab.image = self.tk_img  # This is important for image persistence in tkinter
#
#
# if __name__ == '__main__':
#     app = Img()
#     app.mainloop()
import customtkinter as ct
from customtkinter import *
from PIL import Image, ImageTk
class App(ct.CTk):
    def __init__(self):
        super().__init__()

        # ====================== main window =====================
        self.geometry("700x600")
        self.title("window")

        # Main grid row/column configuration
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=0)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # ====================== first frame with checkbox =====================
        self.frame1 = ct.CTkFrame(self, fg_color="gray", width=300)
        self.frame1.grid(row=0, column=0, padx=(20, 0), pady=(10, 0), sticky="sewn")
        self.frame1.grid_propagate(False)
        self.frame1.grid_columnconfigure(0, weight=1)

        self.checkbox1 = ct.CTkCheckBox(self.frame1, text="checkbox 1")
        self.checkbox1.grid(row=0, column=0, sticky="snew", padx=(10, 0), pady=(10, 0))

        # other checkboxes and buttons...

        # ==================================== frame3 with tabview ==========================
        self.frame3 = ct.CTkFrame(self, fg_color="gray")
        self.frame3.grid(row=2, column=0, padx=(20, 0), pady=(10, 10), sticky="snwe")
        self.frame3.grid_rowconfigure(0, weight=1)  # Make sure the tabview and its contents don't shrink
        self.frame3.grid_columnconfigure(0, weight=1)

        self.tab = ct.CTkTabview(self.frame3, segmented_button_fg_color="#7b13a6",
                                 segmented_button_unselected_color="#132ca6", width=80, height=120, text_color="white")
        self.tab.grid(row=0, column=0, padx=(10, 0), pady=(10, 0))
        self.tab1 = self.tab.add("Tab 1")
        self.tab2 = self.tab.add("Tab 2")

        # Combobox and segmented buttons...

        # ==================================== frame 5 with scrollbar ==========================
        self.frame5 = ct.CTkFrame(self, fg_color="#533838")
        self.frame5.grid(row=2, column=1, pady=(10, 10), sticky="snew", padx=(10, 10))

        self.sc = ct.CTkScrollableFrame(self.frame5, label_text="Colors", label_fg_color="gray",
                                        label_text_color="white")
        self.sc.grid(row=0, column=0, padx=40, pady=20)

        # buttons inside scrollable frame...


if __name__ == '__main__':
    app=App()
    app.mainloop()