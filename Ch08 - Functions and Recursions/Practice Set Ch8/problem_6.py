# 6. Write a python function which converts inches to cms.

def in_cm(inch):
    return inch*2.54

n = float(input("Enter inches: "))
a = in_cm(n)

print(f"{n} inch = {round(a, 2)} cm")   #rounded to two decimal places.