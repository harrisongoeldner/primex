"""
Primex is open source and currently maintained by Harrison Goeldner
The purpose of the program is to calculate all prime numbers between a certain range and saved to a txt file
"""

# import
import sys
from gui import *
from algorithm import *

# set up window
"""window = tk.Tk()
window.title("primex")
window.geometry("250x300") # might be changed
#scroll = tk.Scrollbar(window)
#scroll.grid(column=1,row=2)"""

"""listbox_tk = Listbox(window, yscrollcommand=scroll.set)
for i in range(100):
    listbox_tk.insert(END, str(i))
listbox_tk.pack(side=LEFT, fill=BOTH)
scroll.config(command=listbox_tk.yview)
"""

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
