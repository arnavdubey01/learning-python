a = 65  
# Global variable, can be used everywhere outside func()*


def func():
    global a 
#After this 'global' keyword, the value of global a is being changed.*

    a = 3   # Local variable of 'func()'. 
    print(a)



func()
print(a)



# if 'global a' was not there under func(), the output would have been:
# 3
# 65