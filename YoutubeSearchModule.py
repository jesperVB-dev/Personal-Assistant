import webbrowser
import urllib.parse

class YoutubeSearch:
    def Questions(text):
        if "youtube" in text and "search" in text and "for" in text:
            SplittedText = text.split("for")
            Query = SplittedText[1][1:]
            url = 'https://www.youtube.com/results?search_query='+ urllib.parse.quote_plus(Query)
            webbrowser.open(url)
            return "here it is"
        else:
            return False
