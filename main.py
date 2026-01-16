#1
"""friends_name=["A1","B","C","D","E"]
new_friend=input("Give a name of your friend:")
friends_name.append(new_friend)
imp_frnd=input("Whose your most imp friend?")
friends_name.insert(0,imp_frnd)
print(friends_name)
"""
#2
"""
num=[]
for x in range(11):
    num.append(x)
print(num)
"""
#3
"""
list=[1,10,100,3,6,8]
list.insert(3,59)
list.append(5)
print(list)
print(f"length of list is",len(list))
"""
#4
"""
n=[]
string=["abdfd","gftygyt","as","wie","geht","entschuldigung"]
for x in string:
    if len(x)<4:
        n.append(x)
print(n)
"""
#5
"""
numbers=[i for i in range(20)]
even_odd=[]
for i in numbers:
    if i%2==0:
        even_odd.append("Even")
    else:
        even_odd.append("false")
print(even_odd)
"""
#6
"""
div_numbers=[i for i in range(1,1000) if i%7==0]
print(div_numbers)
"""
#7
"""
str="Wie geht es dir???Ich bin so traurig, weil du hier nicht bist ."
space_num=str.count(' ')
print(space_num)
"""
#8
list_a=1,2,3,4
list_b=2,3,4,5
ans=[i for i in list_a if i in list_b]
print(ans)

