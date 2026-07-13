# 2. Write a program to fill in a letter template given below with name and date. 
# letter = '''  
#        Dear <|Name|>, 
#        You are selected! 
#        <|Date|> 
#         ''' 

letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> 
''' 

print(letter.replace("<|Name|>", "Arnav").replace("<|Date|>", "5 May 2026"))

#So what we basically did, is, we first replaced <|Name|> with "Arnav" in the 'letter' string.
#Then in the string with <|Name|> replaced, we further replaced <|Date|> with "5 May 2026".

#This basically means, .replace function can be chained!



#Mistake: Didn't interpret problem accurately.
# name=input("Enter Your Name: ")
# date=input("Enter Date: ")

# print(f'''Dear {name},
# You are selected!
# {date}
# ''')