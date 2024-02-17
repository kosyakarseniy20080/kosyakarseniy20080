from ast import IsNot
from random import randint

# for i in range(0,255):
#   symbol = chr(i)
#   if i % 10 == 0:
#        print(symbol) 
#   else:
#       print(symbol, end = "  ")



def GeneratePassword(max,sep):

    password = ""
    for i in range(0,max):
        password += chr(randint(65, 122))
        if i % 5==0:
            password += sep
    return 0

pass1 =  GeneratePassword(5,"---")   
print(pass1)

print(GeneratePassword(10,"+++"))
