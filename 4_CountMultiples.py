#Demonstrates range() function
#counts multiples

print("Count from 1 to 10\n")
for counter in range(10):
    print(counter)

print("\nCount from 1 to 100, in multiples of 10\n")
for counter in range(1,100,10):
    print(counter)


print("\nCount from 10 to 0 (Backwards)\n")
for counter in range(10,-1,-2):
    print(counter)


getInput = input("\nPress any key to exit")