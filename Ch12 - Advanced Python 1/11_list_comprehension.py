myList = [1, 2, 5, 6 ,4, 7]

squaredList = []
for item in myList:
    squaredList.append(item*item)

print(squaredList)

# this same thing can be simply done using list comprehension:

squaredList = [item*item for item in myList]
print(squaredList)
