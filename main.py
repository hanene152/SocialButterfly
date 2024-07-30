# main.py

from data_retrieval.twitter_retrieval import TwitterRetrieval
from data_retrieval.reddit_retrieval import RedditRetrieval
from data_storage.database import store_tweets, store_reddit_posts
from data_analysis.analysis import analyze_tweets, analyze_reddit_posts
from reporting.report_generator import generate_report, plot_sentiment

def main():
    twitter = TwitterRetrieval()
    reddit = RedditRetrieval()

    twitter_query = 'OpenAI'
    reddit_query = 'OpenAI'
    subreddit = 'technology'

    tweets = twitter.fetch_tweets(twitter_query, count=10)
    analyzed_tweets = analyze_tweets(tweets)
    store_tweets(analyzed_tweets)

    reddit_posts = reddit.fetch_posts(subreddit, reddit_query, count=10)
    analyzed_reddit_posts = analyze_reddit_posts(reddit_posts)
    store_reddit_posts(analyzed_reddit_posts)

    generate_report(analyzed_tweets, 'tweets_report')
    plot_sentiment(analyzed_tweets, 'Twitter Sentiment Analysis', 'tweets_sentiment')

    generate_report(analyzed_reddit_posts, 'reddit_report')
    plot_sentiment(analyzed_reddit_posts, 'Reddit Sentiment Analysis', 'reddit_sentiment')

    print(f"Stored and analyzed {len(tweets)} tweets and {len(reddit_posts)} Reddit posts.")

if __name__ == "__main__":
    main()
