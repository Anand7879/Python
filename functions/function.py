# def print_name(name):
#     """ this function print the name"""
#     print(str(name))

# print_name("Anand")
# print(print_name.__doc__) #print doc string of the function




# def get_sum(lst):
#     """
#     This function returns the sum of all the elements in a list
#     """

#     sum = 0
#     for num in lst:
#         sum+=num
#     return sum

# s= get_sum([20,50,32,32])
# print(s)




#scope of variables
# global_var = "This is global variable"

# def test_life_time():
#     """
#     This function test the life time of a variable
#     """
#     local_var = "This is the local variable"
#     print(local_var)
#     print(global_var)


# #calling function
# test_life_time()
# #print global variable global_var
# print(global_var)
# #print local variable local_var
# print(local_var) 






#Python Program to print The HCF And LCM of two Numbers

# def hcf(a, b):
#     """
#     Calculate the HCF (Highest Common Factor) of two numbers
#     """
#     while b != 0:
#         a, b = b, a % b
#     return abs(a)

# def lcm(a,b):
#     """
#     Calculate the  LCM of two numbers using
#     """
#     return (a//hcf(a,b))*b

# num1 = 6
# num2 = 8
# Hcf = hcf(num1, num2)
# Lcm = lcm(num1,num2)
# print(f"HCF of {num1} and {num2} is: {Hcf}")
# print(f"LCM of {num1} and {num2} is: {Lcm}")





# print("Select Option")
# print("1. Addition")
# print ("2. Subtraction")
# print ("3. Multiplication")
# print ("4. Division")

# def add(a, b):
#     return a + b

# def multiply(a, b):
#     return a * b

# def subtract(a, b):
#     return a - b

# def division(a, b):
#     return a / b


# choice = int(input("Enter choice 1/2/3/4 "))

# num1 = float(input("Enter first number:"))
# num2 = float(input("Enter second number:"))

# if choice==1:
#     result = add(num1,num2)
#     print(f"Addition of {num1} and {num2} is: {result}")
# elif choice == 2:
#      result = subtract(num1,num2)
#      print(f"Addition of {num1} and {num2} is: {result}")
   
# elif choice == 3:
#     result = multiply(num1,num2)
#     print(f"multiplication of {num1} and {num2} is: {result}")
# elif choice == 4:
#    result = division(num1,num2)
#    print(f"division of {num1} and {num2} is: {result}")
# else:
#     print("Invalid Choice")









# def factorial(num):
#     if num==1:
#         return 1
#     else:
#         return num * factorial(num-1)


# num = 5
# print ("Factorial of {0} is {1}".format(num, factorial(num)))




# n = int(input("Enter n: "))
# a = 0
# b = 1

# print(" Fibonacci numbers:")

# for i in range(n):
#     print(a, end=" ")  
#     next_num = a+b
    
#     a = b
#     b = next_num




# def fibonacci(num):
#     if num <= 1:
#         return num
#     else:
#         return fibonacci(num-1) + fibonacci(num-2)

# n = 10
# print("Fibonacci sequence")
# for num in range(n):
#     print(fibonacci(num))



# def sum(num):
#     if num <= 0:  
#         return 0
#     elif num == 1:
#         return 1
#     else:
#         return num + sum(num - 1)

# n = 10
# for num in range(n+1):
#     result = sum(num)
    
# print(result)



# def Print(num):
#      if num == 0:
#          return
     
#      print(num)     
#      Print(num-1)
     
# n = 5
# Print(n)





# def print_even(n, limit):

#     if n > limit:
#         return
    

    # if n % 2 == 0:
    #     print(n)
    
#     print_even(n + 1, limit)


# print("Even numbers from 1 to 10:")
# print_even(1, 10)


# def print_even(n):

#     if n<=0:
#         return
    
#     print_even(n-1)

#     if n % 2 == 0:
#         print(n)


# print_even(10)    



def sum_of_digits(n,sum):

    if n==0:
        return
    
    digit = n%10
    if digit%2==0:
        sum = sum + digit

    sum_of_digits(n,sum)

n = 232
sum = 0
sum_of_digits(n,sum)        


# a= 232
# sum = 0
# while a>0:
#     digit = a%10
#     if digit%2==0:
#         sum = sum + digit
#     a = int(a/10)
# print(sum)
    
    




    

