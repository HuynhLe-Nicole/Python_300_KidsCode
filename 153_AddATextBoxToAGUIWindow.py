# Write a program to create a GUI window that contains a text box and a button. When the button is clicked, the text in the text box should be cleared.
# Algorithm: 1_Import the tkinter library. 2_Create an instance of the Tk class from the tkinter library. 3_Create a text box using the Entry class from the tkinter library. 4_Create a button using the Button class from the tkinter library.
# 5_Define a function to clear the text in the text box when the button is clicked. 6_Bind this function to the button using the command property of the button. 7_Call the mainloop method on the Tk instance to display the GUI window.

import tkinter as tk

def clear_text():
    entry.delete(0, tk.END) #Clear the text in the Entry widget

#Create the main window
root = tk.Tk()

#Create a text box
entry = tk.Entry(root)
entry.pack() #Add the text box to the window

#Create a button and attach the event handler
button = tk.Button(root, text="Clear text", command=clear_text)
button.pack() # Add the button to the window

#Start the GUI event loop
root.mainloop()

