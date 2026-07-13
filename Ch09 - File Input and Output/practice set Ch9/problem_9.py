# 9. Write a program to find out whether a file is identical and matches the content of another file

with open ("poems.txt") as f:
    content1 = f.read()

with open ("file.txt") as f:
    content2 = f.read()

if content1 == content2:
    print("file1 and file2 are identical.")
else:
    print("file1 and file2 are not identical")