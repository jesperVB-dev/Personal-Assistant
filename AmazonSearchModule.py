import webbrowser
import urllib.parse

class AmazonSearch:
    def Questions(text):
        if "amazon" in text and "search" in text and "for" in text:
            SplittedText = text.split("for")
            Query = SplittedText[1][1:]
            url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords='+ urllib.parse.quote_plus(Query)
            webbrowser.open(url)
            return "here it is"
        else:
            return False

