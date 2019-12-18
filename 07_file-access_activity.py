# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 16:21:06 2019

@author: Jhonnathan
"""

file=open("devices.txt","a")
file1=open("devices2.txt","w")
while True:
    newitem=input("Input a new device: ")
    if newitem=="exit":
        print ("All done")
        break
    file.write(newitem+"\n")
    file1.write(newitem+"\n")
file.close()
file1.close()


  



    
