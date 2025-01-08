# Write a program that uses the Tkinter library to create a GUI with the following requirements: The window should have the title "Fx Studio". The minimum window size should be 600x400. A graph should be added to the window to display mock data on average temperature and rainfall for 12 months of a year.
# Algorithm: 1_Create a GUI window with the title "Fx Studio" and set a minimum size. 2_Add a graph to the window to display the data. 3_Use the Matplotlib library to plot the graph. 4_Embed the Matplotlib graph into Tkinter.

import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

#Mock data for temperature and rainfall over 12 months
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
temperature = [5, 7, 12, 17, 20, 25, 30, 28, 22, 18, 10, 6]
rainfall = [50, 40, 60, 80, 70, 50, 30, 40, 60, 80, 70, 50]

#Create the main window
window = tk.Tk()
window.title("Fx Studio")
window.minsize(600, 400)

#Create figure and axes for the graph
fig, ax1 = plt.subplots()

#Plot the temperature and rainfall data
ax1.plot(months, temperature, 'r-', label='Temperature (C)')
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature (C)', color='r')
ax2 = ax1.twinx()
ax2.plot(months, rainfall, 'b-', label='Rainfall (mm)')
ax2.set_ylabel('Rainfall (mm)', color='b')

#Add legends
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

#Create a canvas to embed the graph in Tkinter
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

#Run the main loop of Tkinter
window.mainloop()
 