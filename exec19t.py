#Write a generatePassword() function that has a length parameter. The length
#parameter is an integer of how many characters the generated password should have. For security
#reasons, if length is less than 12, the function forcibly sets it to 12 characters anyway. The password
#string returned by the function must have at least one lowercase letter, one uppercase letter, one
#number, and one special character. The special characters for this exercise are ~!@#$%^&*()_+.

import random

#FINISHED
LOWER_LETTERS = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
UPPER_LETTERS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
NUMBERS = ["1","2","3","4","5","6","7","8","9","0"]
SPECIAL = ["~","!","@","#","$","%","^","&","*","(",")","_","+"]
def generatePassword(length):
    if length < 12:
        length = 12
    length -= 4
    all = LOWER_LETTERS + UPPER_LETTERS + NUMBERS + SPECIAL
    password = ""
    password += random.choice(LOWER_LETTERS) + random.choice(UPPER_LETTERS) + random.choice(NUMBERS) + random.choice(SPECIAL)
    i = 1
    for i in range(length):
        password += random.choice(all)
    password = random.sample(password, len(password))
    finalpass = ""
    for each in password:
        finalpass += each
    return finalpass
assert len(generatePassword(8)) == 12
pw = generatePassword(14)
assert len(pw) == 14
hasLowercase = False
hasUppercase = False
hasNumber = False
hasSpecial = False
#-------------------------------------------------------------RESULTS
try:
    assert len(generatePassword(8)) == 12
    pw = generatePassword(14)
    assert len(pw) == 14
    hasLowercase = False
    hasUppercase = False
    hasNumber = False
    hasSpecial = False
    for character in pw:
        if character in LOWER_LETTERS:
            hasLowercase = True
        if character in UPPER_LETTERS:
            hasUppercase = True
        if character in NUMBERS:
            hasNumber = True
        if character in SPECIAL:
            hasSpecial = True
    assert hasLowercase and hasUppercase and hasNumber and hasSpecial
    print("All right!")
except:
    print("WRONG ALGORITHM")