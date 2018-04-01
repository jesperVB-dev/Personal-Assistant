from time import strftime
import math

Hour = []
Minute = []
CiphersLetters = ["one","two","three","four","five","six","seven","eight","nine"]
CiphersNumber = ["1","2","3","4","5","6","7","8","9"]

class Alarm:
    def Questions(text):
        if " alarm " in text:
            for i in range(0,len(CiphersLetters)):
                text = text.replace(CiphersLetters[i], CiphersNumber[i])
            if " at " in text:
                SplittedAlarm = text.split(":")
                Hour.append(SplittedAlarm[0][-2:])
                Minute.append(SplittedAlarm[1][:2])
                return "alarm has been set at " + str(Hour[-1]) + " " + str(Minute[-1]) 
            elif " in " in text:
                if " hour" in text and " minute" in text:
                    SplittedHour = text.split("hour")
                    SplittedMinute = text.split("minute")
                    Hour.append(str((int(strftime("%H"))+int(SplittedHour[0][-3:-1]))%24))
                    Minute.append(str(int(strftime("%M"))+int(SplittedMinute[0][-3:-1])))
                    if int(strftime("%M"))+int(SplittedMinute[0][-3:-1]) > 60:
                        Minute[-1] = (int(strftime("%M"))+int(SplittedMinute[0][-3:-1])) % 60
                        Hour[-1] = int(Hour[-1]) + math.floor((int(strftime("%M"))+int(SplittedMinute[0][-3:-1])) / 60)
                    if (int(SplittedHour[0][-3:-1]) + ((int(strftime("%M"))+int(SplittedMinute[0][-3:-1]))/60)) > 24:
                        Hour[-1] = None
                        Minute[-1] = None
                        return "You cannot set alarms loger than 24 hours"
                    else:
                        return "alarm set at " + str(Hour[-1]) + " " + str(Minute[-1])
                elif " hour" in text:
                    SplittedHour = text.split("hour")
                    Hour.append(str((int(strftime("%H"))+int(SplittedHour[0][-3:-1]))%24))
                    Minute.append(strftime("%M"))
                    if int(SplittedHour[0][-3:-1]) > 24:
                        Hour[-1] = None
                        Minute[-1] = None
                        return "You cannot set alarms loger than 24 hours"
                    else:
                        return "alarm set at " + str(Hour[-1]) + " " + str(Minute[-1])

                elif " minute" in text:
                    SplittedMinute = text.split("minute")
                    Minute.append(str((int(strftime("%M"))+int(SplittedMinute[0][-3:-1]))%60))
                    Hour.append(str(int(strftime("%H")) + math.floor((int(strftime("%M"))+int(SplittedMinute[0][-3:-1]))/60)))
                    if int(strftime("%H")) + math.floor((int(strftime("%M"))+int(SplittedMinute[0][-3:-1]))/60) > 24:
                        Hour[-1] = None
                        Minute[-1] = None
                        return "You cannot set alarms loger than 24 hours"
                    else:
                        return "alarm set at " + str(Hour[-1]) + " " + str(Minute[-1])
        else:
            return False
