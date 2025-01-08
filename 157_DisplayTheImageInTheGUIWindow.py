# Write a program using the Tkinter library to create a graphical user interface(GUI) with the following requirements: The window should have the title "Fx Studio". The minimum size of the window should be 400x400. There should be a button to open the system's image selection dialog. The selected image should be displayed in the window.
# Algorithm: 1_Create a GUI window with the title "Fx Studio" and set the minimum size. 2_Add a button to the window to open the image selection dialog. 3_Write a function to open the image selection dialog and display the image in the window. 4_Link the button with the function that opens the image selection dialog. 5_Display the selected image in the window.

import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def open_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if file_path:
        load_image(file_path)

def load_image(file_path):
    img = Image.open(file_path)
    img = img.resize((400, 400), Image.LANCZOS) #Resize image to fit the window
    img_tk = ImageTk.PhotoImage(img)

    if 'image_label' in globals():
        image_label.config(image=img_tk)
        image_label.image = img_tk
    else:
        global image_label
        image_label = tk.Label(window, image=img_tk)
        image_label.image = img_tk
        image_label.pack()

#Create main window
window = tk.Tk()
window.title("Fx Studio")
window.minsize(400, 400)

#Create button to open image selection dialog
open_button = tk.Button(window, text="Choose Image", command=open_image)
open_button.pack(pady=20)

#Run the main loop of Tkinter
window.mainloop()
