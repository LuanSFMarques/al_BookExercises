#Write a printASCIITable() function that displays the ASCII number and its corresponding
#text character, from 32 to 126. (These are called the printable ASCII characters.)
#Your solution is correct if calling printASCIITable() displays output that looks like the
#following:

#Finished
def printASCIITable():
    print("-------------------------")
    list_num = list(range(32,127))
    for each in list_num:
        if chr(each) == " ":
            print (str(each) + " = " + chr(each) + " (Space character)")
        else:
            print (str(each) + " = " + chr(each))
    print("-------------------------")
    return 


printASCIITable()

print (chr(134))
