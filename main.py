from os import system, name 
import time
import sys
from time import sleep 

BoldGreen = "\033[0;32;1m"
Red = "\033[0;31;48m"
Blue = "\033[0;34;48m"
Green = "\033[0;32;48m"
Yellow = "\033[0;33;48m"
Normalize = "\033[0;37;48m"

def Enter_Continue():
  input("Press" + Colour(" ENTER",Red) + " to continue : ")
      
def Colour(string,colour):
  return (colour + string + Normalize)

def clear(): 
    if name == 'nt': 
        _ = system('cls') 
    else: 
        _ = system('clear') 

  
