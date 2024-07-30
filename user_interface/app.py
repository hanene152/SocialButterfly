# user_interface/app.py

import sys
import os
import logging
from flask import Flask, request, jsonify, render_template

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from data_retrieval.twitter_retrieval import TwitterRetrieval
from data_retrieval.reddit_retrieval import RedditRetrieval
from data_storage.database import store_tweets, store_reddit_posts
from data_analysis.analysis import analyze_tweets, analyze_reddit_posts
from reporting.report_generator import generate_report, plot_sentiment

app = Flask(__name__)
twitter = TwitterRetrieval()
reddit = RedditRetrieval()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/search_twitter', methods=['GET'])
def search_twitter():
    query = request.args.get('query')
    count = int(request.args.get('count', 10))
    logging.debug(f"Received Twitter search request with query: {query}, count: {count}")
    if not query:
        return jsonify({"error": "Query parameter is missing"}), 400

    tweets = twitter.fetch_tweets(query, count)
    if not tweets:
        logging.debug("No tweets fetched")
        return render_template('home.html', error="Failed to fetch tweets")
    
    analyzed_tweets = analyze_tweets(tweets)
    store_tweets(analyzed_tweets)
    generate_report(analyzed_tweets, 'tweets_report')
    plot_sentiment(analyzed_tweets, 'Twitter Sentiment Analysis', 'tweets_sentiment')
    return render_template('home.html', tweets=analyzed_tweets)

@app.route('/search_reddit', methods=['GET'])
def search_reddit():
    query = request.args.get('query')
    subreddit = request.args.get('subreddit')
    count = int(request.args.get('count', 10))
    logging.debug(f"Received Reddit search request with query: {query}, subreddit: {subreddit}, count: {count}")
    if not query or not subreddit:
        return jsonify({"error": "Query or Subreddit parameter is missing"}), 400

    posts = reddit.fetch_posts(subreddit, query, count)
    if not posts:
        logging.debug("No Reddit posts fetched")
        return render_template('home.html', error="Failed to fetch Reddit posts")
    
    analyzed_posts = analyze_reddit_posts(posts)
    store_reddit_posts(analyzed_posts)
    generate_report(analyzed_posts, 'reddit_report')
    plot_sentiment(analyzed_posts, 'Reddit Sentiment Analysis', 'reddit_sentiment')
    return render_template('home.html', posts=analyzed_posts)

if __name__ == '__main__':
    app.run(debug=True)
