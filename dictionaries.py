#1
sentence=input("Give me a sentence :")
words=sentence.split()
dict_1={}
word_count=1
for i in words:
    if i in dict_1:
        dict_1[i]+=1
    else:
        dict_1[i]=word_count
print(dict_1)
#2
student_details={
    "alice":56,
    "bob":65,
    "jia":78,
    "henry":45,
}
avg_marks=0
n=0
for k,v in student_details.items():
    avg_marks+=v
    n+=1
avg_marks=avg_marks/n
print(f"the average marks are:{avg_marks}")
for k,v in student_details.items():
    if v>avg_marks:
        print(f"Congrats {k} You scored higher than the average")
#3
dict_2={'a': 50, 'b': 30, 'c': 70}
dict_3={'b': 60, 'c': 65, 'd': 40}
merged_dict={}
for k,v in dict_2.items():
    if k in dict_3:
        if v>dict_3[k]:
            merged_dict[k]=v
        else:
            merged_dict[k]=dict_3[k]
    else:
        merged_dict[k]=v
for k,v in dict_3.items():
    if k not in dict_2:
        merged_dict[k]=v
print(merged_dict)
#4
person_info={
    'name': 'Bob', 'city': 'Hyderabad', 'course': 'Machine Learning'}
id_length=0
output=""
for i in person_info:
 if id_length<len(i):
     id_length=len(i)
     output=i
print(output)
#5
my_dict = {
    'a': 5,
    'b': 15,
    'c': 25,
    'd': 55,
    'e': 50,
    'f': 10,
    'g': 75,
}
new_dict={}
for k,v in my_dict.items():
    if v>10 and v<=50:
        new_dict[k]=v
print(new_dict)
#6
candidate_votes={"Alia":0,
                 "Raju":0,
                 "Rajesh":0,
                 "Happy":0,}
max_list=[]
for k,v in candidate_votes.items():
    votes=int(input(f"What are your votes  for {k}"))
    candidate_votes[k]+=votes
    max_list.append(votes)
winner=max(max_list)
for k,v in candidate_votes.items():
    if v==winner:
        winner_name=k
print(f"The winner with max votes {winner} is {winner_name}")
#7
data={
    "a":12,
    "b":45,
    "c":23,
    "d":80
}
update={"a":45,"b":50}
for k in data:
    if k in update:
        data[k]=update[k]

print(data)

