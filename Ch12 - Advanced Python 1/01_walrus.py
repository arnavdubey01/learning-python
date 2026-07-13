# using walrus operator
if (n := len([1, 2, 3, 4, 5])) > 3:
    print(f"List is too long ({n} elements, expected <= 3)")

# here ' := ' is walrus operator. Looks like a walrus too.

# Basiscally, this is for convenience.

# The following is what this walrus operator does in two lines.
n = len([1, 2, 3, 4, 5])
if n > 3:
    print(f"List is too long ({n} elements, expected <= 3)")