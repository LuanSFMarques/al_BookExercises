#Write a getHoursMinutesSeconds() function that has a totalSeconds parameter. The
#argument for this parameter will be the number of seconds to be translated into the number of hours,
#minutes, and seconds. If the amount for the hours, minutes, or seconds is zero, don’t show it: the
#function should return '10m' rather than '0h 10m 0s'. The only exception is that
#getHoursMinutesSeconds(0) should return '0s'.

#Finished
def getHoursMinutesSeconds(totalSeconds):
    seconds = totalSeconds
    minutes = 0
    hours = 0
    if seconds == 0:
        return "0s"
    if seconds >= 60:
        while seconds >= 60:
            seconds -= 60
            minutes += 1
    if minutes >= 60:
        while minutes >= 60:
            minutes -= 60
            hours += 1 
    if seconds == 0:
        secondsstring = ""
    else:
        secondsstring = str(seconds) + "s "

    if minutes == 0:
        minutesstring = ""
    else:
        minutesstring = str(minutes) + "m "
    if hours == 0:
        hoursstring = ""
    else:
        hoursstring = str(hours) + "h "
    finalstring = hoursstring + minutesstring + secondsstring
    return(finalstring.strip())
#-------------------------------------------------------------RESULTS
try:
    assert getHoursMinutesSeconds(30) == '30s'
    assert getHoursMinutesSeconds(60) == '1m'
    assert getHoursMinutesSeconds(90) == '1m 30s'
    assert getHoursMinutesSeconds(3600) == '1h'
    assert getHoursMinutesSeconds(3601) == '1h 1s'
    assert getHoursMinutesSeconds(3661) == '1h 1m 1s'
    assert getHoursMinutesSeconds(90042) == '25h 42s'
    assert getHoursMinutesSeconds(0) == '0s'
    print("All right!")
except:
    print("WRONG ALGORITHM")