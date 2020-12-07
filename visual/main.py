"""
Primex is open source and currently maintained by Harrison Goeldner
The purpose of the program is to calculate all prime numbers between a certain range and saved to a txt file
"""

# import
import webbrowser
import sys
import tkinter as tk

# A optimized school method based  
# Python3 program to check 
# if a number is prime 

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

# This code is contributed  
# by Nikita Tiwari.

class bookmarks:
    def github():
        webbrowser.open_new_tab('https://github.com/harrisongoeldner/primex')

percent = 0

class windowx:
    def setup(self, name, size, intro):
        self.name = name
        self.size = size
        self.intro = intro
        # setup self.window variable for tkinter
        self.window = tk.Tk()
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
    def printx(self,value):
        """bloop = tk.Text(self.window,height=20,width=10)
        bloop.grid(column=1,row=6)
        try:
            bloop.insert(tk.END,value)
        except Exception:
            print("error")"""
        label1=tk.Label(text=value)
        label1.grid(column=0,row=7)

def run(num,num1):
    global percent
    num = int(num)
    num1 = int(num1)
    diff = num1 - num
    list = []
    percent = 0
    
    w.printx(percent)
    # Create txt file to store data
    t = 1 # used to name file -- could be used in future in a loop
    f= open("prime"+str(num)+'-'+str(num1)+ ".txt","w+")
    old_percent = 0
    # Runs function
    for x in range(num,num1):
        percent = str(round(x/diff*100,1))
        w.printx(percent)
        if(isPrime(num)):
            list.append(num)
            print(str(num) + ' prime'.rjust(20,'-'), end = '')
            #alt could use sys.stdout.write()
        else:
            print(str(num) + ' null-'.rjust(20,'-'), end = '')
        print(percent.rjust(20,'-')+'%')
        percentx = float(percent) + 100
        if float(old_percent) < percentx:
            w.printx(percent)
            old_percent = percent
        num = num + 1
        
    print(list)
    print('collected '+str(len(list))+' prime numbers')
    f.write(str(list)+'\n\ncollected '+str(len(list))+' prime numbers')
    f.close()

# main
def main():
    global w
    w = windowx()
    w.setup("primex","300x400","""
-- Prime Number Algorithm --
Version... 1.1.3
Release Date... April 28, 2020
Source code by Nikita Tiwari
Developed by Harrison Goeldner""")
    w.input()
    w.git_button()
    w.done()


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
