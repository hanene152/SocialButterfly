# data_analysis/analysis.py

from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def analyze_tweets(tweets):
    for tweet in tweets:
        tweet['sentiment'] = analyze_sentiment(tweet['text'])
    return tweets

def analyze_reddit_posts(posts):
    for post in posts:
        post['sentiment'] = analyze_sentiment(post['title'])
    return posts
