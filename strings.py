sample_strings="Coder roots"
if len(sample_strings)>2:
    print(sample_strings[:2]+sample_strings[-2:])
else:
    print("Not possible!!")
#2
str1 = "coder"
str2 = "roots"

new_str1= str2[0]+str1[1:]
new_str2=str1[0]+str2[1:]
result = new_str1 + " " + new_str2

print(result)
#3
given_string='string'
given_string2="abc"
def strings(a):
    if len(a)<3:
        print(a)
    else:
        if 'ing' == a[-3:]:
            a+='ly'
            return a
        else:
            a+='ing'
            return a

print(strings(given_string))
print(strings(given_string2))