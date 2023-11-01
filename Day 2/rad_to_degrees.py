#Author: Aaron Wajah
#Date: 11/01/2023

import math as m #import math module

ui= int(input("enter any number in radians to convert to degrees \n")) #ask for user input

def rad2degree(rads): #function to convert rads to degs
    rads=ui
    degs = rads*(180/m.pi)
    print(str(rads)+ "rads is " +str(round(degs,3))+ "°") #round decimal places to 3

rad2degree(ui)