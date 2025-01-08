# Write a program using the Tkinter library to create a graphical user interface(GUI) with the following requirements: The window should have the title "Fx Studio". The minimum size of the window should be 500x400. There should be a text box(a message box). There should be a button to clear the content of the text box.
# Algorithm: 1_Create a GUI window with the title "Fx Studia" and set the minimum size. 2_Add a text box to this window. 3_Add a button to the window to clear the content of the message box. 
# 4_Write a function to clear the content of the message box when the button is pressed. 5_Link the button to the function that clears the message box.

import tkinter as tk
from tkinter import messagebox

def clear_textbox():
    textbox.delete("1.0", tk.END)
    messagebox.showinfo("Notification", "Content has been cleared")

#Create main window
window = tk.Tk()
window.title("Fx Studio")
window.minsize(500, 400)

#Create message box (Text widget)
textbox = tk.Text(window, width=50, height=10)
textbox.pack(pady=20)

#Create button to clear message box content
clear_button = tk.Button(window, text="Clear Content", command=clear_textbox)
clear_button.pack(pady=20)

#Run the main loop of Tkinter
window.mainloop()