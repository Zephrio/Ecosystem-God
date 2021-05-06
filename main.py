from os import system, name 
import time
import sys
from time import sleep 
 
User_Log = []
BoldGreen = "\033[0;32;1m"
Red = "\033[0;31;48m"
Blue = "\033[0;34;48m"
Green = "\033[0;32;48m"
Yellow = "\033[0;33;48m"
Normalize = "\033[0;37;48m"

count = 0
global count
def StartOptions():
  
  if count == 0:
    print(Colour("Welcome to Ecosystem God,\nwould you like to...",BoldGreen))
  time.sleep(1.5)
  print(Colour("\nStart New Game (1)",BoldGreen))
  time.sleep(0.5)
  print(Colour("Continue Game (2)",BoldGreen))
  time.sleep(0.5)
  print(Colour("EXIT (3)",Red))
  try :
    User_Input = int(input(" : "))
  except:
    global count
    count =+ 1
    print((Colour("\nINVALID INPUT must be ( 1 / 2 / 3 ) ")))
    StartOptions()
  else:
    if User_Input < 1 or User_Input > 3:
      global count
      count =+ 1
      print((Colour("\nINVALID INPUT must be ( 1 / 2 / 3 ) ")))
      StartOptions()
  return User_Input

  
def Add_User(User):
  ErrorPresent = True
  while ErrorPresent:
    try :
      UserNameFile = open(User + ".txt","x")
    except :
      print(Colour("That User Already Exists!",Red))
      ErrorPresent = True
      while ErrorPresent:
        User_Name = input("Please Enter Your Username (6+ letters) " + Colour("User Name : ",Green) )
        if len(User_Name) >= 6:
          ErrorPresent = False
    else:
      ErrorPresent = False
      print(Colour("Succesfully saved Data",Green))
      Enter_Continue()

def Enter_Continue():
  input("Press" + Colour(" ENTER",Red) + " to continue : ")
      
def Colour(string,colour):
  return (colour + string + Normalize)

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 
  
def CollectData():
  ErrorPresent = True
  while ErrorPresent:
    User_Name = input("Please Enter Your Username (5+ letters) " + Colour("User Name : ",Green) )
    if len(User_Name) >= 5:
      Add_User(User_Name)
      ErrorPresent = False
    else:
      print(Colour("Invalid Input", Red))


choice = StartOptions()
if choice == 1:
  CollectData()
elif choice == 2:
  pass
else:
  sys.exit(Colour("EXITED",Red))
