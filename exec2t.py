#Write a convertToFahrenheit() function with a degreesCelsius parameter. This
#function returns the number of this temperature in degrees Fahrenheit. Then write a function named
#convertToCelsius() with a degreesFahrenheit parameter and returns a number of this
#temperature in degrees Celsius.

#Finished
def convertToFahrenheit(degreesCelsius):
    return degreesCelsius * (9 / 5) + 32
def convertToCelsius(degreesFahrenheit):
    return (degreesFahrenheit - 32) * (5 / 9)
#------------------------------------------------test------------------------------------------------
try:
    assert convertToCelsius(0) == -17.77777777777778
    assert convertToCelsius(180) == 82.22222222222223
    assert convertToFahrenheit(0) == 32
    assert convertToFahrenheit(100) == 212
    assert convertToCelsius(convertToFahrenheit(15)) == 15
    print("All right!")
except:
    print("WRONG ALGORITHM")
