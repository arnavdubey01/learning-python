# 1. Write a program using functions to find greatest of three numbers.

def greatestnum():
    n1 = int(input("Enter number:"))
    n2 = int(input("Enter number:"))
    n3 = int(input("Enter number:"))

    if n1>n2 and n1>n3:
        return (f"{n1} is greatest.")
    elif n2>n1 and n2>n3:
        return (f"{n2} is greatest.")
    elif n3>n1 and n3>n2:
        return (f"{n3} is greatest.")
    else:
        return ("Error")
    
print(greatestnum())