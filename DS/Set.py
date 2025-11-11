# Date:-11/11/2025

#Sets
# s = {1,2,3}
# print(s)
# print(type(s))


# Not allowed duplicate

# s={1,2,3,1,4}
# print(s)


# we can make set from a list

# s = set([1,2,3,4,1])
# print(s)


#intialise a set with set() method
# s = set()
# print(type(s))


# s= {1,3}
# set object doesnt support indexing
# print(s[1])


#add element
# s.add(2)
# print(s)


# add multiple elements
# s.update([5,6,1])
# print(s)

# add list and set
# s.update([8,9],{10,2,3})
# print(s)




# Reamove elements from a set
# discard(),remove()

# s = {1,2,3,4,5}
# print(s)

# s.discard(4)
# print(s)


# s.pop()  # remove random element
# print(s)


# s.clear() # remove all items in set using clear() method
# print(s)


# Python SET OPERATION 
# set1 = {1,2,3,4,5}
# set2 = {3,4,5,6,7}

#union of 2 sets using | operator
# print(set1|set2)

# another way 
# print(set1.union(set2))

#intersection of 2 sets using & operator
# print(set1 & set2)

#another way
# print(set1.intersection(set2))


#set difference
# print(set1-set2) # set of elements that are only in set1 but not in set2

#use differnce function
# print(set1.difference(set2))


"""symatric differnce : set of elements in both set1 and set2 except those that are common in both"""

#use ^ operator
# print(set1^set2)

# print(set1.symmetric_difference(set2))




# #find subset
# x = {"a","b","c","d","e"}
# y = {"c","d"}
# print("set 'x' is subset of set 'y':", x.issubset(y))
# print("set 'y' is subset of set 'x':", y.issubset(x))

# #find proper subset
# print("set 'x' is proper subset of set 'y':", x < y)
# print("set 'y' is proper subset of set 'x':", y < x)

# #find superset
# print("set 'x' is superset of set 'y':", x.issuperset(y))
# print("set 'y' is superset of set 'x':", y.issuperset(x))


#Frozen set : immutable set
# fs1 = frozenset([1,2,3,4])
# fs2 = frozenset({3,4,5,6})
# print(fs1)
# print(type(fs1))
# fs1.add(5)  # will give error as frozen set is immutable
# fs1.remove(2) # will give error as frozen set is immutable

# union of frozen set
# print(fs1 | fs2)
# print(fs1.union(fs2))

# intersection of frozen set
# print(fs1 & fs2)
# print(fs1.intersection(fs2))

# difference of frozen set
# print(fs1 - fs2)
# print(fs1.difference(fs2))

# symatric difference of frozen set
# print(fs1 ^ fs2)
# print(fs1.symmetric_difference(fs2))
