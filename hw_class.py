# tkinter learning - hello world (class version)
# imports all of Tkinter
from tkinter import *
# creates class App
class App:
    # instantiates the App with self and window
    def __init__(self, window):
        # creates a frame with the window as the parent
        frame = Frame(window)
        # packs the frame inside of the window
        frame.pack()
        # creates a button inside the frame
        self.button = Button(
            # text is stated, foreground is red, and the comand is to quit the frame
            frame, text = "QUIT", fg = "red", command = frame.quit
            )
        # packs the buttion into the left og the
        self.button.pack(side=LEFT)
        # creates another button inside of the frame that runs the say_hi command
        self.hi_there = Button(frame, text="Hello World", command=self.say_hi)
        # places the button on the left side of the frame, after the quit button
        self.hi_there.pack(side=LEFT)

    def say_hi(self):
        print("Hi there, everyone!")

root = Tk()
app = App(root)

root.mainloop()
# this is an unused termination sequence
# for ending the tk window
# root.destroy()
