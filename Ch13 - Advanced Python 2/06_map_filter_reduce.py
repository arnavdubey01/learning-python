# Map: Map applies a function to all the items in an input_list.

# Map syntax: map(function, input_list)

# Map example:
l = [1, 2, 3, 4, 5]

square = lambda x: x*x

sqList = map(square, l)
print(list(sqList)) #This is iterable.

# ----------------------------

# Filter: Filter creates a list of items for which the function returns true.

# Filter syntax: list(filter(function)

# Filter example:
l = [1, 2, 3, 4, 5]

def even(n):
    if (n%2 == 0):
        return True
    return False    # No need of 'else' anyways.

only_Even = filter(even, l)

print(list(only_Even))

# ----------------------------

# Reduce: Reduce applies a rolling computation to sequential pair of elements.

# Reduce Syntax: 
# from functools import reduce
# val = reduce(function, list1)

# Reduce example:
from functools import reduce
l = [1, 2, 3, 4, 5]

def sum(a, b):
    return a + b

print(reduce(sum,l))
# What it basically does it:
# l = [1, 2, 3, 4, 5], 
# so it first does 1 + 2 (first two elements of list)
# Now, 3, 3, 4, 5; it does 3 + 3 ((1 + 2) + 3).
# Now, 6, 4, 5; it does 6 + 4 ((1 + 2 + 3) + 6).
# Now, 10, 5; it does 10 + 5 ((1 + 2 + 3 + 4) + 5)

# Basically: ((((1+2)+3)+4)+5) = 15 (Output)

# Same can be done for multiplication
mul = lambda x,y: x*y
print(reduce(mul, l)) 

# Same logic: ((((1*2)*3)*4)*5) = 120 (Output)
