import tkinter as tk
from links import *

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
#    def input()
    def git_button(self):
        # github button
        self.button_name = tk.Button(self.window, text = "Github")
        self.button_name.grid(column=0,row=5)
        self.link = links()
        self.button_name.bind("<Button-1>",self.link.github())
    def done(self):
        self.window.mainloop()
        