# 4. Write a recursive function to calculate the sum of first n natural numbers.

def sum(n):
    if n < 0:                   #This is called base condition, this is important as without this, recursion will show error due to calling itself infintely.
        return 0
    return (n + sum(n - 1))

n = int(input("Enter number: "))
print(sum(n))

# n = 5
# 5 + sum(4)
# 5 + 4 + sum(3)
# 5 + 4 + 3+ sum(2)
# 5 + 4 + 3 + 2 + sum(1)
# 5 + 4 + 3 + 2 + 1 + sum(0)
# 5 + 4 + 3 + 2 + 1 + 0

# -------------------------------------

#Mistake: unsupported operand type(s) for +: 'int' and 'str', because return "done", "done" is string, so 0 + done which is int + str shows error because it is not possible.
def sum(n):
    if n <= 0:
        return "done"
    return (n + sum(n - 1))

n = int(input("Enter number: "))
print(sum(n))

# n = 5
# 5 + sum(4)
# 5 + 4 + sum(3)
# 5 + 4 + 3+ sum(2)
# 5 + 4 + 3 + 2 + sum(1)
# 5 + 4 + 3 + 2 + 1 + sum(0)
# 5 + 4 + 3 + 2 + 1 + done          #This 1 + done is the issue. Python can't add integer and string obv!!