#EXERCISE #10:FIND AND REPLACE

#Write a findAndReplace() function that has three parameters: text is the string with text to
#be replaced, oldText is the text to be replaced, and newText is the replacement text. Keep in mind
#that this function must be case-sensitive: if you are replacing 'dog' with 'fox', then the 'DOG' in
#'MY DOG JONESY' won’t be replaced.

#Finished
def findAndReplace(text, oldText, newText):
    replacedText=''
    i = 0
    while i < len(text):
        if text[i:i+len(oldText)] != oldText:
            replacedText += text[i]
            i += 1
        else:
            replacedText += newText
            i += len(oldText)
    return replacedText


#-------------------------------------------------------------RESULTS
try:
    assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'
    assert findAndReplace('fox', 'fox', 'dog') == 'dog'
    assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'
    assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'
    assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
    print("All right!")
except:
    print("WRONG ALGORITHM")