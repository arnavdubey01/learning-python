# 4. Write a program to filter a list of numbers which are divisible by 5.

def divisible5(n):
    if (n%5 == 0):
        return True
    return False

l = list(range(101))        #list: [1, 2, 3, ..., 100]

f = list(filter(divisible5, l))
print(f)

# or,

l = [1, 232, 4425, 4230, 112, 50, 840, 10]      #(Radnom numbers)

f = list(filter(divisible5, l))
print(f)