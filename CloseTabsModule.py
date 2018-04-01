from subprocess import Popen
import webbrowser
import time

class CloseTabs:
    def Questions(text):
        if "close" in text and "all" in text and ("tabs" in text or "windows" in text):
            #Popen('python main.py',shell=True)
            Popen('taskkill /F /IM chrome.exe', shell=True)
            return "Browser has been cleared"
