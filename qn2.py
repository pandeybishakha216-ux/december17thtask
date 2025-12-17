#Write a Python script that uses a for loop to calculate the sum of all elements in the given list.it must show the process

data = [10,20,30,40]
total_sum = 0
for number in data:
    total_sum += number
    print(f"Added {number}. Running total is {total_sum}.")
print(f"Finally, print the total sum after the loop finishes. Total Sum: {total_sum}")