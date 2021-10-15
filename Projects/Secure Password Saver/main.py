import hashlib
import FColor

choice = input('Are you\n(1) Signing Up\n(2) Signing In?: ')
pwd = input("Password: ")

pwd = hashlib.pbkdf2_hmac('sha256', pwd.encode('utf-8'), b'salt', 100000)
pwd = pwd.hex()

if(choice == '1'):
  results = open('save.dat', 'w')
  results.write(pwd)
  results.close()
  print()
  print(FColor.BLUE + 'Sign Up Complete!')

elif(choice == '2'):
  try:
    with open('save.dat', 'r') as file:
      for line in file:
        line = line.replace('\n', '')
        print()
        if(pwd == line):
          print(FColor.GREEN + "Correct Password")
        else:
          print(FColor.RED + f'Incorrect Password')
  except:
    print(FColor.RED + "Couldn't read file 'save.dat'")
