f = open("file.txt")
print(f.read())
f.close()

#The same can be done using 'with' statement: 

with open("file.txt") as f:
    print(f.read())

#Here, there is no need to do f.close() to close the file
#It closees file automatically