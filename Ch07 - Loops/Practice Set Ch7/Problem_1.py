# 1. Write a program to print multiplication table of a given number using for loop.

number = int(input("Enter the number: "))
upto = int(input("Table times?: "))

for i in range(1, upto + 1):
    print(number, "*", i, "=", number * i)

#######################

#Alternatively, to make a simpler version that just prints table from 1 to 10:
n = int(input("Enter the number: "))

for i in range(1,11):
     print(f"{n} * {i} = {n*i}")    #f string used here

#######################

#Mistake: No mistake, but just a bit messier.
number = int(input("Enter the number: "))
upto = int(input("Table upto?: "))

j = 1
for i in range(number, (upto + 1), number):
     print(number,"*",j,"=",i)
     j += 1
