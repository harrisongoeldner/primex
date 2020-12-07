import tkinter as tk

window = tk.Tk()
window.title("hi")
window.geometry("300x300")

entry1 = tk.Entry()
entry1.grid(column=0,row=1)
entry2 = tk.Entry()
entry2.grid(column=0,row=2)

button_name = tk.Button(window, text = "Github")
button_name.grid(column=0,row=5)

window.mainloop()

while 0 == 0:
    print(entry1)