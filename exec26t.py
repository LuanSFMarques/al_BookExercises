#Write a function named printHandshakes() with a list parameter named people which will
#be a list of strings of people’s names. The function prints out 'X shakes hands with Y', where
#X and Y are every possible pair of handshakes between the people in the list. No duplicates are
#permitted: if ―Alice shakes hands with Bob‖ appears in the output, then ―Bob shakes hands with
#Alice‖ should not appear.

#Finished

def printHandshakes(people):
    print("")
    cont = 0 
    for name1 in range(0,len(people)-1):
        for name2 in range(name1,len(people)):
            if people[name1] != people[name2]:
                print(f"{people[name1]} shakes hands with {people[name2]}")    
                cont +=1
    return cont
#-------------------------------------------------------------RESULTS      
try:
    assert printHandshakes(['Alice', 'Bob']) == 1
    assert printHandshakes(['Alice', 'Bob', 'Carol']) == 3
    assert printHandshakes(['Alice', 'Bob', 'Carol', 'David']) == 6
    print("All right!")
except:
    print("WRONG ALGORITHM")
