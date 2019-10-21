end = False 

names= []
for x in range (0,10):
    aname=input("Enter a name: ")
    names.append(aname)
while not end:
    print("At any time you can type End with the capital and no spaces to end your search")
    print (names) 
    search = input ("Enter a name you wish to search for:")
    if search == ("End"):
            end = True
    elif search in names:
            print (search, "was found")
    elif search not in names:
            print (search, "was not found")
   
    

   
