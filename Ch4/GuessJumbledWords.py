#Guess Jumbled Up Words
import random

WORDS = ("Hello", "Wilson", "Today")
getWord = random.choice(WORDS)
origWord = getWord

randomizeWord = ""
#Randomise Word
for counter in range(len(getWord)):
    #Choose one
    randPos = random.randrange(0,len(getWord))
    #print("pos: " , randPos)
    
    #print(getChar)
    randomizeWord += getWord[randPos]
    #print("RandomizeWord: ", randomizeWord)

    #Modify getWord
    getWord = getWord[:randPos] + getWord[(randPos+1):]
    #print("Remaining: ", getWord)


print("Guess Jumbled: ", randomizeWord)

guessStatus = False

#Keep looping until guessed correctly
while not guessStatus:
    getInStr = input("Input guess Str: ")

    #Compare each char from the string
    matchAll = True

    if len(origWord) == len(getInStr):
        for idx in range(len(origWord)):
            #print("  getInStr[",idx,"]", getInStr[idx], "   randomizeWord[",idx,"]", getWord[idx])
            if getInStr[idx] != origWord[idx]:
                matchAll = False
                #print("  matchedAll: ", matchAll)

            if matchAll:   
                print("\nWord Matched: ", getInStr," == ", origWord)
                guessStatus = True
                break

    else:
        matchAll = False;
        print("  size wrong")

    #print()              
    if guessStatus:        
        break
    else:
        print("No matched word in DB, Try again")

getInput = input("\nPress any key to exit")
