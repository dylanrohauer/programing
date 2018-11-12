# game integration
import sause as gt
from tkinter import *

class RunTask:
    def __init__(self, lib, window):
        window.geometry("500x500")
        # saves library as self.lib
        self.lib = lib
        # saves the description
        self.description = self.lib['description']
        # saves the goal prompt
        self.goal = self.lib['goal']

        self.screen = Frame(window)
        self.screen.config(highlightthickness = 1, highlightbackground = 'black')
        self.screen.pack()
        self.initialize()
        self.print_introstuff()
        self.get_choices()
        self.make_buttons()
        window.mainloop()

    def get_choices(self):
        length = len(self.lib['choices'])
        self.ran = range(0,(length))
        self.choices = []
        for x in self.ran:
            self.choices.append(self.lib['choices'][x])

    def choose_return(self, x):
        print(x + 1)

    def make_buttons(self):
        self.button1 = Button()
        self.button2 = Button()
        self.button3 = Button()
        self.button4 = Button()
        self.button5 = Button()
        self.buttons = [self.button1, self.button2, self.button3, self.button4, self.button5]
        button_list = []
        for x in self.ran:
            button_list.append(self.buttons[x])
        for y in button_list:
            for z in self.choices:
                y = Button(self.midframe, text=z)
                y.pack()

    def initialize(self):
        # top frame
        self.topframe = Frame(self.screen)
        self.topframe.pack()
        # mid frame
        self.midframe = Frame(self.screen)
        self.midframe.pack(padx=10, pady=10)
        # lwr frame
        self.lwrframe = Frame(self.screen)
        self.lwrframe.pack()
        # name
        self.name = Label(self.topframe, text="THE RANDOM GAME")
        self.name.pack(side='top')

    def print_introstuff(self):
        self.description = Message(self.topframe, text=self.description)
        self.description.config(highlightthickness = 1, highlightbackground = 'black')
        self.description.pack(fill = X, pady = 5, padx = 5)
        self.goal = Message(self.topframe, text = self.goal)
        self.goal.config(highlightthickness = 1, highlightbackground = 'black')
        self.goal.pack(side = "bottom", fill = X, pady = 5, padx = 5)


root = Tk()
task1 = RunTask(gt.libtsk1,root)
