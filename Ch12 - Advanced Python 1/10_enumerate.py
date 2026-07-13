l = [2, 42, 5, 753]

index = 0
for item in l:
    print(f"The item number at index {index} is {item}")
    index += 1

# This same thing can be simply done with enumerate function.

for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")