#Write a getSmallest() function that has a numbers parameter. The numbers parameter will
#be a list of integer and floating-point number values. The function returns the smallest value in the
#list. If the list is empty, the function should return None. Since this function replicates Python’s
#min() function, your solution shouldn’t use it.

#Finished
def getSmallest(listNum):
    if len(listNum) == 0:
        return None
    debug = False
    for each in listNum:
        if each == listNum[0] and debug == False:
            smallest = each
            debug = True
        elif each < smallest:
            smallest = each
        else:
            continue
    return smallest
#-------------------------------------------------------------RESULTS
try:
    assert getSmallest([1, 2, 3]) == 1
    assert getSmallest([3, 2, 1]) == 1
    assert getSmallest([28, 25, 42, 2, 28]) == 2
    assert getSmallest([1]) == 1
    assert getSmallest([]) == None
    print("All right!")
except:
    print("WRONG ALGORITHM")
    