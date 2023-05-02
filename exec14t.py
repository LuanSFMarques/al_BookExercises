#Write an average() function that has a numbers parameter. This function returns the
#statistical average of the list of integer and floating-point numbers passed to the function. While
#Python’s built-in sum() function can help you solve this exercise, try writing the solution without
#using it.
#Passing an empty list to average() should cause it to return None.

#FINISHED
def average(numbers):
    if len(numbers) == 0:
        return None
    sum = 0
    for each in numbers:
        sum += each
    return sum/len(numbers)
#-------------------------------------------------------------RESULTS
try:
    assert average([1, 2, 3]) == 2
    assert average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2
    assert average([12, 20, 37]) == 23
    assert average([0, 0, 0, 0, 0]) == 0
    import random
    random.seed(42)
    testData = [1, 2, 3, 1, 2, 3, 1, 2, 3]
    for i in range(1000):
        random.shuffle(testData)
        assert average(testData) == 2
    print("All right!")
except:
    print("WRONG ALGORITHM")
