#Sum/Average Program
#Your first and last name: Joseph DeRosa
#Your student ID: s1267829

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:
end = False
numbers=[]


for x in range (0,20):
    anumber= int(input ("Enter a number: "))
    numbers.append(anumber)

(Sumint) = 0
for x in range(0,20):
    Sumint=Sumint+numbers[x]
print("The Sum of the numbers you entred is: ",Sumint)

(avg)=len(numbers)
average=Sumint/avg
print ("The average of the numbers you entered is: ",average)
       


    
    
  
