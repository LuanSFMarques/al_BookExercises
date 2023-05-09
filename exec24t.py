x = "12:00"
time = "am"
#Write a program that displays the time for every 15 minute interval from 12:00 am to 11:45 pm.
#Your solution should produce the following output:
#12:00 am
#12:15 am
#12:30 am
#12:45 am
#1:00 am
#1:15 am
#--cut--
#11:30 pm
#11:45 pm


#Finished
x1 = int(x.split(":")[0])
x2 = int(x.split(":")[1])

print(str(x1)+":"+"{:02d}".format(x2),time)
y = 1
while x1 != 11 or x2 != 45:
    x2 += 15
    if x2 >= 60:
        x2 -= 60
        x1 += 1
    if x1 >= 13:
        x1 -= 12
        if time == "am":
            time = "pm"
        elif time == "pm":
            time = "am"
    y += 1
    print(str(x1)+":"+"{:02d}".format(x2),time)

    
        