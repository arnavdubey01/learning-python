# Write a program to calculate the grade of a student from his marks from the following
# scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 => C
# 50 – 60 => D
# <50 => F

marks= int(input("Enter total marks out of 100: "))

if (marks>100 or marks<0):
    print("Enter valid marks.")

elif (marks>90):
    print("Grade: Ex")
 
elif (marks>80):
    print("Grade: A")
 
elif (marks>70):
    print("Grade: B")
 
elif (marks>60):
    print("Grade: C")
 
elif (marks>50):
    print("Grade: D")

else:
    print("Grade: F")

#or, use grade as variable, print once at the end:
 
marks= int(input("Enter total marks out of 100: "))

if (marks>100 or marks<0):
    print("Enter valid marks.")

elif (marks>90):
    Grade= "Ex"
 
elif (marks>80):
    Grade= "A"
 
elif (marks>70):
    Grade= "B"
 
elif (marks>60):
    Grade= "C"
 
elif (marks>50):
    Grade= "D"

else:
    Grade= "F"


    print("Grade:",Grade)
#Here, you have to give indentation before 'print("Grade:",Grade)', 
#or else, it will show error, as it will sit at level of first 'if'.
 