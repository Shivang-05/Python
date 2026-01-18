#1
months = {
    '1': 'January', '2': 'February', '3': 'March', '4': 'April',
    '5': 'May', '6': 'June', '7': 'July', '8': 'August',
    '9': 'September', '10': 'October', '11': 'November', '12': 'December'
}
month_number = input("Enter a number between 1 and 12: ")
for x in months:
    if x==month_number:
        print(f"The corresponding month is {months[x]}")
#2
user_num1=int(input("Enter number 1:"))
user_num2=int(input("Enter number 2:"))
if user_num1==user_num2:
    print("Equal")
else:
    print("Unequal")
if user_num1-user_num2>0:
    print("The first number is greater")
    print("Shivang\n"*5)
else:
    print("The second number is greater and first is smaller")
    print("Garg\n"*3)
#3
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
if str1 == str2:
    print(" Both strings are equal")
else:
    print("Both strings are NOT equal")
#4
#5
n = int(input("Enter a number: "))
total=(n*(n+1))/2
print(f"The sum till our number is {total}")
#6
number= int(input("Enter a number: "))

print("Even numbers are:")

for i in range(1,number):
    if i%2==0:
        print(i)
#7
num = int(input("Enter a number: "))
op = input("Enter OP (+ or -): ")

if op == "+":
    for i in range(0, num):
        print(i, end=", ")

elif op == "-":
    for i in range(num, 0, -1):
        print(i, end=", ")
