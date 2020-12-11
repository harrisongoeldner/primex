# A optimized school method based
# Python3 program to check
# if a number is prime

# import python libraries
import csv
import importlib
# import file classes and definitions
from dbx import *
import settings
from prime import isPrime
from oauth import oauth_init
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError
try:
    import config
except:
    print("error importing")

data = ["TOKEN = ''\n","APP_KEY = ''\n","APP_SECRET = ''\n","oauth_result =  ''\n"]
try:
    file = open("config.py")
    file.close()
except IOError:
    file = open("config.py","w")
    data[1] = "APP_KEY = '" + input("Enter APP_KEY: ") + "'\n"
    data[2] = "APP_SECRET = '" + input("Enter APP_SECRET: ") + "'\n"
    file.writelines(data)
    file.close()

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

file_name = "prime"+str(num)+'-'+str(num1)+ ".csv"

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
with open("output/"+file_name, mode='w') as primes:
    writer = csv.writer(primes)
    writer.writerows(list)

import config
try:
    dat = data_transfer(config.oauth_result)
    dat.upload("output/"+file_name,"/output/"+file_name)
except dropbox.exceptions.BadInputError:
    print("WARNING: Don't have write permission")
    input("Change permission and click ENTER to fix")
    oauth_init(config.APP_KEY, config.APP_SECRET)
    importlib.reload(config)
    dat = data_transfer(config.oauth_result)
    dat.upload("output/"+file_name,"/output/"+file_name)
except AuthError:
    oauth_init(config.APP_KEY, config.APP_SECRET)
    importlib.reload(config)
    dat = data_transfer(config.oauth_result)
    dat.upload("output/"+file_name,"/output/"+file_name)
except ApiError as err:
    # This checks for the specific error where a user doesn't have
    # enough Dropbox space quota to upload this file
    if (err.error.is_path() and
            err.error.get_path().reason.is_insufficient_space()):
        sys.exit("ERROR: Cannot back up; insufficient space.")
    elif err.user_message_text:
        print(err.user_message_text)
        sys.exit()
    else:
        print(err)
        sys.exit()


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
