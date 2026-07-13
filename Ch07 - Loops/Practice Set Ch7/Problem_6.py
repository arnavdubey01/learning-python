# 6. Write a program to calculate the factorial of a given number using for loop.

num = int(input("Enter the number: "))

pdt = 1

for i in range(1, num +1):
    pdt *= i    #Same as: pdt = pdt * i
print(pdt)



# Mistake:
# num = int(input("Enter the number: "))

# i = 1

# for i in range(0, num + 1):
#     print((num)*(num - i))

#     i += 1
#     num -= i
