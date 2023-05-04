#Write a rollDice() function with a numberOfDice parameter that represents the number of
#six-sided dice. The function returns the sum of all of the dice rolls. For this exercise you must import
#Python’s random module to call its random.randint() function for this exercise.

#FINISHED
import random

def rollDice(numberOfDice):
    x = 0
    sum = 0
    while x < numberOfDice:
        sum += random.randint(1, 6)
        x += 1
    return sum

#-------------------------------------------------------------RESULTS
try:
    assert rollDice(0) == 0
    assert rollDice(1000) != rollDice(1000)
    for i in range(1000):
        assert 1 <= rollDice(1) <= 6
        assert 2 <= rollDice(2) <= 12
        assert 3 <= rollDice(3) <= 18
        assert 100 <= rollDice(100) <= 600
    print("All right!")
except:
    print("WRONG ALGORITHM")