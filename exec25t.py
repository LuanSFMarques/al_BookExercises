#Write a program that displays a multiplication table that looks like this:
#  | 1  2  3  4  5  6  7  8  9 10
#--+------------------------------
# 1| 1  2  3  4  5  6  7  8  9 10
# 2| 2  4  6  8 10 12 14 16 18 20
# 3| 3  6  9 12 15 18 21 24 27 30
# 4| 4  8 12 16 20 24 28 32 36 40
# 5| 5 10 15 20 25 30 35 40 45 50
# 6| 6 12 18 24 30 36 42 48 54 60
# 7| 7 14 21 28 35 42 49 56 63 70
# 8| 8 16 24 32 40 48 56 64 72 80
# 9| 9 18 27 36 45 54 63 72 81 90
#10|10 20 30 40 50 60 70 80 90 100

#Finished
def multTable(lines, columns):
    bar_1 = ("  | 1")
    line = ""


    if lines == 0 or lines > 10:
        return print("Error, lines")
    if columns == 0 or columns > 10:
        return print("Error, columns")

    for i in range(2,(columns+1)):
        bar_1 += str(i).rjust(3)
    bar_1 += "\n--+"
    for i in range(1, (len(bar_1)-5)):
        bar_1 += "-"
    print(bar_1)

    a = 1
    for i in range(1,lines+1):
        line = str(i).rjust(2) + "|"
        mult = i * a
        line += str(mult).rjust(2)
        x = 2
        while x < columns+1:
            jorge = x*i
            if jorge < 100:
                line += str(jorge).rjust(3)
            elif jorge >= 100:
                line += str(jorge).rjust(4)
            x +=1
        print(line)
    print("")

multTable(2,2)
multTable(3,5)
multTable(6,6)
multTable(10,10)
    
