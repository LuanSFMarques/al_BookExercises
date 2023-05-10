#Write a drawRectangle() function with two integer parameters: width and height. The
#function doesn’t return any values but rather prints a rectangle with the given number of hashtags in
#the horizontal and vertical directions.

#finished
def drawRectangle(width, height):
    x = 0
    if width < 1 or height < 1:
        return print("invalid value")
    while x < height:
        print("#"*width)
        x += 1
#-------------------------------------------------------------RESULTS      

drawRectangle(10, 4)