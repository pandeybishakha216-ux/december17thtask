#Given list is [1,2,3,4] but expected output is [1,"a",2,4]
list = [1, 2, 3, 4]
for i in range(len(list)):
    if i == 1:
        print("a")
    print(list[i])
    