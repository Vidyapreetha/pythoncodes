
import random, time, threading, tkinter as tk, tkinter.font as tkFont
from tkinter import *

class MyGui:
    colors = ['red', 'cyan', 'black', 'orange', 'yellow', 'brown']
    colorChoice = []

    def __init__(self, parent, title='popup'):

        self.custFont = tkFont.Font(family = "Times New Roman", size = 12)
        self.growStatus = False

        parent.title("The sample GUI")
        self.label = tk.Label(parent, text = "The GUI label",
                              fg = 'blue',
                              bg = random.choice(self.colors),
                              font = self.custFont)

        self.label.pack(expand = YES, fill = BOTH)

        spamButton = tk.Button(parent, text = "Spam",
                                  command = self.spam)
        growButton = tk.Button(parent, text="Grow",
                                  command=self.grow)
        stopButton = tk.Button(parent, text = "Stop",
                                    command = self.stop)

        spamButton.pack(side="left")
        growButton.pack(side="left")
        stopButton.pack(side="left")

    def spam(self):
        size = self.custFont['size']
        self.custFont.configure(size=size + 5)
        colorChoice = random.choice(self.colors)
        self.label.config(bg=colorChoice)

    def grow(self):
        self.growStatus = True
        self.grower()

    def grower(self):
        size = self.custFont['size']
        if (self.growStatus != False):
	        self.custFont.configure(size = size + 5)
	        threading.Timer(0.5, self.grower).start()

    def stop(self):
        self.growStatus = False


class custSubGui(MyGui):
    colors = ['pink', 'blue', 'magenta', 'grey', 'green']

    def __init__(self, parent, title='pop-up'):
        MyGui.__init__(self, parent, title='Pop-up')

MyGui(Tk(), 'main')
custSubGui(tk.Toplevel())
tk.mainloop()

