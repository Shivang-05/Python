#1
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
#2
def filter_details():
    pass

