# 5. Repeat program 4 for a list of such words to be censored.
 
with open("file.txt") as f:
     content=f.read()

words = ["Donkey", "bad", "ganda"]

for word in words:
     content=content.replace(word, "#"*len(word))

with open("file.txt", "w") as f:
     f.write(content)


#Mistake:

# with open("file.txt", "r") as f:
#     content=f.read()

# words = ["Donkey", "bad", "ganda"]

# with open("file.txt", "w") as f:
#     if word in content:
#             f.replace("words", "#"*len(words))
