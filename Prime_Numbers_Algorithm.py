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

num = int(input("bottom value: "))
num1 = int(input("top value: "))
list = []

# Create txt file to store data
t = str(num)+'-'+str(num1) # used to name file
f= open("prime"+str(t)+".txt","w+")

# Runs function
for x in range(num,num1):
    if(isPrime(num)):
        list.append(num)
        print(str(num) + ' prime')
    else:
        print(str(num) + ' null')
    num = num + 1
      
print(list)
f.write(str(list))
f.close() 

# Coded by Harrison Goeldner
# This code is contributed  
# by Nikita Tiwari.
