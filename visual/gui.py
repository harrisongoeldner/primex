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
        self.button_name = tk.Button(self.window, text = "Github", command=bookmarks.github)
        self.button_name.grid(column=0,row=5)
    def done(self):
        self.window.mainloop()
    def input(self):
        self.entry1 = tk.Entry(self.window,width=25)
        self.entry1.grid(column=0,row=1)
        self.entry2 = tk.Entry(self.window, width=25)
        self.entry2.grid(column=0,row=2)
        button_name1 = tk.Button(self.window, text = "Calculate",command=lambda:run(self.entry1.get(),self.entry2.get()))
        button_name1.grid(column=0,row=3)
    def printx(self):
        """bloop = tk.Text(self.window,height=20,width=10)
        bloop.grid(column=1,row=6)
        try:
            bloop.insert(tk.END,value)
        except Exception:
            print("error")"""
        label1=tk.Label(text=percent)
        label1.grid(column=0,row=7)
