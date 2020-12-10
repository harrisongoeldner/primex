# A optimized school method based
# Python3 program to check
# if a number is prime

#import csv
import csv

# prime number test
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

# important information

print("""
-- Prime Number Algorithm --
Version... 1.1.3
Release Date... April 28, 2020
Source code by Nikita Tiwari
Developed by Harrison Goeldner
""")

# variable assignment
num = int(input("bottom value: "))
num1 = int(input("top value: "))
diff = num1 - num
list = []

# Create txt file to store data
#t = 1 # used to name file -- could be used in future in a loop
#f= open("prime"+str(num)+'-'+str(num1)+ ".txt","w+")

# csv row value in loop
i = 0

# Runs function
for x in range(num,num1):
    list.append([]) # create new nested list
    list[i].append(num) # append number in question to list
    percent = str(round(x/diff*100,1))
    if(isPrime(num)):
        list[i].append("prime") # append 'prime' to list
        print(str(num) + ' prime'.rjust(20,'-'), end = '')
        #alt could use sys.stdout.write()
    else:
        print(str(num) + ' null-'.rjust(20,'-'), end = '')
        list[i].append("null") # append 'null' to list
    print(percent.rjust(20,'-')+'%')
    num = num + 1
    i = i + 1

print(list)
print('collected '+str(len(list))+' prime numbers')

# removed txt output
#f.write(str(list)+'\n\ncollected '+str(len(list))+' prime numbers')
#f.close()

# csv output
with open('prime.csv', mode='w') as primes:
    writer = csv.writer(primes)
    writer.writerows(list)

# Coded by Harrison Goeldner
# This code is contributed
# by Nikita Tiwari.


"""
-- UPDATE LOG --
08 DECEMBER 2020    1.1.4 add csv support
22 APRIL 2020    1.1.3 add custom file name
18 APRIL 2020    1.1.2 add oercent and improved interface
00 UNKNOWN 0000   1.1.1 original version
"""
