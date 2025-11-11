#Q1 print all the characters from the  list which are in all the names in the list use for the beginners in coding and python
list = ["anand", "pravesh", "aman", "rahul", "ankit", "sachin"]
firstElement = list[0]

result = set(firstElement)

for i in range(1, len(list)):
    name = list[i]
    result = result.intersection(set(name))
    
print("Common characters in all names:", result)















