#Given list is [1,2,3,4] but expected output is [1,"a",2,4]
list_6 = [1, 2, 3, 4]
for i in range(2):
    if list_6[i] == 2:
        list_6[i] = "a"
        list_6.pop(i+1)
        list_6.insert(2,2)
print(list_6) 
