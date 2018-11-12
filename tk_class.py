# testing things in Tkinter
from tkinter import *
import time

class App:
    def __init__(self, window, name):
        window.geometry("500x500")
        #window.resizable(0, 0)
        # main frame, holds top, mid and lwr frame
        self.mainframe = Frame(window)
        self.mainframe.config(highlightthickness = 1, highlightbackground = 'black')
        self.mainframe.pack()
        # top frame
        self.topframe = Frame(self.mainframe)
        self.topframe.pack()
        # mid frame
        self.midframe = Frame(self.mainframe)
        self.midframe.pack(padx=10, pady=10)
        # lwr frame
        self.lwrframe = Frame(self.mainframe)
        self.lwrframe.pack()
        # name
        self.name = Label(self.topframe, text=name)
        self.name.pack(side='top')
        # button
        self.button1 = Button(
                            self.lwrframe, text="Push This Button", command = lambda: self.do_something()
                            )
        self.button1.pack(side='left')
        self.button2 = Button(
                            self.lwrframe, text="Remove Text", command = lambda: self.user_output.pack_forget()
                            )
        self.button2.pack(side="right")
        self.initialize()
        window.mainloop()


    def initialize(self):
        self.message = "The message will appear here!"
        self.user_output = Message(self.midframe, text=self.message)
        self.user_output.config(highlightthickness = 1, highlightbackground = 'black')

    def do_something(self):
        self.user_output.pack()



root = Tk()
app = App(root,"Push the Button Below")
