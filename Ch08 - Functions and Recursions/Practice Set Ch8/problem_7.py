# 7. Write a python function to remove a given word from a list and strip it at the same time
#Seems like a vague problem...

def func(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Harry", "Rohan", "an", "Shubhman"]
print(func(l, "an"))




#Mistake: It removed a given word, but didn't strip.
def func(l, word):
    l.remove(word)
    return l

l = ["Harry", "Rohan", "an", "Anshuman"]
print(func(l, "an"))
