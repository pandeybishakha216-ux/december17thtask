#Given list is [1,2,3,4,"a","b"] append each elements datatypes to separate lists.
list = [1, 2, 3, 4, 'a', 'b']
int_types = []
str_types = []
for i in range(len(list)):
    if type(list[i]) == int:
        int_types.append(list[i])
    elif type(list[i]) == str:
        str_types.append(list[i])
print("Integer types:", int_types)
print("String types:", str_types)
