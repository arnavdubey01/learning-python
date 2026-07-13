# 4. Write a program to display a/b where a and b are integers. 
# If b=0, display infinite by handling the 'ZeroDivisionError' 

a = int(input("Enter first number 'a': "))
b = int(input("Enter second number'b': "))

try:
    print(f"a/b = {a/b}")

except ZeroDivisionError as z:
    print("Infinite")