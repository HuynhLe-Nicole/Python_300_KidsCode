# Write a program to create a GUI window with a button. When the button is clicked, an event will be handled
# Algorithm: 1_Import the tkinter library. 2_Create an instance of the Tk class from the tkinter library. 3_Create a button using the Button class from the tkinter library.
# 4_Define a function to handle the event when the button is clicked. 5_Blind this function to the button using the command property of the button. 6_Call the mainloop method on the Tk instance to display the GUI window.


import tkinter as tk

def handle_button_click():
    print("Button clicked!")

#Create the main window
root = tk.Tk()

#Create a button and attack the event handler
button = tk.Button(root, text="Click me!", command=handle_button_click)
button.pack()  #Add the button to the window

#Start the GUI event loop
root.mainloop()