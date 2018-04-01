import webbrowser
import urllib.parse

class GoogleSearch:
    def Questions(text):
        if "google" in text and "search" in text and "for" in text and "internet" not in text:
            SplittedText = text.split("for")
            Query = SplittedText[1][1:]
            url = 'https://www.google.be/search?q='+ urllib.parse.quote_plus(Query)
            webbrowser.open(url)
            return "here it is"
        else:
            return False

