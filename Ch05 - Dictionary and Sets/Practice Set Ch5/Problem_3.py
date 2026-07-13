# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
#Let's try:
# 
s = set()
s.add(18)
s.add("18")

print(s)

#So, yes, 18 shows up twice, as string value and integer.