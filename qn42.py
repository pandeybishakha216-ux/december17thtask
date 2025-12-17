#Write a for loop that removes all vowels (a, e, i, o, u) from a string.
input_string = "This is an example string."
vowels = "aeiouAEIOU"
result_string = ""
for char in input_string:
    if char not in vowels:
        result_string += char
print(result_string)
