#Write a drawPyramid() function with a height parameter. The top of the pyramid has one
#centered hashtag character, and the subsequent rows have two more hashtags than the previous row.
#The number of rows matches the height integer. There are no Python assert statements to check
#the correctness of your program. Instead, you can visually inspect the output yourself. For example,
#calling drawPyramid(8) would output the following:
#       #
#      ###
#     #####
#    #######
#   #########
#  ###########
# #############
################

#Finished
def drawPyramid(height):
    basei = 3
    if height > 1:
        basef = basei + (2 * (height - 2))
    else:
        basef = basei
    i = height
    u = 0
    x = basef-1
    triangle = ""
    while i >= 1:
        triangle += "\n" + " "*(height-u-1) + "#"*(basef-x)
        i -= 1
        u += 1
        x -= 2
    return triangle
    
#-------------------------------------------------------------RESULTS      
print(drawPyramid(8))