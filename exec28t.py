#Write a drawBorder() function with parameters width and height. The function draws the
#border of a rectangle with the given integer sizes. There are no Python assert statements to check
#the correctness of your program. Instead, you can visually inspect the output yourself. For example,
#calling drawBorder(16, 4) would output the following:
#+--------------+
#|              |
#|              |
#+--------------+

#Finished
def drawBorder(width, height):
    if width < 2 or height < 2:
        return print("invalid value")
    linez = "+" + "-"*(width-2) + "+"
    print(linez)
    x = 0
    while x < height-2:
        print("|" + " "*(width-2) + "|")
        x += 1
    print(linez)

#-------------------------------------------------------------RESULTS      

drawBorder(16, 4)