#Write a getSmallest() function that has a numbers parameter. The numbers parameter will
#be a list of integer and floating-point number values. The function returns the smallest value in the
#list. If the list is empty, the function should return None. Since this function replicates Python’s
#min() function, your solution shouldn’t use it.

#FINISHED
def calculateSum(numbers):
    if len(numbers) == 0:
        return 0
    sum = 0
    for each in numbers:
        sum += each
    return sum
def calculateProduct(numbers):
    if len(numbers) == 0:
        return 1
    prod = 1
    for each in numbers:
        prod *= each
    return prod
#-------------------------------------------------------------RESULTS

try:
    assert calculateSum([]) == 0
    assert calculateSum([2, 4, 6, 8, 10]) == 30
    assert calculateProduct([]) == 1
    assert calculateProduct([2, 4, 6, 8, 10]) == 3840
    print("All right!")
except:
    print("WRONG ALGORITHM")