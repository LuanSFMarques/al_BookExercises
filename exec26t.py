#Write a function named printHandshakes() with a list parameter named people which will
#be a list of strings of people’s names. The function prints out 'X shakes hands with Y', where
#X and Y are every possible pair of handshakes between the people in the list. No duplicates are
#permitted: if ―Alice shakes hands with Bob‖ appears in the output, then ―Bob shakes hands with
#Alice‖ should not appear.

#Finished

def printHandshakes(people):
    print("")
    cont = 0 
    for name1 in people:
        x = 0
        for name2 in people:
            if name1 == name2 or x >= 1:
                if name1 == name2:
                    print("", end="")
                else:
                    print(f"{name1} shakes hands with {name2}")
                    cont += 1
                x += 1
    return cont
#-------------------------------------------------------------RESULTS      
try:
    assert printHandshakes(['Alice', 'Bob']) == 1
    assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
    assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
    print("All right!")
except:
    print("WRONG ALGORITHM")
