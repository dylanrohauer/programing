# Tkinter learning program 1 - HelloWord
# imports Tk as a global module so it will work throughout the program
from tkinter import *
# creates the window in which info will be stored
root = Tk()
# creates the label
w = Label(root, text = "Hello World!")
# places the Label into the window
w.pack()
# runs the root 
root.mainloop()
