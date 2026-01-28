#1
name = input("Enter student name: ")
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
total_marks = sum(marks)
percentage = (total_marks / 500) * 100
print("Name:", name)
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
#2
num_1=int(input("Enter first number "))
num_2=int(input("Enter second number "))
num_3=int(input("Enter third number "))
sum_0=num_3+num_2+num_1
print(f'The sum is {sum_0}')
#3
num = float(input("Enter a number: "))
square = num * num
print("The square of the number is:", square)
#4
celsius_str = input("Enter temperature in Celsius: ")
celsius = float(celsius_str)
fahrenheit = (celsius * 9 / 5) + 32
print("Temperature in Celsius:", celsius)
print("Temperature in Fahrenheit:", fahrenheit)
#5
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
quotient = num1 // num2
remainder = num1 % num2
print("Quotient:", quotient)
print("Remainder:", remainder)
#6
P = float(input("Enter Principal (P): "))
R = float(input("Enter Rate of Interest (R): "))
T = float(input("Enter Time (T): "))
SI = (P * R * T) / 100
print("Simple Interest is:", SI)

