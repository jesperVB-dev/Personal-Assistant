from time import strftime
from AlarmModule import Hour,Minute
class Checker:
    def AlarmCheck():
        #print(Hour,Minute)
        ## Alarm
        for i in range(0,len(Hour)):
            if strftime("%H") == Hour[i]:
                if strftime("%M") == Minute[i]:
                    return "You're alarm for " + strftime("%H") + " " + strftime("%M") + " alarm alarm alarm"
        return False    
