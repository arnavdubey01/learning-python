name = 'Arnav'      # "Arnav" is a string
name1 = "Arnav"      # "Arnav" is a string
name2 = '''Arnav'''  # "Arnav" is a string
#All forms given above are correct.

print("namelength".center(40,"-"))
namelength = len(name)  #This prints length of string, which here is 5 (A,r,n,a,v)
print(namelength)


print("nameshort".center(40,"-"))
#stringlength = name[ind_start:ind_end]
nameshort = name[0:3] # start from index 0 all the way till 3, excluding 3.
print(nameshort)

print("character1".center(40,"-"))
character1 = name[1]
print(character1)