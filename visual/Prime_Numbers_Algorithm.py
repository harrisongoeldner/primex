# A optimized school method based  
# Python3 program to check 
# if a number is prime 

import sys
import tkinter as tk
import webbrowser

def github(event):
    webbrowser.open_new_tab('https://github.com/harrisongoeldner/primex')

def isPrime(n) : 
  
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

# set up window
window = tk.Tk()
window.title("primex")
window.geometry("300x100") # might be changed
#scroll = tk.Scrollbar(window)
#scroll.pack(side=tk.RIGHT)

"""listbox_tk = Listbox(window, yscrollcommand=scroll.set)
for i in range(100):
    listbox_tk.insert(END, str(i))
listbox_tk.pack(side=LEFT, fill=BOTH)
scroll.config(command=listbox_tk.yview)
"""

#label
label_name = tk.Label(text = """
-- Prime Number Algorithm --
Version... 1.1.3
Release Date... April 28, 2020
Source code by Nikita Tiwari
Developed by Harrison Goeldner
""")
label_name.grid(column=0,row=0)

# github button
button_name = tk.Button(window, text = "Github")
button_name.grid(column=0,row=5)
button_name.bind("<Button-1>",github)

# entry
entry1 = tk.Entry(window,width=25)
entry1.grid(column=0,row=1)

entry2 = tk.Entry(window, width=25)
entry2.grid(column=0,row=2)



#num=int(num)
#num1=int(num1)

def main(event):
    num=int(entry1.get())
    num1=int(entry2.get())
 #   num = int(input("bottom value: "))
 #   num1 = int(input("top value: "))
    diff = num1 - num
    list = []

    # Create txt file to store data
    t = 1 # used to name file -- could be used in future in a loop
    f= open("prime"+str(num)+'-'+str(num1)+ ".txt","w+")

    # Runs function
    for x in range(num,num1):
        percent = str(round(x/diff*100,1))
        if(isPrime(num)):
            list.append(num)
            print(str(num) + ' prime'.rjust(20,'-'), end = '')
            #alt could use sys.stdout.write()
        else:
            print(str(num) + ' null-'.rjust(20,'-'), end = '')
        print(percent.rjust(20,'-')+'%')
        num = num + 1
        
    print(list)
    print('collected '+str(len(list))+' prime numbers')
    f.write(str(list)+'\n\ncollected '+str(len(list))+' prime numbers')
    f.close() 

# github button
button_name1 = tk.Button(window, text = "calculate")
button_name1.grid(column=0,row=3)
button_name1.bind("<Button-1>",main)

window.mainloop()
# Coded by Harrison Goeldner
# This code is contributed  
# by Nikita Tiwari.

# update window

"""
-- UPDATE LOG --
05 DECEMBER 2020    2.0.0 gui version
22 APRIL 2020    1.1.3 add custom file name
18 APRIL 2020    1.1.2 add oercent and improved interface
00 UNKNOWN 0000   1.1.1 original version
"""
