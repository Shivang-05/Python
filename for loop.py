#1
n = int(input("Enter a number: "))
total=(n*(n+1))/2
print(f"The sum till our number is {total}")
#2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(num, "*", i, "=", num * i)
#3
#4
user_string=input("Enter a number:")
user_string=list(user_string)
reverse_string=user_string[::-1]
if reverse_string==user_string:
    print("The given number is palindrome")
else:
    print("The given number  is not palindrome")
#5
for i in range(1,50):
    if i%3==0 and i%5==0 :
        print("Fizzbuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5 == 0:
        print("buzz")
    else:
        print(i)
