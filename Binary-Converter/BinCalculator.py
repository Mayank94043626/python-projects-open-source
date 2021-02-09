from os import system, name
def clear(): 
  
    #win 
    if name == 'nt': 
        _ = system('cls') 
  
    #GNU Linux,Unix and etc.
    else: 
        _ = system('clear')
clear()

print("Welcome to binary converter app. This app can convert a decimal to a binary or a binary to a decimal.")
print("What you will do?\n")
print("{} {} {}".format("(1)Binary to decimal |", "(2)decimal to binary |", "(3)Exit\n"))
ValSelectionM=int(input("Please select a number for operation:\nUSER>>"))
if(ValSelectionM==1):
    exec(open('main1.py').read())
else:
    if(ValSelectionM==2):
        exec(open('main2.py').read())
    else:
        if(ValSelectionM==3):
            exit()
        else:
            ##Error handler
            if(ValSelectionM>3):
                print("Number not found. Please select a number from table.")
                exec(open('BinCalculator.py').read())#Restart
            else:
                if(ValSelectionM<1):
                    print("Number not found. Please select a number from table.")
                    exec(open('BinCalculator.py').read())#Restart
            