#Write an isValidDate() function with parameters year, month, and day. The function
#should return True if the integers provided for these parameters represent a valid date. Otherwise,
#the function returns False. Months are represented by the integers 1 (for January) to 12 (for
#December) and days are represented by integers 1 up to 28, 29, 30, or 31 depending on the month
#and year. Your solution should import your leapyear.py program from Exercise #20 for its
#isLeapYear() function, as February 29th is a valid date on leap years.

#FINISHED
from exec20t import isLeapYear


def isValidDate(year,month,day):
    if year < 0:
        return False
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        if day >= 1 and day <= 31:
            return True
        else:
            return False
    elif month == 9 or month == 4 or month == 6 or month == 11:
        if day >= 1 and day <= 30:
            return True
        else:
            return False
    elif month == 2:
        if isLeapYear(year) == True:
            if day >= 1 and day <= 29:
                return True
            else:
                return False
        else:
            if day >= 1 and day <= 28:
                return True
            else:
                return False
    else:
        return False
#-------------------------------------------------------------RESULTS
try:
    assert isValidDate(1999, 12, 31) == True
    assert isValidDate(2000, 2, 29) == True
    assert isValidDate(2001, 2, 29) == False
    assert isValidDate(2029, 13, 1) == False
    assert isValidDate(1000000, 1, 1) == True
    assert isValidDate(2015, 4, 31) == False
    assert isValidDate(1970, 5, 99) == False
    assert isValidDate(1981, 0, 3) == False
    assert isValidDate(1666, 4, 0) == False
    print("All right!")
except:
    print("WRONG ALGORITHM")
