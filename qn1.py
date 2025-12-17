 #Write a Python script using a for loop and the range() function to iterate through the numbers from 1 up to and including 5.
#Inside the loop, check if each number is even or odd, and then print the result in the format: "Number X is [even/odd]."

for number in range(1, 6):
    if number % 2 == 0:
       print( f"Number {number} is even." )
    else:
       print( f"Number {number} is odd.")
