# Write a program using the Tkinter library to create a graphical user interface(GUI) window titled "Fx Studio". The window should include a label and a button; when the button is pressed, the content of the label should change.
# Algorithm: 1_Create a GUI window with the title "Fx Studio". 2_Add a label to this window. 3_Add a button to the window. 4_Write a function to change the label content when the button is pressed. 5_Link the button to the function that changes the label's content.

import tkinter as tk

def change_label_text():
    label.config(text="The label content has been changed") #Use the config method of the label object to change the text property.

#Create the main window
window = tk.Tk() #Create the main application window

window.title("Fx Studio") #Set the window title to "Fx Studio"

#Create the label
label = tk.Label(window, text="This is the initial label") #Create a label with the initial content

label.pack() #Pack(display) the button in the window

#Create the button and link it to the change_label_text function
button = tk.Button(window, text="Press to change label", command=change_label_text) #Link the button press event with the change_label_text function
button.pack()

#Run the main loop of Tkinter
window.mainloop() #Start the main loop of Tkinter to keep the window open and ready for interaction
