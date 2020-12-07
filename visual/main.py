"""
Primex is open source and currently maintained by Harrison Goeldner
The purpose of the program is to calculate all prime numbers between a certain range and saved to a txt file
"""

# import
from gui import *
from run import *

# set up window
"""window = tk.Tk()
window.title("primex")
window.geometry("250x300") # might be changed
#scroll = tk.Scrollbar(window)
#scroll.grid(column=1,row=2)"""

"""listbox_tk = Listbox(window, yscrollcommand=scroll.set)s
for i in range(100):
    listbox_tk.insert(END, str(i))
listbox_tk.pack(side=LEFT, fill=BOTH)
scroll.config(command=listbox_tk.yview)
"""
"""
# github button
button_name = tk.Button(window, text = "Github")
button_name.grid(column=0,row=5)
button_name.bind("<Button-1>",github)
"""

def main():
    win = window("primex","300x400","""
-- Prime Number Algorithm --
Version... 1.1.3
Release Date... April 28, 2020
Source code by Nikita Tiwari
Developed by Harrison Goeldner
""")
    win.setup()
    win.input()
    win.git_button()
    win.printx()
    win.done()


if __name__ == "__main__":
    main()

# Coded by Harrison Goeldner
# This code is contributed  
# by Nikita Tiwari.

"""
-- UPDATE LOG --
06 DECEMBER 2020    2.1.0 modular design
05 DECEMBER 2020    2.0.0 gui version
22 APRIL 2020    1.1.3 add custom file names
18 APRIL 2020    1.1.2 add oercent and improved interface
00 UNKNOWN 0000   1.1.1 original version
"""
