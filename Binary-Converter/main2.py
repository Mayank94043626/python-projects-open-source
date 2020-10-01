from os import system, name
import time
def clear(): 
  
    #win 
    if name == 'nt': 
        _ = system('cls') 
  
    #GNU Linux,Unix and etc.
    else: 
        _ = system('clear')
clear()
num=input("Please enter your decimal here:")
bin=0
divisionControl=int(num)

total= []
##Error handler
if(int(num)<0):
    print("This is not a positive number.\n")#Yes this is not a positive number but it can still convertable to binary number system so no destroys.

#Calculate
for i in range(1,99):
    bin = int(divisionControl)%2
    divisionControl = int(divisionControl)//2
    if(int(divisionControl)==0):
        break
    total.append(str(bin))
#Reverse's numbers
total.reverse()
#Output
clear()
print("Your input decimal is ", num)
print("Your binary is")
print("1",end="",sep="")
for i in total:
    print(str(i),sep="",end="")#Place list datas (zero and ones).
print()
time.sleep(6)
exec(open('BinCalculator.py').read())