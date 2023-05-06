#It takes about 365.25 days for the earth to revolve around the sun. This slight offset would cause
our 365-day calendar to become inaccurate over time. Therefore, leap years have an extra day,
#February 29th. A leap year occurs on all years divisible by four (e.g., 2016, 2020, 2024, and so on).
#However, the exception to this rule is that years divisible by one hundred (e.g., 2100, 2200, 2300, and
#so on) aren’t leap years. And the exception to this exception is that years divisible by four hundred
#(e.g., 2000, 2400, and so on) are leap years.
#Exercise Description
#Write a isLeapYear() function with an integer year parameter. If year is a leap year, the
#function returns True. Otherwise, the function returns False.

#FINISHED
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
#-------------------------------------------------------------RESULTS
try:
    assert isLeapYear(1999) == False
    assert isLeapYear(2000) == True
    assert isLeapYear(2001) == False
    assert isLeapYear(2004) == True
    assert isLeapYear(2100) == False
    assert isLeapYear(2400) == True
    print("All right!")
except:
    print("WRONG ALGORITHM")