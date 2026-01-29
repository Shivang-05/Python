#2,7,11,
# employee_details={"id":
#     {"name":"A",
#                   }
# print(employee_details)
# empty_dict={}
# no_of_entries=int(input("How many different numbers you want?"))
# for i in range(no_of_entries):
#     fav_number=int(input("What is your fav number?"))
#     empty_dict[i+1]=fav_number
# print(f"Your favorite numbers are: {empty_dict}")
# Marketing_uses={'Photoshop','Slack',"Zoom","Canva","Trello"}
# Sales_uses={'Salesforce',"Slack","Zoom","LinkedIn","Hubspot"}
# shared_tools=Marketing_uses.intersection(Sales_uses)
# print(f"The shared tools include {shared_tools}")
#
# unique_tools=Marketing_uses.difference(shared_tools)
# unique_tools.update(Sales_uses.difference(Marketing_uses))
# print(f"All the unique tools include:{unique_tools}")
# print(f"The specialized tools are {Marketing_uses.difference(Sales_uses)}")
#
# siloed_tools=Marketing_uses.union(Sales_uses)-Marketing_uses.intersection(Sales_uses)
# print(f"The siloed tools include {siloed_tools}")
# Universal_license={"Slack",'Zoom'}
# is_covered=Universal_license.issubset(Marketing_uses)
# print(is_covered)
# def listsum(**a):
#     print(a["a"])
#     sum=0
#     for i in a.values():
#         sum+=i
#     return sum
# print(listsum(a=23,b=2,c=4))
# n=int(input("enter number"))
# def fact(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# print(fact(n))
"""
def average_marks(*marks):
    avg_marks=0
    for m in marks:
        avg_marks+=m
    print(f"the avg marks are {avg_marks/n}")

n=int(input("enter no of subjects"))
marks=[]
for i in range(n):
    subj_marks = int(input("enter no. of marks "))
    marks.append(subj_marks)
average_marks(*marks)
def filter_details(**kwargs):
    for k,v in kwargs.items():
        if type(v) is  str:
            print(f"{k}={v}")
n=int(input("No. of values you want to give:"))
dict={}
for i in range(n):
    key = input("give a string")
    value=input("give a value")
    dict[key]=value
filter_details(**dict)
"""


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












