# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

D = {
    "kursi" : "Chair",
    "billi" : "Dog",
    "kapde" : "Clothes"
}

word= input("Enter the hindi word you want the meaning of: ")

print(D[word])