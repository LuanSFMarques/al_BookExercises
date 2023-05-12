#Write a drawBox() function with a size parameter. The size parameter contains an integer
#for the width, length, and height of the box. The horizontal lines are drawn with - dash characters,
#the vertical lines with | pipe characters, and the diagonal lines with / forward slash characters. The
#corners of the box are drawn with + plus signs.

#drawBox(1)
#  +--+
# /  /|
#+--+ +
#|  |/
#+--+

#Finished
def drawBox(size):
    if size < 1:
        print ("Non-existent size for box")
    else:
        square = ""
        square += " "*(size+1) + "+" + "-"*(size*2) + "+" + "\n"
        for i in range(0,size):
            square += " "*(size-i) + "/" + " "*(size*2) + "/" + " "*i + "|" + "\n"
        square += "+" + "-"*(size*2) + "+" + " "*size + "+" + "\n"
        for i in range(0,size):
            square += "|" + " "*(size*2) + "|" + " " *(size-1-i) + "/" + "\n"
        square += "+" + "-"*(size*2) + "+" + " "*size + "\n"

        print(square)

#-------------------------------------------------------------RESULTS      
drawBox(5)