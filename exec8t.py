#    You will write three functions for this exercise. First, write a writeToFile() function with
#    two parameters for the filename of the file and the text to write into the file. Second, write an
#    appendToFile() function, which is identical to writeToFile() except that the file opens in
#    append mode instead of write mode. Finally, write a readFromFile() function with one parameter
#    for the filename to open. This function returns the full text contents of the file as a string.
#    These Python instructions should generate the file and the assert statement checks that the
#    content is correct:

#Finished
#-------------------------------------------------------------FIRST FUNCTION
def writeToFile(filename, text):
    try:
        test = text + "hi"
    except:
        return "Wrong type of text!"
    
    try:
        with open(filename, 'w') as file_:
            file_.write(text)
    except:
        return "File not found"
#-------------------------------------------------------------SECOND FUNCTION
def appendToFile(filename,text):
    try:
        test = text + "hi"
    except:
        return "Wrong type of text!"
    
    try:
        with open(filename, 'a') as file_:
            file_.write(text)
    except:
        return "File not found"
#-------------------------------------------------------------THIRD FUNCTION
def readFromFile(filename):
    try:
        file_ = open(filename, 'r')
        file_x = file_.read()
        fulltxt = ""
        for each_line in file_x:
            fulltxt = fulltxt + each_line
        return fulltxt
    except:
        return "File not found"
#-------------------------------------------------------------RESULTS
writeToFile('greet.txt', 'Hello!\n')
appendToFile('greet.txt', 'Goodbye!\n')

try:
    assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
    print("All right!")
except:
    print("WRONG ALGORITHM")