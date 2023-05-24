def convertIntToStr(integerNum):
    DIGITS_INT_TO_STR = {0:"0", 1:"1",2:"2",3:"3",4:"4",5:"5",6:"6",7:"7",8:"8",9:"9"}
    numberList = []
    stringNum = ""
    while integerNum>0:
        onesPlaceDigit = integerNum%10
        numberList += DIGITS_INT_TO_STR[onesPlaceDigit]
        integerNum = integerNum//10
    if integerNum < 0:
        stringNum += "-"
    for i in range(0, len(numberList)):
        stringNum += numberList[-i+1]
    return stringNum

print(convertIntToStr(19))
print(convertIntToStr(199))
