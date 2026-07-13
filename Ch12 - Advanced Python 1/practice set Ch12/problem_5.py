# 5. Store the multiplication tables generated in problem 3 in a file named 
# Tables.txt.

n = int(input("Enter the number: "))

table = [n*i for i in range(1, 11)]

with open(r"C:\Users\arnav\OneDrive\Documents\GitHub\learning-python\Ch12 - Advanced Python 1\practice set Ch12\tables.txt", "a") as f: 
#We open the file in append mode.

    f.write(f"Table of {n}: {str(table)} \n") # did '\n' for new line. 

# line 8:
# with open(r"C:\Users\arnav\OneDrive\Documents\GitHub\learning-python\Ch12 - Advanced Python 1\practice set Ch12\tables.txt", "a") as f:  

# with just 'with open("tables.txt", "a") as f:', it creates tables.txt in the main folder opened with VSCode.
