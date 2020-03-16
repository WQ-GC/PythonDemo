#Display String with Negative Numbers
textStr = "Hello World"

print("Forward: ", end="")
posCount = 0;
for count in range(len(textStr)):
    print(textStr[posCount], end="")
    posCount += 1

print()
print("Reverse: ", end="")
negCount = -1
for count in range(len(textStr)):
    print(textStr[negCount], end="")
    negCount -= 1


getInput = input("\nPress any key to exit")
