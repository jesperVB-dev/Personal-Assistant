import wolframalpha
client = wolframalpha.Client("WKYALT-H9E9PV56Q2")

class WikiSearch:
    def Questions(text):
        if "search" in text and "internet" in text and "for" in text:
            SplittedText = text.split("for")
            Query = SplittedText[1][1:]
            try:
                result = client.query(Query)
                #print(result)
                answer = next(result.results).text
                return str(answer)
            except AttributeError:
                return "could not answer that quetsion"
        else:
            return False
