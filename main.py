import speech_recognition as sr
import webbrowser
from HardCodeModule import HardCoded as HCM
from FormatFitterModule import FormatFitter as FFM
from GoogleSearchModule import GoogleSearch as GSM
from YoutubeSearchModule import YoutubeSearch as YSM
from AmazonSearchModule import AmazonSearch as ASM
from WikiSearchModule import WikiSearch as WSM
from AlarmModule import Alarm as AM
from PokemonModule import Pokemon as PM
from CheckerModule import Checker as CM
from CloseTabsModule import CloseTabs as CTM
Standby = False
r = sr.Recognizer()

webbrowser.open("https://google.com")
Method = "Keyboard"

def TextToSpeech(Method):
    if Method == "Keyboard":
        text = str(input())
        return text
    
    with sr.Microphone() as source:
        audio = r.listen(source)

    try:
        text = str(r.recognize_google(audio)).lower()
        return text
    except sr.UnknownValueError:
        return None
    except sr.RequestError as e:
        return None

def HeyJarvisActive(Standby,AlarmCheck,Method):
    while Standby != True:
        if AlarmCheck != False:
            print(AlarmCheck)

        text = TextToSpeech(Method)
        
        if text != None:
            print(text)
            if "jarvis" in text:
                Standby = True
                print("yes sir")
    return
                
while True:
    AlarmCheck = CM.AlarmCheck()

    if AlarmCheck != False:
        print(AlarmCheck)

    HeyJarvisActive(Standby,AlarmCheck,Method)
    
    text = TextToSpeech(Method)
    while text == None:
        text = TextToSpeech(Method)
        
    print(text)

    HardCoded = HCM.Questions(text)
    FormatFitter = FFM.Questions(text)
    Alarm = AM.Questions(text)
    Pokemon = PM.Questions(text)
    Google = GSM.Questions(text)
    Wiki = WSM.Questions(text)
    Youtube = YSM.Questions(text)
    Amazon = ASM.Questions(text)
    CloseTabs = CTM.Questions(text)
    
    if HardCoded != False:
        print(HardCoded)
    elif Alarm != False:
        print(Alarm)
    elif FormatFitter != False:
        print(FormatFitter)
    elif Pokemon != False:
        print(Pokemon)
    elif Wiki != False:
        print(Wiki)
    elif Google != False:
        print(Google)
    elif Youtube != False:
        print(Youtube)
    elif Amazon != False:
        print(Amazon)
    elif CloseTabs != False:
        print(CloseTabs)
        
    Standby = False    

