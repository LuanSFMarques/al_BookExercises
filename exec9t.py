#EXERCISE #9 : CHESS SQUARE COLOR
#Write a getChessSquareColor() function that has parameters column and row. The
#function either returns 'black' or 'white' depending on the color at the specified column and
#row. Chess boards are 8 x 8 spaces in size, and the columns and rows in this program begin at 0 and
#end at 7 like in Figure 9-1. If the arguments for column or row are outside the 0 to 7 range, the
#function returns a blank string.

#Finished
#-------------------------------------------------------------Def
def getChessSquareColor(column, row):
    column -= 1
    row -= 1 
    if column > 7 or row > 7 or column < 0 or row < 0:
        return ''
    if column % 2 == 0:
        if row % 2 == 0:
            return 'white'
        else:
            return 'black'
    else:
        if row % 2 == 0:
            return 'black'
        else:
            return 'white'
#-------------------------------------------------------------RESULTS
try:
    assert getChessSquareColor(1, 1) == 'white'
    assert getChessSquareColor(2, 1) == 'black'
    assert getChessSquareColor(1, 2) == 'black'
    assert getChessSquareColor(8, 8) == 'white'
    assert getChessSquareColor(0, 8) == ''
    assert getChessSquareColor(2, 9) == ''
    print("All right!")
except:
    print("WRONG ALGORITHM")





