# A optimized school method based
# Python3 program to check
# if a number is prime

#import sys
import csv

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

print("""
-- Prime Number Algorithm --
Version... 1.1.3
Release Date... April 28, 2020
Source code by Nikita Tiwari
Developed by Harrison Goeldner
""")

num = int(input("bottom value: "))
num1 = int(input("top value: "))
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

with open() ('prime', mode='w') as primes:
    writer = csv.writer(primes)
    writer.writerows(list)

# Coded by Harrison Goeldner
# This code is contributed
# by Nikita Tiwari.


"""
-- UPDATE LOG --
22 APRIL 2020    1.1.3 add custom file name
18 APRIL 2020    1.1.2 add oercent and improved interface
00 UNKNOWN 0000   1.1.1 original version
"""
