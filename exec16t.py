#Write a mode() function that has a numbers parameter. This function returns the mode, or
#most frequently appearing number, of the list of integer and floating-point numbers passed to the
#function.

#FINISHED
def mode(numbers):
    if len(numbers) == 0:
        return None
    counts = dict()
    for number in numbers:
        counts[number] = counts.get(number, 0) +1
    largest = 0
    for key, value in counts.items():
        if value > largest:
            largest = value
            largestz = key

    return largestz

#-------------------------------------------------------------RESULTS
try:
    assert mode([]) == None
    assert mode([1, 2, 3, 4, 4]) == 4
    assert mode([1, 1, 2, 3, 4]) == 1
    import random
    random.seed(42)
    testData = [1, 2, 3, 4, 4]
    for i in range(1000):
        random.shuffle(testData)
        assert mode(testData) == 4
    print("All right!")
except:
    print("WRONG ALGORITHM")
