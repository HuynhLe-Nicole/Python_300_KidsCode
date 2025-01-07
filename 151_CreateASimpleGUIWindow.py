# Write a program to create a simple GUI(Graphical User Interface) window with the title "Fx Studio"
# Algorithm: 1_Import the tkinter library. 2_Create an instance of the Tk class from the tkinter library. 3_Set the title of the window to "Fx Studio". 4_Call the mainloop method on this instance to display the GUI window.

import tkinter as tk

#Create the main window
root = tk.Tk()

#Set the title of the window
root.title("Fx Studio")

#Start the GUI event loop
root.mainloop()