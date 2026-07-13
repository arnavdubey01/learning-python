#While loop first checks condition before executing.

i = 1

while(i<6):
    print(i)
    i += 1     # 'i += 1' is same as typing: 'i = i + 1'


#Basically what happens is: 


#The loop first checks: i = 1, so is 1<6 (i<6)? Yes, so it prints '1'

#Then, we have typed i+=1, which means: increase the value of i by 1.

#Now i is 2, the code repeats again and checks: i = 2, so is 2<6? Yes, so it prints '2'

#The loop keeps repeating until the condtion is not met.

#So when on the 5th time when loop repeats, the value of i becomes 6.
#So it checks: i = 6, is 6<6? No. So it stops the loop and doesn't print '6'.

#Note that the given condition must become false once to stop the loop, or else the program will run non-stop, looping infinitely.

#How is while loop different from normal loop (for i in range( , ))??
#Well, both do same thing, but different ways. You have to find which method is suitable for the specific problem.
