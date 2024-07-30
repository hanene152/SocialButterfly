# data_retrieval/twitter_retrieval.py

import tweepy
import sys
import os
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Ensure the root directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from config import TWITTER_BEARER_TOKEN

class TwitterRetrieval:
    def __init__(self):
        logging.debug("Initializing Twitter API authentication")
        self.client = tweepy.Client(bearer_token=TWITTER_BEARER_TOKEN)
        logging.debug("Twitter API authenticated")

    def fetch_tweets(self, query, count=10):
        try:
            logging.debug(f"Fetching tweets for query: {query} with count: {count}")
            response = self.client.search_recent_tweets(query=query, max_results=count, tweet_fields=['created_at', 'text', 'author_id'])
            tweets = [{"text": tweet.text, "user": tweet.author_id, "created_at": tweet.created_at} for tweet in response.data]
            logging.debug(f"Fetched {len(tweets)} tweets")
            return tweets
        except tweepy.TweepyException as e:
            logging.error(f"Error fetching tweets: {e}")
            return []

# Test code to ensure it works standalone
if __name__ == "__main__":
    twitter_retrieval = TwitterRetrieval()
    tweets = twitter_retrieval.fetch_tweets("OpenAI", 5)
    for tweet in tweets:
        print(tweet)
