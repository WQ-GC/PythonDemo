myTuple = (1,2,3) #Tuple
print(myTuple, " - ", type(myTuple))
count = 0
for item in myTuple:
    print("Tuple",count, ":", item)
    count +=1


mySet = {1,2,3} #Set
print(mySet," - ", type(mySet))
count = 0
for item in mySet:
    print("Set",count, ":", item)
    count +=1

myList = [1,2,3] #List
print(myList, " - ", type(myList))
count = 0
for item in myList:
    print("List",count, ":", item)
    count +=1

getInput = input("\nPress any key to exit")
