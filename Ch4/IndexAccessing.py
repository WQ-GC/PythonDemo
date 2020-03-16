charStr = "Testing"
#intArray = {1, 2, 3, 4, 5} #****define as a set type!!!
intArray = [1, 2, 3, 4, 5] #define as a list type!!!
doubleArray = [1.11, 2.22, 3.33]

print(charStr)
print(type(charStr))
for count in range(len(charStr)):
    print(count, ": ", charStr[count])
print()

print(intArray)
print(type(intArray))
for count in range(len(intArray)):
    print(count, ": ", intArray[count])

print(doubleArray)
print(type(doubleArray))
for count in range(len(doubleArray)):
    print(count, ": ", doubleArray[count])

getInput = input("\nPress any key to exit")
