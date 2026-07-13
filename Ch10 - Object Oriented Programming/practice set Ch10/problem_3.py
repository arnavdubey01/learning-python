# 3. Create a class with a class attribute a; create an object from it and set ‘aʼ directly using ‘object.a = 0ʼ. Does this change the class attribute?

class problem3:
    a = 4

object = problem3() 
print(object.a)

object.a = 0    #Instance attribute is set.
print(object.a)



#Answer - No, the class attribute isn't changed.

print(problem3.a)  #This still prints class attribute i.e. 4, this means that obejct.a = 0 was instance attribute. Only limited to that instance.

#In line 7, it prints class attribute because instance attribute is not present.

#In line 9, instance attribute is set. So it prints instance attribute.