# data_retrieval/reddit_retrieval.py

import sys
import os
import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

class RedditRetrieval:
    def __init__(self):
        self.reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=REDDIT_USER_AGENT
        )

    def fetch_posts(self, subreddit, query, count=100):
        try:
            subreddit = self.reddit.subreddit(subreddit)
            posts = subreddit.search(query, limit=count)
            return [{"title": post.title, "user": post.author.name, "created_at": post.created_utc} for post in posts]
        except Exception as e:
            print(f"Error fetching Reddit posts: {e}")
            return []

# Test code to ensure it works standalone
if __name__ == "__main__":
    reddit_retrieval = RedditRetrieval()
    posts = reddit_retrieval.fetch_posts("technology", "OpenAI", 5)
    for post in posts:
        print(post)
