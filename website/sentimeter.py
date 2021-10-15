import tweepy
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def primary(input_hashtag):

    neg = 0.0
    pos = 0.0
    neg_count = 0
    neutral_count = 0
    pos_count = 0

    blob = TextBlob(input_hashtag)
    analyzer = SentimentIntensityAnalyzer()
    vs=analyzer.polarity_scores(input_hashtag)
    if blob.sentiment.polarity < 0:         #Negative
        neg += blob.sentiment.polarity
        neg_count += 1
    elif blob.sentiment.polarity == 0:      #Neutral
        neutral_count += 1
    else:                                   #Positive
        pos += blob.sentiment.polarity
        pos_count += 1
    # print "Total tweets",N
    # print "Positive ",float(pos_count/N)*100,"%"
    # print "Negative ",float(neg_count/N)*100,"%"
    # print "Neutral ",float(neutral_count/N)*100,"%"
    return [['Sentiment', 'no. of tweets'],['Positive',vs['pos']]
            ,['Neutral',vs['neg']],['Negative',vs['neu']]]