import sys

def run(num,num1,event):
    num = num
    num1 = num1
    print(num)
    print(num1)
    #   num = int(input("bottom value: "))
    #   num1 = int(input("top value: "))
    """diff = num1 - num
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
    f.close() """