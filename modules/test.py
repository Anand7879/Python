# import simplemath
# print(simplemath.x)
# simplemath.add(30,20)
# simplemath.product(10,4)


# import simplemath as sm
# print(sm.x)
# sm.add(100,200)
# sm.product(5,6)

# simplemath.add(15,25)  ERROR because simplemath is imported as sm

# from simplemath import x,add
# print(x)
# add(7,8)
# product(3,4)  # ERROR because product is not imported



# check palindrome using lambda 

word = input("Enter a word: ")
reverse = lambda s: ''.join(reversed(s))

is_palindrome = lambda s: s == reverse(s)
if is_palindrome(word):
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")




