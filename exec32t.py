def convertStrToInt(string):
    STR_TO_DIGITS = {"0":0, "1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
    num,count = 0,0
    for each in string:
        num += STR_TO_DIGITS[each] * 10**((len(string)-1)-count)
        count+=1
    return num

number = convertStrToInt("81273")
print(type(number))
print(number)