# lst = ['Mango','Apple','Papaya','banana','kiwi']
# lst1 = [10,40,20,50,30]

# l = len(lst)

# print(lst[0])
# print(lst[l-1])
# print(lst[-1])
# print(lst)


# print(lst1[0])
# print(lst1[l-1])

# for items in lst:
#     print(items)



# lst.append("pineAppple")
# print(lst)


# for items in lst:
#     print("i like "+items)

# lst.insert(2,"blackbery")

# for items in lst:
#     print("i like "+items)


# lst.remove("Apple")
# print(lst)


# a = lst.pop(-1)
# print(a)
# print(lst)


# del lst[-1]
# print(lst)

# a = [1,2]
# b = [3,4]
# print(a+b)


# check  in lst mango pressent or not using in and not in

# if "Mango" in lst:
#     print("present")

# if "Mango" not in lst:
#     print("not present")


# sum = 0
# for i in lst1:
#     sum = sum + i

# print(sum)    

# l= len(lst1)
# average = sum / l
# print(average)

# min and max
# min = lst1[0]
# max = lst1[0]
# for i in lst1:
#     if i < min:
#         min = i
#     if i >max:
#         max = i





#  add dupilcates in lst1
# lst1.append(10)
# lst1.append(10)
# lst1.append(20) 
# lst1.append(30)
# lst1.append(20)


# print count
# print(lst1)
# print(lst1.count(10))


# lst = ['x','y','z','a','y','x']
# find first index of y without function index
# print(lst.index('y'))
# for i in range(len(lst)):
#     if i == 'y':
#         print(lst.index(i))
#         break


# count = 0
# for i in lst:
#     if i == 'y':
#       count = count + 1

# print(count)

# fruits = ['Mango','Apple','Papaya','banana','kiwi']
# fruits.reverse()

# # cnvert fruits into uppercase
# for i in range(len(fruits)):
#     fruits[i] = fruits[i].upper()  

# print(fruits)




# numbers = [10, 20, 30, 40, 50,60,70,80]

#print all numbers
# print(numbers[:]) 

#print from index 0 to index 3
# print(numbers[2:5])




# Date:-10/11/2025

lst = [2,3,2,4,3,5,5]
# new_lst = []
# for i in lst:
#     if i not in new_lst:
#         new_lst.append(i)   
# print("original list:",lst)
# print("list after removing duplicates:",new_lst)


#two sum problem
# target = 6
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i] + lst[j] == target:
#             print("index:",i,j)
#             print("numbers:",lst[i],lst[j])
#             break

# optimized approach
# seen = {}
# for i in range(len(lst)):
#     complement = target - lst[i]
#     if complement in seen:
#         print("index:",seen[complement],i)
#         print("numbers:",complement,lst[i])
#     seen[lst[i]] = i

#running sum
# a = [1,2,3,4]
# lst = []
# sum = 0

# for i in a:
#     sum+=i
#     lst.append(sum)
# print(lst)   
# 


# move all zeros to end without changing the order of other elements inplace
# lst2 = [2,4,0,1,0,2,0,4,3,0]
# new_lst = []
# count = 0
# for i in lst2:
#     if i != 0:
#         new_lst.append(i)
#     else:
#         count += 1
# for i in range(count):
#     new_lst.append(0) 
# print("original list:",lst2)
# print("list after moving zeros to end:",new_lst)




# optimized approach inplace
# lst2 = [2,4,0,1,0,2,0,4,3,0]
# index = 0
# for i in range(len(lst2)):
#     if lst2[i] != 0:
#         lst2[index] = lst2[i]
#         index += 1
# for i in range(index, len(lst2)):
#     lst2[i] = 0
# print("list after moving zeros to end:",lst2)


# names = ["ram", "shyam", "neha", "rohit"]

# count = 0
# for name in names:
#     if 'a' in name:
#         count += 1
# print("Number of names containing 'a':", count)








































