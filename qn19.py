#Print multiplication table of  1,2,3,4,5,6,7,8  using nested for loop
for i in range(1, 9):
    print(f"Multiplication table of {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()  # Print a blank line after each table
    