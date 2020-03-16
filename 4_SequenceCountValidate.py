#Displays the length of the sequence
#Checks if value exists in Sequence

getStr = input("Input text sequence: ")
print("Sequence size: " + str(len(getStr)))
#print("type: ", type(len(getStr)))

getSearchStr = input("Input searched text: ")

if getSearchStr in getStr:
    print("Search string present in Text Sequence")
else:
    print("Search string NOT present in Text Sequence")
    


print("================================")
getStr = "12345"
print("String info: ", getStr)
print("Sequence size: " + str(len(getStr)))
x = input("input Search Element: ")
searchStatus = False;

while searchStatus == False:
    #Search through all strings
    print("\nx: " + str(x))
    for curr in getStr:
        print("\n  curr: " + str(curr))
        if str(x) == str(curr):
            print("\nTRUE: ",str(x),str(curr))
            searchStatus = True
            break

getInput = input("\nPress any key to exit")