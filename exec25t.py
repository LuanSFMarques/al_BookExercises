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
    
