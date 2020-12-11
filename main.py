print("Initializing imports... ", end="")
# import python libraries
import csv, importlib, sys

import info, settings
from dbx import data_transfer
from prime import isPrime
from oauth import oauth_init

if settings.upload == True:
    try:
        import dropbox
        from dropbox.files import WriteMode
        from dropbox.exceptions import ApiError, AuthError
        from dropbox import DropboxOAuth2FlowNoRedirect
    except:
        with open("settings.py","r") as file:
            data = file.readlines()
            file.close()

        data[1] = 'upload = \'False\'\n'

        with open("settings.py","w") as f:
            f.writelines(data)
            f.close()
        importlib.reload(settings)

sys.stdout.write("Done\n")

sys.stdout.write("Initializing functions... ")

# functions
def config_file_test():
    config_file = ["TOKEN = ''\n","APP_KEY = ''\n","APP_SECRET = ''\n","oauth_result =  ''\n"]
    try:
        file = open("config.py")
        file.close()
        sys.stdout.write("Success\n")
    except IOError:
        sys.stdout.write("Not Found\n")
        print("Go to https://www.dropbox.com/developers/apps and get App Key and Secret")
        file = open("config.py","w")
        config_file[1] = "APP_KEY = '" + input("Enter APP_KEY: ") + "'\n"
        config_file[2] = "APP_SECRET = '" + input("Enter APP_SECRET: ") + "'\n"
        file.writelines(config_file)
        file.close()

sys.stdout.write("Done\n")

def main():
    sys.stdout.write("Searching for config.py file... ")
    config_file_test()
    info.title()

    # variable assignment
    num = int(input("Bottom value: "))
    num1 = int(input("Top value: "))
    diff = num1 - num
    list = []
    i = 0 # csv row value in loop
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

    sys.stdout.write("Initializing file write... ")
    # csv output
    with open("output/"+file_name, mode='w') as primes:
        writer = csv.writer(primes)
        writer.writerows(list)
    sys.stdout.write("Done\n")

    if settings.upload == True:
        sys.stdout.write("Initializing dropbox upload... \n")
        sys.stdout.write("Go to https://www.dropbox.com to see more information\n")

        import config
        try:
            dat = data_transfer(config.oauth_result)
            dat.upload("output/"+file_name,"/output/"+file_name)
            sys.stdout.write("OAUTH CONNECTED SUCCESSFULLY\n")
            sys.stdout.write(file_name + " has been uploaded to dropbox\n")

        except dropbox.exceptions.BadInputError:
            print("WARNING: Don't have write permission")
            input("Change permission and click ENTER to fix")
            oauth_init(config.APP_KEY, config.APP_SECRET)
            importlib.reload(config)
            dat = data_transfer(config.oauth_result)
            sys.stdout.write("OAUTH CONNECTED SUCCESSFULLY\n")
            dat.upload("output/"+file_name,"/output/"+file_name)
            sys.stdout.write(file_name + " has been uploaded to dropbox\n")

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

        except:
            oauth_init(config.APP_KEY, config.APP_SECRET)
            importlib.reload(config)
            dat = data_transfer(config.oauth_result)
            dat.upload("output/"+file_name,"/output/"+file_name)
            sys.stdout.write(file_name + " has been uploaded to dropbox\n")

if __name__ == "__main__":
    main()

"""
Coded by Harrison Goeldner
Prime number algorithm developed by by Nikita Tiwari.
Dropbox supported sections of API references


-- UPDATE LOG --
10 DECEMBER 2020    2.0.0 add dropbox support
08 DECEMBER 2020    1.1.4 add csv support
22 APRIL 2020    1.1.3 add custom file name
18 APRIL 2020    1.1.2 add percent and improved interface
00 UNKNOWN 0000   1.1.1 original version
"""
