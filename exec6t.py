#In English, ordinal numerals have suffixes such as the ―th‖ in ―30th‖ or ―nd‖ in ―2nd‖. Write an
#ordinalSuffix() function with an integer parameter named number and returns a string of the
#number with its ordinal suffix. For example, ordinalSuffix(42) should return the string
#'42nd'.
#You may use Python’s str() function to convert the integer argument to a string. Python’s
#endswith() string method could be useful for this exercise, but to maintain the challenge in this
#exercise, don’t use it as part of your solution.

#Finished
def ordinalSuffix(number):
    sufix = str(number)
    if sufix[-2:] in ("11","12","13"):
        return (sufix + "th")
    if sufix[-1:] == "1":
        return (sufix + "st")
    if sufix[-1:] == "2":
        return (sufix + "nd") 
    if sufix[-1:] == "3":
        return (sufix + "rd") 
    else:
        return (sufix + "th") 
try:
    assert ordinalSuffix(0) == '0th'
    assert ordinalSuffix(1) == '1st'
    assert ordinalSuffix(2) == '2nd'
    assert ordinalSuffix(3) == '3rd'
    assert ordinalSuffix(4) == '4th'
    assert ordinalSuffix(10) == '10th'
    assert ordinalSuffix(11) == '11th'
    assert ordinalSuffix(12) == '12th'
    assert ordinalSuffix(13) == '13th'
    assert ordinalSuffix(14) == '14th'
    assert ordinalSuffix(101) == '101st'
    print("All right!")
except:
    print("WRONG ALGORITHM")
