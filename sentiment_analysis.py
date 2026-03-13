from textblob import TextBlob

def analyze_response(text):

    analysis = TextBlob(text)

    polarity = analysis.sentiment.polarity

    if polarity > 0:
        sentiment = "Confident / Positive"
    elif polarity < 0:
        sentiment = "Negative / Hesitant"
    else:
        sentiment = "Neutral"

    score = round((abs(polarity) * 100), 2)

    return score, sentiment
