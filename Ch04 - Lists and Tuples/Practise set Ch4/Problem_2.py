# 2. Write a program to accept marks of 6 students and display them in a sorted manner.

#Just copy paste problem_1 with a few cosmetic changes, and to sort, add .sort to sort it in increasing order.


marks = []

m1 = int(input("Enter marks: "))
marks.append(m1)
m2 = int(input("Enter marks: "))
marks.append(m2)
m3 = int(input("Enter marks: "))
marks.append(m3)
m4 = int(input("Enter marks: "))
marks.append(m4)
m5 = int(input("Enter marks: "))
marks.append(m5)
m6 = int(input("Enter marks: "))
marks.append(m6)

marks.sort()

print(marks)
 
 #Note that if we didn't use 'int(input("..."))' and just used input("..."), then it would have sorted numbers as string. It would not have been increasing order. 
 # I mean,  if sample is 23, 254, 612, 40, 68, 90; enters WITHOUT 'int(input("...")); then it would be sorted as ['23', '254', '40', '612', '68', '90'].