#You have two lists of numbers, and you need to find out which numbers appear in both lists. 
#Given two lists of numbers [1,2,3,4,5] and [3,4,5,6,7] write a for  loop to find the common elements.
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

common_elements = []
for num in list1:
    if num in list2:
        common_elements.append(num)

print("Common elements:", common_elements)
