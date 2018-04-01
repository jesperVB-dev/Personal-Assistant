from time import strftime
import math
Hour = []
Minute = []
CiphersLetters = ["one","two","three","four","five","six","seven","eight","nine"]
CiphersNumber = ["1","2","3","4","5","6","7","8","9"]

class FormatFitter:
    def Questions(text):
        if "calculate" in text:
            SplittedCalculate = text.split("calculate")
            return eval(SplittedCalculate[1])
        elif ("what is" in text or "what's" in text) and "time" in text:
            return "it is " + strftime("%H %M")
        else:
            return False
    
