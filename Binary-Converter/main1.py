from os import system, name
import time
def clear(): 
  
    #win 
    if name == 'nt': 
        _ = system('cls') 
  
    #Linux,Unix and etc.
    else: 
        _ = system('clear')
clear()
BinM= (input("Please enter your binary here:"))
numplus=0
total=0
OUBinM=[]

##Error handler
if(int(BinM)<0):
    print("This is not a binary.")
    exit()

#Reverse's Numbers
lenBin= len(BinM)
while lenBin > 0: 
    OUBinM+=BinM[ lenBin-1]
    lenBin= lenBin-1

#Calculate
for number in OUBinM:
    y=2**numplus
    x=int(number)*y
    total=total+x
    numplus+=1
#Output
clear()
print("Your decimal is")
print(total)
time.sleep(6)
exec(open('BinCalculator.py').read())
