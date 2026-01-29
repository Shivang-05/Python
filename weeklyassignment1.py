#1
for i in range(1,50):
    if i%3==0 and i%5==0 :
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)
#2
prime_num=int(input("Enter any number to check prime"))
Prime=True
if prime_num<=1:
    print("Not a prime")
    Prime=False
elif prime_num>1:
    for i in range(2,prime_num):
        if prime_num%i==0:
            Prime=False
            break
print(Prime)
#3
score=int(input("What is your score?"))
if score>=90 and score<=100:
    print("Grade A")
if score>=80 and score<=89:
    print("Grade B")
if score>=70 and score<=79:
    print("Grade C")
elif score>=60 and score<=69:
    print("Grade D")
elif  score<=60:
    print("Grade F")
#4
score=int(input("What is your desired no.?"))
for i in range(11):
    print(f"{score}x{i}={score*i}")
#5
list_of_squares=[]
for i in range(1,21):
    if i%2==0:
        list_of_squares.append(i**2)

print(list_of_squares)
#6
year=int(input("Give the year u want to check?"))
if year%4==0 and year%100!=0:
    print("leap year")
if year%400==0:
    print("leap year")
#7
side_triangle1=int(input("Give the length of the first side?"))
side_triangle2=int(input("Give the length of the second side?"))
side_triangle3=int(input("Give the length of the third side?"))
if side_triangle1==side_triangle2 and side_triangle3==side_triangle2:
    print("Equilateral triangle")
elif side_triangle1==side_triangle2 or side_triangle3==side_triangle2 or side_triangle3==side_triangle1:
    print("Isosceles triangle")
elif side_triangle1!=side_triangle3 and side_triangle2!=side_triangle1:
    print("Scalene triangle")
#8
integer_input=int(input("Give the number you want to check?"))
if integer_input>0:
    print("Positive")
elif integer_input<0:
    print("Negative")
else:
    print("Zero")
#10
weight=float(input("what is your weight(in kgs)?"))
height=float(input("what is your height?(in m)"))
bmi=weight/height**2
if bmi<18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("Normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
elif  bmi>= 30:
    print("Obesity")
#11
weekday_input=int(input("Type a number to determine the weekday"))
rem=weekday_input%7
if rem==0:
    print("Sunday")
elif rem==1:
    print("Monday")
elif rem==2:
    print("Tueday")
elif rem==3:
    print("Wednesday")
elif rem==4:
    print("Thursday")
elif rem==5:
    print("Friday")
elif rem==6:
    print("saturday")
#12
price = float(input("enter price?$"))
if price >= 1000:
    print("You can recieve 10% discount!")
elif price<1000 and price >=500:
    print("You can recieve 5% discount")
else:
    print("Sorry no discount!")
#13
desired_number=int(input("give the number till which you want to get the sum "))
total=(desired_number+1)*desired_number
print(f"the required sum is{total/2} ")
#14
#15
vowels=["a","e","i","o","u"]
vowel_count=0
given_string="Hi wie geht es bei dir? Ich bin gut!"
for x in given_string:
    if x in vowels:
        vowel_count+=1
print(f"The total number of vowels are:{vowel_count}")
#16
given_number=int(input("Enter any number:"))
given_number=str(given_number)
sum=0
for x in given_number:
    x=int(x)
    sum+=x
print(sum)
#17
pattern_input=int(input("Enter n for pattern of stars:"))
decrement=pattern_input
for i in range(pattern_input):
    print("*"*(pattern_input-(decrement-1)))
    decrement-=1
#18
import random
random_num=random.randint(1,100)
tries=5
while tries!=0:
    guess_number = int(input("What is your guess?"))
    if random_num>guess_number:
        print("Too low")
        tries-=1
        print(f"Tries left :{tries}")
    elif random_num<guess_number:
        print("Too high")
        tries -= 1
        print(f"Tries left :{tries}")
    else:
        print("Correct Guess")
#19
req_number=int(input("Enter any number:"))
for i in range(1,req_number):
    if i%2==0:
        print(i)
#20
number_list=[23,25,25,23,524,33,3,24,45,34]
if 25 in number_list:
    print("25 exists in numbers list")
print(f"The length of list is {len(number_list)}")
number_25=0
for x in number_list:
    if x==25:
        number_25+=1
print(f"total occurrence of 25 in the list is {number_25}")
print("all ements in list include ")
for x in number_list:
    print(x)
print('All the even numbers in the list are:')
for x in number_list:
    if x%2==0:
        print(x)
#21
user_string=input("Enter a string of min 10 words and max 19 words:")
print(user_string)
print(f"The length of string is {len(user_string)}")
reverse_string=user_string[::-1]
if reverse_string==user_string:
    print("The given string is palindrome")
else:
    print("The string is not palindrome")
if len(user_string)%2==0:
    middle_word=int(len(user_string)/2)
else:
    middle_word = int((len(user_string)-1) / 2)
print(f"The middle word in string is {user_string[middle_word]}")
print(f"The second last word in string is {user_string[-2]}")
#22
calc=int(input("Welcome to Calci:\n1. Power\n2. Sum\n3. Sub\n4. Multiply\n "))
def Sum():
    num_1=int(input(f'Enter the first number to add '))
    num_2=int(input(f'Enter the second number to add '))
    addition=num_1+num_2
    return addition
def Power():
    num_1 = int(input(f'Enter the first number for base '))
    num_2 = int(input(f'Enter the second number for power '))
    Pow = num_1 ** num_2
    return Pow
def Sub():
    num_1 = int(input(f'Enter the first number to sub '))
    num_2 = int(input(f'Enter the second number to sub '))
    subt = num_1 - num_2
    return subt
def Multiply():
    num_1 = int(input(f'Enter the first number to Multiply '))
    num_2 = int(input(f'Enter the second number to Multiply '))
    multi = num_1*num_2
    return multi
if calc==1:
    print(f"The sum is {Sum()}")
elif calc==2:
    print(f"The power is{Power()}")
elif calc == 3:
    print(f"The differnce is {Sub()}")
elif calc==4:
    print(f"The multiplication is {Multiply()}")
#23
X = ['abc', 'xyz', 'aba', '1221','buch','kuhlschrank','fenster','abracadabra','bb']
count=0
for i in X:
    if len(i)>2 and i[0]==i[-1]:
        count+=1
print(count)
