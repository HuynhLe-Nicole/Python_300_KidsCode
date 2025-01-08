# Write a program using the Tkinter library to build a GUI with the following requirements: The window should have the title "Fx Studio". The minimum window size should be 600x400. A table (or grid) should be added to the window.
# A button should be available to insert random data into the table. If the table exceeds the window size, a scrollbar should be provided to view the content.
# Algorithm: 1_Create a GUI window title "Fx Studio" with a minimum size of 600x400. 2_Add a table to the window. 3_Add the scrollbar for the table. 4_Add a button to the window to insert random data into the table.
#5_Write a function to insert random data into the table upon button click. 6_Link the button tothe function for adding random data.

import tkinter as tk
from tkinter import ttk
import random

def add_random_data():
    data = [str(random.randint(1, 100)) for _ in range(3)] #Create a list of 3 random integers between 1 and 100
    tree.insert("", "end", values=data) #Insert a new row into the table with the random values

#Create the main window
window = tk.Tk() 
window.title("Fx Studio")
window.minsize(600, 400)

#Create a frame to hold the table and scrollbar
frame = tk.Frame(window) 
frame.pack(fill="both", expand=True)

#Create the table (Treeview)
columns = ("col1", "col2", "col3")
tree = ttk.Treeview(frame, columns=columns, show="headings")
tree.heading("col1", text="Column 1")
tree.heading("col2", text="Column 2")
tree.heading("col3", text="Column 3")

#Create a scrollbar for the table
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
tree.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side="right", fill="y")
tree.pack(fill="both", expand=True)

#Create a button to add random data to the table
add_button = tk.Button(window, text="Add Random Data", command=add_random_data)
add_button.pack(pady=10)

#Run the main loop of Tkinter
window.mainloop()