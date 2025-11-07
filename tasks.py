# a,b,c=10,30,20
# if a>b and a>c:
#     print("a is the greatest")
# elif b>a and b>c:
#     print("b is the greatest")
# else:
#     print("c is the greatest")

# a= 232
# sum = 0
# count = 0
# while a>0:
#     digit = a%10
#     sum = sum + digit
#     a = int(a/10)
#     count = count + 1

# print(sum)
# print(count)




# Q2: Check if a number is prime or not

# from math import sqrt
# a= int(input("Enter a number: "))
# for i in range(2,int(sqrt(a))):
#     if a%i==0:
#         print("Not a prime number")
#         break
# else:
#     print("prime number")


# Q3: Factorial of a number

# a= int(input("Enter a number: "))
# factorial = 1
# for i in range(1,a+1):
#     factorial = factorial * i
# print(factorial)


#Q4 python program to display all prime numbers within an interval

# from math import sqrt
# a = int(input("Enter lower range: "))
# b = int(input("Enter upper range: "))
# for num in range(a,b+1):
#     if num>1:
#         for i in range(2,int(sqrt(num))):
#             if num%i==0:
#                 break
#         else:
#             print(num)



# Q5: Sum of even digits of a number
# a= 232
# sum = 0
# while a>0:
#     digit = a%10
#     if digit%2==0:
#         sum = sum + digit
#     a = int(a/10)
# print(sum)


# Q6: check a number is palindrome or not
# a= int(input("Enter a number: "))
# temp = a
# rev = 0
# while a>0:
#     digit = a%10
#     rev = rev*10 + digit
#     a = int(a/10)
# if temp==rev:
#     print("palindrome")     
# else:
#     print("not a palindrome")

# Q7: check if a number is Armstrong or not
a = int(input("Enter a number:"))
temp = a
sum = 0
count = 0

while a>0:
    count = count + 1
    a = int(a/10)

a = temp
while a>0:
    digit = a%10
    sum = sum + digit**count
    a = int(a/10)

if temp==sum:
    print("Armstrong")
else:
    print("Not an Armstrong")






