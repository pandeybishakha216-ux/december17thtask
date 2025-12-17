#Write a Python script to calculate the product (multiplication) of all numeric elements in a given list. given list=[4,5,3,2]
data = [4,5,3,2]
product = 1
for number in data:
    product *= number
    print(f"Multiplied by {number}. Running product is {product}.")
print(f"Finally, print the total product after the loop finishes. Total Product: {product}")