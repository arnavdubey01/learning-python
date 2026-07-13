# 3. A list contains the multiplication table of 7. Write a program to convert it to vertical string of same numbers.
# 7
# 14
# .
# .
# .

table = [str(7*i) for i in range (1, 11)]  

a = "\n".join(table)
print(a)

# ** join function requires list of string to work, not integer.
# That is why in line 8, we had to type [str(7*i)...]