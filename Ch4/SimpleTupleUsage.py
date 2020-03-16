#Creates a Simple Tuple

myTuple = () #create a tuple
myInt = int(123)
myDouble = float(2.345)
myStr = "Hello Tuple"

myTuple = (myInt, myDouble, myStr)
print(myTuple)
print(type(myTuple))
print("size: " ,len(myTuple))

#Iterate Tuple
print()
print("Iterate by item")
for item in myTuple:
    print(item)


#Iterate Tuple by Indexing
print()
print("Iterate by index")
count = 0
for count in range(len(myTuple)):
    print(count, ":", myTuple[count])
    count +=1


#Check if content is in Tuple
#No need to loop through all values
#in takes care of the entire search
myVar = 123
print()
print("Search in tuple: ", myVar)
if myVar in myTuple:  
    print(myVar, "present in myTuple")
else:
    print(myVar, "NOT present in myTuple")

myVar = 2.345
print()
print("Search in tuple: ", myVar)
if myVar in myTuple:  
    print(myVar, "present in myTuple")
else:
    print(myVar, "NOT present in myTuple")

myVar = "Hello Tuple"
print()
print("Search in tuple: ", myVar)
if myVar in myTuple:  
    print(myVar, "present in myTuple")
else:
    print(myVar, "NOT present in myTuple")

#Print with Index
print("=========================")
print(-1, myTuple[-1])
print(-2, myTuple[-2])
print(-3, myTuple[-3])


#Print with Start Pt and End Pt
print("=========================")
print(myTuple[:])#Entire Tuple
print(myTuple[:3])#First to last
print(myTuple[:2])#First to 2nd
print(myTuple[:1])#First to First

print("=========================")
print(myTuple[:])#Entire Tuple
print(myTuple[0:])
print(myTuple[1:])
print(myTuple[2:])

print("=========================")
print(myTuple[0:3])#Print in Reverse


#Add to Tuple
#Create a new tuple and then concat to existing tuple
myOtherTuple = ("111",222,33.3)
myTuple += myOtherTuple;
print(myTuple)


getInput = input("\nPress any key to exit")
