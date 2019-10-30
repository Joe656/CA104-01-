#Python Richter Scale Calculation
#Your first and last name: Joseph DeRosa
#Your ID:s1267829

#Requirements Version 1:
# ask the user to 'Enter the Richter scale value: '
#   hint1: use an 'input' statement to input a variable called 'richter'
#   hint2: make sure 'richter' is a 'floating point' by using 'float'
# determine the Effect for the Richter scale value entered
#   hint1: use 'if' 'elif' and 'else' statements
#   hint2: remember to use ':' following all 'if' 'elif' and 'else' statements
# display or print the Effect
#   hint: use 'print' statement (only 1 effect should print)

#Additional Requirements Version 2:
# ask the user to 'Enter the Richter scale value or -99 to end: '
#   continue the program until the user enters a richter value of -99
#   if richter = -99, end the program
#   hint1: use a 'while' loop with a 'boolean' like in the guessing game
#   hint2: 'break' may come in handy

# make sure richter scale value is greater than 0
#   if not, print "Value must be greater than 0"
#   and make them enter another value
#   hint: 'continue' may come in handy


# Test your program several times with the following values:
#   8.1, 8.0, 7.1, 7.0, 6.1, 6.0, 4.6, 4.5, 4,4, -4.6

scale=False

while not scale:
    richter = float (input("Enter the Richter scale Value. If you type -99 it will kill the program: "))  
    if (richter == -99):
        scale=True
    elif (richter >= 8.0):
        print ("Most structures will fall")
        continue
    elif (richter >= 7.0):
        print("many building will be destroyed")
        continue
    elif (richter >= 6.0):
        print("most buildings will be considerably damaged, some collapse")
        continue
    elif (richter >= 4.5):
        print("Damage to poorly constructed buidings")
        continue
    elif (richter > 0):
        print("No destruction of buldings") 

    else:
        print("The Value must be greater than 0 enter another value")
        continue 




