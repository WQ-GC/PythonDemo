#include Gets String from user
#Slice the string based on input index

getStr = input("Input string to be sliced: " )
startPt = int(input("Input start pt: "))
endPt = int(input("Input end pt(inclusive): "))

#print("convert all to UPPER: " , getStr.upper())
#print("convert all to LOWER: " , getStr.lower())

#prints startIdx till endIdx (excluding endIdx)
print("\nLeft Str:", getStr[:startPt])
print("\nExtracted Str:", getStr[startPt:endPt])
print("\nRight Str:", getStr[endPt:])

getInput = input("\nPress any key to exit")
