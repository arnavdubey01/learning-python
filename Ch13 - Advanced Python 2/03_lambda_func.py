def square(n):
    return n*n

print(square(5))

# The same thing as above can be done by:

square = lambda x: x*x
print(square(5))

# lambda arguments: expression

# We can also give multiple arguements:

sum = lambda a, b, c: a + b + c
print(sum(1,2,3))
