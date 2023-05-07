#Write a program that displays the lyrics to ―99 Bottles of Beer.‖ Each stanza of the song goes like
#this:
#X bottles of beer on the wall,
#X bottles of beer,
#Take one down,
#Pass it around,
#X – 1 bottles of beer on the wall,
#The X in the song starts at 99 and decreases by one for each stanza. When X is one (and X – 1 is
#zero), the last line is ―No more bottles of beer on the wall!‖ After each stanza, display a blank line to
#separate it from the next stanza.

#Finished
x = 99
if x > 1:
    while x > 1:
        print(f"{x} bottles of beer on the wall,")
        print(f"{x} bottles of beer,")
        print("Take one down,")
        print("Pass it around,")
        x -= 1
if x == 1:
    print("1 bottle of beer on the wall,")
    print("1 bottles of beer,")
    print("Take one down,")
    print("Pass it around,")
    print("No more bottles of beer on the wall!")
