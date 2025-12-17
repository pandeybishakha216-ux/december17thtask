#Write a for loop which print "Hello!, " plus each name in the list. i.e.: "Hello!, Ram". 
from tkinter.font import names

names= ["Ram", "Shyam",1,2]
for i in names:
    if isinstance(i, str):
        print("Hello!, " + i) 


        

