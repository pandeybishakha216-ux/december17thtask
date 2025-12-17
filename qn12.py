#Given list is [1,2,3,4,5] separate the elements into odd and even categories
list = [1, 2, 3, 4, 5]
odd = []
even = []
for i in range(len(list)):
    if list[i] % 2 == 0:
        even.append(list[i])
    else:
        odd.append(list[i])
print("Odd numbers:", odd)
print("Even numbers:", even)
