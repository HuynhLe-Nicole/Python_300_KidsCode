# Write a program using the Tkinter library to create a simple calculator application with GUI. The calculator should support basic operations such as addition, subtraction, multiplication, and division.
# Algorithm: 1_Create a GUI window with Tkinter. 2_Add a display screen for the results. 3_Add buttons for the numbers 0-9 and the operations(+,-,*,/). 4_Add a button for calculating the result(=) and a button for clearing (C). 5_Write functions to handle button press events and display the results on the screen.

import tkinter as tk

def click_button(item):
    global expression
    expression += str(item)
    input_text.set(expression)

def clear():
    global expression
    expression = ""
    input_text.set("")

def calculate():
    global expression
    try:
        result = str(eval(expression))
        input_text.set(result)
        expression = result
    except Exception as e:
        input_text.set("error")
        expression = ""

#Initialize the main window
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("400x500")

expression = ""
input_text = tk.StringVar()

#Create a frame for the display
input_frame = tk.Frame(window, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
input_frame.pack(side=tk.TOP)

#Create the display field
input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=input_text, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
input_field.grid(row=0, column=0)
input_field.pack(ipady=10)

#Create a frame for the buttons
btns_frame = tk.Frame(window, width=400, height=450, bg="grey")
btns_frame.pack()

#Define buttons
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
    ('=', 4, 2), ('C', 4, 0),
]

#Add buttons the frame
for (text, row, col) in buttons:
    if text == "=":
        btn = tk.Button(btns_frame, text=text, width=10, height=3, bd=0, bg="#eee", cursor="hand2", command=calculate)
    elif text == "C":
        btn = tk.Button(btns_frame, text=text, width=10, height=3, bd=0, bg="#f44336", cursor="hand2", command=clear)
    else:
        btn = tk.Button(btns_frame, text=text, width=10, height=3, bd=0, bg="#fff", cursor="hand2", command=lambda text=text: click_button(text))

        btn.grid(row=row, column=col, padx=1, pady=1)

#Run the main loop of Tkinter
window.mainloop()