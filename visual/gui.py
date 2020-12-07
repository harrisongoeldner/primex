import tkinter as tk
from links import *
from run import *
from functools import partial

class window:
    def __init__(self, name, size, intro):
        self.name = name
        self.size = size
        self.intro = intro
        # setup self.window variable for tkinter
        self.window = tk.Tk()
    def setup(self):
        self.window.title(str(self.name))
        self.window.geometry(str(self.size))
        self.code = tk.Label(text = self.intro)
        self.code.grid(column=0, row=0)
    def git_button(self):
        # github button
        self.button_name = tk.Button(self.window, text = "Github")
        self.button_name.grid(column=0,row=5)
        self.button_name.bind("<Button-1>",bookmarks.github)
    def done(self):
        self.window.mainloop()
    def input(self):
        self.entry1 = tk.Entry(self.window,width=25)
        self.entry1.grid(column=0,row=1)
        self.entry2 = tk.Entry(self.window, width=25)
        self.entry2.grid(column=0,row=2)
    def calculate(self):
        runtime = partial(run,self.entry1,self.entry2)
        button_name1 = tk.Button(self.window, text = "calculate")
        button_name1.grid(column=0,row=3)
        button_name1.bind("<Button-1>",runtime)