# add_lambda = lambda x, y: x + y
# print(add_lambda(5, 3)) 


from functools import reduce

number = 544
sum_of_digits = reduce(lambda x, digit: x + int(digit), str(number), 0)
print(sum_of_digits) 


number = 7447
sum_of_digits = sum(map(lambda x: int(x), str(number)))
print(sum_of_digits) 





