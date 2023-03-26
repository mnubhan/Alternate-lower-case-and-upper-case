string = "Hello World"
alternate_upper = ""
alternate_lower = ""
string_list=string.split(" ")
for word in string_list:
    for i in range(len(word)):
        if i%2==0:
            alternate_upper+=word[i].upper()
        else:
            alternate_upper+=word[i].lower()
    alternate_upper+=" "
print(alternate_upper)

# function alternating lower and upper case
for word in string_list:
    for i in range(len(word)):
        if i%2==0:
            alternate_lower+=word[i].lower()
        else:
            alternate_lower+=word[i].upper()
    alternate_lower+=" "
print(alternate_lower)
