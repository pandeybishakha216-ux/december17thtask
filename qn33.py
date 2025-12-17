#Write a for loop which appends the type of each element in the first list to the second list.
lst1 = [10, 15.5, "hello", True, None, 3+4j]
types_list = []
for item in lst1:
    types_list.append(type(item))
print(types_list)
