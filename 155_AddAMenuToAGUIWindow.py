# Write a program using the Tkinter library to create a graphical user interface(GUI) with the following requirements: The window should have the title "Fx Studio". There should be a menu in the window. There should be a label to display the selected item from the menu.
# Algorithm: 1_Create a GUI window with the title "Fx Studio". 2_Add a label to this window. 3_Create a menu and its items. 4_Write a function to change the label's content based on the selected menu item.
# 5_Link the menu items with the function to change the label content. 6_Add the menu to the window.

import tkinter as tk
from tkinter import Menu

def show_selected(option):
    label.config(text=f"You selected: {option}")

#Create the main window
window = tk.Tk()
window.title("Fx Studio")

#Create the label
label = tk.Label(window, text="Select an item from the menu")
label.pack()

#Create the menu bar
menu_bar = Menu(window)
window.config(menu=menu_bar)

#Create the main menu
main_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Menu", menu=main_menu)

#Add items to the main menu
main_menu.add_command(label="Option 1", command=lambda: show_selected("Option 1"))
main_menu.add_command(label="Option 2", command=lambda: show_selected("Option 2"))
main_menu.add_command(label="Option 3", command=lambda: show_selected("Option 3"))

#Run the main loop of Tkinter
window.mainloop()