# multiplication table of a given number. number= 11
number = 11
print(f"--- Multiplication Table of {number} ---")
for i in range(1, 11):
    product = number * i
    print(f"{number} x {i} = {product}")
print("-------------------------------------")
