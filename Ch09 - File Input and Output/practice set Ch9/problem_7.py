# 7. Write a program to find out the line number where python is present from ques 6.

with open("log.txt") as f:
    lines = f.readlines()

line_number = 1

for line in lines:
    if("python" in line):
        print(f"Yes, \"python\" is present on line number: {line_number}")
        break   #else won't work if we use break. When the whole loop is exhausted, only then else works.

    line_number += 1
    
else:
    print("python is not present.")


#Alternative (Run for individual line)
# line = 1
# with open("log.txt") as f:
#     line = f.readline()

#     if("python" in line):
#         print(f"Yes, \"python\" is present on line number: {line}")
#     else:
#         print("Python is not present")